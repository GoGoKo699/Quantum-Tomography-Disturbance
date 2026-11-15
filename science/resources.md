# Preparation, numerical precision and measurement controls

[Model](model.md) · [Sequential learner](algorithm.md) · [Upper-bound proof](upper_bound.md)

The copy frontier counts physical specimens. Implementing the attaining policy also requires classical arithmetic and measurement controls. This page gives a sufficient finite-digit implementation. It preserves the order of the frontier with a larger universal feasibility constant; it does not preserve the displayed ideal-arithmetic constants $`100`$ and $`1200`$ in the upper-bound proof.

## Resource statement

There are universal constants $`C_{\rm dig},C,K>0`$ with the following property. Let $`r\in[1/2,1]`$ be supplied, let $`T\ge2`$, and suppose the meaningful terminal target satisfies

$$
\frac{C_{\rm dig}}{T}\le\epsilon\le1.
$$

The controller can use $`O(\log(T+1))`$ digits per stored numerical variable and inverse-polynomial control accuracy to achieve

$$
\sup_n\mathbb E[1-F(\rho_{r,n},\widehat\rho_T)]\le\epsilon,
$$

$$
\sup_n D_T\le
C\left[\log(1+T)+\sqrt{\kappa T}+\frac{\kappa}{\epsilon}\right],
\qquad \kappa=1-r^2.
$$

The construction consumes exactly $`T`$ fresh source specimens and uses exactly $`T`$ logical single-qubit projective readouts. It retains no quantum register between specimens. Its persistent numerical state has $`O(\log(T+1))`$ bits, while arithmetic and a conservative gate compiler use $`\operatorname{polylog}(T+1)`$ classical working bits and elementary bit operations per round. Each basis measurement has a $`\operatorname{polylog}(T+1)`$ logical gate synthesis. These are sufficient costs, not optimal gate or arithmetic bounds.

If one preparation has cost $`G`$, its contribution is $`TG`$, in addition to the $`T\operatorname{polylog}(T+1)`$ classical and logical control work and the $`T`$ readouts. The source is a native unknown-state source: the controller is not given its preparation circuit, inverse, purification or a state-loading oracle. The supplied radius is classical input. If it is specified numerically, $`O(\log(T+1))`$ accurate bits suffice; estimating an unsupplied radius would be a separate experiment.

## A digital state and a local comparison

Store the three coordinates of $`v_t`$ on a fixed binary grid with spacing $`2^{-B}`$, with $`B=K\lceil\log_2(T+1)\rceil`$. Store the round counter and a bounded number of scalar parameters at comparable precision. No outcome list is needed.

The analysis conditions on this **actual stored vector** before each round. If it is nonzero, define the reference direction by its exact mathematical normalization,

$$
w=\frac{v}{\|v\|}.
$$

Use the fixed north pole at zero. This is a comparison within the current round. It never compares a rounded adaptive trajectory with a different ideal trajectory, whose future normalizations might be far apart.

The exploration schedule satisfies

$$
c\ge\frac1{\sqrt2},\qquad
s^2\ge\min\left\{\frac12,\frac{64}{t}\right\},\qquad
\frac1s\le C\sqrt{T+1}.
$$

Because $`r\ge1/2`$ and $`b\in\{-1,+1\}`$, the ideal one-round vector $`g`$ consequently has $`\|g\|\le C\sqrt{T+1}`$. The digital averaging update is a convex average plus its rounding error. Induction gives $`\|v_t\|\le C\sqrt{T+1}+CT2^{-B}`$ for all $`t\le T`$. The required integer part therefore has $`O(\log(T+1))`$ bits. A nonzero grid vector also satisfies $`\|v_t\|\ge2^{-B}`$.

Both bounds matter. Computing its unit direction to accuracy $`\delta`$ may require resolving the small norm, but only $`O(B+\log(T+1)+\log(1/\delta))`$ working digits. Taking $`\delta=(T+1)^{-K}`$ keeps that number logarithmic.

## A well-conditioned tangent frame

Choose the Cartesian coordinate whose approximate component in $`w`$ has the smallest absolute value, breaking ties by index. If the normalization is computed accurately, its exact component has absolute value at most $`1/\sqrt3+O(\delta)`$. Crossing $`w`$ with that coordinate axis has norm at least $`\sqrt{2/3}-O(\delta)`$. Normalizing this cross product and taking a second cross product therefore give a tangent pair with uniformly bounded denominators.

For the local reference calculation, use the coordinate selected by the digital controller and the exact normalized stored vector. The resulting exact tangent pair is orthonormal. The conditional identities used in the upper-bound proof hold for **any** such pair. A tie or a change of coordinate does not require continuity of a global frame-selection rule.

