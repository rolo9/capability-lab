# Capability Lab

A public learning repository for building durable technical and quantitative capability in an AI-first environment.

## Purpose and horizon

**AI-first operation, Human-owned understanding.**

The long-term direction is to understand, experiment with, evaluate, and keep catching up with **ML, DL, Physical AI, and other frontier AI / AI Native developments**. Python, Git, Docker, testing, and software delivery are the first-stage foundation for that direction. They are not the final capability goal. AI can assist heavily with implementation; the Human owns problem framing, meaning, interpretation, modification, validation, and judgment.

Grow a coherent public-safe artifact rather than a collection of disconnected exercises. SCM knowledge can supply meaningful questions, but this repository is not a mirror of confidential enterprise work. Learning must include concepts, assumptions, limitations, and decisions as well as working code.

## First artifact and its place in the wider learning path

**Notebook exploration → reusable Python modules → tests → Git/GitHub → browser UI → public Live Demo**

This is the delivery path for the first artifact, not the entire curriculum or a prerequisite checklist that indefinitely postpones ML/DL. The current shipment-versus-consumption exploration connects data meaning, time-series behavior, and evaluation of analytical indicators. A small function extraction is useful only as a bounded bridge from exploration to reusable, testable analysis. Do not fill the learning path with trivial functions or environment work.

As the artifact develops, progress toward statistics, prediction/ML, and model evaluation when the analytical question justifies them. DL and Physical AI remain explicit longer-term directions; their concrete projects, hardware, and prerequisites are not selected yet. Do not claim an inventory moving-average demo alone prepares or certifies those capabilities.

Choose Web UI/framework/hosting when browser interactions and runtime requirements are concrete. The Notebook and eventual UI should reuse analytical logic rather than maintain independent copies.

## Current — HC08, 2026-10-31

This section is the current entry point. The [learning contract](LEARNING_CONTRACT.md) defines collaboration; executable files establish what is actually implemented. Dated notes are historical evidence and context, not competing next-step instructions.

