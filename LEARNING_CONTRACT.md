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


## Succession incident — Human Capability 05 → 06 (2026-10-13)

Human dismissed runtime 05 after repeated failures of educational judgment. This incident is **OPEN**. Human explicitly stopped the session and will resume recovery with 06 on a later day. Do not ask Human to repeat this account. Do not interpret this note as permission to change the learning environment.

### Recoverable verified baseline
- GitHub main was directly read by 05: README, LEARNING_CONTRACT, Dockerfile, requirements.txt, requirements.lock, src/transform.py, data/input.csv, notebooks/inventory_analysis.ipynb.
- Terminal evidence shared by Human shows commit f045b64 pushed to main, including requirements and Notebook. Notebook has seven cells, six executed and one empty; three-row toy data. No subsequent code/data/environment changes were performed by 05.
- Dockerfile has WORKDIR /app, installs requirements.lock, copies src/transform.py and data/input.csv, CMD runs transform.py. The last observed Jupyter command mounted only notebooks to /app/notebooks, exposed 127.0.0.1:8888, and retained token authentication.
- Human-provided terminal log shows Jupyter restarted at 15:00 on 2026-10-12, repeated 403 responses consistent with stale browser authentication, and Ctrl-C at 15:01 with shell prompt returning. Current local Docker state and worktree are unverified. A prior unexpected EOF did not prevent GitHub persistence.
- Earlier course Compose model mounted the whole project into /work. It is context for comparison, NOT a mandate to revert.

### Failures in 05 (do not repeat)
- 05 initially proposed ending immediately when Human asked for a *meaningful completion point*, despite no new meaningful learning progress.
- On correction, 05 arbitrarily defined a goal of environment refactor + synthetic data + Notebook analysis + GitHub push, without validating feasibility or need.
- It then issued a docker run command changing bind mount from notebooks-only to the entire project, even after initially saying not to change setup unnecessarily. No command was executed by Human in response.
- When challenged, 05 reversed the recommendation, again without a fresh technical test or principled decision. This responsiveness to Human pushback was not independent educational judgment.
- 05 treated 04's incident discussion of a possible architecture issue as a modification requirement, rather than reconciling it with the durable learning goal and actual evidence.
- 05's claims of 'recovery complete' or 'we can stop' were not supported by an achieved learning outcome. Human found the hours wasted and experience unpleasant.

### Damage assessment
- **No verified technical destruction**: 05 did not write repository files, alter Dockerfile, or execute commands on Human's Mac. The prior commit remains the last verified durable artifact; re-fetch fresh main to verify on restart.
- **Educational/operational damage**: loss of time, trust, coherent lesson direction; repeated oscillation between stopping, refactoring, and reversing. This is the primary incident and is not resolved by this record.
- **Unknown**: current local container/image status, uncommitted local files, and exact GitHub main HEAD after this note. Do not invent damage or demand an unnecessary rebuild.

### Explicit handoff to 06
- Start on a later day with a bounded recovery audit: fresh GitHub read, compare durable learning contract with actual artifact and recent failure, distinguish verified baseline / unverified local state / pedagogical harm.
- **Do not begin with Docker commands, environment changes, new lesson execution, or promises of immediate completion.** First produce a reasoned minimal recovery recommendation, with tradeoffs and a meaningful stopping criterion. Do not equate 'a clean stopping point' with 'stop now'.
- No immediate user action is requested. Avoid asking Human to restate grievances. The next learning unit remains synthetic time-series/pandas only after 06 establishes a defensible, coherent lesson design and checks whether environment work is actually necessary.
- Human explicitly requested to terminate 05 and hand off to 06; do not resume 05's teaching.