The remaining divisions, square roots and the inverse factors $`1/s,1/c,1/r`$ have condition numbers bounded by a fixed power of $`T+1`$. Bisection and fixed-precision arithmetic evaluate them to inverse-polynomial error with polynomially many operations on $`O(\log(T+1))`$-bit numbers. Increasing the universal digit constant $`K`$ absorbs these polynomial condition factors.

## Radius and exploration parameters

Let $`\nu=(1-r^2)/r^2\in[0,3]`$. From the supplied radius, compute an upper approximation $`\bar\nu`$ with

$$
\nu\le\bar\nu\le\nu+\delta.
$$

Clamping the computed value to the permitted interval, then rounding upward, gives this convention even when the state is much closer to purity than the working grid. Use

$$
s_t^2=\min\left\{\frac12,\frac{64}{t}
                 +64\sqrt{\frac{\bar\nu}{t}}+q\right\},
\qquad
q=\frac{Q\bar\nu}{T\epsilon},
$$

where $`Q`$ is a sufficiently large universal constant. Choose $`C_{\rm dig}`$ large enough that $`q\le1/2`$. This is the same family of schedules as the ideal algorithm, with a more conservative precision floor. The required rescaling $`b/r`$ is computed from an approximation to $`r`$ whose error is at most $`\delta`$.

The upper approximation cannot underestimate the true mixed-state variance. Its extra contribution to the disturbance bound is controlled by

$$
\sqrt{\bar\nu T}\le\sqrt{\nu T}+\sqrt{\delta T},
\qquad
\frac{\bar\nu}{\epsilon}\le\frac{\nu}{\epsilon}
                                  +\frac{\delta T}{C_{\rm dig}}.
$$

These additional terms are bounded constants at the chosen precision. In particular, an unresolved very small $`\kappa`$ does not create a finite noise floor or spoil the pure-state logarithmic order.

## Implementing the actual Lüders instrument

For each selected reference axis $`a`$, compute a one-qubit unitary $`U`$ with $`U^\dagger ZU=a\cdot\sigma`$. Synthesize an approximation $`\widetilde U`$ with operator-norm error at most $`\delta`$. Apply $`\widetilde U`$, measure $`Z`$, and apply the exact inverse gate sequence $`\widetilde U^\dagger`$ before releasing the specimen.

This basis computation also admits bounded denominators. When $`a_z\ge0`$, take its positive eigenvector proportional to $`(1+a_z,a_x+i a_y)`$; when $`a_z<0`$, use $`(a_x-i a_y,1-a_z)`$. The respective normalizing factors are $`\sqrt{2(1+a_z)}`$ and $`\sqrt{2(1-a_z)}`$, each at least $`\sqrt2`$ on its chosen chart. Complete the vector to a two-by-two special unitary $`V`$ and take $`U=V^\dagger`$. A chart switch only changes the chosen representation; it introduces no small denominator.

This realizes **exactly a rank-one Lüders instrument** along a unit axis $`\widetilde a`$, with $`\|\widetilde a-a\|\le C\delta`$. Using the inverse sequence is part of implementing the chosen projectors; it is not an outcome-dependent output repair. The model continues to assume ideal logical gates and readout. Gate synthesis is a controlled deterministic change of basis, not a theorem about arbitrary apparatus noise.

