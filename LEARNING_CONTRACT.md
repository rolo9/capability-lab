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
