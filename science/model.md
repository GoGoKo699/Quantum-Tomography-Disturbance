# Sequential tomography with a disturbance budget

[Scientific route](README.md) · [Frontier](frontier.md) · [Physical interpretation](interpretation.md)

Accurate tomography and low disturbance impose two different demands on a sequence of measurements. A controller can become good at choosing a nearly aligned measurement without learning the state to the precision available from the entire sample. The question here is the cumulative physical price of imposing that terminal precision as well.

## Source, controls and chronology

The source supplies independent preparations of the same qubit state

$$
\rho_{r,n}=\frac{I+r n\cdot\sigma}{2},\qquad n\in\mathbb S^2,\qquad \frac12\le r\le1.
$$

The Bloch radius $`r`$ is supplied; the unit direction $`n`$ is unknown and fixed. Set $`\kappa=1-r^2`$ and $`\nu=\kappa/r^2`$. The range bounded away from zero excludes the separate loss of directional identifiability near the maximally mixed state. The supplied spectrum is a favorable assumption for the learner, including in the lower bound.

At round $`t`$, the controller selects a unit vector $`a_t`$ using its classical history and private randomness. It applies the rank-one Lüders instrument with projectors

$$
P_{a,\pm}=\frac{I\pm a\cdot\sigma}{2}.
$$

Its outcome $`b_t\in\lbrace -1,+1\rbrace `$ obeys $`\mathbb E[b_t\mid a_t,n]=r n\cdot a_t`$. The specimen leaves immediately in its measured state. No quantum information persists to the next specimen. Arbitrarily long classical records are allowed in the lower bound; the constructive algorithm uses a small numerical state.

There is no outcome-dependent repair, replacement, or feedback rotation on the released specimen. Choosing a later specimen's measurement is allowed. Implementing the selected projective basis as a rotation, a computational-basis measurement, and the inverse rotation is simply the specified Lüders instrument. A different instrument, weak measurement, source oracle, purification, or retained quantum memory is a different access model.

## Fidelity and physical cost

Fidelity means the squared Uhlmann fidelity,

$$
F(\rho,\tau)=\left(\mathrm{Tr}\sqrt{\sqrt\rho \tau\sqrt\rho}\right)^2.
$$

For a fixed chosen axis $`a`$, forgetting the outcome gives

$$
\Delta_a(\rho)=\sum_{b=\pm1}P_{a,b}\rho P_{a,b}
=\frac{I+r(n\cdot a)a\cdot\sigma}{2}.
$$

The disturbance is $`d_{\star}(n,a)=1-F(\rho_{r,n},\Delta_a\rho_{r,n})`$. The cost of a policy is

$$
D_T(\pi,n)=\sum_{t=1}^T\mathbb E_{n,\pi} d_{\star}(n,a_t).
$$

The expectation includes past outcomes and randomized measurement choices. The outcome average defining $`\Delta_a`$ is taken for the fixed selected axis before fidelity; this is not fidelity with a state additionally averaged over the controller's history. It is also not the sum of infidelities to the individual pure conditional poststates.

Write $`z=n\cdot a`$ and $`u=r^2(1-z^2)`$. The qubit fidelity formula gives

$$
d_{\star}(n,a)=\frac{\kappa+u-\sqrt\kappa\sqrt{\kappa+u}}2.
$$

At $`u>0`$, rationalization gives

$$
d_{\star}(n,a)=\frac u2\frac{\sqrt{\kappa+u}}{\sqrt{\kappa+u}+\sqrt\kappa},\qquad
\frac u4\le d_{\star}(n,a)\le\frac u2.
$$

At $`u=0`$ define the expression by continuity as zero. Thus $`d(n,a)=u/2`$ is an exact, uniformly equivalent algebraic proxy: $`d/2\le d_{\star}\le d`$. All bounds hold at the pure endpoint, including aligned axes.

Both $`a`$ and $`-a`$ describe the same physical basis. In contrast, the directed reward regret

$$
\ell(n,a)=\frac r2(1-n\cdot a)
$$

distinguishes their signs. It is only a construction tool here: $`d\le2r\ell\le2\ell`$. A lower bound on directed regret alone is not a lower bound on physical disturbance.

The expected fidelity loss to the actual conditional pure poststate is $`\kappa/2+d(n,a)`$. Its excess over the eigenbasis floor is $`d`$; its total has the unavoidable baseline $`\kappa T/2`$. No such baseline is subtracted in $`D_T`$, because the outcome-averaged eigenbasis measurement already fixes $`\rho`$.

## Terminal accuracy and minimax quantifiers

After $`T`$ rounds the controller outputs a classical unit vector $`\hat n_T`$ and the same-radius state $`\hat\rho_T=(I+r\hat n_T\cdot\sigma)/2`$. This output convention avoids conflating angular learning with radial boundary estimation. Exactly,

$$
1-F(\rho_{r,n},\hat\rho_T)=\frac{r^2}{4}\Vert n-\hat n_T\Vert ^2.
$$

Let $`\mathcal P(T,r,\epsilon)`$ be the policies with $`\sup_n\mathbb E[1-F(\rho_{r,n},\hat\rho_T)]\le\epsilon`$. The quantity studied is

$$
D_{\min}(T,r,\epsilon)=\inf_{\pi\in\mathcal P(T,r,\epsilon)}\ \sup_{n\in\mathbb S^2}D_T(\pi,n).
$$

The requirement is expected terminal accuracy uniformly over fixed states. There is no high-probability or prescribed all-times accuracy constraint. The same controller does output an estimate at intermediate times, but that fact does not impose an additional constraint on the minimax definition. Randomized policies, biased estimates and arbitrary causal classical processing are included.

Each preparation, basis control, measurement, classical operation and requested output is charged in [resources](resources.md). In particular, the model supplies neither a free state-loading oracle nor QRAM.