| Area | Verified repository state / evidence | Remaining work or limit |
| --- | --- | --- |
| Notebook | Original exploration from `39f16c1` retained; AI-prepared explanation and module-reuse cell added to [inventory_analysis.ipynb](notebooks/inventory_analysis.ipynb) | Full Notebook executed successfully in a new kernel in Docker on 2026-11-09 |
| Python | [src/analysis.py](src/analysis.py): existing Human-authored rolling-average function; [tests](tests/test_analysis.py): 3 AI-prepared behavior checks | All 3 runtime tests passed on 2026-11-09 |
| Environment | [Dockerfile](Dockerfile) now includes source/data/notebook/tests and `PYTHONPATH=/app`; pinned runtime and dependencies retained. [Replay steps](docs/reproduce.md) document build, mount-free checks and development mount | Image build and checks without a mount passed on the existing Mac checkout. Dependency installation reused the build cache |
| Mac observations | [HC07 checkpoint](learning/2026-10-31-hc07-succession.md): local rolling-average function ran in a one-off container; Jupyter mounted only notebooks and could not see `src` | On 2026-11-09 the Mac checkout fast-forwarded to `90475af` with a clean working tree. Prior work was preserved in the local Git stash |
| Public delivery | Public GitHub repository with notebook and dependency artifacts | No Web UI, hosting choice, or tested Live Demo |
| Operational incident | [Issue #2](https://github.com/rolo9/capability-lab/issues/2), including architecture-failure comment | OPEN. Clarifying documentation does not prove technical remediation |
| Recording review | [Issue #1](https://github.com/rolo9/capability-lab/issues/1) | OPEN. HC08 recommends retaining dated records plus this entry point; no proficiency certification or scoring system |

HC08 first clarified Current in `4ce99f3`, then prepared the replay unit from that source revision. See [Current review](learning/2026-10-31-hc08-current-review.md) and the newer [replay preparation/status](learning/2026-10-31-hc08-replay-preparation.md). The Human ran the Docker verification on 2026-11-09, and HC08 confirmed the log. The learning exercise is next. See the [verification record](learning/2026-11-09-hc08-replay-verification.md).

## Reproducibility: intended scope and present coverage

The aim is that the Human's learning and its meaningful history remain in GitHub, and that a reader following the repository can repeat the core experiments and obtain substantially equivalent analytical results. The repo must preserve both **how to run** and **what was learned, questioned, corrected, and remains uncertain**.

The first verification target is the existing **Apple Silicon Mac + Docker Desktop + containerized Python/Jupyter** workflow, reconstructed from a clean clone rather than dependent on one machine's leftover image, container, absolute home path, or uncommitted files. This is a bounded target, not a claim that the complete current workflow has already passed clean-clone verification.

- Record the tested host architecture, Docker/runtime versions, source revision, dependency definition, build/start commands, working directory, mount mapping, import setup, data creation/retrieval, execution order, expected results, and actual verification outcome.
- Repeatability means the relevant calculations, behavior, and interpretation agree; use explicit numerical tolerances where needed. Pixel-identical plots, identical generated binaries, or guaranteed independent Human proficiency are not promised.
- Windows, Intel Macs, and other hosts are untested until exercised. State platform-specific command/path differences when adding support; do not make universal compatibility a prerequisite for this first artifact.
- No indefinite or 30-year execution guarantee is made. Recovery depends on retained sources and availability of referenced dependencies/services. Pinning reduces uncontrolled change and creates a maintenance responsibility; it is not a permanent availability guarantee.
- Public deployment is a separate verification target: record its build/start requirements, source revision, and a checked Live Demo when implemented.

**Verified scope:** [the replay procedure](docs/reproduce.md) passed from the existing, clean Mac checkout. A fresh clone, a build without cache, and interactive Jupyter startup with a mount remain unverified.

## Development and publication decision

A bind mount is acceptable when its role is explicit and its method is reproducible. It exposes a chosen local checkout inside the container; the local checkout can be on another suitable Mac. The method must be documented using the checkout location as an input, not depend on `/Users/rolo9/...`.

The [replay instructions](docs/reproduce.md) define two complementary workflows.

1. **Development:** documented build and Jupyter invocation, with deliberate mount mapping, working directory and Python import configuration so Notebook and module edits persist in the checkout.
2. **Verification/publication:** a clean checkout containing the required code, notebook and data-generation inputs; run the documented procedure and checks without relying on unpublished files or an old container.

HC08 selected a whole-project development mount at `/app`, explicit `PYTHONPATH=/app`, and kernel working directory `/app/notebooks`, preserving the existing CSV relative path. The existing Dockerfile was expanded to include the required files for mount-free checks; no second Dockerfile or Compose layer was added. The checks without a mount passed on the Mac. The development mount still needs a browser session to verify it. See the replay instructions for the rationale and exact commands.

## Next sequence

1. **Runtime verification completed on 2026-11-09:** Docker build, three tests without a mount, and full Notebook execution in a new kernel passed at `90475af`.
2. **Human learning:** inspect the existing function, expected results and Notebook reuse; compare window 3 with 6 and explain why stable consumption can coexist with a later low shipment average. AI-prepared scaffolding is not a completed Human lesson.
3. **Record the result:** preserve observed output and understanding separately; fix any actual failures, then update this Current and reassess Issue #2 against its full acceptance conditions.
4. **Exit condition:** repository instructions reproduce the unit within the stated scope, and the Human can explain the analytical meaning and Notebook/module/test relationship. The original Mac edits are available in the local Git stash.
5. **Move onward:** return to the substantive analytical question and next statistics/ML need; evolve the same logic toward browser interaction and public demonstration without extending this into an open-ended infrastructure course.

## Learning and operational history

- [Cycle 1](learning/cycle-01.md): systems, storage/runtime boundaries and recovery experiments. Historical checkpoints are not today's task list.
- [2026-10-30 learning record](learning/2026-10-30-time-series-and-reproducibility.md): time series, indicator limitations, dependency and Git practice.
- [HC06 handoff](learning/2026-10-30-hc06-succession.md) and [HC07 handoff](learning/2026-10-31-hc07-succession.md): historical continuity and incident evidence.
- [HC08 review](learning/2026-10-31-hc08-current-review.md): current clarification and scope decisions.
- [HC08 replay preparation](learning/2026-10-31-hc08-replay-preparation.md): fresh Mac file observations, prepared implementation and pending execution checks.
- [2026-11-09 verification](learning/2026-11-09-hc08-replay-verification.md): Mac integration, Docker build, three passing tests, and Notebook execution without a mount.
- [Replay procedure](docs/reproduce.md): steps and verification coverage for the learning artifact.

Keep explanations close to the notebook/code when they explain the experiment. Use dated notes for milestone reasoning and AI-owned operational continuity; link rather than duplicate detailed evidence. No record of AI-assisted execution alone establishes independent Human proficiency.
