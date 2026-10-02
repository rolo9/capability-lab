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
