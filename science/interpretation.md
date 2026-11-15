# What purity changes during learning

[Frontier](frontier.md) · [Model](model.md) · [Resources](resources.md) · [Related work](../references/related_work.md)

The least-disturbing projective measurement is the eigenbasis measurement. If its basis is already known, the outcome-averaged state is unchanged, even for a mixed input. The difficulty is to discover that basis from the same stream while keeping each selected basis close to it.

For a pure qubit, the outcome variance shrinks as a probe aligns with the state. The learner can reduce the probing angle while retaining enough information to sharpen its estimate. A centered inverse-design estimate exploits this vanishing variance. The pure endpoint and the learning strategy behind it are inherited from earlier work.

At nonzero mixedness, an aligned measurement still has Bernoulli outcome variance $`\kappa/4`$. Its result mostly reflects the intrinsic eigenvalue mixture, rather than a small angular misalignment. A slightly tilted measurement changes its outcome probabilities too weakly to resolve that misalignment efficiently. The exact one-round information budget relates directional Fisher information to physical disturbance divided by $`\kappa`$.

This observation alone is local. The full result needs a global adaptive learner, a converse valid for biased estimates and random histories, and a bound that stays meaningful as $`\kappa\to0`$. The [upper proof](upper_bound.md) and [lower bounds](lower_bounds.md) provide those pieces. In particular, the pure logarithmic lower bound must predict an unoriented axis: choosing $`a`$ or $`-a`$ changes a directed reward convention but not the physical measurement basis.

## A concrete precision comparison

Consider a fixed large horizon and a source whose radius is known. If only a coarse final model is needed, the controller can concentrate its probes near its current estimate and accumulate disturbance of order $`\log(1+T)+\sqrt{\kappa T}`$. Requiring a final error near $`1/T`$ forces continued probing at a nonvanishing impurity-dependent angular scale. The added cost is $`\kappa T`$. The terminal estimate improves, while the measured stream pays for the information used to obtain it.

This is a statement about all selected bases across the stream. It is not a newly discovered purity crossover for ordinary tomography performed without a disturbance budget. It also does not say that every nonzero amount of mixedness produces a visible linear regime at a small finite horizon: all three terms in the theorem must be compared.

## Instrument choices matter

The released specimen is the direct output of the selected Lüders instrument. A controller that measures in a convenient informative basis and then prepares a fresh estimated state performs a different operation. Marginal output fidelity can conceal replacement, so the present theorem makes that restriction explicit rather than claiming an unrestricted quantum impossibility.

The model has two useful physical disturbance conventions. Ignoring each measurement outcome gives the infidelity $`d_*`$ between input and nonselective output. Comparing to the actual pure conditional poststate gives a total loss with intrinsic floor $`\kappa/2`$ per specimen. Its excess is $`d`$, with $`d/2\le d_*\le d`$. Both give the same order frontier after the second convention's floor is accounted for; their raw totals must not be interchanged.

The result therefore specifies a precise information–backaction law for adaptive projective tomography. The relevant quantum feature is the purity-dependent Born variance and projective disturbance geometry. The controller itself is classical, and the result asserts neither a quantum computational advantage nor superiority over a controller allowed more general instruments.
