# The joint accuracy–disturbance frontier

[Model](model.md) · [Construction](algorithm.md) · [Upper proof](upper_bound.md) · [Converse](lower_bounds.md)

## Uniform order theorem

There are universal positive constants $`c,C,C_0,\epsilon_0`$ such that, for every known radius $`1/2\le r\le1`$, every integer $`T\ge1`$, and every $`C_0/T\le\epsilon\le\epsilon_0`$,

$$
c\left[\log(1+T)+\sqrt{\kappa T}+\frac\kappa\epsilon\right]
\le D_{\min}(T,r,\epsilon)
\le C\left[\log(1+T)+\sqrt{\kappa T}+\frac\kappa\epsilon\right],\qquad
\kappa=1-r^2.
$$

The definition of $`D_{\min}`$, including the instrument and fidelity conventions, is in [the model](model.md). Constants are independent of $`r,T,\epsilon`$. The theorem permits these parameters to vary jointly. It does not identify the smallest feasible constant multiplying $`1/T`$, optimal leading constants, or the infeasible high-precision endpoint. A standard pure-state estimation relaxation gives the necessary scale $`\epsilon\gtrsim1/T`$; the construction attains a sufficiently large universal multiple of it.

For a finite-digit realization, choose $`C_0`$ at least as large as both the ideal construction's sufficient constant $`1200`$ and the sufficient digital constant in [resources](resources.md). These constants are not optimized.

The upper bound uses one source specimen and one projective measurement per round, no quantum memory between rounds, and a three-vector classical estimate. It is uniform over every fixed unknown direction. The converse permits arbitrary causal classical processing and randomization within the stated measurement model.

## Why the three terms appear

| Term | Operational source | Proof route |
| --- | --- | --- |
| $`\log(1+T)`$ | Even pure-state histories cannot predict the next measurement axis perfectly | Haar quadratic-axis posterior bound in [lower bounds](lower_bounds.md) |
| $`\sqrt{\kappa T}`$ | In a mixed state, low-disturbance measurements carry little new directional information | Causal Fisher-information budget and Van Trees |
| $`\kappa/\epsilon`$ | The requested final model must accumulate enough directional information | Terminal Van Trees bound and precision-tunable tangent probing |

Different priors can witness different lower terms: minimax performance dominates each Bayes lower bound. The maximum of three nonnegative terms differs from their sum by at most a factor of three. The construction achieves all three requirements with the same policy, so the upper bound is not a sum of mutually incompatible protocols.

## Precision changes the answer

At fixed nonzero mixedness, optimizing measurement reward or disturbance without a stringent final estimate has a square-root sample cost. A final estimate at the standard tomography scale is more demanding. If $`\epsilon=A/T`$ with a sufficiently large fixed $`A`$, then

$$
D_{\min}=\Theta\!\left(\log(1+T)+\kappa T\right).
$$

Here $`\sqrt{\kappa T}`$ is absorbed by $`1+\kappa T`$. At any fixed $`\kappa>0`$, this is linear in $`T`$; at $`\kappa=0`$ it is logarithmic. Thus sample-optimal terminal tomography and sublinear cumulative projective disturbance cannot coexist at fixed mixedness in this model. This is an order statement for $`\epsilon=\Theta(1/T)`$, not for every precision described loosely as “sample-optimal up to logarithms.” For example, $`\epsilon=\log(T)/T`$ only incurs the terminal lower term $`\kappa T/\log T`$.

In joint limits, logarithmic cost at $`\epsilon=A/T`$ is possible at order $`\kappa T\lesssim\log T`$. More generally, the terminal requirement becomes comparable to the square-root term at $`\epsilon\asymp\sqrt{\kappa/T}`$. The logarithmic term can dominate near purity, so neither crossover should be asserted without its other terms.

## Attribution and limits

Pure-state gentle tomography, its logarithmic lower mechanism, the existing centered pure-qubit update, variance-aware bandit tools and generic inference–regret incompatibility are inherited. The contribution here is the matching uniform joint law for physical projective disturbance and terminal accuracy, with an explicit learner through the rank-deficient endpoint. [Related work](../references/related_work.md) compares the actual earlier models.

The theorem is specific to direct Lüders measurements followed by release. It is not a bound for weak measurements, outcome-dependent repair, state replacement or persistent coherent memory. It asserts no computational speedup, thermodynamic work law, unknown-radius result, or arbitrary-dimensional extension. Finite expected-risk checks support their stated scope; they are not the proof of the uniform theorem.