Conservative finite-set compilation is enough. For example, the [Dawson–Nielsen Solovay–Kitaev construction](https://arxiv.org/abs/quant-ph/0505030v2) compiles a one-qubit rotation with sequence length and classical computation polynomial in $`\log(1/\delta)`$. At inverse-polynomial $`\delta`$, both are polylogarithmic in $`T+1`$. Compiler working space is at most its polynomial running time. The resource statement counts logical gates; a hardware-specific fault-tolerant overhead is additional.

## Conditional moment perturbation

Condition on the actual digital past. Let $`g_t^0`$ denote the mathematical one-round expression using its exact normalized $`w`$, the exact locally selected tangent pair, and the schedule with $`\bar\nu`$. Its source rescaling uses the true supplied radius. The upper-bound proof gives

$$
\mathbb E[g_t^0\mid\mathcal F_{t-1}]=n
$$

and its stated conditional variance formula, with the true $`\nu`$ and the selected $`s_t,c_t`$.

The actual basis changes a conditional sign probability by at most $`C\delta`$. Since $`\|g_t^0\|\le C\sqrt{T+1}`$, its effect on the first and second moments is bounded by a fixed polynomial in $`T+1`$ times $`\delta`$. The arithmetic expression has the same type of bound: all of its denominators and its normalization precision have already been bounded. Finally, rounding the update of $`v_t`$ to its grid can be folded into the one-round vector as an error at most $`Ct2^{-B}`$.

Choose the digit and synthesis constants large enough to make the resulting effective vector $`\widetilde g_t`$ satisfy, uniformly over every digital history,

$$
\big\|\mathbb E[\widetilde g_t\mid\mathcal F_{t-1}]-n\big\|
\le\eta,
\qquad \eta\le(T+1)^{-4},
$$

$$
\mathbb E[\|\widetilde g_t-n\|^2\mid\mathcal F_{t-1}]
\le
\mathbb E[\|g_t^0-n\|^2\mid\mathcal F_{t-1}]+1.
$$

The digital recursion is then exactly

$$
v_t=\left(1-\frac1t\right)v_{t-1}
                         +\frac{\widetilde g_t}{t}.
$$

Only these conditional moment bounds are used. There is no requirement that the entire adaptive history match a separate ideal experiment.

## The contraction survives rounding

Let $`M_t=\mathbb E\|v_t-n\|^2`$. The bias adds a cross term at most $`2\eta\sqrt{M_{t-1}}/t`$. Young's inequality gives

$$
\frac{2\eta\sqrt{M_{t-1}}}{t}
\le\frac{M_{t-1}}{8t}+\frac{8\eta^2}{t}.
$$

For $`t\ge129`$, the ideal recursion coefficient was at most $`1-7/(4t)+1/t^2`$. After the displayed bias allowance it is at most $`1-3/(2t)`$. Because $`t\le T`$ and $`\eta\le(T+1)^{-4}`$, the remaining bias term is absorbed by a universal constant times $`t^{-2}`$. The additional second moment contributes another $`t^{-2}`$. Thus

$$
M_t\le\left(1-\frac3{2t}\right)M_{t-1}
       +\frac{C+4\bar\nu/s_t^2}{t^2}.
$$

Startup has only $`128`$ rounds, $`s_t^2=1/2`$, and uniformly bounded one-round vectors, so a larger universal starting constant suffices. For later rounds,

$$
\frac{\bar\nu}{s_t^2}\le C+\frac{\sqrt{\bar\nu t}}{64},
\qquad
\frac{\bar\nu}{s_t^2}\le\frac{\bar\nu}{q}\quad(q>0).
$$

The same induction as in the ideal proof, with its enlarged contraction margins, gives

$$
M_t\le C\left(\frac1t+\sqrt{\frac{\bar\nu}{t}}\right),
\qquad
M_t\le\frac{C(1+\bar\nu/q)}{t}\quad(q>0).
$$

For completeness, if $`b_t=1-3/(2t)`$, then

$$
\frac1t-\frac{b_t}{t-1}=\frac1{2t(t-1)},
\qquad
\frac1{\sqrt t}-\frac{b_t}{\sqrt{t-1}}
\ge\frac1{t^{3/2}}\quad(t\ge2).
$$

The latter follows by squaring $`1-3/(2t)\le(1-1/t)^{3/2}`$. These margins dominate the harmonic and square-root forcing terms after increasing $`C`$.

Normalization of the stored $`v_T`$ therefore gives the same expected terminal infidelity order. Choosing $`Q`$ and then $`C_{\rm dig}`$ sufficiently large makes it at most $`\epsilon`$. A finite output can encode the three grid coordinates and the instruction to normalize them, together with the supplied radius. This is an exact unit-direction description of logarithmic size. If a numerical density matrix is requested instead, approximating its radius and direction to the working precision adds only inverse-polynomial infidelity, which is absorbed by the same feasibility margin.

## Physical disturbance and total work

For the reference axis in each round, the ideal directed-loss estimate still gives the upper cost

$$
C\left[\log(1+T)+\sqrt{\bar\nu T}+qT\right]
$$

using the digital mean-square bounds. It remains to compare that axis with the actually synthesized projective axis. As a function of $`u=r^2[1-(n\cdot a)^2]`$, the physical disturbance satisfies

$$
\frac14\le\frac{\partial d_*}{\partial u}\le\frac12
$$

where the derivative is understood by continuity at the pure endpoint. Also $`|u(\widetilde a)-u(a)|\le2\|\widetilde a-a\|`$. Hence the actual physical disturbance differs by at most $`C\delta`$ per round, uniformly in $`\kappa`$. The total extra term is $`CT\delta`$, a bounded quantity. Substituting $`q=Q\bar\nu/(T\epsilon)`$, $`\nu\le4\kappa`$ and the precision bounds above proves the resource statement.

The controller uses two random classical bits per tangent draw, a round counter, a three-vector and a bounded number of scalar work registers. One source qubit is active at a time; the released output is the postmeasurement specimen. The finite classical output and the optional numerical state conversion are counted. Keeping or printing every past outcome would require additional output storage, but it is unnecessary for the stated policy.

This account establishes a finite implementation with the same statistical order. It does not establish optimal bit complexity, physical clock time, a hardware crossover, or robustness to an unknown noise channel. Those conclusions do not follow from a copy law or from deterministic synthesis accuracy.
