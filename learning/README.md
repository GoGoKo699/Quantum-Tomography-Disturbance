# Learn the accuracy–disturbance frontier

[Project home](../README.md) · [30-milestone map](milestones.md) · [Watrous bridge](watrous_bridge.md) · [Scientific account](../science/README.md)

A source repeatedly supplies the same unknown qubit state. Each specimen must be measured and released before the next arrives. The controller keeps a classical record and gradually improves its estimate. The question is how much these measurements disturb the entire stream when a precise final model is required.

The educational anchor is **John Watrous, The Theory of Quantum Information (2018)**. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the book, its standard-layout manuscript and errata. The bridge selects the relevant sections, translates the conventions and supplies the additional project arguments. Reading the whole book is not a prerequisite.

## A route through the project

The common [30-milestone map](milestones.md) has twelve background milestones and eighteen narrative milestones. M01–M12 connect an individual state and measurement to the complete sequential learning task. M13–M30 connect its physical loss, attaining learner, information lower bounds and final resource law. This allocation follows the argument's dependencies rather than a reader's prior assessment.

| Entry | What it makes understandable |
| --- | --- |
| [Watrous bridge](watrous_bridge.md) | The book sections, notation changes and a complete one-qubit calculation |
| [M01–M12](milestones.md#m01) | States, projective instruments, fidelity, the copy stream and the precise learning objective |
| [M13–M30](milestones.md#m13) | The three lower-bound mechanisms, the precision-controlled construction and their joint consequence |
| [Scientific route](../science/README.md) | Canonical models, statements and full proofs |
| [Finite verification](../verification/README.md) | Reproducible checks and what finite computations do not establish |

The map states shared understanding targets, dependencies and source pointers. It contains no personal progress record or assessment procedure.

## Three objects to keep separate

The source is a density operator, the selected measurement is a pair of projectors, and the final model is a classical description of a density operator. They play different roles.

Write the fixed source as

$$
\rho_{r,n}=\frac{I+r\,n\cdot\sigma}{2},
\qquad n\in\mathbb S^2,\qquad \frac12\le r\le1.
$$

The radius $`r`$ is supplied, so only the direction $`n`$ must be learned. For a selected unit axis $`a`$, the sign outcome has probability

$$
p_+(n,a)=\frac{1+r\,n\cdot a}{2}.
$$

The projective outcome changes the specimen. Ignoring that outcome for the fixed selected axis gives the state $`\Delta_a(\rho)`$. The physical cost compares this state with the input. The final accuracy compares the source with the separately reported same-radius estimate $`\widehat\rho_T`$. A good terminal estimate does not by itself show that the earlier specimens were measured gently.

The [worked example](watrous_bridge.md#a-complete-one-qubit-example) calculates these quantities separately. Its selected axis has physical disturbance about $`0.03389`$, whereas its average outcome-conditioned infidelity is $`0.3848`$. These are different operations of averaging and comparing states.

## The result to understand

Define the source mixedness parameter $`\kappa=1-r^2`$. For expected terminal infidelity at most $`\epsilon`$, uniformly over the unknown direction, the minimum worst-case cumulative physical disturbance satisfies

$$
D_{\min}(T,r,\epsilon)
\asymp
\log(1+T)+\sqrt{\kappa T}+\frac{\kappa}{\epsilon},
\qquad
\frac{C_0}{T}\le\epsilon\le\epsilon_0.
$$

Here $`C_0`$ is a sufficiently large universal constant and $`\epsilon_0`$ is a fixed small positive constant. The symbol $`\asymp`$ means upper and lower bounds within universal constant factors, not an exact formula. The theorem permits $`r,T,\epsilon`$ to vary together. The [frontier chapter](../science/frontier.md) states the quantifiers and feasibility limits.

The three terms express three different demands. Earlier specimens never reveal the next axis perfectly, producing the logarithm. At nonzero mixedness, an almost aligned probe has a nonzero outcome-variance floor, producing a square-root causal cost. A specified terminal precision requires enough accumulated directional information, producing $`\kappa/\epsilon`$.

If $`\epsilon=A/T`$ for a sufficiently large fixed constant $`A`$, the order reduces to $`\log(1+T)+\kappa T`$. At fixed mixedness this is linear in the number of specimens; at purity it is logarithmic. This precise accuracy statement is stronger than saying only that noise changes the asymptotic behavior of a learning algorithm.

## What carries over from the book

Watrous supplies the language of states, channels and measurements; fidelity; and the invariant-measure and symmetric-subspace tools behind the pure-state relaxation. The project supplies the qubit calculations, the specified instrument chronology, the adaptive estimator, the Fisher-information budget and the Bayesian information inequality used in the converse. Their proof sources remain linked in the [scientific account](../science/README.md) and [related-work comparison](../references/related_work.md).

A particularly important translation is fidelity: Watrous's Definition 3.11 uses root fidelity. This project squares it. The [notation table](watrous_bridge.md#notation-and-convention-translation) makes that conversion explicit before any loss is calculated.

## Scope at the end of the route

The theorem concerns independent fixed-state preparations, supplied radius, direct rank-one Lüders measurements, classical memory and a same-radius terminal estimate. The measured specimen is released without repair. More general instruments or outcome-dependent replacement change the physical question.

The expected guarantees are uniform over fixed directions; they are not high-probability guarantees on every run. Disturbance and infidelity are dimensionless. Preparing $`T`$ specimens, implementing their measurements, computing the classical update and reporting the model are additional counted resources, as explained in [resources](../science/resources.md). The result is not a computational speedup or a thermodynamic work law.

