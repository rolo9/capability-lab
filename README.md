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
| Notebook | [inventory_analysis.ipynb](notebooks/inventory_analysis.ipynb), artifact commit `39f16c1`: 10 SKU × 12 months, pandas exploration, 9-month shipment/consumption/wholesale-inventory example, rolling averages and matplotlib output | Reusable module integration is not in GitHub |
| Python | [src/transform.py](src/transform.py) reads the tracked CSV | `src/analysis.py` and tests are absent from the reviewed GitHub tree |
| Environment | [Dockerfile](Dockerfile): Python 3.13 base pinned by digest, `/app`, installs [requirements.lock](requirements.lock); direct dependency intent in [requirements.txt](requirements.txt) | Copies only `src/transform.py` and `data/input.csv`; default command runs that script. No documented complete Jupyter startup/replay procedure |
| Mac observations | [HC07 checkpoint](learning/2026-10-31-hc07-succession.md): local rolling-average function ran in a one-off container; Jupyter mounted only notebooks and could not see `src` | Historical observations, not a fresh HC08 inspection. Local file contents, saved notebook edits, running container and sync with main remain unverified |
| Public delivery | Public GitHub repository with notebook and dependency artifacts | No Web UI, hosting choice, or tested Live Demo |
| Operational incident | [Issue #2](https://github.com/rolo9/capability-lab/issues/2), including architecture-failure comment | OPEN. Clarifying documentation does not prove technical remediation |
| Recording review | [Issue #1](https://github.com/rolo9/capability-lab/issues/1) | OPEN. HC08 recommends retaining dated records plus this entry point; no proficiency certification or scoring system |

HC08 reviewed GitHub main `02bd1f290d934d771277021ed1c6af10230795bf` and reorganized the documentation following the Human's clarification. See [HC08 decisions and remaining gaps](learning/2026-10-31-hc08-current-review.md). This documentation change does not complete module extraction or environment recovery.

## Reproducibility: intended scope and present coverage

The aim is that the Human's learning and its meaningful history remain in GitHub, and that a reader following the repository can repeat the core experiments and obtain substantially equivalent analytical results. The repo must preserve both **how to run** and **what was learned, questioned, corrected, and remains uncertain**.

The first verification target is the existing **Apple Silicon Mac + Docker Desktop + containerized Python/Jupyter** workflow, reconstructed from a clean clone rather than dependent on one machine's leftover image, container, absolute home path, or uncommitted files. This is a bounded target, not a claim that the complete current workflow has already passed clean-clone verification.

- Record the tested host architecture, Docker/runtime versions, source revision, dependency definition, build/start commands, working directory, mount mapping, import setup, data creation/retrieval, execution order, expected results, and actual verification outcome.
- Repeatability means the relevant calculations, behavior, and interpretation agree; use explicit numerical tolerances where needed. Pixel-identical plots, identical generated binaries, or guaranteed independent Human proficiency are not promised.
- Windows, Intel Macs, and other hosts are untested until exercised. State platform-specific command/path differences when adding support; do not make universal compatibility a prerequisite for this first artifact.
- No indefinite or 30-year execution guarantee is made. Recovery depends on retained sources and availability of referenced dependencies/services. Pinning reduces uncontrolled change and creates a maintenance responsibility; it is not a permanent availability guarantee.
- Public deployment is a separate verification target: record its build/start requirements, source revision, and a checked Live Demo when implemented.

**Present gap:** environment pinning and saved notebook outputs exist, but a complete documented and verified clean-clone Notebook/module replay does not. Do not present the historical image name or container state as a supported setup recipe.

## Development and publication decision

A bind mount is acceptable when its role is explicit and its method is reproducible. It exposes a chosen local checkout inside the container; the local checkout can be on another suitable Mac. The method must be documented using the checkout location as an input, not depend on `/Users/rolo9/...`.

Compare two complementary workflows when implementing the next unit:

1. **Development:** documented build and Jupyter invocation, with deliberate mount mapping, working directory and Python import configuration so Notebook and module edits persist in the checkout.
2. **Verification/publication:** a clean checkout containing the required code, notebook and data-generation inputs; run the documented procedure and checks without relying on unpublished files or an old container.

A whole-project mount is a possible development choice, not itself proof of publication or reproducibility. Copying required files into an image is another useful verification mechanism, not an automatic requirement for a new Dockerfile. No mount, container replacement, Compose configuration, Dockerfile change or exact startup command is adopted by this documentation review. Preserve local work before any later environment transition.

## Next sequence

1. **Finish Current clarification first:** purpose, scope, evidence and unresolved work are organized here. Preserve the distinction between repository state, historical Mac observations and fresh verification.
2. **Then one bounded learning unit:** explain the rolling-average input/output and assumptions; reuse it against `df_push["shipment"]`; check explicit expected results and initial missing values; connect Notebook and reusable module. Three rows correspond to three months only for suitably ordered, complete monthly data.
3. **Make that unit replayable:** preserve local changes, reconcile the local checkout safely with GitHub, document and verify the chosen build/start/import procedure, publish code/tests/notebook and learning explanation. Do not force-push or assume a GitHub documentation update has changed the Mac checkout.
4. **Exit condition:** a clean clone can repeat the unit, and the Human can inspect and explain the analytical meaning and the Notebook/module/test relationship. Report assisted execution separately from demonstrated independent understanding.
5. **Move onward:** return to the substantive analytical question and the next statistics/ML learning need; evolve the same logic toward browser interaction and public demonstration without extending this into an open-ended infrastructure course.

## Learning and operational history

- [Cycle 1](learning/cycle-01.md): systems, storage/runtime boundaries and recovery experiments. Historical checkpoints are not today's task list.
- [2026-10-30 learning record](learning/2026-10-30-time-series-and-reproducibility.md): time series, indicator limitations, dependency and Git practice.
- [HC06 handoff](learning/2026-10-30-hc06-succession.md) and [HC07 handoff](learning/2026-10-31-hc07-succession.md): historical continuity and incident evidence.
- [HC08 review](learning/2026-10-31-hc08-current-review.md): current clarification, decisions and verification limits.

Keep explanations close to the notebook/code when they explain the experiment. Use dated notes for milestone reasoning and AI-owned operational continuity; link rather than duplicate detailed evidence. No record of AI-assisted execution alone establishes independent Human proficiency.
