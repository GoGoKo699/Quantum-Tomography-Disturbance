# A precision-controlled sequential learner

[Source and disturbance model](model.md) · [Upper-bound proof](upper_bound.md)

The source supplies independent copies of

$$
\rho_{r,\boldsymbol n}
=\frac{I+r\boldsymbol n\cdot\boldsymbol\sigma}{2},
\qquad \boldsymbol n\in\mathbb S^2,\qquad \frac12\le r\le1.
$$

The radius $`r`$ is supplied and the direction $`\boldsymbol n`$ is unknown and fixed. Each round uses one direct rank-one projective measurement. Its outcome persists classically, and the measured specimen is released without output repair. No quantum register survives between rounds.

The pure-state centered estimator is inherited from [Quantum Learning Dissipation](https://github.com/GoGoKo699/Quantum-Learning-Dissipation/blob/8cf0cbc671da060e8c27da8e3b07db13c39155b8/science/learner.md). The known-radius rescaling and the precision floor below control the additional mixed-state variance. No new pure endpoint is claimed.

## Inputs

Choose a horizon $`T\ge1`$ and expected terminal infidelity target $`\epsilon\ge1200/T`$. Set

$$
\kappa=1-r^2,\qquad
\nu=\frac{\kappa}{r^2},\qquad
q=\frac{200\nu}{T\epsilon}.
$$

Then $`0\le\nu\le3`$ and $`0\le q\le1/2`$. At $`r=1`$, both $`\nu`$ and $`q`$ are zero. The constant $`1200`$ is a conservative sufficient feasibility constant, not the optimal tomography constant.

## One round

Initialize the real three-vector $`\boldsymbol v_0=\boldsymbol0`$. For $`t=1,\ldots,T`$:

### 1. Normalize the estimate

Normalize $`\boldsymbol v_{t-1}`$ to a unit vector $`\boldsymbol w_t`$. At zero, use the north pole $`(0,0,1)`$.

### 2. Choose a tangent frame

Choose a deterministic orthonormal tangent pair $`\boldsymbol e_{t,1},\boldsymbol e_{t,2}`$ perpendicular to $`\boldsymbol w_t`$. An explicit rule crosses $`\boldsymbol w_t`$ with the Cartesian axis having the smallest absolute component, breaking ties by index, normalizes that cross product, and obtains the second vector by another cross product.

### 3. Select the probe

Draw $`\boldsymbol u_t`$ uniformly from the four vectors $`\lbrace \boldsymbol e_{t,1},-\boldsymbol e_{t,1},\boldsymbol e_{t,2},-\boldsymbol e_{t,2}\rbrace `$, independently of the source and previous draws. Set

$$
s_t^2=\min\lbrace\frac12,\frac{64}{t}
               +64\sqrt{\frac{\nu}{t}}+q\rbrace,
\qquad c_t=\sqrt{1-s_t^2}.
$$

### 4. Measure one specimen

Measure the fresh specimen along the unit Bloch direction

$$
\boldsymbol a_t=c_t\boldsymbol w_t+s_t\boldsymbol u_t.
$$

The projectors are $`(I\pm\boldsymbol a_t\cdot\boldsymbol\sigma)/2`$. Record $`b_t\in\lbrace -1,+1\rbrace `$ and put $`y_t=b_t/r`$. Born's rule gives $`\mathbb E[b_t\mid\boldsymbol a_t,\text{past}]=r\boldsymbol n\cdot\boldsymbol a_t`$.

### 5. Update the classical vector

Form

$$
\boldsymbol g_t
=\boldsymbol w_t+(y_t-c_t)
    \left(\frac{\boldsymbol w_t}{c_t}
                 +\frac{2\boldsymbol u_t}{s_t}\right),
$$

and update

$$
\boldsymbol v_t
=\left(1-\frac1t\right)\boldsymbol v_{t-1}
   +\frac1t\boldsymbol g_t.
$$

The three coordinates of this real update come from one physical outcome; they are not simultaneous measurements of three Pauli observables.


## Output and guarantee

Normalize $`\boldsymbol v_T`$ using the same zero convention and return the classical description

$$
\widehat\rho_T
=\frac{I+r\widehat{\boldsymbol n}_T\cdot\boldsymbol\sigma}{2}.
$$

For squared fidelity $`F(\rho,\sigma)=\Vert \sqrt\rho\sqrt\sigma\Vert _1^2`$, every fixed direction satisfies

$$
\mathbb E_{\boldsymbol n}
 [1-F(\rho_{r,\boldsymbol n},\widehat\rho_T)]\le\epsilon.
$$

Let $`\Delta_{\boldsymbol a_t}`$ be the nonselective channel of the actual projective measurement. The cumulative expected disturbance obeys

$$
\sum_{t=1}^T\mathbb E_{\boldsymbol n}
 [1-F(\rho_{r,\boldsymbol n},
               \Delta_{\boldsymbol a_t}(\rho_{r,\boldsymbol n}))]
\le2+264H_T+1056\sqrt{\kappa T}+\frac{800\kappa}{\epsilon},
$$

where $`H_T=\sum_{t=1}^Tt^{-1}`$. The [proof](upper_bound.md) is global over the unknown direction and includes startup and zero-vector events.

The same normalization supplies intermediate estimates, but the imposed precision constraint is terminal. These are ideal expected-risk bounds. Source preparation, arithmetic precision, record storage and control synthesis are implementation costs; no high-probability confidence sequence or optimal finite-gate implementation is asserted.

