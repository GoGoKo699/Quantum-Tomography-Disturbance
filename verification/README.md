# Finite verification

The verifier independently checks the finite mechanisms behind the disturbance–tomography account. Its recorded output is [results.json](results.json). The [learner](../science/algorithm.md), [upper bound](../science/upper_bound.md), and [lower bounds](../science/lower_bounds.md) remain authoritative for the analytical statements. The universal minimax theorem and all-parameter induction are not inferred from this finite suite.

From the repository root, using Python 3.12 or newer:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_frontier.py
```

The run uses the fixed seed `20261115053041`. It writes its actual results as JSON and exits with an error if an asserted finite check fails. To retain a separate run, pass `--output PATH`. The optional `--skip-monte-carlo` omits only the stochastic stress observations. NumPy is the only external dependency.

| Check | Independent calculation | Finite scope |
|---|---|---|
| Centered learner moments | Enumerate four tangent directions and both outcomes, obtaining Born probabilities from explicit qubit density matrices and projectors | 420 cases, including alignment, opposite alignment, pure and mixed radii, and small probe angles |
| Physical disturbance | Form the actual nonselective dephasing channel and evaluate squared Uhlmann fidelity using matrix square roots; also evaluate conditional output states | 360 cases; checks the closed expression, proxy comparison, axis-sign invariance and same-radius final loss |
| Fisher budget | Differentiate Born probabilities through explicit matrices; compare with finite differences and the physical disturbance budget | 800 actions and nine complete six-round adaptive trees, each with all 64 histories |
| Quadratic Haar prediction | Integrate full tensor-product pure-state matrices using Gauss–Legendre and phase quadrature; separately integrate Beta densities with exact rational factorial ratios | Zero through seven prior pure copies, 36 exact rational Beta values |
| Learner recursion | Propagate the exact conditional variance with the normalization bound, before the proof's simplified coefficient and forcing estimates | 54 parameter/horizon combinations, through 65,536 rounds; both the base and positive-floor envelopes |
| Learner stress | Simulate the specified adaptive learner on random fixed directions, recording terminal infidelity and cumulative physical disturbance | 16 cases with 192 repetitions each; horizons 256 and 4,096, four mixedness values and two exploration floors |

The matrix-fidelity check uses an absolute tolerance of `8e-8` because eigenvalue square roots near rank-one states can amplify floating-point roundoff. The moment variance comparison uses relative tolerance `1e-9`: its pure aligned cases explicitly compute rare Born probabilities of order the squared probe angle before inverse weighting. Other numerical tolerances are stated in the script. The Beta integral comparison is exact rational arithmetic; the separate matrix quadrature comparison is floating point.

The adaptive-tree check verifies Fisher score additivity with choices depending on preceding outcomes. It does not assume that all measurements use a fixed axis. The recursion grid includes zero and very small mixedness, maximal permitted mixedness, zero exploration floor and two positive floors. Passing this grid does not prove the recurrence for every real parameter or every time.

Monte Carlo values are reproducible stress observations. Their reported standard errors describe uncertainty of the simulated sample means. They are not simultaneous confidence guarantees, an asymptotic scaling fit, evidence of minimax optimality, or validation of a noisy hardware implementation. No test certifies an unrestricted-instrument statement: the implemented learner uses the specified direct rank-one projective measurements.
