# 勾配ブースティング — 木を1本ずつ足して予測を補正する

検索用の別名：勾配ブースティング、gradient boosting、残差、residual、学習率、learning rate

[決定木の分岐](2026-11-24-decision-tree-first-split.md#6件から分岐を作る)では1本の木が答えを出した。今回は、**浅い決定木の出力を順に足し、前の予測を補正する**方法を学ぶ。[最小二乗法の復習](2026-11-22-auto-ranking.md#最小二乗法)で扱った残差（residual）は、実測から予測を引いた値。二乗誤差の半分を損失にすると、予測についての負の勾配がこの残差になる。今回はその残差を回帰木で近似する。分類など、ほかの損失でも同じ残差を使うとは限らない。

## 4件で補正を追う

説明用に入力を0、1、2、3、正解を0、0、2、6とした。初期予測は正解の平均2。1本目は残差 `[-2, -2, 0, 4]` を入力の位置で分け、葉ノード（leaf node）ごとに平均を返す。学習率（learning rate）は補正値に掛ける倍率。今回は足し算を追いやすいよう1に設定した。

| 段階 | 入力0 | 入力1 | 入力2 | 入力3 |
| --- | ---: | ---: | ---: | ---: |
| 実測 | 0 | 0 | 2 | 6 |
| 初期予測 | 2 | 2 | 2 | 2 |
| 1本目の補正後 | 0.667 | 0.667 | 0.667 | 6 |
| 2本目の補正後 | 0 | 0 | 1.333 | 6.667 |

入力3を見る。1本目は境界2.5の右で補正値4を返し、予測は2+4=6。2本目は境界1.5の右に入る。入力2と3の残差（1.333と0）の平均を同じ葉で使うので、約0.667を足して6.667になる。**全体の二乗誤差を減らす途中で、すでに合っていた1件が悪化することもある。** この4件は学習データ。新しい例で良くなるかは[学習・検証・最終テストの分け方](2026-11-23-digit-classification.md#学習検証最終テストの分け方)に従って評価する。

## Pythonの入力と実行出力

`X` は4行×1列、`y` は4件の正解。`fit` は初期値と補正用の木2本を学習する。`staged_predict(X)` は1本足すごとに4件の予測を返す。`export_text` が出す `value` はその木の補正値。最終予測は初期値と各木の補正値の和。クラウド環境のPythonで実行した。

```python
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import export_text

X = [[0], [1], [2], [3]]
y = [0, 0, 2, 6]
model = GradientBoostingRegressor(
    loss="squared_error", n_estimators=2, max_depth=1,
    learning_rate=1.0, random_state=0,
).fit(X, y)

previous = model.init_.predict(X)
print("initial", previous.round(3).tolist())
for i, prediction in enumerate(model.staged_predict(X), start=1):
    print("stage", i, "residual before", (y - previous).round(3).tolist())
    print(export_text(model.estimators_[i - 1, 0], feature_names=["x"]).strip())
    print("prediction", prediction.round(3).tolist())
    previous = prediction
```

```text
initial [2.0, 2.0, 2.0, 2.0]
stage 1 residual before [-2.0, -2.0, 0.0, 4.0]
|--- x <= 2.50
|   |--- value: [-1.33]
|--- x >  2.50
|   |--- value: [4.00]
prediction [0.667, 0.667, 0.667, 6.0]
stage 2 residual before [-0.667, -0.667, 1.333, 0.0]
|--- x <= 1.50
|   |--- value: [-0.67]
|--- x >  1.50
|   |--- value: [0.67]
prediction [0.0, 0.0, 1.333, 6.667]
```
