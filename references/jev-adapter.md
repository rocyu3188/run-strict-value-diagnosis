# Optional Jev Batch Decisions

Read this reference only when using Jev. Follow the currently available tool or skill documentation. Do not assume that an installation path, API, credential, or previous connection remains valid.

1. Freeze the state, prohibited inferences, question bank, and candidate sets. Send only authorized material, never secrets or unrelated private context.
2. If the user requests one batch, include all noul/choice/score questions in one logical batch and verify complete coverage. Follow documented transport limits where needed, without silently dropping questions.
3. Preserve questions, candidates, results, and version information. Keep the tool's confidence semantics; normalized candidate weights are not necessarily calibrated real-world probabilities.
4. Calculate the user's defined composite, then apply independent gates. If weights, scales, or thresholds are absent, state “undefined.” A proposed heuristic must be labeled as a new proposal, not an established algorithm.
5. Write `human review` for low-confidence verdicts or primary-risk rankings. A high average score cannot override a failed critical delivery or evidence gate.
6. Disclose unavailability or failure. Independent analysis may continue, but never fabricate Jev outputs, confidence values, or a completed-batch claim.

Jev provides model judgments, not interviews, willingness-to-pay evidence, delivery outcomes, causal proof, or profitability evidence. Do not make one project's question bank universal. The user's bank takes precedence; any newly designed bank must be labeled as a design.
