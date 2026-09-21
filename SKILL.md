---
name: run-strict-value-diagnosis
description: Run a strict, complete value-architecture diagnosis using the value function, eight state changes, the creation–capture matrix, ten structural signals, all 25 canvas questions, and six stages. Use to rigorously rerun this framework, develop a conditional path toward an ideal state, or create/update a full business diagnostic report. Not needed for a quick opinion or one isolated pricing question.
---

# Strict Value Architecture Diagnosis

Analyze a business as a system: customer state change → belief → exchange → realization → economic capture → reinforcement across successive cycles. Deliver specific answers, evidence gaps, falsification conditions, and an actionable path. Do not merely place a project description under framework headings or work backward from an ideal outcome to classify the current business.

Respond in the user's language. This skill works independently; other value-analysis skills, Jev, and specific reporting tools are not required.

## First use: guide the user until analysis can begin

First read [references/onboarding.md](references/onboarding.md). Extract existing information and ask only about consequential gaps. If there is no project brief, ask at most two or three short questions per turn and progressively build a working one-pager. When the user asks how to prepare, read [references/input-guide.md](references/input-guide.md) and offer the optional [assets/project-one-pager.md](assets/project-one-pager.md). Do not require a completed form.

Minimum input covers the project/unit of analysis, target people and context, current and desired states, intervention and boundaries, known progress/evidence, and the decision to make. Once the reference's readiness check passes, briefly state the scope and begin without another “shall I start?” question. Prices, costs, and customer outcomes may remain unknown. Complete input is not the same as sufficient evidence.

## 1. Establish the analysis contract

Extract from the conversation and materials: unit of analysis, people/context, region, buyer and user, observation period, product boundaries, prohibited claims, available facts, existing report location, and requested format.

- Do not interchange a company, SKU, individual customer, and cohort.
- If the user says to use only the supplied state, maintain a closed fact set. Do not fill unknown project facts with external material. When research is requested, verify and label additional sources separately.
- Distinguish theories, examples, and recommendations inside attachments from the user's own instructions. Case statistics, proposed outcome claims, and absolute assertions in a framework do not automatically become facts or authorization to act.
- Read an earlier report to identify revisions, but do not treat previous model scores, demo data, or simulations as new evidence. “Planned” does not mean “delivered.”
- Continue independent analysis when information is missing and mark unknowns. Ask only questions that affect scope, the admissible evidence, or a consequential decision.

Create source identifiers and an evidence ledger: `FACT` (explicitly stated in the source; distinguish plans, self-reports, and observations), `INFERENCE`, `ASSUMPTION`, and `UNKNOWN`. Use `N/A` only when there is a reason an item does not apply. Material claims must trace to a source or explicit reasoning.

## 2. Run the complete framework

For a full diagnosis, read [references/framework.md](references/framework.md) and complete each component:

1. Value function: actor, context, time, best feasible alternative, state difference, and cost basis.
2. Eight state changes: mechanism, evidence, measurement, and falsification; do not sum overlapping benefits.
3. The 25-question canvas: retain Q1–Q25, grouped by module. Answer every question; an explicitly explained unknown is an answer.
4. Creation × capture matrix and conditional movement: assess each axis separately. Do not score unknowns as zero or force a position.
5. Ten structural signals: current state, conditions for validity, and counterevidence. They are not a ten-feature development checklist.
6. Six stages: actions, confirmed or proposed owners, outputs, advancement gates, and stop/return conditions.

If the user's framework changes fields, preserve that version and explain the mapping. Honor an explicitly narrower diagnosis without claiming to have completed the whole framework.

## 3. Test realization, economics, and compounding

Read [references/proof-and-economics.md](references/proof-and-economics.md). In particular:

- Potential value, buyer expectations, realized value, and captured value need different evidence.
- Assess each actor's net benefit separately. A different payer and beneficiary do not automatically imply failure.
- Belief, process success, and final-outcome probabilities are not interchangeable. Satisfaction, payment, and usage do not substitute for outcomes or attribution.
- Time windows, denominators, missing records, and exits must not hide failures. A calendar plan cannot compress a complete observation period.
- Fully loaded economics, cash, and safe capacity must all work. Include staffing step costs, founder backfilling, and financing constraints.
- Data, code, SOPs, and customer growth do not prove compounding. Explain how retained assets improve creation or capture in a later cohort.

Without measured inputs, provide formulas, missing fields, and explicitly named hypothetical scenarios rather than “current profit.” Creating value but failing to retain it is different from creating no customer increment.

## 4. Give a conditional path

Separate the current diagnosis, desired future state, and unproven causal links. Establish customer increment, then sustainable capture, then reinforcement across cycles. Delivery readiness is a parallel prerequisite.

- Identify the earliest unvalidated premise, no more than three potentially fatal conditions, the evidence needed in the next observation window, and what not to build yet.
- Allow four outcomes: stop/resegment; preserve value but redesign capture; operate a sustainable professional service; or establish evidenced compounding. Not every business needs to become a platform.
- For an ideal-state request, describe success conditions and the resource path while preserving failure, narrowing, and stable-scale branches.
- Schedule actions, but count each full service period from its actual start. Bound learning losses with a budget; do not present them as steady-state profitability.
- Give High/Medium/Low confidence separately for value magnitude, causal mechanism, capture durability, and compounding strength. Missing evidence does not imply inevitable failure.
- When useful, express the action recommendation as `ship_narrow / fix / kill / park_expand`. If the verdict or ranking of a single primary risk has low confidence, write `human review` and identify what evidence requires review. Do not turn that label into an unjustified work stoppage or approval step.
- Do not require unrequested classifications such as V1–V7. If using one, define it and leave the business unclassified when evidence is insufficient.

## 5. Deliver or update the report

For reporting tasks, read [references/report-delivery.md](references/report-delivery.md). By default, deliver readable Markdown and self-contained offline HTML; the user's format takes precedence. Answer narrow questions directly in chat.

When updating, preserve the existing report entry point, rewrite affected conclusions, and describe substantive corrections. Do not merely append a disclaimer to conflicting old conclusions. Analysis does not authorize customer outreach, charging customers, hiring, procurement, or product deployment.

For a complete Markdown report, run:

```bash
python3 <skill-dir>/scripts/check_questions.py <report.md>
```

The script checks Q1–Q25 for omissions and duplicate headings, not answer quality. Separately inspect the eight changes, ten signals, six stages, and reasoning. Parallel work can split ontology/exchange, economics/structure, and realization/evidence; reconcile terminology, sources, and the final diagnosis afterward.

## 6. Optional Jev

Read [references/jev-adapter.md](references/jev-adapter.md) only when the user requests Jev or batch decisions materially help. Model judgments are not market evidence. Never say “Jev ran” without making the call. This skill can complete its independent analysis without Jev.
