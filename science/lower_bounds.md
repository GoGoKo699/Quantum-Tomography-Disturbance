# Lower bounds for cumulative projective disturbance

The lower bound has three parts. Even a pure source incurs a logarithmic cost because each measurement axis must be selected using only earlier specimens. Positive mixedness limits the directional information obtainable per unit disturbance. This gives both a causal square-root cost and the extra cost of a prescribed final precision.

## Model and theorem

The source supplies independent qubits

$$
\rho_{r,n}=\frac{I+r n\cdot\sigma}{2},
\qquad n\in\mathbb S^2,
\qquad \frac12\le r\le1,
\qquad \kappa=1-r^2.
$$

The radius $`r`$ is known. The direction $`n`$ is fixed and unknown. Before specimen $`t`$ is measured, a policy chooses a unit vector $`a_t`$ using its previous classical record and parameter-independent internal randomness. It then performs the two-outcome projective measurement along that axis. For the recorded sign $`B_t\in\{-1,+1\}`$,

$$
\Pr_n(B_t=b\mid a_t)
=\frac{1+b r n\cdot a_t}{2}.
$$

Arbitrary classical records, randomized policy kernels and classical estimators are allowed. Quantum information from an earlier specimen is not retained. The output specimen is the state immediately after this measurement: an outcome-dependent repair or re-preparation is outside the model.

Let $`\Delta_a`$ denote the nonselective projective-measurement channel, and use squared quantum fidelity. The physical single-copy disturbance and an algebraic proxy are

$$
\delta_r(n,a)
=1-F(\rho_{r,n},\Delta_a(\rho_{r,n})),
\qquad
d_r(n,a)=\frac{r^2}{2}\left(1-(n\cdot a)^2\right).
$$

They satisfy, uniformly in all parameters,

$$
\frac12d_r(n,a)\le\delta_r(n,a)\le d_r(n,a).
\tag{1}
$$

Both losses depend on the measurement axis, so replacing $`a`$ by $`-a`$ changes neither. For a policy $`\pi`$, define

$$
D_T^\pi(n)
=\sum_{t=1}^T\mathbb E_n^\pi\delta_r(n,a_t),
\qquad
M_T^\pi=\sup_{n\in\mathbb S^2}D_T^\pi(n).
$$

The final estimator is a unit direction $`\widehat n_T`$, corresponding to the known-radius state $`\widehat\rho_T=\rho_{r,\widehat n_T}`$. Its loss is exactly

$$
L_r(n,\widehat n)
=1-F(\rho_{r,n},\rho_{r,\widehat n})
=\frac{r^2}{4}\|n-\widehat n\|_2^2.
\tag{2}
$$

Let $`\mathcal P(T,r,\epsilon)`$ contain all such policies with

$$
\sup_n\mathbb E_n^\pi L_r(n,\widehat n_T)\le\epsilon,
$$

and define $`D_{\mathrm{opt}}(T,r,\epsilon)=\inf_{\pi\in\mathcal P(T,r,\epsilon)}M_T^\pi`$, with the infimum of an empty class equal to $`+\infty`$.

**Theorem.** There is a universal $`c>0`$ such that, whenever $`T\ge1`$ and $`\mathcal P(T,r,\epsilon)`$ is nonempty,

$$
D_{\mathrm{opt}}(T,r,\epsilon)
\ge c\left[
\log(1+T)+\sqrt{\kappa T}+\frac\kappa\epsilon
\right].
\tag{3}
$$

The last term is zero at $`\kappa=0`$. In particular, (3) holds throughout the constant-factor feasible regime $`C_0/T\le\epsilon\le\epsilon_0`$ used for the matching upper bound, for sufficiently large universal $`C_0`$ and fixed positive $`\epsilon_0`$. The lower bound does not assert the exact smallest feasible constant multiplying $`1/T`$.

The proof allows biased final estimators and arbitrary parameter-independent policy randomization. Its Fisher-information argument is specific to the stipulated projective measurements; it is not a converse for general weak instruments or retained quantum memory.

