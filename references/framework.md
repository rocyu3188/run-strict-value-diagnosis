# Complete Framework and Question-by-Question Requirements

## The Nature of Value

`V(X | A,C,t) = E[U_A(S_with X) − U_A(S_without X)] − Cost_A(X)`

Specify X (the intervention), A (the evaluating party), C (the context), and t (the time window). The without-intervention state uses the best alternative actually feasible in the same context. This may include an existing product, human labor, an existing internal workflow, or taking no action. Do not construct a baseline designed to fail; mark the alternative as unknown when it is unknown.

Costs must be converted to the same utility scale as U before subtraction. Without preference weights, keep separate accounts of state changes and monetary, time, and burden costs; do not calculate a falsely precise aggregate score. Resources can instead be included in the state: `E[U_A(S_with,R_with)] − E[U_A(S_without,R_without)]`. In that case, do not subtract the same resource costs again.

Do not directly sum different people's utilities. Identify who benefits, who bears the burdens, and whether they accept those burdens voluntarily; averages must not conceal a transfer of burdens onto one party. Risk concerns both probabilities and consequences, and average convenience must not offset severe tail losses. If option value is already reflected in the payoff from choosing the best action in each scenario, do not add it again.

## Eight Types of State Change

For each type, specify the party, mechanism relative to the baseline, existing evidence, measurement definition, disconfirming evidence, and reasons for any Unknown/N/A designation.

| No. | Type | Change to identify | Common error |
|---|---|---|---|
| 1 | Reduced risk | The probability and consequence distribution of adverse states, including newly introduced risks | Process completion rates do not establish a reduction in ultimate losses |
| 2 | Greater certainty | More accurate judgments and greater control over relevant variability | Greater confidence does not mean greater accuracy; an unknown result may be honest feedback |
| 3 | Expanded options | More actions or goals that are actually accessible and executable | More menu choices or a theoretically available path do not establish practical usability |
| 4 | Reduced friction | Lower net burdens of operation, coordination, understanding, and transactions | Reducing one party's burden by transferring it to another |
| 5 | Reduced time costs | Less waiting or active effort required to reach the goal, measured separately | Do not count the same improvement twice as both reduced waiting and saved labor hours |
| 6 | Certainty-providing feedback | Timely, credible, understandable feedback that helps decisions | This is often a mechanism for type 2, rather than an additional independent benefit |
| 7 | Lower probability of failure | The distribution of success after defining the task, eligible opportunities, and failure modes | Uploading, logging in, or making contact does not establish task success; this type may overlap with risk reduction |
| 8 | Improved financial capital position | Net improvement in the party's future cash flows, financial assets, and room to allocate capital | Do not substitute knowledge, records, or SOPs for financial improvement; those belong under options or business assets |

These are projections of the same underlying state, not eight additive pools of value. Without evidence of financial improvement, type 8 can be unknown or not applicable; other benefits may still be sufficient to justify a purchase.

## The 25-Question Canvas

In a complete report, give each question its own Markdown heading, such as `### Q1 | Who is in what state?`, through Q25. Questions may be arranged by module in the order Q1–18, Q22, Q19–21, Q23–25, but each question must have exactly one formal heading.

Each answer must establish: **current answer → supporting mechanism/conditions → evidence and confidence → next validation step and conditions that would overturn the answer**. There is no need to repeat these labels mechanically, but do not merely paste the question or end with “to be validated.”

| Module | Question | Answer requirements |
|---|---|---|
| Creation | Q1 Who is in what state? | Specify the party, event, and context; do not infer needs from demographic or segment labels |
| Creation | Q2 What is the target state? | Describe observable changes; distinguish outcomes from features and activities |
| Creation | Q3 How important is the state gap? | Examine frequency, consequences, and resources devoted to alternatives; a severe underlying problem does not establish a large incremental product benefit |
| Creation | Q4 What is the value-creation mechanism? | Intervention → behavior → intermediate state → outcome → net value; every arrow must be open to challenge |
| Creation | Q5 How large is the potential value? | Deduplicate incremental value at the individual level; do not substitute TAM, total losses, or revenue |
| Exchange expectations | Q6 How can the value proposition be stated concisely? | Specify the intended recipient, scope, change, and boundaries |
| Exchange expectations | Q7 Why should anyone believe it? | Match evidence to the claim; distinguish vision, demonstration, cases, and strength of causal evidence |
| Exchange expectations | Q8 What is the expected probability of success? | Separate subjective judgment from the actual probability of the mechanism succeeding; do not invent numbers for unknowns |
| Exchange expectations | Q9 Who benefits? | Identify net improvements and harms for each party |
| Exchange expectations | Q10 Who uses it? | Identify actual participants and required capabilities, rather than only listing people who log in |
| Exchange expectations | Q11 Who decides? | Those who propose, veto, approve, and participate on an ongoing basis may differ |
| Exchange expectations | Q12 Who controls the budget? | Identify available budget, competing uses, and cost sharing; having money does not establish a budget for this purchase |
| Exchange expectations | Q13 Who pays? | Identify the funding source, unit of exchange, and evidence of payment; a provisional price is not a completed transaction |
| Exchange expectations | Q14 What are the alternatives? | Identify the best combination that can actually be executed in the same context |
| Capture | Q15 At what point is payment charged? | Explain its relationship to deliverables, acceptance, fulfillment, and exit |
| Capture | Q16 What is the pricing unit? | Examine alignment with value, cost heterogeneity, and perverse incentives |
| Capture | Q17 Are price and value aligned? | Examine actual willingness to pay, non-price costs, customer surplus, and full costs |
| Capture | Q18 Where do capture rights reside? | Examine contracts, capabilities, rights, and pressure to bypass the business; an account is not a moat |
| Realization | Q19 How long does it take for value to arrive? | Track purchase, access becoming available, activation, first and repeated core value, and the full cycle |
| Realization | Q20 How is state change demonstrated? | Specify baseline, end state, difference, window, full denominator, burdens, and failures |
| Realization | Q21 How is the change attributed? | Examine the causal chain, comparisons, alternative explanations, selection bias, and the limits of what the evidence supports |
| Capture | Q22 Do unit economics hold after all costs? | Test economics, cash, capacity, demand, and competition together |
| Realization | Q23 Do users perceive the value? | Compare each role's account against actual records; perception does not replace outcomes |
| Compounding | Q24 What long-term assets accumulate? | Identify assets that actually remain, can be used and maintained, and have a purpose |
| Compounding | Q25 How do those assets improve the next cycle? | Demonstrate comparable improvements across cohorts or personnel, ruling out explanations such as selecting easier customers |

