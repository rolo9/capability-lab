# Cycle 1 — Reproducible Data State

## Step 0 — Human Prediction Baseline

Recorded before implementation and before correction.

The purpose of this baseline is not to be correct. It preserves the Human's current mental model so that later observations can be compared against it.

### Current prediction

> Mac / ローカル
>
> Git repository / クラウド、他の人のフォークしたり、自分、あるいは自分の組織のリポジトリを更新
>
> Docker image / クラウド、Python3.14もこれで取得
>
> Docker container / クラウド、イメージなどを詰め込まれた実行環境
>
> input data / 入力
>
> output data / 出力

## Initial uncertainty exposed

No correction is applied at this stage.

The implementation phase will specifically test the boundaries among:

- local Host and remote services;
- Git and GitHub;
- Docker image storage and image distribution;
- Docker image and running container;
- input/output data location and persistence.

## Next edge

Build the smallest executable system and observe where each object actually exists.


## Step 0 — Immediate clarification before implementation

After the baseline was recorded, the Human clarified the intended mental model before any correction was given:

> DockerもGitHubもローカルに引っ張ってくるってことを言うべきでした？

Interpretation preserved as evidence rather than correction:

- there was already an operational intuition that remote resources are pulled to the local Mac for use;
- the unresolved point is the explicit separation of local vs remote objects and the distinct roles of Git/GitHub and Docker image/registry/container;
- this is treated as a boundary-articulation gap, not absence of prior experience.

This clarification was recorded before Step 1 implementation.


## Checkpoint — 2026-10-03

This checkpoint preserves reusable learning state and the reasoning path that materially changed the Human mental model. It is intentionally not a conversation transcript.

### Filesystem and Git boundaries

Observed on the actual Mac:

- `~` resolves to `/Users/rolo9`.
- `~/workspace` is an ordinary Host directory used as the Human project workspace.
- `~/workspace/capability-lab` is a local Git repository; `.git/` is the local Git metadata/history boundary.
- `origin` names a remote; Git and GitHub are not the same system.
- A local working-tree change does not automatically mutate GitHub.

Mental-model update: prior operational experience was present, but local/remote and filesystem boundaries were not yet consistently articulated.

### Docker object and lifecycle boundaries

Observed directly with `alpine:3.22`:

1. An image exists locally in Docker Desktop.
2. `docker run` creates a container from that image.
3. A short-lived main process such as `echo` exits and leaves a stopped container.
4. Removing the container does not remove the image.
5. State written only into a container writable layer survives stop/start of that same container.
6. Removing that container destroys that container-local state; creating a new container with the same name/image does not restore it.

Durable model:

`Image != Container`, and stop/restart is different from remove/recreate.

### Bind mount

Experiment:

- Host source: `~/workspace/capability-lab/data`
- Container target: `/data`
- A file written from the container appeared as `data/hello.txt` on the Mac.
- The file remained after the container was removed.

Mental-model update:

A bind mount exposes an existing Host path at a container path. The durable data is on the Host; it is not preserved by the container.

Compose syntax such as:

```yaml
volumes:
  - .:/work
```

is a bind mount even though it appears under the Compose key `volumes:`. This reconciles prior course experience: the earlier Desktop/work ↔ container /work setup was also a bind mount.

### Docker volume

Experiment:

- created named volume `capability-lab-data`;
- mounted it at container `/data`;
- wrote `volume.txt`;
- removed the container;
- the named volume remained.

`docker volume inspect` exposed the Docker-Linux-side mountpoint:

`/var/lib/docker/volumes/capability-lab-data/_data`

Mental-model update:

Both bind mounts and named volumes can outlive containers. The distinction is not persistence alone:

- bind mount: Human chooses an ordinary Host filesystem path;
- named volume: Human names a Docker storage object and Docker manages its physical path.

On Docker Desktop for Mac, Docker-managed storage ultimately consumes the Mac SSD through Docker Desktop's managed Linux/VM storage.

### Storage is not Authority

A key conceptual separation emerged:

