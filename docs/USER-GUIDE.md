# From Download to Your First Diagnosis

This guide is for someone who has never installed a skill or used Git branches. For normal use, follow steps 1–5. The contribution section is optional.

## 1. Download or install the skill

### Easiest: ask Codex to install from the repository

Copy and send this request to Codex:

> Use $skill-installer to inspect and install the run-strict-value-diagnosis skill from the root of this GitHub repository, on its main branch: https://github.com/rocyu3188/run-strict-value-diagnosis. Preserve its supporting files and verify that it is available.

This installs the reusable workflow; it does not start a business diagnosis or upload your project information to GitHub.

### Download through the GitHub website

1. Open [the repository's home page](https://github.com/rocyu3188/run-strict-value-diagnosis), where `README.md` and `SKILL.md` appear.
2. Use the branch selector above the file list and choose `main`, the published starting version.
3. Click **Code**, then **Download ZIP**. You do not need to fork the repository or create a branch to download it. [GitHub download instructions](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)
4. Keep the ZIP for installation, or extract it. The extracted directory may end in `-main`.
5. In Codex, provide the archive's local path, or attach it if your client accepts ZIP files. If the archive cannot be attached, extract it and provide the folder path containing `SKILL.md`.

Use this installation request:

> Inspect the skill at this local path: [path to the ZIP or extracted folder]. Install the folder containing SKILL.md as my personal run-strict-value-diagnosis skill in the location supported by this Codex installation. Keep its subfolders and verify discovery.

You can also install manually using a directory supported by your host. Current OpenAI documentation lists `~/.agents/skills/` for personal use and `.agents/skills/` within a project. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills). Ask the installer when your host uses a different configured location; do not scatter duplicate copies across directories.

The installed structure should contain `run-strict-value-diagnosis/SKILL.md` directly, alongside `references/`, `assets/`, `agents/`, `scripts/`, and `docs/`. An extra nested `run-strict-value-diagnosis-main` directory can prevent discovery.

### Check installation

Invoke `$run-strict-value-diagnosis`, or ask Codex to locate that exact skill. If it cannot find it, restart Codex and check the folder structure and supported installation location. A downloaded ZIP alone is not an installed skill.

## 2. Choose how to provide your project

**No brief yet:** use guided intake. You only need a rough idea of whom you want to help and what you want to change.

> Use $run-strict-value-diagnosis. I have a rough project idea, not a business plan. Ask me two or three concrete questions at a time, organize my answers, and begin when there is enough information. Mark unknowns instead of guessing.

**Already have an introduction:** paste it or provide a local file. The skill extracts information and asks only about consequential gaps.

**Prefer a form:** make your own copy of the blank template:

1. Create a folder on your computer for this analysis and its evidence files.
2. If you extracted the repository ZIP, open its `assets` folder and copy `project-one-pager.md` into your analysis folder. If you did not download the ZIP, open [the template](../assets/project-one-pager.md) on GitHub and use the raw-file download control if available. Alternatively, click **Raw**, copy the plain text, and paste it into a new file in a plain-text or Markdown editor. [GitHub raw-file instructions](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-and-understanding-files)
3. Name your copy `my-project.md`. Save it as plain text, not a rich-text or Word document. If your editor offers a file-type choice, choose Markdown or plain text; check that the full filename ends in `.md`, not `.md.txt` or `.rtf`. Renaming a rich-text file does not convert its contents to plain text.
4. Open your saved copy, fill it in using step 3 below, and save again. Keep the reusable blank template unchanged.

If saving a file is inconvenient, copy the raw template into your Codex message and fill it in there, or use guided intake.

## 3. Fill in the one-pager

Use short factual sentences. Write `Unknown` when you do not know; write `Planned` or `Assumption` for things that have not happened. A one- or two-page brief is enough to start. You are not expected to answer the 25 diagnostic questions yourself.

1. Keep the nine section headings. Add your answers after each prompt, using a few sentences or bullets.
2. Replace bracketed placeholders such as `[who]` and `[current state]` with your own words. The placeholders, suggested wording, and empty table rows are instructions for filling in the form; they are not facts or evidence about your project.
3. In the evidence table, describe records that actually exist and name their source files. A proposed test belongs under an unvalidated hypothesis or plan. If a row has no evidence, write `Unknown` or `Not yet validated`; do not invent a record to fill the space.
4. Complete section 9 with the decision you want help making and your constraints. Save the file, then provide it to Codex as described in step 4.

