# From Watrous to sequential tomography with disturbance

[Learning route](README.md) · [30-milestone map](milestones.md) · [Scientific route](../science/README.md)

The single educational anchor is **John Watrous, The Theory of Quantum Information (2018)**. Use the [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) for the standard-layout source and errata. This repository links the source and does not redistribute it.

The bridge starts with one measured qubit, then connects that operation to the adaptive stream and the joint theorem. The book establishes the quantum-information foundations; the project supplies the statistical and adaptive arguments listed below.

## Selected source sections

The section numbers and printed pages refer to the standard-layout author manuscript.

| Source location | Focus for this project | Where it enters |
| --- | --- | --- |
| Section 2.1, pp. 58–71 | Registers, density operators and the distinction between a state and a preparation | [Source model](../science/model.md); M01–M03 |
| Section 2.2, pp. 72–99 | Channels and their operator representations | The nonselective map $`\Delta_a`$ and the depolarizing relaxation |
| Section 2.3, pp. 100–119 | Outcome probabilities and measurement effects | Born probabilities, classical outcomes and the chosen projective instrument |
| Section 3.2, pp. 139–163 | Fidelity, its properties and rank-one special cases | Terminal error and input–output disturbance; M04–M05 |
| Section 7.1, pp. 390–407 | Symmetric vectors and permutation-invariant operators | The $`m`$-qubit symmetric subspace in the logarithmic converse |
| Section 7.2, pp. 408–428 | Spherical and Haar averages and their applications | Uniform pure-state averaging and the quadratic-axis bound |

Chapter 1 can be consulted as a reference for operators, norms and elementary probability. The route does not require the later channel-capacity or entanglement chapters.

## Notation and convention translation

| Book language or convention | Convention used here |
| --- | --- |
| A register has a complex Euclidean state space $`\mathcal X`$ | One specimen has $`\mathcal X=\mathbb C^2`$; the retained history is classical |
| A state is an element of $`\mathrm D(\mathcal X)`$ | The qubit is $`\rho_{r,n}=(I+r n\cdot\sigma)/2`$ |
| A pure state can be written $`vv^{*}`$ for a unit vector $`v`$ | $`P_n=(I+n\cdot\sigma)/2`$ is a pure qubit state; $`n`$ is a real three-vector, not the complex state vector $`v`$ |
| Measurement effects give probabilities through $`\langle\mu(b),\rho\rangle`$ | The effects are $`P_{a,b}=(I+b a\cdot\sigma)/2`$, and $`p_b=\mathrm{Tr}(P_{a,b}\rho)`$ |
| An adjoint is written $`X^{*}`$ | The project also uses $`X^\dagger`$ when convenient |
| Definition 3.11 and Eq. (3.64) define $`F_{\mathrm W}(\rho,\tau)=\Vert \sqrt\rho\sqrt\tau\Vert _1`$ | This project's fidelity is $`F(\rho,\tau)=F_{\mathrm W}(\rho,\tau)^2`$ |

The fidelity square is essential. For a pure output projector $`P`$, this project has $`F(\rho,P)=\mathrm{Tr}(\rho P)`$, whereas the book's root fidelity is the square root of that probability. Loss here is $`1-F`$, not $`1-F_{\mathrm W}`$.

Measurement effects alone specify probabilities, not a unique postmeasurement state. The project makes the additional instrument choice explicit:

$$
\mathcal I_{a,b}(\rho)=P_{a,b}\rho P_{a,b}.
$$

Its normalized conditional output is a pure eigenstate when the outcome probability is positive. Forgetting the sign gives

$$
\Delta_a(\rho)=\sum_{b=\pm1}\mathcal I_{a,b}(\rho).
$$

That sum is taken for the selected axis before computing fidelity. Averaging over the controller's random axes before fidelity would define a different cost.

## A complete one-qubit example

The source direction is hidden from the controller. To calculate a single round, take its true values to be

$$
r=\frac35,\qquad n=(0,0,1),\qquad
\rho=\begin{pmatrix}4/5&0\\
0&1/5\end{pmatrix}.
$$

Suppose the selected measurement axis is

