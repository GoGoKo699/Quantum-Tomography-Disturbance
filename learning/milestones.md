# Thirty milestones for the disturbance–tomography frontier

This common map follows one project, from one measured qubit to the complete accuracy–disturbance law. Its 30 understanding targets are independent of any reader's assessment history. They identify the load-bearing ideas and their connections; specialist proofs and implementation details remain in the scientific account.

The single educational anchor is **John Watrous, The Theory of Quantum Information (2018)**, using the author's standard-layout manuscript with the January 2018 preface. The [author's source page](https://jhwatrous.github.io/books-and-courses.html) supplies the manuscript for personal use. Read the selected passages through the [project bridge](watrous_bridge.md), rather than treating the whole book as a prerequisite. The source pointers below distinguish its quantum/probability foundations from Fisher information, van Trees and adaptive-recursion arguments developed in the project. Primary research references retain their attribution role and are not additional educational anchors.

**Allocation and order.** M01–M12 are 12 background/preliminary milestones: states, one instrument, its cost, one adaptive history, risk and the two statistical proof languages combine into a complete operational problem. M13–M30 are 18 narrative/innovation milestones: local physical identities and variance lead to one global learner; distinct converse mechanisms then meet in the uniform frontier, its resources, consequence and scope. Each phase moves from local objects to a global synthesis. The split reflects this project's connection between quantum backaction and adaptive inference.

**Conventions throughout.** The source radius is supplied and lies in 1/2≤r≤1; n is the unknown fixed unit direction, κ=1−r², and each fresh copy is measured and released through the selected rank-one Lüders instrument without outcome-dependent repair. For every selected axis, form the nonselective output before taking fidelity, then average its loss over the controller's histories. The final target ε is expected same-radius infidelity, uniformly over n, equivalently r²/4 times direction mean-square error. The matching theorem is in the stated constant-factor feasible regime C₀/T≤ε≤ε₀. Watrous uses root fidelity F_W; the project uses its square.

Dependencies name earlier milestones and their role, not required personal passes. The direct specialist route is [model](../science/model.md) → [frontier](../science/frontier.md) → [construction](../science/algorithm.md), [upper proof](../science/upper_bound.md), [lower bounds](../science/lower_bounds.md) and [resources](../science/resources.md).

## Phase 1: Background and preliminaries

### M01

**Phase:** Background and preliminaries.

**Central question:** What is unknown when the spectrum of a qubit is supplied?

**Understanding target:** Separate the fixed unknown unit direction n from the known radius r, the state ρ=(I+r n·σ)/2, and impurity κ=1−r². Explain why r≥1/2 keeps direction learning away from the maximally mixed degeneracy.

**Dependencies and story role:** None. Establishes the single physical object before introducing measurements or learning.

**Conceptual connection:** A density operator can be partly known: supplying eigenvalues does not supply its eigenbasis.

**Source pointers:** Watrous §§2.1.1–2.1.2; [Model: source, controls and chronology](../science/model.md#source-controls-and-chronology).

### M02

**Phase:** Background and preliminaries.

**Central question:** What does one projective measurement reveal about that direction?

**Understanding target:** Connect the two rank-one projectors along a unit axis a to a single sign b with mean r n·a. Distinguish one random observed sign from its Born probability.

**Dependencies and story role:** M01. Adds a local observation to the source model.

**Conceptual connection:** Quantum measurement statistics become a controlled Bernoulli experiment without turning the state into a classical description.

**Source pointers:** Watrous §§2.3.1–2.3.2; [Model](../science/model.md#source-controls-and-chronology); [Algorithm: one round](../science/algorithm.md#one-round).

### M03

**Phase:** Background and preliminaries.

**Central question:** Which output state does the specified measurement actually release?

**Understanding target:** Distinguish the pure conditional poststate from the outcome-forgotten Lüders output Δ_a(ρ). Explain why basis rotation, computational measurement and its inverse implement the chosen instrument, whereas outcome-dependent repair changes it.

**Dependencies and story role:** M01–M02. Completes the one-copy input–measurement–output experiment.

**Conceptual connection:** Outcome probabilities specify an observation law; an instrument additionally specifies physical backaction.

**Source pointers:** Watrous §§2.2.1–2.2.3 and §2.3; [Model](../science/model.md#source-controls-and-chronology); [Resources: implementing the actual Lüders instrument](../science/resources.md#implementing-the-actual-lüders-instrument).

### M04

**Phase:** Background and preliminaries.

**Central question:** How are similarity, disturbance and final estimation error compared?

**Understanding target:** Use the project's squared Uhlmann fidelity consistently. Watrous's Definition 3.11 uses root fidelity F_W, so F_project=F_W². Explain the exact relation between same-radius terminal infidelity and r²||n−n̂||²/4.

**Dependencies and story role:** M01–M03. Fixes the metric before either objective is accumulated.

**Conceptual connection:** One quantum similarity function connects a physical output channel and a classical direction estimate, with a convention conversion that matters numerically.

**Source pointers:** Watrous §3.2, especially Definition 3.11; [Model: fidelity and physical cost](../science/model.md#fidelity-and-physical-cost) and [terminal accuracy](../science/model.md#terminal-accuracy-and-minimax-quantifiers).

### M05

**Phase:** Background and preliminaries.

**Central question:** Which averaging order defines the physical cost?

**Understanding target:** For each selected axis, first form its nonselective output and evaluate fidelity; then average that loss over adaptive histories and random choices. Distinguish this from fidelity to an output additionally averaged over axes, and from average loss to conditional pure poststates.

**Dependencies and story role:** M02–M04. Lifts one instrument to a randomized physical experiment without changing its loss.

**Conceptual connection:** Nonlinear fidelity makes averaging order part of the operational definition.

**Source pointers:** Watrous §1.2.2 and §3.2; [Model: fidelity and physical cost](../science/model.md#fidelity-and-physical-cost).

### M06

**Phase:** Background and preliminaries.

**Central question:** What information can influence a later measurement?

**Understanding target:** Describe a history-dependent classical policy and the immediate release of every measured specimen. Separate fresh independent copies from preparation, inverse, purification or QRAM access; arbitrary classical memory does not create coherent memory.

**Dependencies and story role:** M02–M05. Turns the local experiment into the source stream that every upper and lower bound uses.

**Conceptual connection:** Adaptation carries past information forward through a classical record, not through an uncharged quantum system.

**Source pointers:** Watrous §§2.1.1, 2.2 and 2.3; [Model: source, controls and chronology](../science/model.md#source-controls-and-chronology); [Resources: resource statement](../science/resources.md#resource-statement).

### M07

**Phase:** Background and preliminaries.

**Central question:** How can a lower bound use a prior when the guarantee is uniform?

**Understanding target:** Distinguish expected risk for one fixed state, a prior-averaged risk and a supremum over unknown directions. Explain why a minimax guarantee dominates each chosen Bayes risk, and why biased estimators and randomized policies remain included.

**Dependencies and story role:** M04–M06. Establishes the quantifiers needed to compare one learner with all permitted policies.

**Conceptual connection:** A prior is a proof device for a uniform impossibility statement, not promised knowledge of the source.

**Source pointers:** Watrous §1.2.2 and §2.3; [Model: terminal accuracy and minimax quantifiers](../science/model.md#terminal-accuracy-and-minimax-quantifiers); [Lower bounds: model and theorem](../science/lower_bounds.md#model-and-theorem).

### M08

**Phase:** Background and preliminaries.

**Central question:** Why can a random tangent probe inform a three-coordinate estimate?

**Understanding target:** Relate an orthonormal pair perpendicular to the current estimate to four possible nearby probe directions. Understand a design matrix as an average over chosen probes; one vector update still uses only one physical sign.

**Dependencies and story role:** M01–M02 and M06. Supplies the geometry of the constructive policy.

**Conceptual connection:** Randomized experimental design can yield a full-vector unbiased estimate without simultaneous incompatible measurements.

**Source pointers:** Watrous §§1.1.1–1.1.2 and §1.2.2; [Algorithm: one round](../science/algorithm.md#one-round); [Upper proof: conditional unbiasedness](../science/upper_bound.md#conditional-unbiasedness).

### M09

**Phase:** Background and preliminaries.

**Central question:** Why do conditional mean and variance control a sequential estimator?

**Understanding target:** Explain how a conditionally unbiased increment removes the cross term in the averaging update's mean-square recursion. Distinguish a real numerical estimate from its normalized physical probe direction.

**Dependencies and story role:** M06 and M08. Connects individual observations to an all-history statistical guarantee.

**Conceptual connection:** Conditioning on the actual past permits a global expected-risk argument even when future probes depend on earlier outcomes.

**Source pointers:** Watrous §1.2.2 for probability foundations; [Upper proof: conditional unbiasedness](../science/upper_bound.md#conditional-unbiasedness) and [global mean-square recursion](../science/upper_bound.md#global-mean-square-recursion). The recursion is developed in the project.

### M10

**Phase:** Background and preliminaries.

**Central question:** What is the information content of an adaptive history?

**Understanding target:** Understand a Bernoulli score, its Fisher information and the zero conditional mean of each score increment. Explain why parameter-independent action kernels add no separate score and why a Bayesian information inequality need not assume an unbiased estimate.

**Dependencies and story role:** M02, M06–M07. Builds the statistical language for the mixed-state converse.

**Conceptual connection:** The observation chain and the controller's adaptation must be analyzed together rather than replaced by a fixed-axis experiment.

**Source pointers:** Watrous §1.2.2 for probability foundations; [Lower bounds: biased-estimator information inequality](../science/lower_bounds.md#a-fixed-prior-and-a-biased-estimator-information-inequality) and [adaptive projective information](../science/lower_bounds.md#information-acquired-by-an-adaptive-projective-policy). Fisher information and van Trees are supplied there.

### M11

**Phase:** Background and preliminaries.

**Central question:** How can symmetry bound what earlier copies predict?

**Understanding target:** Relate a uniform pure-qubit prior to the symmetric subspace of repeated copies. Explain how Haar moment operators and positive measurement effects convert a state-prediction question into an operator inequality.

**Dependencies and story role:** M01–M02 and M07. Supplies the independent proof route that remains useful at exact purity.

**Conceptual connection:** Permutation symmetry exposes information retained by identical specimens without assuming a particular measurement strategy.

**Source pointers:** Watrous §§7.1.1 and 7.2.1–7.2.2; [Lower bounds: a logarithmic bound for unoriented axes](../science/lower_bounds.md#a-logarithmic-bound-for-unoriented-axes).

### M12

**Phase:** Background and preliminaries.

**Central question:** What is the complete comparison problem before any theorem is used?

**Understanding target:** Put together the supplied spectrum, unknown fixed direction, causal projective instrument, physical cumulative cost and uniform expected terminal infidelity constraint. Locate the role of horizon T and the feasible precision scale 1/T, without assuming an optimal feasibility constant.

**Dependencies and story role:** M01–M11. Integrates the phase's local objects into the global operational framework.

**Conceptual connection:** Learning the state accurately at the end and disturbing the measured stream little are separate requirements on the same policy.

**Source pointers:** Watrous §§2.1–2.3 and §3.2; [Model](../science/model.md); [Frontier: uniform order theorem](../science/frontier.md#uniform-order-theorem); [Resources: resource statement](../science/resources.md#resource-statement).

## Phase 2: Narrative and innovation

### M13

**Phase:** Narrative and innovation.

**Central question:** Which simple axis loss exactly controls the physical disturbance?

**Understanding target:** Derive the nonselective output's qubit fidelity and compare d_* with u/2, where u=r²[1−(n·a)²]. Preserve the uniform bounds u/4≤d_*≤u/2 at pure and aligned endpoints, and recognize a and −a as the same basis.

**Dependencies and story role:** M03–M05 and M12. Begins the contribution with its one-copy physical identity.

**Conceptual connection:** The correct algebraic proxy is quadratic in an unoriented axis, rather than a directed reward convention.

**Source pointers:** Watrous §§2.2.3 and 3.2; [Model: fidelity and physical cost](../science/model.md#fidelity-and-physical-cost); [Lower bounds: physical loss identities](../science/lower_bounds.md#physical-loss-identities).

### M14

**Phase:** Narrative and innovation.

**Central question:** What changes in an almost aligned observation when the source is mixed?

**Understanding target:** Explain the nonzero Born variance at eigenbasis alignment when κ>0 and its disappearance at purity. Separate intrinsic eigenvalue randomness from the small directional signal generated by a tilted probe.

**Dependencies and story role:** M02, M08 and M13. Identifies the local mechanism that the learner must pay to overcome.

**Conceptual connection:** Purity changes information efficiency even though the least-disturbing eigenbasis channel fixes every state in the family.

**Source pointers:** Watrous §§2.1.2 and 2.3; [Interpretation](../science/interpretation.md); [Upper proof: exact conditional variance](../science/upper_bound.md#exact-conditional-variance).

### M15

**Phase:** Narrative and innovation.

**Central question:** Which part of the centered tangent estimator is inherited, and why is it unbiased here?

**Understanding target:** Trace the known-radius rescaling y=b/r through the inverse design and the centering y−c. Explain conditional unbiasedness over the tangent draw and one observed sign, crediting the existing pure-qubit centered update.

**Dependencies and story role:** M08–M09 and M14. Connects the inherited local learner to the present mixed-source experiment.

**Conceptual connection:** Supplying r permits unbiased rescaling; it does not remove the extra sampling variance.

**Source pointers:** Watrous §1.2.2 and §2.3; [Algorithm](../science/algorithm.md); [Upper proof: conditional unbiasedness](../science/upper_bound.md#conditional-unbiasedness); [Related work: pure-qubit precursor](../references/related_work.md#the-inherited-pure-qubit-estimator).

### M16

**Phase:** Narrative and innovation.

**Central question:** Where does mixedness enter the exact conditional variance?

**Understanding target:** Separate the pure centered variance from the added ν(1/c²+4/s²), with ν=κ/r². Explain why reducing the probing angle too aggressively amplifies this floor instead of producing cost-free directional information.

**Dependencies and story role:** M14–M15. Makes the schedule's statistical constraint explicit before choosing it.

**Conceptual connection:** The same inverse weighting that extracts tangent information also magnifies unavoidable mixed-state outcome noise.

**Source pointers:** Watrous §§1.1.2 and 1.2.2 for foundations; [Upper proof: exact conditional variance](../science/upper_bound.md#exact-conditional-variance).

### M17

**Phase:** Narrative and innovation.

**Central question:** How can one exploration schedule serve both cheap measurements and final precision?

**Understanding target:** Read the three contributions 64/t, 64√(ν/t) and q in s_t², including its cap at 1/2. Explain the roles of stabilization, mixedness and the precision floor q=200ν/(Tε), and why q vanishes at the pure endpoint.

**Dependencies and story role:** M12 and M16. Chooses the policy's control parameter using the actual two-objective task.

**Conceptual connection:** The controller must deliberately acquire extra information when the final model is more precise than reward optimization alone requires.

**Source pointers:** Watrous §1.2.2 for probability foundations; [Algorithm: inputs and one round](../science/algorithm.md#inputs); [Upper proof: upper-bound theorem](../science/upper_bound.md#upper-bound-theorem).

### M18

**Phase:** Narrative and innovation.

**Central question:** Why is the upper proof global over directions and histories?

**Understanding target:** Use the normalization inequality, the fixed zero-vector convention and conditional unbiasedness to obtain a deterministic mean-square recursion. Include startup instead of conditioning on a favorable estimate or a warm-start event.

**Dependencies and story role:** M09 and M15–M17. Turns local identities into an analysis of the full adaptive policy.

**Conceptual connection:** A potentially nonlinear normalization is controlled within the actual recursion rather than assumed harmless along an ideal trajectory.

**Source pointers:** Watrous §§1.1.1 and 1.2.2; [Upper proof: global mean-square recursion](../science/upper_bound.md#global-mean-square-recursion) and [startup and two envelopes](../science/upper_bound.md#startup-and-two-envelopes).

### M19

**Phase:** Narrative and innovation.

**Central question:** How do the two risk envelopes enforce a chosen terminal accuracy?

**Understanding target:** Distinguish the harmonic-plus-square-root error envelope from the positive-floor envelope. Explain how substituting q gives expected terminal same-radius infidelity≤ε in a sufficiently large constant-factor 1/T regime, including ν=0.

**Dependencies and story role:** M04, M17–M18. Converts the adaptive estimator into the requested final model.

**Conceptual connection:** One recursion supplies two useful guarantees; selecting the stronger one at the terminal time preserves the same physical policy.

**Source pointers:** Watrous §3.2 for fidelity foundations; [Upper proof: startup and two envelopes](../science/upper_bound.md#startup-and-two-envelopes) and [terminal fidelity](../science/upper_bound.md#terminal-fidelity).

### M20

**Phase:** Narrative and innovation.

**Central question:** Why does that same policy attain all three cumulative-cost terms?

**Understanding target:** Sum the probing angles and estimation errors, then use directed loss only as an upper bound on physical d_*. Recover the logarithmic, square-root and κ/ε contributions without combining incompatible algorithms or using directed regret as a physical converse.

**Dependencies and story role:** M13 and M17–M19. Completes the global attaining construction.

**Conceptual connection:** Cheap online choices and accurate final tomography are reconciled by one precision-tuned control schedule.

**Source pointers:** Watrous §1.2.2 and §3.2; [Upper proof: physical disturbance](../science/upper_bound.md#physical-disturbance); [Frontier: why the three terms appear](../science/frontier.md#why-the-three-terms-appear).

### M21

**Phase:** Narrative and innovation.

**Central question:** How much directional information can physical disturbance purchase?

**Understanding target:** Connect the tangent derivative of the sign probability to the bound I_θ(a)≤4d_*(n,a)/κ for κ>0. Extend it to arbitrary causal classical histories using score orthogonality and parameter-independent selection kernels.

**Dependencies and story role:** M10, M13–M14. Begins the converse from the same local physical experiment used by the construction.

**Conceptual connection:** Backaction constrains available directional information independently of how the controller processes its classical record.

**Source pointers:** Watrous §§1.2.2 and 2.3 for foundations; [Lower bounds: information acquired by an adaptive projective policy](../science/lower_bounds.md#information-acquired-by-an-adaptive-projective-policy).

### M22

**Phase:** Narrative and innovation.

**Central question:** Why must a precise final model pay κ/ε disturbance?

**Understanding target:** Apply the fixed-prior functional van Trees inequality to a direction coordinate and the complete history. Explain how uniform expected terminal accuracy yields a minimax lower term despite biased estimators and a finite startup subtraction.

**Dependencies and story role:** M07, M10 and M21. Converts the information budget into the terminal-precision obstruction.

**Conceptual connection:** A local prior witnesses a global minimax limit because the required estimator must work uniformly over the source family.

**Source pointers:** Watrous §1.2.2 for probability foundations; [Lower bounds: information inequality](../science/lower_bounds.md#a-fixed-prior-and-a-biased-estimator-information-inequality) and [cost of final precision](../science/lower_bounds.md#the-cost-of-final-precision).

### M23

**Phase:** Narrative and innovation.

**Central question:** Why does learning the next measurement axis already cost √(κT)?

**Understanding target:** Use the sign-invariant coordinate product a_xa_z as the estimate available before the next outcome. Connect the information budget for the previous history to a lower bound on the next disturbance and solve the cumulative quadratic inequality.

**Dependencies and story role:** M10, M13 and M21. Adds the causal cost that exists even without a stringent terminal target.

**Conceptual connection:** The measurement basis is an axis: a directed n·a prediction bound cannot replace a converse for the actual physical loss.

**Source pointers:** Watrous §§1.1.2 and 1.2.2 for foundations; [Lower bounds: a causal square-root cost](../science/lower_bounds.md#a-causal-square-root-cost).

### M24

**Phase:** Narrative and innovation.

**Central question:** Why does a logarithmic physical cost survive at exact purity?

**Understanding target:** Follow the quadratic Haar axis-prediction operator through its Dicke-basis Beta moments, its largest generalized eigenvalue and its positive-operator bound. Sum the resulting per-round axis error, and explain the depolarization relaxation that also transfers this lower bound to mixed sources.

**Dependencies and story role:** M11 and M13. Supplies the endpoint argument where division by κ is unavailable.

**Conceptual connection:** The symmetric-state machinery is inherited, while the evaluated quadratic loss matches the unoriented basis that is physically disturbed.

**Source pointers:** Watrous §§7.1.1 and 7.2.1–7.2.2; [Lower bounds: logarithmic bound for unoriented axes](../science/lower_bounds.md#a-logarithmic-bound-for-unoriented-axes); [Related work: standard proof ingredients](../references/related_work.md#standard-proof-ingredients).

### M25

**Phase:** Narrative and innovation.

**Central question:** How do the upper and lower arguments become one uniform frontier?

**Understanding target:** Combine the distinct Bayes witnesses through the minimax criterion and absorb bounded startup terms using the logarithmic bound. Match their sum with the same-policy upper bound for C₀/T≤ε≤ε₀, keeping constants uniform as r, T and ε vary jointly.

**Dependencies and story role:** M07, M12 and M19–M24. Integrates the construction and converse into the central theorem.

**Conceptual connection:** The maximum of separately necessary nonnegative costs is equivalent in order to their sum; a matching upper bound needs a single feasible policy.

**Source pointers:** Watrous §1.2.2 for the probability framework; [Frontier: uniform order theorem](../science/frontier.md#uniform-order-theorem); [Lower bounds: combining bounds and feasibility](../science/lower_bounds.md#combining-the-bounds-and-locating-feasibility).

### M26

**Phase:** Narrative and innovation.

**Central question:** When does terminal sample-optimality make disturbance linear?

**Understanding target:** At ε=A/T with sufficiently large fixed A, compare logarithmic cost at κ=0 with log(1+T)+κT at nonzero impurity. Distinguish this from the coarser-precision square-root regime, and retain all three terms when locating joint-limit crossovers.

**Dependencies and story role:** M25. Extracts the physical consequence from the complete law rather than a selected asymptotic term.

**Conceptual connection:** Optimizing measurements along the stream and demanding a standard-rate final estimate are different learning goals away from purity.

**Source pointers:** Watrous §§2.1.2 and 3.2 for state/metric foundations; [Frontier: precision changes the answer](../science/frontier.md#precision-changes-the-answer); [Interpretation: a concrete precision comparison](../science/interpretation.md#a-concrete-precision-comparison).

### M27

**Phase:** Narrative and innovation.

**Central question:** What does implementing the attaining policy actually consume?

**Understanding target:** Account for T preparations and readouts, the small persistent classical estimate, per-round arithmetic and basis synthesis, and the finite classical output. Explain why finite-digit errors are bounded by conditioning on the actual stored vector, with a possibly larger sufficient feasibility constant.

**Dependencies and story role:** M06, M18–M20 and M25. Connects the statistical law to a finite executable resource account.

**Conceptual connection:** A copy frontier becomes an implementation statement only after numerical conditioning, controls and outputs are charged.

**Source pointers:** Watrous §§2.1–2.3 for register/channel foundations; [Resources: resource statement](../science/resources.md#resource-statement), [digital state](../science/resources.md#a-digital-state-and-a-local-comparison) and [contraction under rounding](../science/resources.md#the-contraction-survives-rounding).

### M28

**Phase:** Narrative and innovation.

**Central question:** Which changes to the experiment escape the theorem's scope?

**Understanding target:** Keep the supplied-radius promise and no-quantum-memory chronology explicit. Distinguish implementing the selected Lüders basis from repairing the measured specimen, and distinguish nonselective physical disturbance from total conditional loss with its κT/2 floor.

**Dependencies and story role:** M03–M06, M13 and M25–M27. Sets the operational boundary before assessing significance.

**Conceptual connection:** An information–backaction theorem is a claim about a specified instrument; more general instruments or state replacement require a new comparison.

**Source pointers:** Watrous §§2.2–2.3 and §3.2; [Model](../science/model.md); [Interpretation: instrument choices matter](../science/interpretation.md#instrument-choices-matter); [Frontier: attribution and limits](../science/frontier.md#attribution-and-limits).

### M29

**Phase:** Narrative and innovation.

**Central question:** Which parts of the scientific account are inherited, proved and finitely checked?

**Understanding target:** Separate prior pure-state gentle tomography, the centered pure update, variance-aware bandits and generic information inequalities from the present uniform physical frontier. Match matrix, adaptive-tree, Beta-moment, recursion and simulation checks to their tested scope; none certifies every real parameter or an unrestricted instrument.

**Dependencies and story role:** M15, M21–M25 and M27–M28. Reconciles attribution and evidence with the exact contribution.

**Conceptual connection:** Independent finite calculations support mechanisms and implementations, while analytical arguments and source comparisons establish their respective broader claims.

**Source pointers:** Watrous §§2.2–2.3, 3.2 and 7.1–7.2 for the checked mathematical foundations; [Related work](../references/related_work.md); [Finite verification](../verification/README.md). Primary research citations provide attribution, not extra educational anchors.

### M30

**Phase:** Narrative and innovation.

**Central question:** What is the complete physical learning story for a chosen horizon, radius and target?

**Understanding target:** Explain the supplied source, one-copy policy, released states, terminal output, three necessary cost mechanisms, attaining schedule and charged implementation as one account. State the pure/mixed precision consequence together with its feasible regime, instrument restrictions and evidence limits.

**Dependencies and story role:** M12 and M25–M29, supported by the earlier mechanism and proof milestones. Integrates the entire project from local measurement to global capability and boundary.

**Conceptual connection:** The result is a joint information–backaction law for adaptive projective tomography, with a classical controller and no asserted quantum computational speedup or thermodynamic work theorem.

**Source pointers:** Watrous §§2.1–2.3, 3.2 and 7.1–7.2; [Scientific route](../science/README.md); [Frontier](../science/frontier.md); [Interpretation](../science/interpretation.md); [Resources](../science/resources.md); [Finite verification](../verification/README.md).