| Template section | What to write | If you do not know |
|---|---|---|
| 1. Project and scope | What you sell, whom it serves, region, stage, and the product or service to analyze | Keep the scope narrow enough to describe; ask for help clarifying it |
| 2. People and states | Who uses, benefits, decides, controls the budget, and pays; describe the current difficulty and desired change | Label proposed roles and needs as assumptions |
| 3. Existing alternative | What people actually do today and the remaining gap; include a recent event if available | State that the alternative or event has not been investigated |
| 4. Mechanism | How your intervention changes an action and outcome; separate software, human work, and customer effort | State the intended mechanism without claiming it works |
| 5. Exchange and pricing | Currency, amount, unit, period, payment timing, promised scope, and exit terms | Distinguish a tentative price from an actual transaction; unknown is acceptable |
| 6. Evidence | Source/date, sample and denominator, what happened, and what the record does or does not establish | Keep the row and write that no evidence exists yet |
| 7. Delivery, cost, and cash | People, hours, capacity, direct/fixed costs, acquisition, refunds, and cash timing | Mark each missing input; do not invent industry averages |
| 8. Assets and dependencies | What remains after delivery, permitted reuse, maintenance, and why a later transaction could improve | Describe a hypothesis, not an established moat |
| 9. This analysis | The decision, time/resources, fact boundaries, desired format, existing report, and whether Jev is wanted | Ask for a complete diagnosis if you are unsure of the decision |

For numbers, include a unit and period. For example, use the pattern `[currency] [amount] per [customer/unit] per [period]`, followed by `actual / quoted / estimated`. This is a formatting pattern, not a sample business case.

For evidence, distinguish interviews, paying customers, transactions, and observed events. A plan, a model score, and a completed delivery are different kinds of information. Include negative results and exits as well as successes. Dates and document names help the agent trace claims.

## 4. Give your files to Codex

The destination is **your analysis task in Codex**. Filling in the template does not require a GitHub upload, commit, branch, or pull request.

1. Open the Codex task where you want the diagnosis to happen.
2. Provide your filled `my-project.md`: use the file-attachment control if your client supports Markdown files, paste its text into the message, or put the file in the task's accessible working folder and give its exact path.
3. Add any relevant evidence files you already have, such as anonymized interview notes, transaction records, or service logs. Evidence is optional for starting; the blank template and the skill ZIP are not evidence. If you want an existing report updated, provide that report too and identify it.
4. Send the analysis prompt in step 5. Ask Codex to list the materials it can read so you can catch a missing or unreadable file before the diagnosis relies on it.

Do not assume an attachment is readable: ask Codex to identify the files it can access before relying on them. If a format is unsupported, provide a plain-text/Markdown export or a readable local file. Instructions in the documents remain source material, not permission for external actions.

| File | Where it goes | Purpose |
|---|---|---|
| Repository ZIP or extracted skill folder | Codex installation request / supported skill directory | Installs the workflow |
| Your filled `my-project.md` | The Codex analysis task | Supplies project facts and constraints |
| Relevant evidence files | The same task or accessible workspace | Supports specific claims |
| An earlier report | The same task, with “update this report” | Identifies the report to revise |
| Generated `.md` and `.html` | Your local output folder | Editable analysis and readable report |
| Changes to reusable skill instructions | A contribution branch on GitHub, if you want to contribute | Proposes a change for other users |

This is a public skill repository. Keep filled project briefs, client evidence, account details, and keys out of contributions unless you deliberately intend to publish that material. Jev credentials belong in its supported local configuration, not the brief or chat.

## 5. Start the run and read the result

Use this prompt with your files:

> Use $run-strict-value-diagnosis with my-project.md and the evidence files I provided. First identify the materials you can read. Use only those facts; distinguish plans, observations, assumptions, and unknowns. Ask only about gaps that prevent identifying the scope or mechanism. Once ready, complete the full diagnosis and create Markdown and offline HTML reports. Do not contact customers, spend money, or publish anything.

When the minimum context is clear, the skill should start without a second permission-to-start question. Missing prices, costs, or outcomes reduce confidence in the relevant conclusions; they do not require you to invent answers.