$$
a=\left(\frac35,0,\frac45\right).
$$

It has unit norm and $`n\cdot a=4/5`$. Its two projectors are

$$
P_+=\begin{pmatrix}9/10&3/10\\
3/10&1/10\end{pmatrix},
\qquad
P_-=\begin{pmatrix}1/10&-3/10\\
-3/10&9/10\end{pmatrix}.
$$

### 1. Outcomes and variance

Born's rule gives

$$
p_+=\mathrm{Tr}(\rho P_+)=\frac{37}{50},
\qquad
p_-=\frac{13}{50}.
$$

For the indicator of a plus outcome, the mean is $`37/50`$ and the variance is

$$
p_+(1-p_+)=\frac{481}{2500}=0.1924.
$$

For the sign variable $`b\in\lbrace -1,+1\rbrace `$, the mean and variance are instead

$$
\mathbb E b=p_+-p_-=\frac{12}{25},
\qquad
\mathrm{Var}(b)=\frac{481}{625}=0.7696.
$$

The factor of four between the two variances comes from changing the outcome coding. The mixedness parameter is $`\kappa=1-r^2=16/25`$. Even an exactly aligned probe has indicator variance $`\kappa/4=0.16`$; alignment does not eliminate mixed-state outcome randomness.

### 2. The outcome-averaged physical output

The two conditional quantum outputs are $`P_+`$ and $`P_-`$. Ignoring the outcome gives

$$
\Delta_a(\rho)=p_+P_++p_-P_-
=\begin{pmatrix}
173/250&18/125\\
18/125&77/250
\end{pmatrix}.
$$

Its Bloch vector is $`(36/125,0,48/125)`$. The output retains only the input's component along the selected axis.

Set $`z=n\cdot a`$ and $`u=r^2(1-z^2)`$. Here

$$
u=\frac{81}{625},\qquad
\kappa+u=\frac{481}{625}.
$$

For two qubit states with Bloch vectors $`x,y`$, squared fidelity is

$$
F(\rho_x,\rho_y)
=\frac{1+x\cdot y+
       \sqrt{(1-\Vert x\Vert ^2)(1-\Vert y\Vert ^2)}}2.
$$

Substituting the input and output yields the physical disturbance

$$
d_{*}=1-F(\rho,\Delta_a\rho)
=\frac{481-20\sqrt{481}}{1250}
\approx0.0338926.
$$

The convenient proxy is $`d=u/2=81/1250=0.0648`$. It obeys

$$
\frac d2=0.0324\le d_{*}\le d=0.0648.
$$

This is the same constant-factor comparison used in the theorem.

### 3. A different average: conditional output fidelity

If each sign is retained when comparing the state to its actual pure output, then

$$
F(\rho,P_+)=\frac{37}{50},
\qquad
F(\rho,P_-)=\frac{13}{50}.
$$

The average conditional infidelity is therefore

$$
p_+[1-F(\rho,P_+)]+p_-[1-F(\rho,P_-)]
=\frac{481}{1250}=0.3848.
$$

An eigenbasis measurement has conditional average infidelity $`\kappa/2=0.32`$. The excess in this example is $`0.3848-0.32=0.0648=d`$. By contrast, an outcome-averaged eigenbasis measurement leaves $`\rho`$ unchanged, so its physical cost $`d_{*}`$ is zero. These two raw averages must not be interchanged.

Reversing $`a`$ exchanges the sign labels but leaves both projectors as a set, the channel and the physical disturbance unchanged. This explains why the lower bound must learn an unoriented axis rather than depend on a chosen reward label.

### 4. A final model is a third state

If the controller reports the same-radius model with direction $`\widehat n=a`$, then its terminal error is

$$
1-F(\rho_{r,n},\rho_{r,a})
=\frac{r^2}{2}(1-n\cdot a)
=\frac9{250}=0.036.
$$

This is neither the physical disturbance $`0.0338926`$ nor the conditional average $`0.3848`$. The reported model keeps radius $`r=0.6`$, while the postmeasurement specimen's outcome-averaged Bloch radius is $`0.48`$.

