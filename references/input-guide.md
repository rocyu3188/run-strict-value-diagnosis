# Preparing Inputs and Checking Tool Dependencies

## What is enough to start?

A business plan is not required. These six pieces of information are enough to begin:

1. What the project is, and whether to analyze the whole company or one product or service.
2. Who has the problem, in what situation, who uses the solution, and who might pay.
3. How they handle it now, and what state you want to change.
4. How the product would produce that change, including what it explicitly does and does not do.
5. What has been done and what evidence exists. If there is none, write “not yet validated.”
6. What decision this analysis should support, plus constraints on resources, time, factual sources, and output.

Extract answers directly from an existing introduction when possible. Ask only the minimum questions if the core description remains unclear. Prices, costs, and roles can be marked unknown; do not make the user gather every data point first. If the project is entirely undefined, do not fill the diagnosis with invented details.

## Recommended one-pager

Use [../assets/project-one-pager.md](../assets/project-one-pager.md). Aim for roughly one or two pages, with a few sentences in each of the nine sections. The project name can be anonymous, and trade secrets are not needed. Give the period, unit, and source for each number. For each piece of evidence, explain what it supports and what it does not support.

| Section | What to include | Why it matters |
|---|---|---|
| Project and scope | One-sentence description, business unit, region, stage, and service or value observation period | Prevents mixing units of analysis and situations |
| People and states | Users, beneficiaries, decision-makers, budget owners, and payers; before and after states; real events | Identifies who benefits and who bears the burden |
| Existing alternatives | What people actually do, the costs and time involved, and what remains unresolved | Establishes what would realistically happen without the solution |
| Mechanism of change | Key actions, division of work between people and software, dependencies, and boundaries | Allows each causal link to be examined |
| Exchange design | Who buys and why, the pricing unit, when payment occurs, promises, and exit terms | Separates willingness to pay, ability to pay, and transaction structure |
| Existing evidence | Sources, dates, samples, sales, use, outcomes, and failures; say plainly when data is missing | Separates proposals and self-reports from observed behavior and outcomes |
| Delivery and economics | Staff and capacity, effort per customer, variable and fixed costs, acquisition, and cash | Tests reliable delivery and how much value the business actually retains |
| Assets and dependencies | Reusable capabilities, data usage rights, external dependencies, and how the next cycle improves | Prevents mistaking growth for compounding |
| This assignment | Decision, resources and deadline, allowed factual sources, prohibited claims, report path, and whether to use Jev | Establishes the scope and deliverables for this round |

An “ideal customer profile” cannot replace evidence from real customers. Specify whether “interest” means a verbal statement, registration, a deposit, or full payment. Separate the working price, actual transaction price, and net revenue. Do not combine posts, interviewees, customers, and transactions into one sample count.

## Include these if available; they are not prerequisites

- Anonymized interview summaries and recent real events. Include views from both or all sides, rather than selecting only praise.
- Actual quotes, payments and refunds, service logs, before and after baselines, and failure records.
- Equipment or supplier quotes, staff hours, capacity, acquisition sources, and definitions of what costs include.
- Previous reports and factual source files, with outdated or corrected information identified.
- Validation conditions and business boundaries that cannot change. Include only the parts of existing contracts or permissions needed for the analysis.

A one-pager can start a full diagnosis, but is usually not enough to establish causality, stable demand, complete economics, or compounding. The deliverable must clearly show which conclusions remain hypotheses because evidence is missing.

## Jev is optional

The base version only needs an agent that supports local skills. The included Q1–Q25 checking script is optional and uses only the Python 3 standard library. Verify HTML rendering with the tools available in the current environment; do not assume the recipient has software installed on the author's machine.

If the user chooses Jev, first check whether callable Jev tools or skills are available and credentials are configured. Then read [jev-adapter.md](jev-adapter.md). If anything is missing, state clearly: “Jev is not available yet; it needs to be installed and configured first.” Obtain the steps from tool documentation that can be verified in the current environment or from official installation instructions. Do not invent installation commands or URLs, and do not ask the user to send an API key in chat.

Install or change integration settings only with the user's authorization. If Jev is optional, clearly state that Jev was not run this round and continue with the framework-based diagnosis without it. If the user requires Jev results, complete the remaining work and explicitly leave the Jev portion pending. Do not silently substitute another approach. If installation is unavailable, provide verifiable next steps rather than claiming it has been installed.
