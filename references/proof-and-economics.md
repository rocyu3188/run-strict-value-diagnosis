# Constraints on Realization, Attribution, Economics, and Compounding

## Evidence of Realization

Record purchase commitment, usable access, activation, first small value, first core value, repeated core value, and results over the full observation window separately. Clocks may run in parallel; do not move the starting point to the end of installation to hide the buyer's wait.

Define the measurement unit, eligible population or events, baseline, start and end points, state outcomes, resource burdens, sources, and missing-data rules. For businesses involving coordination among multiple parties, track “state known,” “responsibility assigned,” “action taken,” and “outcome verified” as separate dimensions so that assigning an owner does not conceal an unknown outcome. Establish precedence rules before aggregating mutually exclusive statuses; do not double-count.

The denominator includes all eligible opportunities during the service period, including events that should have been handled before exit but involved failed contact, incomplete work, or missing records. Report the exit rate, reasons, and unfulfilled obligations separately. Do not force events outside the service period after exit into the task denominator. If no opportunity occurred naturally, record it as unobserved; do not manufacture events to improve results.

Define the SOP, subjects, window, minimum meaningful improvement, and severe errors before setting thresholds. Unsupported thresholds of 90% or 95% are not universal standards. Average improvement must not conceal severe errors, tail waiting times, hidden labor, or work performed by other parties to fill gaps.

Separate the buyer's subjective belief, the conditional probability of the mechanism succeeding, and the probability of the final target event. Do not infer the latter from the former. A chain of conditional probabilities may express the mechanism; without measurements, do not assume independence and multiply probabilities to produce a falsely precise success rate.

## Attribution

State conclusions at the strength the evidence actually supports: a hypothesized mechanism, a verifiable case, before-and-after change, a comparable control, or stronger causal evidence. Weak evidence still permits a process review, but does not justify stronger causal language.

Check explanations such as natural adaptation, customer selection, task difficulty, observer attention, additional labor, parallel services, subsidies, and loss to follow-up. Comparison designs must fit the constraints of the domain; do not withdraw necessary support or create danger. Assess perception by checking accounts of specific events against records. Satisfaction, renewal, and payment support only the corresponding claims.

## Full Economics

First align the time window and cost attribution. The following is an illustrative formula that may be adapted:

`EP = R − D − C − L − A − S − F − J − T − kK`

- R: Net revenue from the portion fulfilled within this window, rather than total contract value or advance payments.
- D/C: Actual equipment, goods, communication, or resource costs.
- L: Full direct labor costs, including necessary idle time and employer costs.
- A: Customer acquisition, including a reasonable replacement cost for founder-led sales.
- S/F: Setup, support, quality, research and development, maintenance, administration, and other costs; distinguish direct from fixed attribution.
- J/T: Risk losses, taxes, and fees not already included elsewhere.
- kK: The cost of tied-up funds or required return on capital, calculated on a consistent basis without duplicating financing costs already deducted.

Deduct refunds, bad debt, and cancellations of unfulfilled work only once. When an entire device is delivered, count its actual cost. Reuse requires evidence of recovery, cleaning, wear, idle periods, and demand from the next customer. Attribute wages by task to avoid double-counting; unpaid founder work must not disappear. Capital principal is not an expense, but the timing of cash outflows must be included in the funding plan.

Distinguish contract value, net revenue, gross profit, contribution surplus with explicitly stated deductions, economic profit after all costs, and cash. Label sensitivity calculations as “the balance under this set of assumptions,” rather than current profit or a certain forecast. List unknown inputs as quotes or records still to be obtained; do not use figures from other cases as if they belonged to the business under review.

## Human Service Capacity, Where Applicable

Define the customer or other service unit explicitly. Use the same staffing block and the same complete time window:

```text
H = Required service labor hours per customer
W = Total employer cost per paid scheduled hour
B = All paid scheduled hours in the period
L = W × B
u = N × H / B
Labor cost per customer = W × H / u
```

If W already includes employer burdens, do not deduct them again. After allocating costs through utilization, do not add idle-time wages again. N is the number of customers actually served on the same measurement basis, not visits, new customers added in a month, or customers not observed over a complete window.

For a fixed, already staffed scheduling block, let g equal net revenue per additional customer minus incremental costs other than service labor and minus incremental acquisition costs. L is the labor cost already committed to that block. F is other fixed costs and excludes L. If g > 0:

```text
N_BE = (L + F) / g
N_safe ≤ u_safe × B / H
Required: N_BE ≤ Actual number of eligible, paying customers that can be served as promised ≤ N_safe
```

Round the break-even customer count up to the next integer. Measure u_safe empirically; peaks, review, support, and backup requirements constrain it. Do not assume it is close to 100%. Actual N_safe may be below the average-based formula. When g ≤ 0, adding customers cannot achieve break-even. When N_BE > N_safe, accepting more customers on the same staffing schedule cannot fix the problem. Recalculate L, F, g, and capacity when crossing staffing or overtime cost steps. For heterogeneous customers, recalculate by group and task mix.

Do not omit necessary service to make the formula work. Total labor growing linearly with customer count does not automatically disprove that expertise has been converted into software; examine changes in repetitive labor per unit and quality.

Build a separate cash timeline: can the lowest cumulative available cash balance plus available reserves cover delivery, possible refunds, and collection delays? Installments and prepayment are design choices contingent on the circumstances; do not assume either is superior. Earlier receipt of cash does not automatically improve economic profit.

## Compounding

Specify the chain: transaction completed → assets actually remain → rights to use them exist and they can be maintained → they improve a mechanism in the next cycle → outcomes or full economics improve at the same quality and difficulty → returns can be reinvested.

Assets may include funds, methods, evidence, product capabilities, relationships, and reputation. Not all assets have network effects. Account for maintenance, obsolescence, employee turnover, non-exclusivity, and competitive substitutes.

Test the arrows using comparable cohorts, personnel, and conditions. Rule out easier customers, higher prices, subsidies, and founder overtime. Without evidence, state: “No validated structural compounding has been identified.” Stable, high-quality service can be viable without pursuing unsuitable membership models, platforms, or product expansion.