One round consumes one source specimen, one selected basis measurement, one sign record and the basis-control work. The full learner repeats such rounds with axes chosen from past data. The example specifies a true direction only to make the calculation inspectable; the controller is not supplied that direction.

## From one round to the joint theorem

The [model](../science/model.md) fixes the source chronology and distinguishes the three states just calculated. The [algorithm](../science/algorithm.md) keeps a real three-vector estimate, normalizes its direction and probes four nearby tangent directions at random. Averaging its centered update over both that choice and the observed sign produces an unbiased estimate of the hidden direction.

The pure estimator's variance falls as its direction improves. For a mixed source the exact variance has an additional term proportional to $`\nu=\kappa/r^2`$. The [upper-bound proof](../science/upper_bound.md) controls this term by choosing an exploration angle and a terminal-precision floor together. Its two mean-square envelopes explain why the same policy meets both requirements.

The [lower bounds](../science/lower_bounds.md) connect the quantum experiment to a classical information calculation. On a small fixed great-circle family, the Fisher information of each sign is at most its physical disturbance times $`4/\kappa`$. Conditional scores add across an adaptive history. A Bayesian information inequality then turns the required terminal fidelity into the cost $`\kappa/\epsilon`$, and applying it before each next measurement gives the causal square-root term.

At $`\kappa=0`$, that information inequality cannot be used by dividing by zero. The proof instead averages pure copies over directions. Sections 7.1–7.2 support the symmetric-subspace and Haar machinery; the project evaluates the resulting quadratic-axis prediction loss. This gives the logarithmic term and also handles the physical equivalence of opposite axes.

Together these arguments yield the [uniform frontier](../science/frontier.md),

$$
D_{\min}(T,r,\epsilon)
\asymp
\log(1+T)+\sqrt{\kappa T}+\frac{\kappa}{\epsilon},
\qquad
\frac{C_0}{T}\le\epsilon\le\epsilon_0.
$$

The constants are universal, and the radius remains in $`[1/2,1]`$. The theorem is about expected terminal precision uniformly over fixed states. It neither demands prescribed accuracy at every earlier time nor guarantees a fixed loss on every realization.

## What the project supplies beyond the anchor

| Needed bridge step | Canonical project source |
| --- | --- |
| Bloch coordinates, supplied spectrum, direct Lüders instrument and averaging order | [Model](../science/model.md) |
| Exact qubit fidelity identities and axis-invariant physical loss | [Model](../science/model.md) and [lower bounds](../science/lower_bounds.md#physical-loss-identities) |
| Conditional classical Fisher information, adaptive score additivity and a biased-estimator Van Trees proof | [Lower bounds](../science/lower_bounds.md) |
| The evaluated Haar quadratic-axis inequality | [Logarithmic converse](../science/lower_bounds.md#a-logarithmic-bound-for-unoriented-axes) |
| Centered tangent update, exact mixed variance and mean-square induction | [Algorithm](../science/algorithm.md) and [upper proof](../science/upper_bound.md) |
| The joint limiting regimes and instrument restrictions | [Frontier](../science/frontier.md) and [interpretation](../science/interpretation.md) |
| Finite arithmetic, basis synthesis and preparation costs | [Resources](../science/resources.md) |
| Reproducible finite calculations and their limits | [Verification](../verification/README.md) |

These statistical arguments are not attributed to the textbook. Their classical inequalities and inherited research mechanisms retain their primary citations in [related work](../references/related_work.md). The single educational anchor does not replace those scientific attributions.

## Linking the thirty understanding targets

[M01–M12](milestones.md#m01) assemble the objects needed to read the model: state, measurement, channel, fidelity, stream, information and resource conventions. [M13–M30](milestones.md#m13) assemble the scientific mechanism: physical loss, pure-axis uncertainty, the mixed-state information budget, precision control, matching bounds and final synthesis. The map identifies exact source pointers for each target; it is not a claim to cover every neighboring theorem.

The final synthesis should keep two facts together. Supplying the exact spectrum still leaves an unknown eigenbasis whose information has a measurable cost. The cost theorem applies to directly measured and released specimens; outcome-dependent repair, replacement, weak measurements or persistent quantum memory are different instruments and can change the question.

