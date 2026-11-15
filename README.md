# Quantum Tomography Disturbance

How much cumulative measurement disturbance is required to learn an unknown qubit to a specified final accuracy?

For independent qubits with a known Bloch radius $`1/2\le r\le1`$ and an unknown fixed direction, adaptive rank-one projective measurements obey the joint expected minimax law

$$
D_{\min}(T,r,\epsilon)
=\Theta\left(\log(1+T)+\sqrt{\kappa T}+\frac\kappa\epsilon\right),
\qquad \kappa=1-r^2.
$$

Here $`T`$ is the number of source preparations, $`\epsilon`$ is the required final squared-fidelity infidelity, and $`C_0/T\le\epsilon\le\epsilon_0`$ for universal constants with sufficiently large $`C_0`$. The physical cost sums the fidelity disturbance between each input and its outcome-averaged postmeasurement state, for the chosen basis. The final estimate has the supplied radius. The instrument is the direct Lüders measurement followed by release, with no output repair or replacement and no quantum memory between copies.

At final accuracy $`\epsilon=A/T`$ with fixed sufficiently large $`A`$, the cost is $`\Theta(\log(1+T)+\kappa T)`$. Thus pure qubits permit logarithmic cumulative disturbance, while any fixed nonzero mixedness forces linear cumulative disturbance at that terminal accuracy. The theorem quantifies the joint transition; pure-state gentle tomography and generic inference–regret conflict are inherited.

| Result | What it establishes | Authoritative source |
| --- | --- | --- |
| Uniform joint frontier | Matching upper and lower orders in horizon, impurity and terminal precision | [Theorem](science/frontier.md) |
| Explicit one-copy learner | A centered tangent-probe update, with a precision-dependent exploration floor | [Algorithm](science/algorithm.md), [upper proof](science/upper_bound.md) |
| Adaptive physical converse | Biased-estimator information bounds and an unoriented-axis Haar lower bound | [Lower bounds](science/lower_bounds.md) |
| Charged implementation | Source, measurement, classical precision, logical control and output costs | [Resources](science/resources.md) |

## Read the account

Start with the [scientific route](science/README.md), or read the [physical interpretation](science/interpretation.md) before the proofs. The [model](science/model.md) distinguishes nonselective disturbance, excess conditional disturbance and directed reward regret. The [related-work comparison](references/related_work.md) identifies inherited results and the surviving contribution; [bibliography](references/bibliography.bib) gives publication and version metadata.

## Learn the result

The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's standard-layout manuscript. Begin with the [source-to-project bridge](learning/watrous_bridge.md) and follow the [30-milestone map](learning/milestones.md), or use the [learning entrypoint](learning/README.md) to choose a reading route. The bridge distinguishes Watrous's root fidelity from the squared fidelity used here.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_frontier.py
```

The [verification guide](verification/README.md) explains the matrix, adaptive-history, Haar, recurrence and simulation checks. [Recorded output](verification/results.json) reports the actual run. These finite checks support selected mechanisms and do not replace the analytical uniform proof.

## Scope

The controller is classical and the source copies are quantum. The result supplies no quantum computational speedup, arbitrary-instrument optimum, thermodynamic work theorem, unknown-spectrum theorem or higher-dimensional extension. Weak measurements, coherent memory and feedback repair change the task. The output-state fidelity convention and expected-risk quantifiers remain essential to the statement.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
