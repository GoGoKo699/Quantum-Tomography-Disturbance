# Achieving the joint disturbance–precision order

[Source and disturbance model](model.md) · [Algorithm](algorithm.md)

The source is $`\rho_{r,\boldsymbol n}=(I+r\boldsymbol n\cdot\boldsymbol\sigma)/2`$, with supplied radius $`r\in[1/2,1]`$ and fixed unknown direction $`\boldsymbol n\in\mathbb S^2`$. The algorithm measures and releases one independent specimen per round, retaining only classical information. All expectations below are pointwise in the direction.

The centered pure-qubit estimator is inherited from [Quantum Learning Dissipation](https://github.com/GoGoKo699/Quantum-Learning-Dissipation/blob/8cf0cbc671da060e8c27da8e3b07db13c39155b8/science/learner.md). Here the known-radius rescaling exposes the additional mixed-state variance, and an exploration floor enforces a chosen terminal precision.

## Upper-bound theorem

Let $`T\ge1`$ be an integer and $`\epsilon\ge1200/T`$. Write

$$
\kappa=1-r^2,\qquad
\nu=\frac{\kappa}{r^2},\qquad
q=\frac{200\nu}{T\epsilon}.
$$

The [algorithm](algorithm.md) returns a same-orbit estimate satisfying

$$
\sup_{\boldsymbol n}\mathbb E_{\boldsymbol n}
 [1-F(\rho_{r,\boldsymbol n},\widehat\rho_T)]\le\epsilon.
$$

For its actual nonselective projective outputs, put

$$
D_T(\boldsymbol n)=
\sum_{t=1}^T\mathbb E_{\boldsymbol n}
 [1-F(\rho_{r,\boldsymbol n},
            \Delta_{\boldsymbol a_t}(\rho_{r,\boldsymbol n}))].
$$

Then

$$
\sup_{\boldsymbol n}D_T(\boldsymbol n)
\le2+264H_T+1056\sqrt{\kappa T}+\frac{800\kappa}{\epsilon}.
$$

Thus the sufficient cost has order $`\log(1+T)+\sqrt{\kappa T}+\kappa/\epsilon`$ in a constant-factor feasible precision regime. The theorem does not identify optimal leading constants or the smallest feasible value of $`T\epsilon`$.

The proof first allows any fixed floor $`q\in[0,1/2]`$ and substitutes its displayed value at the end.

## Conditional unbiasedness

Condition on the entire classical history before a round. Abbreviate the normalized estimate by $`\boldsymbol w`$, the exploration parameters by $`s,c`$, and the random tangent vector by $`\boldsymbol u`$. Its conditional moments are

$$
\mathbb E\boldsymbol u=\boldsymbol0,\qquad
\mathbb E[\boldsymbol u\boldsymbol u^{\mathsf T}]
=\frac{I-\boldsymbol w\boldsymbol w^{\mathsf T}}2.
$$

For $`\boldsymbol a=c\boldsymbol w+s\boldsymbol u`$, the design matrix is

$$
A=\mathbb E[\boldsymbol a\boldsymbol a^{\mathsf T}]
=c^2\boldsymbol w\boldsymbol w^{\mathsf T}
+\frac{s^2}{2}(I-\boldsymbol w\boldsymbol w^{\mathsf T}),
$$

so

$$
A^{-1}\boldsymbol a
=\frac{\boldsymbol w}{c}+\frac{2\boldsymbol u}{s}.
$$

Both denominators are positive. Since $`y=b/r`$ has conditional mean $`\boldsymbol n\cdot\boldsymbol a`$,

$$
\mathbb E[yA^{-1}\boldsymbol a]
=A^{-1}A\boldsymbol n=\boldsymbol n.
$$

Also $`\mathbb E[cA^{-1}\boldsymbol a]=\boldsymbol w`$. Therefore

$$
\boldsymbol g=\boldsymbol w+(y-c)A^{-1}\boldsymbol a
\quad\Longrightarrow\quad
\mathbb E[\boldsymbol g\mid\text{past}]=\boldsymbol n.
$$

The expectation averages the random probe and its one observed sign.

## Exact conditional variance

Put $`e=\Vert \boldsymbol n-\boldsymbol w\Vert ^2`$. Unit norms imply $`\boldsymbol n\cdot\boldsymbol w=1-e/2`$. Because $`y^2=r^{-2}=1+\nu`$,

$$
\mathbb E[(y-c)^2\mid\text{past}]
=\nu+s^2+c^2e.
$$

Moreover,

$$
\Vert A^{-1}\boldsymbol a\Vert ^2=\frac1{c^2}+\frac4{s^2},
\qquad
\boldsymbol w\cdot A^{-1}\boldsymbol a=\frac1c,
\qquad
\mathbb E[y-c]=-\frac{ce}{2}.
$$

Expanding $`\Vert \boldsymbol g\Vert ^2`$ and subtracting $`\Vert \mathbb E\boldsymbol g\Vert ^2=1`$ gives

$$
\mathbb E[\Vert \boldsymbol g-\boldsymbol n\Vert ^2\mid\text{past}]
=
4+\frac{s^2}{c^2}+\frac{4c^2}{s^2}e
+\nu\left(\frac1{c^2}+\frac4{s^2}\right).
$$

The final term is the mixed-state variance floor. At $`\nu=0`$, this reduces to the inherited pure-state identity. No rejected outcomes or favorable-history event enter the calculation.

## Global mean-square recursion

Normalizing any real vector $`\boldsymbol v`$ to $`\boldsymbol w`$ gives

$$
\Vert \boldsymbol w-\boldsymbol n\Vert 
\le2\Vert \boldsymbol v-\boldsymbol n\Vert .
$$

For nonzero $`\boldsymbol v`$, use the triangle inequality and $`|\Vert \boldsymbol v\Vert -1|\le\Vert \boldsymbol v-\boldsymbol n\Vert `$. At zero, the squared inequality follows from $`\Vert \boldsymbol w-\boldsymbol n\Vert ^2\le4`$ and $`\Vert \boldsymbol0-\boldsymbol n\Vert ^2=1`$. Thus the algorithm's fixed zero convention is covered.

Write $`M_t=\mathbb E_{\boldsymbol n}\Vert \boldsymbol v_t-\boldsymbol n\Vert ^2`$. Conditional unbiasedness removes the cross term in the averaging update:

$$
M_t=
\left(1-\frac1t\right)^2M_{t-1}
+\frac1{t^2}\mathbb E_{\boldsymbol n}\Vert \boldsymbol g_t-\boldsymbol n\Vert ^2.
$$

Using $`c_t^2\ge1/2`$, $`s_t^2\le1/2`$, $`\nu\le3`$ and the normalization bound gives

$$
M_t\le
\left[\left(1-\frac1t\right)^2+\frac{16}{t^2s_t^2}\right]M_{t-1}
+\frac{11+4\nu/s_t^2}{t^2}.
$$

The schedule is deterministic once the source radius and floor are fixed, so there is no random denominator in this recursion.

## Startup and two envelopes

For $`1\le t\le128`$, the schedule has $`s_t^2=c_t^2=1/2`$. Applying $`e\le4`$ directly to the exact variance bounds it by

$$
5+4e+10\nu\le51.
$$

The averaging recursion gives $`M_t\le51/t`$. At $`t=1`$, the previous-vector coefficient is zero, which starts the induction.

For $`t\ge129`$, the schedule satisfies $`s_t^2\ge64/t`$. Its recursion coefficient is therefore at most

$$
a_t=1-\frac7{4t}+\frac1{t^2}.
$$

If the schedule is capped at $`1/2`$, then $`\nu/s_t^2=2\nu\le6`$. Otherwise its square-root term gives $`\nu/s_t^2\le\sqrt{\nu t}/64`$. Both cases imply

$$
\frac{\nu}{s_t^2}\le6+\frac{\sqrt{\nu t}}{64}.
$$

The additive term is at most

$$
\frac{35}{t^2}+\frac{\sqrt\nu}{16t^{3/2}}.
$$

For $`t\ge129`$, elementary algebra gives

$$
\frac1t-\frac{a_t}{t-1}
=\frac{3/4-1/t}{t(t-1)}
\ge\frac7{10t^2}.
$$

A second margin is

$$
\frac1{\sqrt t}-\frac{a_t}{\sqrt{t-1}}\ge\frac1{t^{3/2}}.
$$

To verify it, use $`\sqrt{t/(t-1)}\le1+1/[2(t-1)]`$ and $`0\lt a_t\le1`$, obtaining

$$
1-a_t\sqrt{\frac t{t-1}}
\ge\frac1t\left(\frac74-\frac1t-\frac{t}{2(t-1)}\right)
\ge\frac1t.
$$

Multiplying the harmonic and square-root margins by $`100`$ dominates the displayed additive term. Induction from startup proves

$$
M_t\le100\left(\frac1t+\sqrt{\frac\nu t}\right)
\qquad(t\ge1).
$$

When $`q>0`$, the separate bound $`s_t^2\ge q`$ makes the additive term at most $`(11+4\nu/q)/t^2`$. The harmonic margin multiplied by $`100(1+\nu/q)`$ dominates it, and the startup bound fits. Hence

$$
M_t\le\frac{100(1+\nu/q)}{t}
\qquad(t\ge1,\ q>0).
$$

Combining the two envelopes yields

$$
M_t\le\frac{100}{t}
+100\min\lbrace\sqrt{\frac\nu t},\frac{\nu}{qt}\rbrace
\qquad(q>0).
$$

When $`q=0`$, the first envelope remains valid. In particular the pure case has $`M_t\le100/t`$.

## Terminal fidelity

For unit directions, squared qubit fidelity gives the exact identity

$$
1-F(\rho_{r,\boldsymbol n},\rho_{r,\widehat{\boldsymbol n}})
=\frac{r^2}{4}\Vert \boldsymbol n-\widehat{\boldsymbol n}\Vert ^2.
$$

Normalization therefore implies

$$
\mathbb E_{\boldsymbol n}
 [1-F(\rho_{r,\boldsymbol n},\widehat\rho_t)]
\le r^2M_t\le M_t.
$$

For $`\nu>0`$, substitute $`q=200\nu/(T\epsilon)`$ into the second envelope:

$$
\mathbb E_{\boldsymbol n}
 [1-F(\rho_{r,\boldsymbol n},\widehat\rho_T)]
\le\frac{100}{T}+\frac{\epsilon}{2}\le\epsilon.
$$

The condition $`\epsilon\ge1200/T`$ ensures both the last inequality and $`q\le1/2`$, using $`\nu\le3`$. For $`\nu=0`$, use $`q=0`$ and $`100/T\le\epsilon`$. This proves the stated uniform precision guarantee.

## Physical disturbance

Introduce only as an upper-bound device the directed probe loss

$$
\ell_t=\frac r2(1-\boldsymbol n\cdot\boldsymbol a_t).
$$

Opposite directions have the same projective basis but can have different directed losses. The theorem's objective is the physical disturbance below, not this auxiliary quantity.

Averaging the tangent draw gives

$$
\mathbb E_{\boldsymbol n}\ell_t
=\frac r2(1-c_t)+\frac{rc_t}{4}
 \mathbb E_{\boldsymbol n}\Vert \boldsymbol n-\boldsymbol w_t\Vert ^2
\le\frac{s_t^2}{2}+M_{t-1}.
$$

Use this for $`t\ge2`$ and $`\mathbb E\ell_1\le1`$ at startup. Since $`\sum_{t=1}^Tt^{-1/2}\le2\sqrt T`$, summing the schedule and first mean-square envelope gives

$$
\sum_{t=1}^T\mathbb E_{\boldsymbol n}\ell_t
\le1+132H_T+264\sqrt{\nu T}+\frac{qT}{2}.
$$

Put $`z=\boldsymbol n\cdot\boldsymbol a`$ and $`u=r^2(1-z^2)`$. The actual nonselective postmeasurement state is

$$
\Delta_{\boldsymbol a}(\rho_{r,\boldsymbol n})
=\frac{I+rz\boldsymbol a\cdot\boldsymbol\sigma}{2}.
$$

Its exact squared-fidelity disturbance is

$$
d_{\star}(\boldsymbol a)
=\frac{\kappa+u-\sqrt\kappa\sqrt{\kappa+u}}2.
$$

For $`u>0`$, rationalization gives

$$
d_{\star}(\boldsymbol a)
=\frac u2 
 \frac{\sqrt{\kappa+u}}{\sqrt{\kappa+u}+\sqrt\kappa}.
$$

At $`u=0`$, the disturbance is zero directly, including the pure aligned case. Thus universally

$$
\frac u4\le d_{\star}(\boldsymbol a)\le\frac u2
=\frac{r^2}{2}(1-z^2)
\le2r \ell(\boldsymbol a)\le2\ell(\boldsymbol a).
$$

The outcome-conditioned postmeasurement infidelity has instead the average value $`\kappa/2+u/2`$. Its intrinsic eigenbasis floor is not included in the nonselective objective.

Summation gives

$$
D_T(\boldsymbol n)\le2+264H_T+528\sqrt{\nu T}+qT.
$$

Finally $`\nu\le4\kappa`$ and $`qT=200\nu/\epsilon\le800\kappa/\epsilon`$, so

$$
D_T(\boldsymbol n)\le
2+264H_T+1056\sqrt{\kappa T}+\frac{800\kappa}{\epsilon}.
$$

## Scope

The expected-risk bounds hold globally over the direction and include all histories. The theorem assumes fixed independent preparations, supplied radius bounded away from zero, and the specified direct projective instrument without output repair. Weak instruments, state replacement, coherent collective processing and unknown radius are different operational models.

The construction supplies neither a high-probability confidence sequence nor a finite-digit or finite-gate optimum. Source preparation, record storage, arithmetic precision and physical control costs require their own implementation account.

