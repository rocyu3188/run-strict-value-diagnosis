# Strict Value Architecture Diagnosis

A reusable Codex skill for evaluating whether a business improves customers' lives, retains enough economic value to operate sustainably, and becomes better at doing both over time.

Start with a project brief or a rough idea. The skill guides you through missing information, then runs an evidence-based diagnosis. It contains no built-in client case, personal data, account details, or credentials.

**New here?** Follow the [step-by-step user guide](docs/USER-GUIDE.md): download → install → fill or discuss your brief → give it to Codex → receive a report. You do not need Git commands or your own branch to use the skill.

**Which file goes where?** The repository ZIP installs the skill. Your filled-in one-pager and evidence go into your Codex task, not into this public repository. Branches and pull requests are only for changing the shared skill itself.

## Quick start

After installation, paste this into Codex:

> Use $run-strict-value-diagnosis. I want to analyze a project, but I do not have a complete brief. Ask me two or three questions at a time and build a working one-pager. Once there is enough information, start the diagnosis and generate the report.

Already have a brief?

> Use $run-strict-value-diagnosis with the project introduction below. Extract what is already known and ask only about consequential gaps. Use only the facts I supply. Mark unknowns rather than inventing them, then complete the diagnosis.

Paste your introduction or attach it. You can also fill in the [project one-pager template](assets/project-one-pager.md). Unknown prices, costs, and customer outcomes are acceptable: they limit confidence, but do not automatically block analysis.

## Install

**With Codex (recommended):** paste this request:

> Use $skill-installer to inspect and install the run-strict-value-diagnosis skill from the root of https://github.com/rocyu3188/run-strict-value-diagnosis on its main branch. Preserve all supporting files and verify that it is available.

Alternatively, open the [repository](https://github.com/rocyu3188/run-strict-value-diagnosis), choose **Code → Download ZIP**, and provide the ZIP's local path or attach it if your client supports that file type:

> Inspect this archive and install the folder containing SKILL.md as my personal run-strict-value-diagnosis skill. Preserve the supporting files, use the skill directory supported by my Codex installation, and verify that it is discoverable.

**Manually:** extract the repository and copy the entire folder into a supported skill directory, naming it `run-strict-value-diagnosis`. Current OpenAI documentation lists `~/.agents/skills/` for personal skills and `.agents/skills/` inside a project for project-specific skills. Prefer the installer if your setup uses another configured location. Keep all supporting folders; do not copy only `SKILL.md`. If the skill does not appear, restart Codex. [Official skill documentation](https://learn.chatgpt.com/docs/build-skills)

For website-only downloading and detailed installation checks, see the [user guide](docs/USER-GUIDE.md). GitHub's ZIP may unpack as `run-strict-value-diagnosis-main`; the installed folder should be named `run-strict-value-diagnosis`.

## What input is needed?

The minimum is enough information to identify:

- The product or service and the unit you want analyzed.
- Its intended users or beneficiaries and their situation.
- The current problem, desired state, and proposed mechanism.
- Product boundaries and any claims it must not make.
- What has actually happened, versus what is planned or assumed.
- The decision you want to make.

You do not need a business plan or completed sales. The guided intake asks at most two or three short questions per turn, distinguishes essential gaps from missing evidence, and starts automatically once the minimum is clear. It does not ask you to answer the 25 diagnostic questions yourself.

For stronger conclusions, optionally supply anonymized interviews, transaction and refund records, service logs, costs, capacity, baseline comparisons, and an earlier report. See the [input guide](references/input-guide.md).

## What the diagnosis covers

| Component | Coverage |
|---|---|
| Value function | Actor, context, time, best feasible alternative, and net state change |
| Eight state changes | Risk, certainty, options, friction, time, feedback, failure, and financial capital |
| 25-question canvas | Creation, buyer belief, exchange, capture, realization, and compounding |
| Creation × capture matrix | Separate evidence for each axis and conditional movement |
| Ten structural signals | Testable mechanisms rather than assumed moats or feature requirements |
| Six-stage path | Create → Believe → Exchange → Realize → Capture → Compound |
| Economics and proof | Attribution, fully loaded costs, cash, and safe capacity where relevant |

Every material claim is distinguished as `FACT`, `INFERENCE`, `ASSUMPTION`, or `UNKNOWN`. Unknown is not zero. An ideal future state is a conditional path, not a predetermined verdict. A reliable, profitable professional service is a valid outcome; a platform is not mandatory.

Full reports default to editable Markdown and self-contained offline HTML. You can request a different format or a narrower chat response. To update a report, provide the existing file and ask for an update.

## Optional Jev

Jev is **not required** for the core analysis. If you want it, add:

> Also use Jev for batch decisions. First check that the tool and credentials are configured. If anything is missing, guide me through installation or configuration. Do not ask me to paste an API key into chat, and do not label ordinary analysis as a Jev result.

Provide your question bank, candidates, composite formula, and gates if you have them. Otherwise the skill distinguishes newly proposed rules from predefined ones. Jev scores support analysis; they are not customer or market evidence.

## Optional question-coverage check

The included checker uses only Python 3's standard library:

```bash
python3 scripts/check_questions.py path/to/report.md
```

It checks that Q1–Q25 headings each appear once, and flags missing, duplicate, or out-of-range questions. It does **not** verify answer quality or evidence. Without Python, the agent can check coverage manually.

## Scope

This skill produces analysis and reports. It does not authorize customer outreach, charging customers, hiring, procurement, or deployment. It works without other value-analysis skills or a specific reporting framework. It responds in the user's language, even though these instructions are written in English.