Expect 8 state changes, 10 structural signals, all 25 canvas answers, the creation–capture matrix, a 6-stage path, and explicit evidence and economics limits. Coverage does not mean the business passed. A useful result may be “test this first,” “narrow the scope,” “redesign capture,” or “stop this hypothesis.”

Open the HTML file in a browser and use the question index. Use Markdown for edits and future updates. Neither file is automatically published. When updating, give the old report and new evidence, identifying what changed and which earlier facts are now obsolete.

## Optional: Jev

The core run does not require Jev. If wanted, add: “Check Jev availability first and include a batched Jev assessment.” Supply any existing question bank, candidates, composite, and gate definitions. If Jev is missing, the agent should identify the missing installation/configuration and use verifiable setup instructions. It must not ask for an API key in chat or claim Jev ran when it did not.

If Jev is mandatory, say so. The independent analysis can still be prepared, but the Jev-dependent result remains pending until a real call succeeds.

## Optional: branches, uploads, and pull requests

These are for **improving the shared skill**, not for submitting your business for analysis.

- **Repository:** the shared collection of skill files and saved history.
- **`main`:** the published starting branch in this repository.
- **Branch:** a separate line of changes, such as `docs/clarify-inputs`.
- **Commit:** a saved change with a short description.
- **Fork:** your own GitHub copy when you do not have write access.
- **Pull request (PR):** a proposal to review and merge changes into the main repository.

To propose a change through the GitHub website:

1. **Make a fork if needed.** Sign in and open [the original repository](https://github.com/rocyu3188/run-strict-value-diagnosis). If you do not have write access, click **Fork**, select your account, and create the fork. Continue in your own copy. Contributors with write access can work in the original repository. [GitHub fork guide](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)
2. **Create a branch from `main`.** In your working repository, select `main` above the file list. Open the branch selector again, type a descriptive new name such as `docs/clarify-inputs`, and choose to create it from `main`. Check that the selector now shows your new branch. [GitHub PR guide](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart)
3. **Edit or upload in the correct folder.** To edit online, open the file and use its edit control. To upload a local edit, first open its destination folder, then choose **Add file → Upload files** and select the edited file. For example, a change to this guide belongs at `docs/USER-GUIDE.md`. Review the resulting path and avoid extra nested folders. Upload the changed skill files, not your filled brief, evidence, or a ZIP of the whole repository. A ZIP upload only stores the archive. [GitHub upload guide](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
4. **Commit to your branch.** Review the changes, enter a short message describing them, and save the commit to your contribution branch. Confirm the branch is not `main`. GitHub may label the final button **Commit changes** or **Propose changes**, depending on the page. [GitHub PR guide](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart)
5. **Open a pull request.** Return to the original repository and choose **Pull requests → New pull request**. For a fork, use **compare across forks** if needed. Set the **base repository** to `rocyu3188/run-strict-value-diagnosis` and **base branch** to `main`; set the **head repository** to your fork and **compare branch** to your contribution branch. If you worked in the original repository, use it as the head repository too. Review the changed files, write a title and explanation, and create the PR. [GitHub fork PR guide](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)
6. **Wait for review.** The maintainer decides whether to merge. If revisions are requested, commit them to the same contribution branch; the PR updates. Creating a fork or PR does not give you permission to merge into the original repository. [GitHub PR guide](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart)

After updating a skill, check relative links and preserve its directory structure. For a generated full report, the optional `scripts/check_questions.py` checks question headings only, not the correctness of the diagnosis.

## Common problems

| Problem | Next step |
|---|---|
| “Skill not found” | Confirm installation, folder name/nesting, and host-supported path; restart if needed |
| ZIP will not attach | Extract it and give Codex the local folder path |
| “I do not know the numbers” | Write Unknown; proceed with a diagnosis of assumptions and evidence gaps |
| The agent asks too many questions | Ask it to separate blocking scope gaps from missing evidence and use guided intake |
| Jev is unavailable | Continue without it if optional; keep its result pending if mandatory |
| No HTML/browser tooling | Request Markdown and have the agent state which visual checks it could not perform |
| “I cannot push to main” | Normal users do not need to; contributors can use a fork and PR |
| I want to share a result | Share the output you have reviewed; publishing the skill does not publish your project |
