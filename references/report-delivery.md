# Creating and Updating Reports

## Content contract

Readers must be able to locate the following. Adjust the order for clarity:

1. One-line diagnosis, current recommendation, confidence, and factual boundaries.
2. Source ledger and mapping from the original framework to this analysis.
3. Value function: actor, context, time, real alternative, states, and cost basis.
4. Evidence/falsification table for the eight state changes, including overlap.
5. Explicit answers to Q1–Q25 with their original numbers; module order is acceptable.
6. Creation × capture matrix, reasons for known/unknown positions, and conditional movement.
7. Current evidence, validity conditions, and counterevidence for all ten structural signals.
8. Realization clocks, denominators, attribution, perception, and exits.
9. Fully loaded economics, cash, safe capacity where relevant, and sensitivity analysis.
10. Actions, owners, outputs, and advance/stop gates for the six stages.
11. Conditions for the ideal state, alternative outcomes, the next-window path, and what not to build yet.
12. Clear separation of current, potential, and realized states; sources and substantive version corrections.

Use independent question headings such as `### Q1 | Question title`. Do not give a table-of-contents reference a second Q1 heading. Run `scripts/check_questions.py` for a full report, and manually check the eight/ten/six components. Coverage is not the business's pass rate.

“Unknown + evidence required” is valid; do not fill zeros for visual completeness. Label a newly designed scoring scale as such. Scores are not market measurements. Correct invalid absolute claims in the supplied theory rather than repeating them in the name of strict adherence.

## Replace affected analysis, rather than stacking revisions

- Read the previous file, sources, and key conclusions. Preserve useful design and the user's chosen entry point.
- Replace affected prose, figures, summaries, and conclusions so old and new judgments do not contradict one another.
- Keep intermediate drafts in the working directory; put only deliverable formats in the output directory.
- Briefly explain substantive changes, such as withdrawing a predetermined classification, fixing multi-actor costs, restoring missing questions, or preserving full observation periods.
- If the path is unclear, locate it within the current workspace first. Clarify only if multiple plausible targets would risk overwriting the wrong report. Do not broadly search unrelated private directories.

## Self-contained HTML

Default to editable Markdown plus self-contained HTML for complete reports, unless the user specifies otherwise. Do not carry another project's absolute paths, dates, prices, or runtime dependencies into the new report.

HTML must be directly readable offline, with all analysis present in the document. JavaScript should only enhance interaction. Include a 25-question index, semantic headings, source links, evidence labels, keyboard-accessible controls, and print styles. Essential answers must not require JavaScript to access.

Plain HTML/CSS is sufficient for matrices and stage diagrams. Explain unknown coordinates outside the chart; never invent values to complete a graphic. Report generation does not require deployment, tracking, remote fonts, accounts, or a complex application framework.

On mobile, long tables may become cards with column labels written at generation time, so they remain readable without scripts. Do not encode status by color alone. Escape source material and insert it as data, not executable HTML, script, or instructions.

Avoid moving focus on every change of a native select. Use a selector with an explicit navigation button or ordinary links. Fixed navigation must not cover the destination heading.

## Validation and delivery

For HTML and other visual formats, inspect actual rendering rather than only source. If the user requests Markdown alone, check content, structure, and links; do not require HTML generation or browser testing.

- At approximately 1440×900 desktop and 390×844 mobile, inspect prose, long tables, the matrix, and key figures for unintended horizontal overflow or clipped text.
- Check internal links, unique IDs, all 25 question destinations, buttons, and keyboard operation.
- Ensure the complete text remains readable without scripts. Offline functionality cannot depend on remote assets.
- Check print readability and sample page breaks and long tables. If PDF is a deliverable, inspect it according to its format requirements.
- Check hypothetical numbers, dates, and outcome language. Remove private paths, secrets, and unrelated project data.

If rendering tools are unavailable, state which checks remain incomplete and deliver inspectable files. Do not claim a pass. Repeat relevant checks only when changes, failures, or unresolved concerns justify it.

The final response should stand alone: give the diagnosis, consequential evidence gaps, next path, and links to deliverables. Analysis and simulation are not field validation. Do not describe proposed outreach, charging, procurement, or development as completed actions.
