# Related work and attribution

The task is sequential tomography of a qubit with a supplied Bloch radius and an unknown direction. Each copy undergoes one rank-one projective measurement. The cost is the sum of squared-fidelity disturbances between the input and its **nonselective post-measurement state**. A separate constraint controls the final direction estimate. Measurements, post-measurement channels, reward regret and estimation loss are distinguished throughout.

The contribution is the uniform joint dependence of the optimum on the horizon, impurity and terminal precision. The statistical mechanisms, the pure-state learning problem and the general connection between information and disturbance have substantial antecedents.

## Pure-state tomography with small cumulative cost

Lumbreras, Terekhov and Tomamichel, **Learning pure quantum states almost without regret**, *npj Quantum Information* (2026), [DOI](https://doi.org/10.1038/s41534-026-01305-z), formulate sample-optimal sequential tomography together with low cumulative measurement disturbance. The current published abstract gives a pure-state protocol in arbitrary finite dimension with expected regret $`O(d^3\log^2 T)`$ and online infidelity $`\widetilde O(1/t)`$, and a logarithmic lower bound at fixed dimension. The earlier [arXiv version](https://arxiv.org/abs/2406.18370v2) contains the qubit analysis. Its qubit-only scope must not be substituted for the current published claim.

Lumbreras and Tomamichel's [all-dimensional pure-state account](https://arxiv.org/abs/2605.09019v1) develops local tangent measurements and variance-adaptive estimation. Thus low-cost sample-optimal **pure** tomography, its geometric mechanism and its higher-dimensional extension are prior work. The present result concerns the uniform approach to that pure boundary from known nonzero mixedness, with a prescribed final precision and an unoriented physical measurement-axis cost. It does not claim the first joint tomography/disturbance objective or a new general-dimensional theorem.

## The inherited pure-qubit estimator

Ruge Lin's **Quantum Learning Dissipation**, at the [cited scientific revision](https://github.com/GoGoKo699/Quantum-Learning-Dissipation/tree/8cf0cbc671da060e8c27da8e3b07db13c39155b8), contains the direct pure-qubit precursor used here. Its [centered inverse-design learner](https://github.com/GoGoKo699/Quantum-Learning-Dissipation/blob/8cf0cbc671da060e8c27da8e3b07db13c39155b8/science/learner.md) uses four random tangent probes and an unbiased recursive estimate. For every fixed pure direction it proves mean-square error at most $`21/t`$ and cumulative expected probe regret at most $`76+38\ln T`$. That pure expected-risk endpoint and the centered update are inherited.

The present algorithm extends the conditional-moment calculation to the supplied mixed radius and chooses its exploration scale using the impurity, horizon and required terminal accuracy. Its comparison theorem also needs lower bounds for the sign-insensitive physical disturbance. The earlier thermodynamic work-deficit theorem is a different objective and is not a heat or work consequence of the present result.

## Variance-dependent bandit regret already gives a crossover

Zhao, He, Zhou, Zhang and Gu, **Variance-Dependent Regret Bounds for Linear Bandits and Reinforcement Learning: Adaptivity and Computational Efficiency**, [COLT 2023, Theorem 2.3](https://proceedings.mlr.press/v195/zhao23a.html), prove a variance-adaptive regret bound of order $`\widetilde O(d\sqrt{\sum_t\sigma_t^2}+d)`$ for bounded-noise linear bandits.

For the qubit's signed outcome $`b_t`$, put $`z_t=\boldsymbol n\cdot\boldsymbol a_t`$ and $`\ell_t=r(1-z_t)/2`$. Its variance obeys

$$
\sigma_t^2=1-r^2z_t^2
\leq\kappa+4r\ell_t,
\qquad \kappa=1-r^2.
$$

The standard self-bounding substitution therefore already yields a directed-regret upper bound $`\widetilde O(1+\sqrt{\kappa T})`$ in fixed dimension. This crossover alone is not a new result here. The earlier [vanishing-noise bandit work of Lumbreras and Tomamichel](https://proceedings.mlr.press/v247/lumbreras24a.html) is another direct algorithmic foundation.

These regret statements do not impose the requested terminal tomography accuracy or provide a lower bound for the unoriented physical disturbance. Here directed regret is used for an upper construction; the physical converse treats measurement axes directly.

## Inference and reward are already competing objectives

Shao and Fang, **The Pareto-optimal Trade-off between Regret and Statistical Inference in Linear Stochastic Bandits under Safety Constraints**, [ICML 2026](https://proceedings.mlr.press/v306/shao26c.html), study a finite fixed arm set with additive sub-Gaussian noise and safety constraints. Their Theorem 3.1 relates estimation error to regret and safety budgets. Its proof uses a three-arm construction with fixed Gaussian variance and an optimal safe policy whose design matrix is rank deficient.

The need to explore for inference, and the use of a joint feasible frontier, are therefore established ideas. Their theorem does not give the known-radius Bernoulli-sphere frontier uniformly in impurity, nor the nonselective quantum-state disturbance. The present comparison must be read as an evaluated physical model with a singular pure endpoint, rather than as the first inference/regret trade-off.

## Nearly-pure tomography and noise floors

Zhang, Zhang, Xu, Li and Zhang, **Adaptive tomography of qubits: Purity versus statistical fluctuations**, *Journal of Physics A* **51**, 395304 (2018), [DOI](https://doi.org/10.1088/1751-8121/aadad3), analyze static, known-basis and adaptive MUB/SIC tomography. Their treatment of nearly-pure states identifies the interplay between a small eigenvalue and finite-sample fluctuations, including a transition at a sample scale of order the inverse small eigenvalue. Purity-dependent tomography crossover is prior work. Their objective is final full-state infidelity; they do not optimize the accumulated disturbance of every measured copy.

Aasen and Gärttner, **Limitations for adaptive quantum state tomography in the presence of detector noise**, *Physical Review A* **114**, 012414 (2026), [DOI](https://doi.org/10.1103/3q13-xpc8), [reviewed preprint](https://arxiv.org/abs/2601.04020v2), show how nonzero readout noise removes an asymptotic adaptive-tomography advantage in their reconstruction setting. Section III A explicitly focuses on mixed-state estimators for pure target states; it notes that a rank-appropriate pure-state estimator can attain the standard rate without adaptive measurements. That detector-noise and estimator-boundary effect is distinct from the present ideal-detector experiment with a supplied source spectrum. Neither result should be presented as a general impossibility of accurate noisy-state tomography.

## Information–disturbance relations and the instrument boundary

Seveso and Paris, **Trade-off between information and disturbance in qubit thermometry**, *Physical Review A* **97**, 032129 (2018), [DOI](https://doi.org/10.1103/PhysRevA.97.032129), compare Fisher information with several disturbance measures for a thermal-qubit parameter model. Their Section II A specifies fine-grained Lüders instruments without outcome-dependent unitary controls. The efficient measurements depend on the chosen disturbance measure.

That work establishes an important predecessor for measurement-dependent information–disturbance analysis. The present task instead estimates an unknown eigenbasis at fixed known spectrum, accumulates disturbance along an adaptive sequence and imposes a final accuracy target. Its theorem is for the stated rank-one projective instruments. It is not an optimization over all POVMs, weak measurements, recovery operations or general instruments.

## Standard proof ingredients

The Haar moment and symmetric-subspace machinery underlying pure-state estimation are established foundations; see Massar and Popescu, **Optimal Extraction of Information from Finite Quantum Ensembles**, *Physical Review Letters* **74**, 1259–1263 (1995), [DOI](https://doi.org/10.1103/PhysRevLett.74.1259). The quadratic axis-prediction quantity needed here is evaluated explicitly rather than identified with a directed state-overlap loss.

The Fisher-information chain rule, Bayesian Cramér–Rao/van Trees method, data processing and recursive mean-square analysis are standard tools. See Gill and Levit, **Applications of the van Trees inequality: a Bayesian Cramér–Rao bound**, *Bernoulli* **1**, 59–79 (1995), [author manuscript](https://dspace.library.uu.nl/bitstream/handle/1874/1190/van_trees.pdf?isAllowed=y&sequence=1). The new use is the model-specific relation between accumulated physical disturbance and the information available for direction estimation.

The [bibliography](bibliography.bib) records source versions and publication metadata. This comparison identifies the closest inspected statements and their limits; it is not an exhaustive priority claim. The result does not establish a quantum computational speedup, an unrestricted-instrument limit or a thermodynamic cost theorem.

