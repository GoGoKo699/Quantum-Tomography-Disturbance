#!/usr/bin/env python3
"""Finite, independent checks of the qubit disturbance/tomography account.

The script checks selected identities and a finite recursion grid. It does not
prove a minimax theorem or establish asymptotic scaling from simulations.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np


SEED = 20261115053041
PAULI = np.array(
    [[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]],
    dtype=np.complex128,
)
IDENTITY = np.eye(2, dtype=np.complex128)


def unit(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def state(r: float, n: np.ndarray) -> np.ndarray:
    return (IDENTITY + r * np.einsum("i,ijk->jk", n, PAULI)) / 2


def projector(a: np.ndarray, outcome: int = 1) -> np.ndarray:
    return (IDENTITY + outcome * np.einsum("i,ijk->jk", a, PAULI)) / 2


def tangent_pair(w: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    seed = np.eye(3)[int(np.argmin(np.abs(w)))]
    e1 = unit(np.cross(w, seed))
    return e1, np.cross(w, e1)


def matrix_fidelity(rho: np.ndarray, sigma: np.ndarray) -> float:
    """Squared Uhlmann fidelity through a matrix square root, not Bloch formula."""
    values, vectors = np.linalg.eigh(rho)
    root = (vectors * np.sqrt(np.maximum(values, 0))) @ vectors.conj().T
    middle = root @ sigma @ root
    middle = (middle + middle.conj().T) / 2
    spectrum = np.maximum(np.linalg.eigvalsh(middle), 0)
    return float(np.square(np.sqrt(spectrum).sum()))


def check_moments(rng: np.random.Generator) -> dict:
    mean_residual = variance_residual = normalization_residual = 0.0
    cases = 0
    for index in range(420):
        w = unit(rng.normal(size=3))
        n = w if index % 7 == 0 else (-w if index % 7 == 1 else unit(rng.normal(size=3)))
        r = [0.5, 0.75, 0.99, 1.0][index % 4] if index < 80 else rng.uniform(0.5, 1.0)
        s2 = [0.5, 0.1, 1e-3, 1e-6][index % 4] if index < 80 else 10 ** rng.uniform(-5, math.log10(0.5))
        s, c = math.sqrt(s2), math.sqrt(1 - s2)
        nu = (1 - r * r) / (r * r)
        e1, e2 = tangent_pair(w)
        rho = state(r, n)
        mean = np.zeros(3)
        second = probability = 0.0
        # Probabilities are computed from explicit density matrices and effects.
        for u in [e1, -e1, e2, -e2]:
            a = c * w + s * u
            for b in [-1, 1]:
                p = float(np.trace(rho @ projector(a, b)).real) / 4
                g = w + (b / r - c) * (w / c + 2 * u / s)
                mean += p * g
                second += p * np.dot(g - n, g - n)
                probability += p
        e = np.dot(n - w, n - w)
        formula = 4 + s2 / (1 - s2) + 4 * (1 - s2) * e / s2 + nu * (1 / (1 - s2) + 4 / s2)
        mean_residual = max(mean_residual, float(np.linalg.norm(mean - n)))
        variance_residual = max(variance_residual, abs(second - formula) / max(1.0, abs(formula)))
        normalization_residual = max(normalization_residual, abs(probability - 1))
        cases += 1
    assert mean_residual < 5e-10
    # A pure aligned case has rare Born probabilities of order s². Explicit
    # matrix subtraction loses relative precision before inverse weighting.
    assert variance_residual < 1e-9
    assert normalization_residual < 2e-14
    return dict(cases=cases, outcomes_per_case=8, mean_max_absolute_residual=mean_residual,
                variance_max_relative_residual=variance_residual,
                probability_max_residual=normalization_residual)


def check_disturbance(rng: np.random.Generator) -> dict:
    disturbance_residual = conditional_residual = sign_residual = same_radius_residual = 0.0
    minimum_ratio, maximum_ratio = 1.0, 0.0
    cases = 0
    for index in range(360):
        n = unit(rng.normal(size=3))
        a = n if index % 9 == 0 else (-n if index % 9 == 1 else unit(rng.normal(size=3)))
        # Include the pure endpoint; keep near-pure arithmetic well conditioned.
        r = [0.5, 0.9, 1 - 1e-5, 1.0][index % 4] if index < 80 else rng.uniform(0.5, 1.0)
        rho = state(r, n)
        post = np.zeros((2, 2), dtype=complex)
        conditional = 0.0
        for b in [-1, 1]:
            pmat = projector(a, b)
            block = pmat @ rho @ pmat
            p = float(np.trace(block).real)
            post += block
            if p > 1e-14:
                conditional += p * (1 - matrix_fidelity(rho, block / p))
        flipped = sum(projector(-a, b) @ rho @ projector(-a, b) for b in [-1, 1])
        kappa = 1 - r * r
        u = r * r * max(0.0, 1 - np.dot(n, a) ** 2)
        d = u / 2
        ratio = math.sqrt(kappa + u) / (math.sqrt(kappa + u) + math.sqrt(kappa)) if kappa + u else 1.0
        closed = d * ratio
        measured = 1 - matrix_fidelity(rho, post)
        disturbance_residual = max(disturbance_residual, abs(measured - closed))
        conditional_residual = max(conditional_residual, abs(conditional - (kappa / 2 + d)))
        sign_residual = max(sign_residual, float(np.linalg.norm(post - flipped)))
        other = unit(rng.normal(size=3))
        final_loss = 1 - matrix_fidelity(rho, state(r, other))
        same_radius = r * r * (1 - np.dot(n, other)) / 2
        same_radius_residual = max(same_radius_residual, abs(final_loss - same_radius))
        if d > 1e-9:
            minimum_ratio, maximum_ratio = min(minimum_ratio, closed / d), max(maximum_ratio, closed / d)
        assert d / 2 - 1e-15 <= closed <= d + 1e-15
        cases += 1
    # Eigenvalue square roots near a rank-one state incur ~sqrt(machine epsilon).
    assert disturbance_residual < 8e-8
    assert conditional_residual < 8e-8
    assert same_radius_residual < 8e-8
    assert sign_residual < 1e-13
    return dict(cases=cases, matrix_disturbance_max_residual=disturbance_residual,
                matrix_conditional_loss_max_residual=conditional_residual,
                matrix_same_radius_loss_max_residual=same_radius_residual,
                axis_sign_matrix_max_residual=sign_residual,
                observed_closed_proxy_ratio_min=minimum_ratio,
                observed_closed_proxy_ratio_max=maximum_ratio,
                matrix_tolerance=8e-8)


def probabilities_and_derivatives(theta: float, r: float, a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = np.array([math.sin(theta), 0, math.cos(theta)])
    derivative = np.array([math.cos(theta), 0, -math.sin(theta)])
    rho = state(r, n)
    drho = r * np.einsum("i,ijk->jk", derivative, PAULI) / 2
    probabilities = np.array([np.trace(rho @ projector(a, b)).real for b in [-1, 1]])
    derivatives = np.array([np.trace(drho @ projector(a, b)).real for b in [-1, 1]])
    return probabilities, derivatives


def check_fisher(rng: np.random.Generator) -> dict:
    maximum_proxy_ratio = maximum_physical_ratio = derivative_residual = 0.0
    for index in range(800):
        theta = rng.uniform(-0.4, 0.4)
        r = [0.5, 0.9, 0.99, 1 - 1e-6][index % 4]
        a = unit(rng.normal(size=3))
        p, dp = probabilities_and_derivatives(theta, r, a)
        information = float(np.sum(dp * dp / p))
        h = 1e-6
        plus, _ = probabilities_and_derivatives(theta + h, r, a)
        minus, _ = probabilities_and_derivatives(theta - h, r, a)
        derivative_residual = max(derivative_residual, float(np.max(np.abs(dp - (plus - minus) / (2 * h)))))
        n = np.array([math.sin(theta), 0, math.cos(theta)])
        kappa = 1 - r * r
        u = r * r * (1 - np.dot(n, a) ** 2)
        d = u / 2
        ds = d * math.sqrt(kappa + u) / (math.sqrt(kappa + u) + math.sqrt(kappa))
        maximum_proxy_ratio = max(maximum_proxy_ratio, information * kappa / (2 * d))
        maximum_physical_ratio = max(maximum_physical_ratio, information * kappa / (4 * ds))
        assert information <= 2 * d / kappa * (1 + 1e-12)
        assert information <= 4 * ds / kappa * (1 + 1e-12)
    assert derivative_residual < 3e-10

    # An explicit six-round adaptive tree, with all 64 histories, checks score
    # additivity and the cumulative physical-information budget independently.
    trees = []
    for theta, r in itertools.product([-0.3, 0.0, 0.27], [0.5, 0.9, 0.999]):
        tree = [(1.0, 0.0, tuple())]
        summed_information = physical_cost = 0.0
        for t in range(1, 7):
            new = []
            for mass, score, history in tree:
                a = unit(np.array([0.4 + 0.15 * sum(history), 0.3 * (-1) ** t, 1 + 0.02 * t]))
                p, dp = probabilities_and_derivatives(theta, r, a)
                summed_information += mass * float(np.sum(dp * dp / p))
                n = np.array([math.sin(theta), 0, math.cos(theta)])
                u = r * r * (1 - np.dot(n, a) ** 2)
                kappa = 1 - r * r
                ds = u / 2 * math.sqrt(kappa + u) / (math.sqrt(kappa + u) + math.sqrt(kappa))
                physical_cost += mass * ds
                for j, b in enumerate([-1, 1]):
                    new.append((mass * p[j], score + dp[j] / p[j], history + (b,)))
            tree = new
        joint_information = sum(mass * score * score for mass, score, _ in tree)
        mean_score = sum(mass * score for mass, score, _ in tree)
        assert abs(joint_information - summed_information) < 2e-12
        assert abs(mean_score) < 2e-12
        assert joint_information <= 4 * physical_cost / (1 - r * r) * (1 + 1e-12)
        trees.append(dict(theta=theta, r=r, histories=len(tree), joint_information=joint_information,
                          sum_conditional_information=summed_information,
                          expected_physical_disturbance=physical_cost))
    return dict(single_action_cases=800, finite_difference_max_residual=derivative_residual,
                maximum_information_over_proxy_budget=maximum_proxy_ratio,
                maximum_information_over_physical_budget=maximum_physical_ratio,
                adaptive_trees=trees, adaptive_rounds=6)


def beta_moment(k: int, m: int, power: int) -> Fraction:
    return Fraction(math.factorial(k + power) * math.factorial(m - k), math.factorial(m + power + 1))


def check_haar() -> dict:
    rational_cases = 0
    matrix_residual = identity_residual = 0.0
    levels = []
    for m in range(8):
        dim = 2 ** m
        # Dicke coordinates are independently built from computational strings.
        dicke = np.zeros((dim, m + 1), dtype=complex)
        for integer in range(dim):
            k = integer.bit_count()
            dicke[integer, k] = 1 / math.sqrt(math.comb(m, k))
        xnodes, weights = np.polynomial.legendre.leggauss(m + 4)
        xnodes, weights = (xnodes + 1) / 2, weights / 2
        phases = 2 * math.pi * np.arange(2 * m + 5) / (2 * m + 5)
        omega = np.zeros((dim, dim), dtype=complex)
        quadratic = np.zeros_like(omega)
        for x, weight in zip(xnodes, weights):
            for phi in phases:
                ket = np.array([math.sqrt(x), math.sqrt(1 - x) * np.exp(1j * phi)])
                vector = np.array([1.0 + 0j])
                for _ in range(m):
                    vector = np.kron(vector, ket)
                block = np.outer(vector, vector.conj()) * weight / len(phases)
                omega += block
                quadratic += (2 * x - 1) ** 2 * block
        reduced_omega = dicke.conj().T @ omega @ dicke
        reduced_moment = dicke.conj().T @ quadratic @ dicke
        identity_residual = max(identity_residual, float(np.linalg.norm(reduced_omega - np.eye(m + 1) / (m + 1))))
        exact = []
        for k in range(m + 1):
            # Integrate the Beta density as factorial ratios, rather than using
            # the advertised eigenvalue formula to generate its own reference.
            integral = (m + 1) * math.comb(m, k) * (4 * beta_moment(k, m, 2) - 4 * beta_moment(k, m, 1) + beta_moment(k, m, 0))
            formula = Fraction((2 * k - m) ** 2 + m + 2, (m + 2) * (m + 3))
            assert integral == formula
            exact.append(float(integral))
            rational_cases += 1
        matrix_residual = max(matrix_residual, float(np.linalg.norm((m + 1) * reduced_moment - np.diag(exact))))
        observed_maximum = float(np.linalg.eigvalsh((m + 1) * reduced_moment)[-1])
        expected_axis_loss = Fraction(4 * (m + 1), (m + 2) * (m + 3))
        assert abs(1 - observed_maximum - float(expected_axis_loss)) < 2e-13
        levels.append(dict(previous_pure_copies=m, eigenspace_dimension=m + 1,
                           maximum_quadratic_posterior=observed_maximum,
                           minimum_axis_sine_squared=str(expected_axis_loss)))
    assert matrix_residual < 5e-13
    assert identity_residual < 5e-13
    return dict(matrix_levels=levels, exact_rational_beta_cases=rational_cases,
                matrix_quadrature_max_residual=matrix_residual,
                averaged_state_max_residual=identity_residual,
                quadrature="Gauss-Legendre in |psi_0|^2 and uniform phase; full tensor matrices through m=7")


def check_recursion() -> dict:
    cases = []
    maximum_base_ratio = maximum_floor_ratio = 0.0
    for nu, floor, horizon in itertools.product([0.0, 1e-12, 1e-6, 1e-3, 0.1, 3.0], [0.0, 1e-6, 0.1], [129, 4096, 65536]):
        bound = 1.0
        case_base = case_floor = 0.0
        for t in range(1, horizon + 1):
            s2 = min(0.5, 64 / t + 64 * math.sqrt(nu / t) + floor)
            c2 = 1 - s2
            # This independently propagates the exact variance formula using
            # angular error <= min(4,4M), rather than the published simplified
            # induction coefficient and forcing term.
            angle_bound = min(4.0, 4 * bound)
            variance_bound = 4 + s2 / c2 + 4 * c2 * angle_bound / s2 + nu * (1 / c2 + 4 / s2)
            bound = (1 - 1 / t) ** 2 * bound + variance_bound / t ** 2
            envelope = 100 * (1 / t + math.sqrt(nu / t))
            case_base = max(case_base, bound / envelope)
            assert bound <= envelope * (1 + 2e-13)
            if floor:
                floor_envelope = 100 * (1 + nu / floor) / t
                case_floor = max(case_floor, bound / floor_envelope)
                assert bound <= floor_envelope * (1 + 2e-13)
        maximum_base_ratio = max(maximum_base_ratio, case_base)
        maximum_floor_ratio = max(maximum_floor_ratio, case_floor)
        cases.append(dict(nu=nu, q=floor, horizon=horizon, final_propagated_bound=bound,
                          maximum_ratio_to_base_envelope=case_base,
                          maximum_ratio_to_floor_envelope=case_floor if floor else None))
    assert len(cases) == 54
    return dict(cases=cases, parameter_cases=54, maximum_ratio_to_base_envelope=maximum_base_ratio,
                maximum_ratio_to_floor_envelope=maximum_floor_ratio,
                limitation="Finite grid and finite times only; the proof of induction for every parameter is analytical.")


def monte_carlo(rng: np.random.Generator) -> dict:
    rows = []
    replications = 192
    for kappa, floor, horizon in itertools.product([0.0, 1e-4, 0.25, 0.75], [0.0, 0.05], [256, 4096]):
        r = math.sqrt(1 - kappa)
        nu = kappa / (r * r)
        directions = rng.normal(size=(replications, 3))
        directions /= np.linalg.norm(directions, axis=1)[:, None]
        estimates = np.zeros_like(directions)
        costs = np.zeros(replications)
        for t in range(1, horizon + 1):
            norms = np.linalg.norm(estimates, axis=1)
            w = estimates / np.maximum(norms[:, None], 1e-300)
            w[norms == 0] = [0.0, 0.0, 1.0]
            seeds = np.eye(3)[np.argmin(np.abs(w), axis=1)]
            e1 = np.cross(w, seeds)
            e1 /= np.linalg.norm(e1, axis=1)[:, None]
            e2 = np.cross(w, e1)
            choices = rng.integers(0, 4, size=replications)
            u = np.where((choices < 2)[:, None], e1, e2)
            u *= np.where(choices % 2 == 0, 1, -1)[:, None]
            s2 = min(0.5, 64 / t + 64 * math.sqrt(nu / t) + floor)
            s, c = math.sqrt(s2), math.sqrt(1 - s2)
            a = c * w + s * u
            z = np.sum(directions * a, axis=1)
            outcomes = np.where(rng.random(replications) < (1 + r * z) / 2, 1, -1)
            g = w + (outcomes[:, None] / r - c) * (w / c + 2 * u / s)
            estimates = (1 - 1 / t) * estimates + g / t
            perturbation = r * r * np.maximum(0, 1 - z * z)
            if kappa:
                root = np.sqrt(kappa + perturbation)
                costs += perturbation / 2 * root / (root + math.sqrt(kappa))
            else:
                costs += perturbation / 2
        final = estimates / np.linalg.norm(estimates, axis=1)[:, None]
        losses = r * r * np.sum((directions - final) ** 2, axis=1) / 4
        mse = np.sum((directions - estimates) ** 2, axis=1)
        assert np.all(np.isfinite(losses)) and np.all(np.isfinite(costs))
        rows.append(dict(kappa=kappa, q=floor, horizon=horizon,
                         mean_terminal_infidelity=float(losses.mean()),
                         terminal_infidelity_standard_error=float(losses.std(ddof=1) / math.sqrt(replications)),
                         mean_cumulative_physical_disturbance=float(costs.mean()),
                         cumulative_disturbance_standard_error=float(costs.std(ddof=1) / math.sqrt(replications)),
                         mean_unnormalized_vector_mse=float(mse.mean())))
    return dict(replications_per_case=replications, cases=rows,
                interpretation="Reproducible stress observations over random directions. No asymptotic fit, optimality inference, or proof assertion.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    parser.add_argument("--skip-monte-carlo", action="store_true")
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    checks = dict(centered_conditional_moments=check_moments(rng),
                  physical_disturbance=check_disturbance(rng),
                  fisher_information=check_fisher(rng),
                  haar_axis_prediction=check_haar(),
                  recursive_bound=check_recursion())
    if not args.skip_monte_carlo:
        checks["monte_carlo_stress"] = monte_carlo(rng)
    result = dict(schema_version=1, passed=True, seed=SEED,
                  runtime=dict(python=platform.python_version(), numpy=np.__version__),
                  scope="Selected finite identities, exact rational integrals, finite adaptive histories, a finite recursion grid and optional Monte Carlo. Not a general proof or priority certificate.",
                  checks=checks)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(dict(passed=True, output=str(args.output), seed=SEED,
                          checks=list(checks), recursive_parameter_cases=54)))


if __name__ == "__main__":
    main()
