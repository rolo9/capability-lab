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
| Environment | [Dockerfile](Dockerfile) now includes source/data/notebook/tests and `PYTHONPATH=/app`; pinned runtime and dependencies retained. [Replay steps](docs/reproduce.md) document build, mount-free checks and development mount | Existing checkout replay passed on 2026-11-09. A separate clean clone passed the no-cache build, three tests and mount-free Notebook replay on 2026-11-18. See [2026-11-18のクリーン再現検証](https://github.com/rolo9/capability-lab/issues/2#issuecomment-6981231923) |
| Mac observations | [HC07 checkpoint](learning/2026-10-31-hc07-succession.md): local rolling-average function ran in a one-off container; Jupyter mounted only notebooks and could not see `src` | On 2026-11-09 the Mac checkout fast-forwarded to `90475af` with a clean working tree. Prior work was preserved in the local Git stash |
| Public delivery | Public GitHub repository with notebook and dependency artifacts | No Web UI, hosting choice, or tested Live Demo |
| Operational incident | [Issue #2](https://github.com/rolo9/capability-lab/issues/2), including architecture-failure comment | OPEN. Clarifying documentation does not prove technical remediation |
| Recording review | [Issue #1](https://github.com/rolo9/capability-lab/issues/1) | OPEN. HC08 recommends retaining dated records plus this entry point; no proficiency certification or scoring system |

HC08 first clarified Current in `4ce99f3`, then prepared the replay unit from that source revision. See [Current review](learning/2026-10-31-hc08-current-review.md) and the newer [replay preparation/status](learning/2026-10-31-hc08-replay-preparation.md). The Human ran the Docker verification on 2026-11-09, and HC08 confirmed the log. The comparison exercise ran on the Mac. The learning roadmap below gives the current entry point. See the [verification record](learning/2026-11-09-hc08-replay-verification.md).

## Reproducibility: intended scope and present coverage

The aim is that the Human's learning and its meaningful history remain in GitHub, and that a reader following the repository can repeat the core experiments and obtain substantially equivalent analytical results. The repo must preserve both **how to run** and **what was learned, questioned, corrected, and remains uncertain**.

The first verification target is the existing **Apple Silicon Mac + Docker Desktop + containerized Python/Jupyter** workflow, reconstructed from a clean clone rather than dependent on one machine's leftover image, container, absolute home path, or uncommitted files. This is a bounded target. The clean-clone trial verified the image and mount-free replay at the recorded revision.

- Record the tested host architecture, Docker/runtime versions, source revision, dependency definition, build/start commands, working directory, mount mapping, import setup, data creation/retrieval, execution order, expected results, and actual verification outcome.
- Repeatability means the relevant calculations, behavior, and interpretation agree; use explicit numerical tolerances where needed. Pixel-identical plots, identical generated binaries, or guaranteed independent Human proficiency are not promised.
- Windows, Intel Macs, and other hosts are untested until exercised. State platform-specific command/path differences when adding support; do not make universal compatibility a prerequisite for this first artifact.
- No indefinite or 30-year execution guarantee is made. Recovery depends on retained sources and availability of referenced dependencies/services. Pinning reduces uncontrolled change and creates a maintenance responsibility; it is not a permanent availability guarantee.
- Public deployment is a separate verification target: record its build/start requirements, source revision, and a checked Live Demo when implemented.

**Verified scope:** [the replay procedure](docs/reproduce.md) passed from the existing, clean Mac checkout. The interactive Jupyter launch with a mount also passed, including running and saving the module-reuse cell. Separately, [2026-11-18のクリーン再現検証](https://github.com/rolo9/capability-lab/issues/2#issuecomment-6981231923) confirmed a fresh clone at `62037c0`, a `--no-cache` build with dependency reinstallation, three passing tests, and full Notebook execution without a host mount. The pinned base image was not forcibly re-pulled.

## Development and publication decision

A bind mount is acceptable when its role is explicit and its method is reproducible. It exposes a chosen local checkout inside the container; the local checkout can be on another suitable Mac. The method must be documented using the checkout location as an input, not depend on `/Users/rolo9/...`.

The [replay instructions](docs/reproduce.md) define two complementary workflows.

1. **Development:** documented build and Jupyter invocation, with deliberate mount mapping, working directory and Python import configuration so Notebook and module edits persist in the checkout.
2. **Verification/publication:** a clean checkout containing the required code, notebook and data-generation inputs; run the documented procedure and checks without relying on unpublished files or an old container.

HC08 selected a whole-project development mount at `/app`, explicit `PYTHONPATH=/app`, and kernel working directory `/app/notebooks`, preserving the existing CSV relative path. The existing Dockerfile was expanded to include the required files for mount-free checks; no second Dockerfile or Compose layer was added. The checks without a mount passed on the Mac. The Human opened JupyterLab using this development mount and saved the Notebook after the module-reuse cell produced output. See the replay instructions for the rationale and exact commands.

## Next sequence

[学習ロードマップ](ROADMAP.md)に、基礎からML、DL、Physical AIへのつながりと、手法・ライブラリ・分析対象の対応を記載している。入口は、過去の記録から新しい1件を予測し、結果を評価する流れ。線形回帰と決定木の比較およびXGBoost実習の続きは、この土台を押さえてから再開する。

Macでの[可視化実習](learning/2026-11-19-hc08-visualization.md)と[XGBoost実行結果](learning/2026-11-20-hc08-xgboost.md)は、再現可能な記録として保存した。

### 最初のML実習 — XGBoost

[実習Notebook](notebooks/xgboost_first_run.ipynb)では、2つの測定値から合成スコアを予測する。評価用120行について、学習データの平均を返す基準モデルとXGBoostのMAEと散布図を比べる。最初は `max_depth = 3`、次は `1` で再実行する。

**Apple Silicon Macでの準備。** 既存のJupyterLabコンテナを使う。停止中ならリポジトリのルートから [手順どおり起動](docs/reproduce.md#5-open-jupyter-for-development) する。作業中のチェックアウトに新しいNotebookだけを取り込む場合は、次を同じルートで実行する。

```sh
git fetch origin main &&
  git cat-file -e FETCH_HEAD:notebooks/xgboost_first_run.ipynb &&
  (set -C; git show FETCH_HEAD:notebooks/xgboost_first_run.ipynb > notebooks/xgboost_first_run.ipynb)
```

コンテナ起動後、この実習の依存パッケージを入れる。

```sh
docker exec capability-lab-jupyter sh -c 'python -m pip install --only-binary=:all: -c /app/requirements.lock scipy==1.17.1 && python -m pip install --only-binary=:all: --no-deps xgboost==3.2.0'
```

SciPyと既存のNumPyを使うCPU実習なので、XGBoostのインストール時はLinux向けのGPU通信依存を省く。追加パッケージは起動中のコンテナに入る。コンテナを作り直したときはこのインストールを再実行する。

JupyterLabのファイル一覧を更新し、`notebooks/xgboost_first_run.ipynb` を開いて **Run → Run All Cells** を選ぶ。評価値と図は実行の記録として保存した。2026-11-20にMacのDocker/JupyterLabで両方の深さを確認し、[評価値・図・再現手順](learning/2026-11-20-hc08-xgboost.md)を記録した。

## Learning and operational history

**手法名から復習する**場合は、[学習記録の索引](learning/README.md)へ。関連する実習、図、Notebook、そこで分かったことをたどれる。

- [Cycle 1](learning/cycle-01.md): systems, storage/runtime boundaries and recovery experiments. Historical checkpoints are not today's task list.
- [2026-10-30 learning record](learning/2026-10-30-time-series-and-reproducibility.md): time series, indicator limitations, dependency and Git practice.
- [HC06 handoff](learning/2026-10-30-hc06-succession.md) and [HC07 handoff](learning/2026-10-31-hc07-succession.md): historical continuity and incident evidence.
- [HC08 review](learning/2026-10-31-hc08-current-review.md): current clarification and scope decisions.
- [HC08 replay preparation](learning/2026-10-31-hc08-replay-preparation.md): fresh Mac file observations, prepared implementation and pending execution checks.
- [2026-11-09 verification](learning/2026-11-09-hc08-replay-verification.md): Mac integration, Docker build, three passing tests, and Notebook execution without a mount. The [2026-11-10 scope review](learning/2026-11-09-hc08-replay-verification.md#scope-review-2026-11-10) records the earlier assessment of what the ML exercise should teach.
- [Replay procedure](docs/reproduce.md): steps and verification coverage for the learning artifact.

Keep explanations close to the notebook/code when they explain the experiment. Use dated notes for milestone reasoning and AI-owned operational continuity; link rather than duplicate detailed evidence. No record of AI-assisted execution alone establishes independent Human proficiency.
