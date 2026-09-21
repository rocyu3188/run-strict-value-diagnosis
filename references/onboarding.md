# Getting Started and Filling Gaps

Help a new user turn even a rough introduction into enough context for a diagnosis. Make clear what is known and what is unknown, then begin. The goal is not to collect a complete business plan or ask the user to answer all 25 diagnostic questions first.

## Choose the starting point

- If the user has already provided a one-pager, business plan, conversation context, or previous report, extract the information from it. Do not start asking the same questions again.
- If there are no materials, or the user says they do not know where to start, guide them through the missing information.
- If the user explicitly asks for an immediate analysis of the available materials, run it as soon as the business can be identified. Mark missing information as unknown. If even the subject of the analysis is unclear, ask only what should be analyzed.
- If the user only wants a template, provide the template and brief instructions for filling it in. Do not start a new project diagnosis without being asked.

A short introduction can help: “You can paste a project description. If you do not have one, I can ask a few questions at a time and organize your answers into the input for the analysis. It is fine to say ‘unknown’ when you are unsure.” Do not turn this introduction into a mandatory choice of modes.

## Pace the questions

The groups below describe gaps to fill, not a fixed questionnaire. Ask no more than two or three short, specific questions per round. Prioritize missing information that would change the analysis. Skip anything already answered. After each reply, update the working summary before asking the next group. Use an asynchronous question tool if the environment provides one; otherwise, use normal conversation. While a key question remains unanswered, do not treat silence as agreement or repeatedly send the same questions.

### A. Clarify what is being analyzed

Possible questions:

1. “What product or service do you plan to sell, and who will mainly use it?”
2. “When do they usually need it? What specifically is difficult for them now?”
3. Only if needed: “What decision do you most want this analysis to help with: what demand to validate first, whether to launch, or how to fix an existing business?”

Do not ask for business-model terminology, complete costs, or a position in the matrix at this stage. If the user only says “an AI platform,” ask for one specific task and one specific type of user. Do not invent a market for them.

### B. Clarify the change and the existing alternatives

Possible questions:

1. “How do they handle this today without your solution? Do you know of a recent, specific example?”
2. “Which step would your solution change? What do you ultimately want to improve for them?”
3. “Who uses it, who decides, and who pays? Your current assumptions are fine.”

If there is no real example, label the problem as a hypothesis. Do not pressure the user to invent a case. If the user does not know the alternatives, record them as unknown and make them an early validation priority in the report. When explaining “alternatives,” use general categories such as phone calls, manual work, or existing tools. Do not present these examples as facts about the project.

### C. Establish progress and boundaries

Ask only about information that is still missing and matters:

1. “Is this an idea, a prototype, a trial, or something people already pay for? What records could be checked?”
2. “What does the software do, what depends on people, and what do you explicitly not promise?”
3. “How much time and what resources can you commit to this round? What conditions cannot change?”

If price or cost is central to the current decision, ask for known amounts, the billing unit, the period, and whether each figure is estimated or actual. If these are unknown, continue the diagnosis with those unknowns recorded. Do not keep asking for data that does not exist.

## Working summary and gap log

Briefly show a summary when useful:

| Field | Current record | Status |
|---|---|---|
| Unit of analysis, subject, and situation | Extracted from the user's materials | Clear / Needs confirmation |
| Current approach, intended change, and mechanism | Condensed from the user's words without upgrading the evidence | Fact / Hypothesis / Unknown |
| Payment, delivery, costs, and outcomes | Record the source, observation period, and units | Measured / Self-reported / Planned / Unknown |
| Current decision and boundaries | Requirements from the conversation | Clear / Critical gap |

Classify gaps as **blocking the analysis** (the subject, mechanism, or task is not identifiable), **limiting confidence** (actual willingness to pay, costs, outcomes, and similar information are unknown), or **safe to fill later** (noncritical details). Do not classify every unknown as a blocker.

## Minimum readiness check

Start as soon as these conditions are met:

- One product, service, or company-level unit specified by the user can be identified.
- At least one type of beneficiary or user and their situation can be identified.
- The intended improvement and the mechanism for producing it can be described. They may be hypotheses explicitly identified as such by the user.
- Major boundaries are known, or nothing in the materials indicates an unresolved conflict about scope.
- It is clear whether the user wants a full diagnosis or help with a particular decision. “Run this skill” can be treated as a request for a full diagnosis.
- Existing evidence can be distinguished from missing evidence. A completed sale is not required.

Actual alternatives, prices, costs, buyers, and outcomes may remain unknown. These unknowns limit the corresponding conclusions; they do not automatically block the entire analysis. If a critical scope conflict remains, ask only about that conflict rather than sending a long questionnaire.

Once the conditions are met, state: “This round will analyze [scope]. [Key unknowns] will remain explicitly marked as assumptions or evidence gaps.” Then read the framework and begin. Do not add an unnecessary “Please confirm that I should start” step. If the user corrects the scope, update it and continue.

## Defaults and tool checks

- Use the user's language. If no boundary on factual sources is specified, prioritize the materials they provided. If external verification is needed, follow the environment's rules and distinguish the sources. Do not present external research as internal company facts.
- If no output format is specified, provide a full diagnosis in Markdown and HTML. In a limited environment, provide readable text first and explain which parts could not be generated or verified.
- Jev is not required by default. If the user mentions Jev, check the tools and configuration using [input-guide.md](input-guide.md) and [jev-adapter.md](jev-adapter.md). If unavailable, state that installation or configuration is needed. Do not invent an interface or ask the user to send credentials in chat.
- If the user requires Jev, do not claim that a complete Jev diagnosis is finished unless Jev was successfully called. Other analysis and input preparation can continue.
- Gathering the missing information does not authorize external actions such as contacting customers, charging money, or deploying a product.
