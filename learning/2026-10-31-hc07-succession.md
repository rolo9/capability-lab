# Human Capability 07 — operational succession checkpoint (2026-10-31)

**Purpose:** authoritative handoff of the current HC07 work and failures to the next runtime. This is an AI-owned *operational continuity record*, not a learning achievement or a new policy. Read together with README, LEARNING_CONTRACT.md, actual code/notebook, and Issues #1/#2. Distinguish **GitHub Current**, **Human Mac observed state**, and **unverified changes**. Earlier HC04/05 incidents in the contract remain relevant.

## Durable goal / learning contract (unchanged)

**AI-first operation, Human-owned understanding.** Grow one public-safe reproducible artifact through **Notebook exploration → reusable `src/*.py` → tests → Git/GitHub → browser UI → public Live Demo**. Introduce tooling only when it solves a real need; do not pick a web framework prematurely. Human learns problem framing, interpretation, modification, validation, and judgment; AI maintains continuity, documentation, and coherent exercises. Do not treat AI-assisted runs as independent Human proficiency. Avoid command-by-command/OK loops and unnecessary setup refactors.

## Verified GitHub Current (fresh-read 2026-10-31)

- README: synthetic 10-SKU monthly pandas/time-series and shipment-versus-consumption analysis, matplotlib, pinned dependencies, notebook published in artifact commit `39f16c1`. README's older next-step prose predates HC07 local work; this checkpoint is newer.
- Dockerfile: pinned `python:3.13-slim` digest; `WORKDIR /app`; `COPY requirements.lock`, install lock; copies only `src/transform.py` and `data/input.csv`; `CMD ["python","src/transform.py"]`. **It does not include `src/analysis.py` or specify Jupyter startup**. Do not infer the locally named Jupyter image is reproducible from the checked-in Dockerfile as-is.
- requirements.txt: `pandas==3.0.6`, `jupyterlab==4.6.4`, `matplotlib==3.11.2`; resolved dependency versions in requirements.lock. Pinning serves environment reproducibility, not automatic publication/deployment.
- LEARNING_CONTRACT.md documents HC04 and HC05 incidents. HC05 **already repeated the exact architectural mistake** of proposing a whole-project bind mount without principled review, reversing it, and mistaking a possible issue for a mandate. HC07 failed to apply this existing record.
- Issue #1 OPEN: independently assess minimal learning history vs capability evidence; do not impose new scoring or recording architecture.
- Issue #2 OPEN: HC07 operational failures and required correction; an additional verified comment records the repeated Docker/Jupyter architecture failure. Do not claim these are resolved.

## Observed Human Mac / Jupyter state (10/31; NOT automatically synced to GitHub)

From Human-shared iTerm2 transcript:
- Working directory `/Users/rolo9/workspace/capability-lab`, branch `main`. `src/analysis.py` created locally, not yet verified committed/pushed. Function:
  ```python
  import pandas as pd

  def calculate_rolling_average(series: pd.Series, window: int = 3) -> pd.Series:
      """指定した行数の移動平均を計算する。"""
      return series.rolling(window=window).mean()
  ```
- Host `python -c` failed (`zsh: command not found: python`); guessed `capability-lab:latest` Docker image failed to pull. Correct local image `capability-lab-jupyter:latest` is present.
- **Successful isolated function execution** via existing image, `docker run --rm -v "$PWD:/app" -w /app --entrypoint python capability-lab-jupyter -c ...`; pandas series `[100,200,300,400]` with window=3 returned NaN, NaN, 200, 300. This verifies that function in that one-off container, not the running Jupyter container.
- `docker ps` showed running container `brave_volhard`, image `capability-lab-jupyter:latest`, `127.0.0.1:8888->8888/tcp`. `docker inspect` verified bind mount **`/Users/rolo9/workspace/capability-lab/notebooks -> /app/notebooks` only**. Do not infer exact launch options/token from these two commands.
- Browser/Jupyter inspection: `inventory_analysis.ipynb` had executed synthetic-data, shipment/consumption, 3-row rolling average and matplotlib cells through [26]. Cell [27] attempted `from src.analysis import calculate_rolling_average` and failed `ModuleNotFoundError: No module named 'src'`. It also erroneously used `df["shipment"]`; correct dataset is **`df_push["shipment"]`**, with 9 monthly rows and columns `month,consumption,shipment,wholesale_inventory,shipment_ma3,consumption_ma3`. Cell [28] reported `Path.cwd() == /app/notebooks` and `(Path.cwd().parent / "src" / "analysis.py").exists() == False`. This confirms a mount/import boundary, not a defect in the rolling-average function.
- Local notebook edits from cells [27]/[28] are **not verified saved/pushed**. Do not claim notebook current on GitHub reflects these cells. Local worktree/remote divergence needs safe verification before future commit (previous rebase after direct GitHub documentation updates).
- Earlier strange rendering of Japanese docstring was repeatedly raised without a proven syntax error; do not resurrect absent concrete evidence.

## Failure and recovery status

HC07 repeatedly issued narrow terminal commands (`docker ps`, `docker inspect`) and moved toward Jupyter container recreation/full-project mount solely to resolve Notebook import. This **repeated a known HC05 failure** and ignored the higher goal: a GitHub-reproducible artifact and eventual Live Demo. The Human explicitly challenged the local optimization and requested runtime change due to repeated low-quality responses and wasted typing. The assistant acknowledged this, logged Issue #2, and stopped further terminal instructions. **No Jupyter container was stopped/recreated, no Dockerfile changed, no Web UI chosen, and no tested deployment exists.** Issue #2 remains OPEN: recording is not remediation.

## Required next-runtime decision (do BEFORE asking Human to type commands)

1. Fresh-read current GitHub README, contract, Dockerfile, dependency files, latest notebook, this checkpoint, and both open Issues. Treat these as authority, not conversation or memory. Distinguish current repo files from observed local uncommitted work.
2. **Independently** evaluate the architecture across three separate concerns: (a) local development convenience/import (mount, import path, or other minimal approach), (b) reproducible setup from a clean GitHub clone (documented build and Jupyter invocation, lock/digest and source inclusion), (c) eventual Web UI/public Live Demo deployment (different runtime needs). Compare minimal options and tradeoffs; do not prescribe a full-project bind mount, container recreation, Compose, a new Dockerfile, or new framework before justified. Do not mistake pinning for a complete reproducible startup contract. Preserve current notebook/data.
3. Propose a **bounded, coherent next learning unit**: validate reusable `calculate_rolling_average` with a focused test, reuse it correctly against `df_push["shipment"]` in Jupyter, and make code/test/environment reproducible from GitHub. Resolve the import issue only as part of that architecture decision. Use the fewest justified Human commands, with explanation and meaningful stopping criterion. Preserve existing notebook; no destructive action.
4. AI must **proactively record operational state and verified decisions** separately from learning history; update durable record and read-back after a meaningful milestone, not only on explicit Human prompting. Issue #1 remains separate. Reassess/close Issue #2 only after demonstrated correction, not after creating documentation.
5. Do not ask Human to restate prior work. Do not imply Work has access to the local Mac or that Work alone cures reasoning failures. User **chose Work, GPT-6.1 Medium**, for the next runtime, superseding prior historical default of Classic for this handoff. The successor should respect this selection and avoid needless debate.

## Handoff status

**Paused intentionally at architecture review; not a completed lesson.** Local `src/analysis.py` works in an isolated Docker invocation; Jupyter import fails because the running container mounts only notebooks; GitHub publication of the new module/test/notebook and reproducible startup is pending. Human wants an independent plan grounded in the durable goal before further typing. No additional Human action is required merely to start successor recovery.
