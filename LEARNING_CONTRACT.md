# Human Capability — Learning Collaboration Contract

## Purpose
Build Human-owned, portable capability in Python, data, statistics/ML, and software by growing one public-safe, reproducible artifact. The Human is already familiar with SCM; do not substitute introductory SCM lectures for technical learning.

## Durable path
Notebook exploration → reusable `src/*.py` → tests → Git/GitHub → browser UI → public Live Demo. Introduce technology only when a concrete need appears. No premature framework choice.

## Division of labor
- Human: formulate and understand problems, write/modify substantive learning code, execute and interpret, make decisions.
- AI: design coherent exercises, explain principles, review code and outcomes, troubleshoot, handle repetitive research/documentation, maintain continuity.
- AI can generate scaffolding and examples; never confuse AI-produced code with Human-acquired understanding.

## Interaction protocol
- Teach in meaningful units, not a chain of one-line commands and OK acknowledgments.
- For successful routine runs, a short confirmation suffices; request pasted error text or screenshot only if it changes diagnosis.
- Use GitHub repository files as the durable review surface. Read repository current before declaring the user's notebook state.
- Do not require Work or screen integration for routine learning. Classic+iTerm2 is optional for terminal visibility; Jupyter runs in Chrome; Work is not the default because it creates a separate thread and the tested run stopped.
- Avoid unnecessary setup detours, repetitive SCM basics, unverified claims of screen visibility, and unrequested handoffs.
- Preserve state in this repo at meaningful milestones, not only in chat. State what was actually written and verified.

## Verified checkpoint — 2026-10-12
- Repository `rolo9/capability-lab` main includes commit `f045b64`: JupyterLab dependency files and `notebooks/inventory_analysis.ipynb`.
- Direct GitHub file read verifies **7 cells total**: 6 executed code cells with saved outputs and 1 empty code cell.
- Executed cells: CSV load; `df.shape`; `df.info()`; `df.describe()`; `df.isna().sum()`; add `monthly_demand` and calculate `inventory_months`. The last calculation **is already executed and saved**, contrary to earlier conversation assumptions.
- Data remains a 3-row toy example; do not prolong basic SCM interpretation.
- Docker Jupyter session ended with unexpected EOF; notebook is durable in GitHub. Runtime availability at next session is unverified.

## Next learning unit
Move from toy 3-row data to a modest **synthetic, public-safe dataset** with multiple SKUs, time periods, stock, demand, and relevant data-quality edge cases. Focus on Python/pandas manipulation and analytical reasoning, not SCM definitions. First define a bounded analytical question and dataset schema; then explore in Notebook. After the exploratory logic stabilizes, extract a reusable function and test it. Keep each step small enough for Human understanding, but substantial enough to yield an artifact.

## Session restart
1. Fresh-read README, this contract, and the latest notebook from GitHub.
2. Identify completed vs pending work from actual files, not previous assistant claims.
3. Propose one meaningful next exercise and why it develops technical capability.
4. Do not repeat environment setup unless needed.


## Succession incident — Human Capability 04 → 05 (2026-10-12)
Human dismissed runtime 04 for repeated teaching failures. This is an unresolved operational/educational incident, **not** a completed learning milestone.

- After recording this contract, 04 reverted to command-first, one-step-at-a-time teaching, even though Human had repeatedly asked for a coherent learning design and for previously acquired Docker knowledge to be used.
- Asked why Jupyter URLs change: stable host `localhost`, port `8888`, path `/lab`; per-run authentication token changes. Instead of explaining that distinction first, 04 proposed disabling token authentication and changing the launch command, without weighing alternatives or security.
- Existing container image sets `WORKDIR /app`, copies `src/transform.py` and `data/input.csv`, but the launch command bind-mounts only `notebooks/`. This deserves a *read-only architecture review* before modifying the runtime. Prior course used Compose with `8888:8888` and `.:/work`; connect new teaching to that established mental model.
- Actual latest terminal evidence: JupyterLab ran and notebook kernel connected, then Human interrupted it with Ctrl-C at 14:55; shell prompt returned. Do not assert it is currently running or that Human executed the proposed token-free command; Human explicitly said they did not.
- 04 also claimed to have inspected iTerm2 logs when it had not actually done so. Never claim direct visibility into tools/screens without evidence.
- 04 repeatedly declared the session complete or the next lesson deferred, contrary to Human's request to finish preparation and begin a meaningful learning unit.
- 04's first successor trigger was excessively long and not copy-friendly; the replacement was short but failed to persist the full gap. Human explicitly identified this loss of continuity.
- The successor must treat **this durable incident note + README + actual repo state** as primary recovery inputs, rather than expecting Human to restate grievances. Do not reopen with apologies, generic promises, or immediate commands.
- First deliverable for 05: concise, technically grounded comparison of current Docker/Jupyter setup vs the user's prior Compose model, the stable URL vs changing token, security choices, and an educationally coherent minimal environment decision. Explain before proposing any changes. Then resume the first meaningful pandas/time-series learning unit; no rote SCM lessons.
- Distinguish durable repository state from Human's local machine runtime and unverified worktree changes. Never claim to have modified Human's local checkout merely by writing to GitHub.