- Storage — where state physically/logically persists;
- Access — who can read/write it;
- Authority — who is expected to define Current/canonical state;
- Interface — how actors are supposed to change it;
- Verification — how correctness/currentness is checked.

Bind mounts and volumes primarily address storage/access. They do not by themselves establish Source of Truth or single-writer authority.

Example to revisit later: source/input can be Host-owned and mounted read-only, while database internal files can be application-owned in a named volume and normally changed through the database interface.

### COPY vs bind mount

From the historical ML Dockerfile:

- `COPY environment.yml .` takes a build-time snapshot into the image build context/layer.
- a bind mount provides a runtime connection to a Host path.

Changing the Host file after an image is built does not retroactively change what was copied into that image.

### Historical ML environment audit

The existing `ml-learning-01_Foundations_Part_1` repository was inspected rather than rebuilt or deleted.

It retains durable definitions and Human work including:

- Dockerfile;
- environment.yml;
- docker-compose.yml;
- Makefile;
- notebooks/source/data structure;
- Git history.

The Dockerfile contains explicit Apple Silicon adaptation through `Miniforge3-Linux-aarch64.sh`. CPU architecture (amd64 vs arm64) and shell choice (bash/sh/zsh) are separate concerns.

The Compose configuration mounts `.:/work`, confirming that the project repository itself was bind-mounted into the Jupyter container. Human work was therefore designed to persist on the Host rather than live only in the container.

Git tracked state was clean and synchronized with `origin/main` at inspection time. Ignored/local-only files have not yet been exhaustively audited.

### Layer and build-cache model recovered

Prior course knowledge was recovered and connected to current evidence.

Docker image construction is layered. The goal is not simply to maximize or minimize the number of `RUN` instructions. Useful layer boundaries reflect logical dependency and change frequency so unchanged earlier work can be reused from cache while related operations remain coherent.

Current Docker disk evidence:

- Images: about 20.14 GB;
- Containers: about 16.11 MB;
- Local Volumes: about 48.4 MB;
- Build Cache: about 24.67 GB, with about 13.12 GB reclaimable.

This makes build cache concrete: it is useful build-time optimization/intermediate state, not the durable learning artifact or Source of Truth.

### Lifecycle gap identified

The earlier course effectively taught much of:

`Design → Build → Use`

The missing practical experience was the later lifecycle:

`Verify → Maintain → Retire → Recover`

For the historical M4 adaptation, the stronger completion sequence would have been:

1. get the adapted environment working;
2. move all required fixes back into durable definitions rather than relying on a hand-modified container;
3. verify reconstruction from those definitions, ideally from a clean clone/build path;
4. classify definitions/Human outputs versus generated images, runtime containers, persistent state, and cache;
5. only then remove artifacts whose recovery path is proven;
6. retain enough documentation to recover after a long absence.

Key principle:

**Do not treat cleanup as the proof. First prove recovery from durable definition; then cleanup becomes a lifecycle decision.**

### Human understanding at this checkpoint

The Human can now explain, with direct experimental evidence:

- local Host vs remote service;
- local Git repository vs GitHub remote;
- local Docker image vs container;
- stop/start vs remove/recreate;
- container-local writable state;
- bind mount vs Docker-managed named volume;
- why Compose `volumes:` does not necessarily mean a named Docker volume;
- COPY at build time vs bind mount at runtime;
- image layers and why cache exists;
- why cache value changes across build/use/retirement phases;
- why persistence and Source of Truth are separate problems.

Remaining uncertainty is intentionally preserved rather than hidden:

- exact ignored/local-only content in the historical ML repositories has not yet been fully audited;
- Part 2 has not yet received the same reproducibility audit;
- no Docker cleanup has been performed;
- Cycle 1's own reproducible data pipeline has not yet been implemented.

### Next edge

Resume from this checkpoint rather than replaying today's Docker foundations.

Before deleting historical Docker artifacts, finish the bounded reproducibility audit (including Part 2 and any material local-only state). Then return to the Cycle 1 implementation and make lifecycle/recovery part of its Definition of Done.