## Physical loss identities

Write $`z=n\cdot a`$ and $`u=r^2(1-z^2)`$. The nonselective output has Bloch vector $`rz a`$. The qubit fidelity formula gives

$$
F(\rho_{r,n},\Delta_a\rho_{r,n})
=\frac{1+r^2z^2+\sqrt\kappa\sqrt{1-r^2z^2}}2.
$$

Consequently

$$
\delta_r(n,a)
=\frac{\kappa+u-\sqrt\kappa\sqrt{\kappa+u}}2
=\frac u2\,
\frac{\sqrt{\kappa+u}}
{\sqrt{\kappa+u}+\sqrt\kappa}.
\tag{4}
$$

The fraction lies between $`1/2`$ and $`1`$, proving (1). If $`\kappa=u=0`$, the value is defined by the first expression in (4) and equals zero. Thus the inequality also covers pure states and exactly aligned or anti-aligned axes.

If the classical outcome is retained, the conditional quantum output is a pure eigenstate of the chosen axis. Its average infidelity with the input is

$$
\mathbb E_{B\mid a}\left[1-F(\rho_{r,n},\rho_{\mathrm{out},B})\right]
=\frac{1-r^2z^2}{2}
=\frac\kappa2+d_r(n,a).
\tag{5}
$$

Hence $`d_r`$ is the excess conditional infidelity above the eigenbasis floor. The nonselective loss $`\delta_r`$ itself has zero eigenbasis baseline. The total conditional loss includes $`\kappa T/2`$ and is a different objective.

## A fixed prior and a biased-estimator information inequality

For the mixed-state bounds, restrict the direction to the great-circle patch

$$
n(\theta)=(\sin\theta,0,\cos\theta),
\qquad -\alpha\le\theta\le\alpha,
\qquad \alpha=\frac\pi8.
$$

Use the fixed prior density

$$
w(\theta)=\frac1\alpha
\cos^2\left(\frac{\pi\theta}{2\alpha}\right)
\mathbf 1_{[-\alpha,\alpha]}(\theta).
\tag{6}
$$

It integrates to one, vanishes at both endpoints and has prior Fisher information

