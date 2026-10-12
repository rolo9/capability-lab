# Capability Lab

A public learning repository for building durable technical and quantitative capability in an AI-first environment.

## Operating principle

**AI-first operation, Human-owned understanding.**

AI may assist heavily with syntax, boilerplate, implementation, debugging, and documentation. The learning target is not manual code production. The Human remains responsible for framing, decomposition, meaning, inspection, validation, modification, explanation, recovery, and judgment.

## Capability direction

The repository will grow through reproducible learning cycles across:

**Systems → Data → Statistics / ML → Decision**

Frontier AI / AI Native remains the North Star. Real enterprise work may provide evidence, but this repository uses only public-safe or synthetic material and is not an enterprise-work mirror.

## Durable learning path

Capability Lab is intended to close the gap between learning data analysis in a notebook and turning that work into a durable, usable artifact.

The target path is:

**Jupyter exploration → reusable Python modules → tests → Git/GitHub → browser-usable UI → public deployment**

Jupyter Notebook is the exploration surface: inspect data, test hypotheses, visualize, iterate, and explain reasoning. When analysis logic becomes stable and reusable, promote that logic into `src/*.py` rather than leaving the entire result trapped in notebook cells. Verify the promoted logic with tests, preserve the code and reproducible environment in Git, and make the resulting project understandable from its public GitHub repository.

The first substantial public artifact should continue beyond source code alone. The repository should ultimately link to a **Live Demo** that can be opened and interacted with in a browser. Use synthetic or otherwise public-safe data; do not copy confidential enterprise data into this repository. Domain knowledge, including SCM problem framing, may shape the problem and interpretation.

Git, Docker, dependency management, testing, Web UI, and deployment are not separate checklist subjects to rush through. Introduce them when the evolving artifact creates a real need for them. Likewise, do not choose a web framework prematurely; first build a meaningful analysis and reusable logic, then add the next layer when its purpose is concrete.

This path is durable project direction and should survive chat/runtime transitions. A fresh Human Capability runtime should recover this repository state rather than reverting to disconnected Python or ML tutorials.

## Cycle 1 — Reproducible Data State

Cycle 1 established the initial reproducible execution foundation:

- Python runtime in Docker
- source and input data preserved in Git
- Python base image pinned by digest
- direct dependency intent recorded in `requirements.txt`
- resolved dependency versions captured in `requirements.lock`
- pandas used by the executable transformation
- recovery from GitHub and container rebuild verified

The conceptual outcome is that reproducibility requires control over code, data, runtime, and dependencies, while pinning also creates an explicit maintenance responsibility.

## Current state

Cycle 1 reproducibility foundation is complete and pushed to `main`.

**Next edge:** add Jupyter to the current reproducible Docker environment and begin exploratory data analysis. Use the notebook for exploration, then deliberately identify the point at which stable logic should be promoted into reusable Python code.

