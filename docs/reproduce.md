# Reproduce the Notebook/module learning unit

## Scope and verification status

Target: Apple Silicon Mac, Docker Desktop with Linux containers, Git, a terminal and a browser. Commands below use zsh/bash syntax and are run from the repository root. Required downloads need network access. Other platforms are not verified.

On 2026-11-09 the Human ran sections 2–4 from the existing Apple Silicon Mac checkout at `90475af` using Docker Desktop. The image built successfully using cached dependencies, all three tests passed, and the full Notebook executed in a new kernel without a mount. A fresh clone, uncached dependency installation, and the interactive development launch in section 5 remain to be verified. See the [verification record](../learning/2026-11-09-hc08-replay-verification.md).

## Files and boundaries

- GitHub preserves source, Notebook, synthetic inputs, tests, Dockerfile and dependency intent/lock. A commit is the reproducible source reference.
- Docker build installs the lock and copies the needed artifact into the image. The image tag below is explicitly created by this build; it is not assumed to exist.
- `PYTHONPATH=/app` makes the project root available for imports even when the Notebook kernel is in `/app/notebooks`. `from src.analysis import ...` and `../data/input.csv` therefore refer to different, deliberately configured roots.
- Development bind mount: host checkout → `/app`; edits persist in that checkout and still require commit/push to reach GitHub.
- Mount-free verification: run the files copied into the image, exposing dependencies on missing/unpublished host files.
- Keep token authentication. Development uses host port 8889 to coexist with the previously observed session on 8888. No old container needs to be stopped.

## 1. Obtain a clean checkout

Use a fresh destination rather than overwriting an existing learning checkout:

```sh
git clone https://github.com/rolo9/capability-lab.git capability-lab-replay
cd capability-lab-replay
git rev-parse HEAD
```

To repeat a particular milestone later, check out its recorded full commit SHA before building. An existing dirty checkout must first preserve its changes and integrate remote documentation safely. These instructions do not prescribe reset, force-push or a blind pull/rebase on the original Mac checkout.

## 2. Build the environment and artifact

```sh
docker build -t capability-lab:hc08 .
```

The base digest and resolved Python package versions are fixed in repository definitions. Build success alone is not replay proof. Downloads may fail or become unavailable; report the actual failure rather than silently replacing the pinned inputs.

## 3. Check module behavior without a mount

```sh
docker run --rm capability-lab:hc08 python -m unittest discover -s tests -v
```

Expected: 3 passing tests. They check the initial missing values, explicit averages, a changed window, index/name preservation, no mutation of the input, and the later low moving average following shipment front-loading. This checks calculation behavior, not whether shipments are a valid proxy for consumption or whether the Human independently understands the implementation.

## 4. Replay the Notebook in a clean kernel, without a mount

```sh
docker run --rm capability-lab:hc08 jupyter nbconvert --to notebook --execute notebooks/inventory_analysis.ipynb --output inventory_analysis.executed --output-dir /tmp --ExecutePreprocessor.timeout=180
```

Expected: all cells execute without error. The generated Notebook is intentionally temporary inside this verification container; the original tracked file is not overwritten. At the module-reuse cell, the 3-row result must agree with the earlier exploratory calculation. In July, shipment MA(3) is about 33.33 even though consumption is 100. Saved historical outputs are not a substitute for this clean-kernel execution.

## 5. Open Jupyter for development

From the root of the checkout used for development:

```sh
docker run --rm --publish 127.0.0.1:8889:8888 --mount "type=bind,source=$PWD,target=/app" --workdir /app/notebooks capability-lab:hc08 jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --ServerApp.root_dir=/app
```

Open `http://localhost:8889/lab` and use the token printed by this new server. The container reports its internal port 8888; the browser uses the mapped host port 8889. Open `notebooks/inventory_analysis.ipynb` in Jupyter. For another free host port, change only the host side and browser URL consistently.

This whole-project mount hides the files copied into `/app` at build time. That is intentional for editing, and is why the separate mount-free checks matter. Do not use the development session as the sole proof that the published artifact is complete.

Save Notebook changes before exiting. Ctrl-C stops the server; `--rm` removes that new container, while bind-mounted files remain in the checkout. Dependencies must be changed in their durable definitions and rebuilt, rather than installed only into a running container.

## 6. What the learning unit establishes

The existing Human-authored rolling-average function is copied unchanged. The new tests, integration cell and setup definitions are AI-prepared scaffolding; their presence is not evidence of a completed Human lesson.

Before expanding the code, explain:
- Why are the first two outputs missing for a window of three?
- Why can a mathematically correct shipment average be misleading about consumption?
- What changes when a Notebook and a future browser UI call the same Python function?
- What is preserved by the mount, by the image, and by GitHub?

One deliberate change from window 3 to 6, comparison of results, and explanation of the changed response are enough for this bridge. Do not turn it into repeated trivial function exercises. Return to the next substantive statistical/ML question once the unit is understood and reproducible.

## Record actual verification

After execution, record the source SHA, host architecture/OS, Docker client/server or Desktop version, build result, test result, clean-kernel replay result and any deviations in the milestone record. Keep failures and pending checks visible. A public Live Demo is a later, separately verified browser-access milestone.