$$
J_0=\int_{-\alpha}^{\alpha}
\frac{w'(\theta)^2}{w(\theta)}\,d\theta
=\frac{\pi^2}{\alpha^2}=64.
\tag{7}
$$

For an experiment $`H`$ with Fisher information $`I_\theta(H)`$, any real estimator $`Z=Z(H)`$ and differentiable scalar target $`\psi`$ satisfy the functional van Trees inequality

$$
\mathbb E_w\mathbb E_\theta
\left[(Z-\psi(\theta))^2\right]
\ge
\frac{
\left(\mathbb E_w\psi'(\theta)\right)^2
}{J_0+\mathbb E_w I_\theta(H)}.
\tag{8}
$$

Here and below $`\mathbb E_w`$ averages over the prior. No unbiasedness condition is imposed. For completeness, let $`q_\theta(h)`$ be the likelihood and let $`S=\partial_\theta\log(w(\theta)q_\theta(h))`$ be the joint score. Integration by parts, using the zero boundary values of $`w`$, yields

$$
\mathbb E[(Z-\psi(\theta))S]
=\mathbb E_w\psi'(\theta),
\qquad
\mathbb E S^2=J_0+\mathbb E_w I_\theta(H).
$$

Cauchy–Schwarz proves (8). The estimators used below are bounded coordinates or coordinate products, so the required second moments exist. This is the standard Bayesian information inequality; see [Gill and Levit, *Applications of the van Trees inequality*](https://dspace.library.uu.nl/bitstream/handle/1874/1190/van_trees.pdf?isAllowed=y&sequence=1).

## Information acquired by an adaptive projective policy

Assume for this section that $`\kappa>0`$. For any unit axis $`a`$, the conditional Fisher information of its sign outcome is

$$
I_\theta(a)
=\frac{r^2(a\cdot n'(\theta))^2}
{1-r^2(n(\theta)\cdot a)^2}.
\tag{9}
$$

Since $`n'(\theta)`$ is a unit tangent vector,

$$
(a\cdot n'(\theta))^2
\le1-(n(\theta)\cdot a)^2.
$$

The denominator in (9) is at least $`\kappa`$. Using (1),

$$
I_\theta(a)
\le\frac{2d_r(n(\theta),a)}\kappa
\le\frac{4\delta_r(n(\theta),a)}\kappa.
\tag{10}
$$

This bound holds for every chosen axis, including axes anti-aligned with $`n`$.

To justify additivity under arbitrary classical adaptation, include the axes and recorded signs in the history

$$
H_t=(a_1,B_1,\ldots,a_t,B_t).
$$

Its likelihood is the product of parameter-independent action kernels and the conditional Bernoulli probabilities. The action kernels therefore contribute no derivative of their own. The conditional score increment of each sign has mean zero given the previous history and the current axis. Score increments are thus orthogonal in expectation, giving

$$
I_\theta(H_t)
=\mathbb E_\theta^\pi
\sum_{s=1}^t I_\theta(a_s).
\tag{11}
$$

One may equivalently include an independent random seed in the record. Conditioning on that seed and then averaging gives the same identity. For fixed positive $`\kappa`$ all outcome probabilities are strictly positive, and the finite-horizon differentiation and integration are regular. The pure endpoint is handled separately below.

Let the Bayes cumulative disturbance be

$$
\mathcal D_t
=\mathbb E_w D_t^\pi(n(\theta)).
$$

Equations (10)–(11) imply the information budget

$$
\mathbb E_w I_\theta(H_t)
\le\frac{4\mathcal D_t}\kappa.
\tag{12}
$$

The same bound applies after appending a newly chosen axis $`a_{t+1}`$ but before observing its outcome: that choice is a parameter-independent randomized function of the existing history.

## The cost of final precision

Apply (8) with $`\psi_1(\theta)=\sin\theta`$ and $`Z=(\widehat n_T)_x`$. Since

$$
\mathbb E_w\psi_1'(\theta)
=\mathbb E_w\cos\theta
\ge\cos\alpha,
$$

the information budget gives

$$
\mathbb E_w\mathbb E_\theta
\left[((\widehat n_T)_x-\sin\theta)^2\right]
\ge
\frac{\cos^2\alpha}{J_0+4\mathcal D_T/\kappa}.
\tag{13}
$$

The uniform final fidelity guarantee and (2) imply that the left side is at most $`4\epsilon/r^2`$. Rearranging proves

$$
M_T^\pi\ge\mathcal D_T
\ge
\frac{\kappa r^2\cos^2\alpha}{16\epsilon}
-\frac{\kappa J_0}{4}.
\tag{14}
$$

In particular, because $`r\ge1/2`$ and $`\cos^2\alpha\ge1/2`$,

$$
M_T^\pi\ge\frac{\kappa}{128\epsilon}-16\kappa.
\tag{15}
$$

This is a global minimax implication of a fixed-prior bound. It does not assume that the final estimator is locally unbiased, nor that the unknown direction converges to one selected point as the horizon grows.

## A causal square-root cost

A physical axis has no preferred sign. The appropriate scalar target for a lower bound on each chosen axis is therefore

$$
\psi_2(\theta)=\sin\theta\cos\theta,
\qquad Z_t=(a_t)_x(a_t)_z.
$$

On the patch, $`\psi_2'(\theta)=\cos(2\theta)\ge\cos(2\alpha)`$. Also,

$$
\begin{aligned}
|Z_t-\psi_2(\theta)|^2
&\le\|a_ta_t^{\mathsf T}-n(\theta)n(\theta)^{\mathsf T}\|_F^2\\
&=2\left(1-(n(\theta)\cdot a_t)^2\right)\\
&=\frac{4d_r(n(\theta),a_t)}{r^2}
\le\frac{8\delta_r(n(\theta),a_t)}{r^2}.
\end{aligned}
\tag{16}
$$

The estimator $`Z_t`$ is determined before the $`t`$th sign is observed. Apply (8) to the previous history with its newly selected axis, and then use (12) and (16). The expected increment of Bayes disturbance obeys

$$
\mathcal D_t-\mathcal D_{t-1}
\ge
\frac{r^2\cos^2(2\alpha)}
{8\left(J_0+4\mathcal D_{t-1}/\kappa\right)}.
\tag{17}
$$

Put $`c_*=r^2\cos^2(2\alpha)/8\ge1/64`$. Disturbance is nonnegative, so $`\mathcal D_{t-1}\le\mathcal D_T`$. Summing (17) yields

$$
\mathcal D_T
\ge\frac{c_*T}{J_0+4\mathcal D_T/\kappa},
\qquad
4\mathcal D_T^2+\kappa J_0\mathcal D_T
\ge c_*\kappa T.
\tag{18}
$$

Solving this quadratic inequality gives the explicit bound

$$
\begin{aligned}
M_T^\pi\ge\mathcal D_T
&\ge
\frac{\sqrt{\kappa^2J_0^2+16c_*\kappa T}-\kappa J_0}{8}\\
&\ge\frac1{16}\sqrt{\kappa T}-8\kappa.
\end{aligned}
\tag{19}
$$

The last display keeps the finite startup term visible. The logarithmic bound below absorbs that term uniformly, including the regime where $`\kappa T`$ is small.

## A logarithmic bound for unoriented axes

This part applies to every $`r\in[1/2,1]`$, including $`r=1`$. It uses the symmetric-subspace method underlying [Massar and Popescu, *Optimal Extraction of Information from Finite Quantum Ensembles*](https://doi.org/10.1103/PhysRevLett.74.1259). The evaluated quadratic loss below is the axis loss needed here.

Let $`P_n=(I+n\cdot\sigma)/2`$ and let $`\mu`$ be the uniform measure on the Bloch sphere. For $`m`$ pure copies, set

$$
\Omega_m=\int P_n^{\otimes m}\,d\mu(n)
=\frac{\Pi_m}{m+1},
\qquad
Q_{m,a}=\int(n\cdot a)^2P_n^{\otimes m}\,d\mu(n),
\tag{20}
$$

where $`\Pi_m`$ projects onto the symmetric subspace. For $`m=0`$ these are scalar operators.

Choose the Dicke basis with $`k=0,\ldots,m`$ excitations along $`a`$. Azimuthal averaging makes both operators diagonal. Writing $`x=(1+n\cdot a)/2`$, the generalized eigenvalue of $`(Q_{m,a},\Omega_m)`$ in the $`k`$th Dicke component is the expectation of $`(2x-1)^2`$ for a beta distribution with parameters $`k+1,m-k+1`$. The beta moments give

$$
\begin{aligned}
\beta_{m,k}
&=1-\frac{4(k+1)(m-k+1)}{(m+2)(m+3)}\\
&=\frac{4(k-m/2)^2+m+2}{(m+2)(m+3)}.
\end{aligned}
\tag{21}
$$

Its maximum occurs at $`k=0,m`$ and equals

$$
\beta_m
=\frac{m^2+m+2}{(m+2)(m+3)}
=1-\frac{4(m+1)}{(m+2)(m+3)}.
$$

Hence, for every axis,

$$
Q_{m,a}\le\beta_m\Omega_m.
\tag{22}
$$

Consider any procedure that obtains an axis from $`m`$ pure copies, allowing even an arbitrary collective measurement of those copies. Fold its classical randomization into an axis-valued POVM $`M_m(da)`$. Equation (22) implies

$$
\begin{aligned}
\mathbb E_\mu\mathbb E[(n\cdot a)^2]
&=\int\operatorname{Tr}\left(Q_{m,a}M_m(da)\right)\\
&\le\beta_m\int\operatorname{Tr}\left(\Omega_mM_m(da)\right)
=\beta_m.
\end{aligned}
\tag{23}
$$

This argument directly handles random axes and arbitrary outcome spaces; it does not require conditioning on an individual history of positive probability.

The mixed source is a channel of the pure source:

$$
\rho_{r,n}=\mathcal E_r(P_n),
\qquad
\mathcal E_r(X)=rX+(1-r)\operatorname{Tr}(X)\frac I2.
\tag{24}
$$

Any policy history obtained from $`m`$ mixed copies can therefore be produced by a POVM on $`m`$ pure copies, by composing its measurement with $`\mathcal E_r^{\otimes m}`$. Thus (23) also bounds the axis selected by the mixed-source policy. This is a relaxation used only to prove the logarithmic lower bound; it does not extend the Fisher bounds to a different measurement model.

At time $`t`$ the axis uses only $`m=t-1`$ previous copies. From (1) and (23),

$$
\mathbb E_\mu\mathbb E\delta_r(n,a_t)
\ge\frac{r^2}{4}(1-\beta_{t-1})
=\frac{r^2t}{(t+1)(t+2)}.
\tag{25}
$$

Consequently every policy, whether or not it satisfies a terminal accuracy constraint, obeys

$$
\begin{aligned}
M_T^\pi
&\ge r^2\sum_{t=1}^T\frac{t}{(t+1)(t+2)}\\
&=r^2\left(H_{T+1}+\frac2{T+2}-2\right)\\
&\ge\frac1{24}\log(1+T).
\end{aligned}
\tag{26}
$$

For the last inequality, $`t/[(t+1)(t+2)]\ge1/(6t)`$ for $`t\ge1`$, $`H_T\ge\log(1+T)`$, and $`r^2\ge1/4`$.

## Combining the bounds and locating feasibility

The prior used in (14) and (19) is the fixed local prior (6); the prior in (26) is Haar. These need not be the same. A minimax cost dominates every Bayes cost, and the final accuracy premise is uniform over all directions, so it applies to the local prior as well.

Equations (15), (19) and (26) give, with universal constants,

$$
M_T^\pi\ge c_1\log(1+T),
\qquad
M_T^\pi\ge c_2\sqrt{\kappa T}-C_2\kappa,
\qquad
M_T^\pi\ge c_3\frac\kappa\epsilon-C_3\kappa.
\tag{27}
$$

Because $`0\le\kappa\le3/4`$ and $`\log(1+T)\ge\log2`$, the startup terms are bounded by a universal multiple of the first lower bound. Thus each of $`\log(1+T)`$, $`\sqrt{\kappa T}`$ and $`\kappa/\epsilon`$ is at most a universal multiple of $`M_T^\pi`$. Their sum is as well. This proves (3), and taking the infimum over the accuracy-constrained policy class preserves it. At $`\kappa=0`$, (26) alone proves the required conclusion.

There is also a source-copy feasibility limit independent of disturbance. The first-moment version of the beta calculation above gives the standard Haar prediction bound

$$
\mathbb E_\mu\mathbb E
\frac{1+n\cdot\widehat n_T}{2}
\le\frac{T+1}{T+2}
$$

for any estimator from $`T`$ pure copies. Depolarization simulation and (2) therefore imply

$$
\sup_n\mathbb E_n L_r(n,\widehat n_T)
\ge\frac{r^2}{T+2}
\ge\frac1{4(T+2)}.
\tag{28}
$$

Thus precision below a constant multiple of $`1/T`$ is impossible in this model. The matching upper construction works above a sufficiently large constant multiple. Neither statement identifies the exact feasibility constant between them.

## Consequence at sample-optimal final precision

For $`\epsilon`$ a sufficiently large fixed constant times $`1/T`$, the term $`\kappa/\epsilon`$ is proportional to $`\kappa T`$. Any fixed nonzero mixedness therefore forces linear cumulative physical projective disturbance when the final estimate is sample-optimal. At the pure endpoint, the lower cost is logarithmic and a matching expected-order construction is available. The theorem quantifies this transition while supplying the spectrum exactly; uncertainty in the radius is not needed for the obstruction.
