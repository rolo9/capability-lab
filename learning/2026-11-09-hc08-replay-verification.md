# HC08 Mac integration and replay verification (2026-11-09)

The Human ran the agreed adoption and verification script in iTerm. HC08 checked the local log and Git status.

- Source revision: `90475af71b42792439d450682dda149e48972451`. The Mac checkout fast-forwarded from `39f16c1` and the working tree was clean afterward.
- The edited Notebook and untracked files were saved in the local Git stash named `HC08 before adopted integration`.
- The Apple Silicon Mac built `capability-lab:hc08` with Docker Desktop. The pinned base image resolved and the dependency layer was reused from the build cache. Docker server and Desktop version numbers were not captured in this run.
- Three unit tests passed in a fresh container without a bind mount.
- Jupyter nbconvert executed the full Notebook in a new kernel in a separate container without a bind mount. The log reports writing the temporary result and the script's success marker. The kernel emitted a TCP warning and execution completed successfully.

This run verifies the published calculation module, its tests, and Notebook execution within the built image. Fresh-clone replay and uncached installation remain separate checks.

The Human learning exercise remains open. Next, use the same function with windows 3 and 6 and interpret the response to a shipment spike while consumption stays stable. Preserve the Human's explanation separately from the execution result.

## Interactive Jupyter and next workflow

The Human started JupyterLab with the checkout mounted at `/app`. The browser connected through Mac port 8889 to container port 8888. HC08 read the saved local Notebook and confirmed output from the module-reuse cell. July shipment and consumption were both 100, while shipment MA(3) was 33.33 and MA(6) was 100. The later consumption-drop exercise is recorded below.

The Human agreed to implement the shorter startup workflow after the current learning exercise. Use `make up` to start Jupyter and `make jupyter` to open the authenticated URL automatically. Keep the generated token and Mac loopback binding. The current browser session is available for the learning exercise.

## Learning exercise and startup shortcut

The Human ran and saved the scenario with consumption falling from 100 to 60 in July. The saved output showed MA(3) crossing the threshold of 80 or below in August (73.33) and MA(6) reaching it in September (80). At this threshold, the longer window delays investigation by one month because it retains more pre-change observations.

After this exercise, HC08 added the agreed Makefile. `make up` builds and starts the named container, `make jupyter` opens its loopback login URL, and `make down` stops it. The Make recipes and URL selection passed a local check with simulated Docker and browser commands. Docker daemon access from the assistant shell was denied, so live verification of the new shortcut remains pending.