Insufficient willingness to pay establishes only that exchange has not occurred under the current offer, level of belief, budget, or adoption conditions. It does not, on its own, disprove potential value; nor can potential value justify claiming payment that does not exist.

## Creation × Capture and Movement Between Positions

Horizontal axis: incremental state improvement relative to the best alternative. Vertical axis: the ability to retain economic returns sustainably after fulfillment, full costs, and competition.

- High creation × high capture: a candidate for strong economic structure; calling it a compounding machine additionally requires cross-cycle evidence for Q24–25.
- Low creation × high capture: a candidate for rents or control rights; examine rights, bypass options, and customer surplus.
- Low creation × low capture: a candidate for a commoditization trap; “unknown” is not evidence of low creation.
- High creation × low capture: a candidate for value leakage; establish high creation first.

Judge each axis separately, and mark only an axis with insufficient evidence as unknown. If both axes are unknown, place `Unknown / Unknown` outside the chart. If evidence supports a conclusion on one axis, preserve it—for example, “creation unknown; capture does not hold under the current cost structure.” Do not relabel a known problem as unknown. Do not invent coordinates or maturity levels without sufficient grounds. When scoring, state the scale, basis, and confidence; do not score unknowns as zero or fill them with midpoint values, and do not let an aggregate score override a critical disqualifying condition.

Describe the evidence that would trigger movement: the incremental-value mechanism for moving right, the capture mechanism for moving up, and the ways stronger alternatives or changing contexts could move the position left, while upstream providers, channels, competition, or costs could move it down. Profit growth resulting from reduced necessary delivery or misleading claims does not count as healthy movement.

## Ten Structural Signals

For each signal, list current evidence, the conditions under which it holds, and disconfirming evidence. Not all signals are required. An important task is not automatically a bottleneck, and reasonable returns earned by other participants are not automatically leakage.

| No. | Signal | Test for whether it holds |
|---|---|---|
| 1 | An unavoidable transaction node | Real transactions must pass through it for settlement, trust, or an essential function, and bypassing it is difficult; an entry point or QR code is insufficient |
| 2 | A mission-critical workflow | Removing it materially worsens the same task, after ruling out equally effective existing alternatives |
| 3 | Bottleneck economics | It removes a specific constraint, the critical capability is scarce and difficult to replace, and the business can retain the resulting returns |
| 4 | A standard setter | Independent external participants actually adopt the standard, with a basis for governance and capture; an internal SOP is insufficient |
| 5 | Two-sided network effects | Growth on one side improves the other, which reinforces the first, after accounting for additional inputs and congestion |
| 6 | A high outcome-value-to-cost ratio | Attributable incremental value exceeds price and adoption costs; do not claim all potential losses as value created by the product |
| 7 | Expertise converted into software | Repetitive labor, rework, or errors per unit decline at the same quality and task difficulty; necessary human staffing may still grow linearly |
| 8 | A platform ecosystem | Independent complementors actively invest to create complementary value, with sustainable distribution of returns; a procurement supply chain is insufficient |
| 9 | A membership aggregator | Ongoing benefits meet recurring demand, aggregation adds incremental value, and costs are affordable; a fixed-term service package is insufficient |
| 10 | Long-term compounding assets | Assets from one cycle improve the next within authorized uses, after maintenance, depreciation, and attrition |

## The Six-Stage Path

For each stage, specify actions, confirmed or proposed owners, outputs, evidence gates, and failure or return gates.

1. **Create:** Establish a real residual state gap and an executable mechanism.
2. **Believe:** Use evidence matched to the claim to update buyer judgment; the buyer's restatement must stay within the actual scope.
3. **Exchange:** Participants accept the burdens, the decision and budget chain holds, and a real commitment with a cost occurs.
4. **Realize:** Observe net improvement, failures, burdens, and attribution using the complete measurement scope.
5. **Capture:** Full economics, cash obligations, reliable capacity, and real demand hold together.
6. **Compound:** Usable assets enable other personnel or subsequent comparable customers to achieve better creation or capture.

Measure each cohort over a complete cycle beginning when access actually becomes available. Exploratory samples identify mechanisms and failures; they do not support stable estimates of market-wide rates. Separate learning losses from mature profitability. A normal exit at the end of the term may indicate task completion; do not automatically interpret it as churn or require renewal.
