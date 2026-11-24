# XGBoost — 補正をどれくらい抑えるか

検索用の別名：XGBoost、正則化、regularization、L2、reg_lambda、葉の重み、leaf weight

前提は[勾配ブースティングの4件](./2026-11-24-gradient-boosting.md#なぜ木を足すと学習になるのか)。前回は残差を近似する木を足した。今回は同じ4件で、**葉ノードが返す補正を大きくしすぎないようにすると何が変わるか**を見る。XGBoostは勾配ブースティングを実装したライブラリで、木を足しながら、予測の損失とモデルへのペナルティを合わせて評価する。 [XGBoost公式の導出](https://xgboost.readthedocs.io/en/stable/tutorials/model.html)

## 1. 式が意味すること

正則化（regularization）は、学習データへの当てはまりを評価するときに、モデルの複雑さや大きな係数にペナルティを加える考え方。ここで扱うL2正則化は、葉の重み（leaf weight、ここでは木が返す補正値）を二乗してペナルティにする。

二乗誤差で、ある葉の補正値を w、そこに入った各例の残差を r、葉に入った件数を n とする。その葉について最小にする量は次のとおり。

$$
\frac12\sum_i(r_i-w)^2 + \frac{\lambda}{2}w^2
$$

第1項は補正後のずれ、第2項は補正の大きさへのペナルティ。w について微分すると、ずれの項は「n × w − 残差の合計」、ペナルティの項は「λ × w」。合計を0にする補正値は **残差の合計 ÷ (件数 + λ)**。λ（ラムダ）を0にすると前回の残差の平均に戻る。λを増やすと補正が0に近づき、同じλでも件数が少ない葉ほど縮む割合が大きい。この式は重みなしの二乗誤差の場合。

## 2. 同じ4件で手計算する

入力0、1、2、3に対する実測は0、0、2、6。初期予測は全件2なので残差は −2、−2、0、4。木を1本、深さを1、学習率を1に固定し、λだけを0から3へ変えた。どちらも実行結果の境界は2.5だったため、同じ葉の補正を比較できる。

| 入力 | 葉内の残差の合計／件数 | λ = 0 の補正 | λ = 3 の補正 | λ = 3 の最終予測 |
| --- | --- | ---: | ---: | ---: |
| 0・1・2 | −4 ／ 3件 | −4/3 | −4/6 | 約1.333 |
| 3 | 4 ／ 1件 | 4/1 | 4/4 | 3 |

入力3では、λ=0なら2+4=6、λ=3なら2+1=3。学習データ1件への大きな補正が抑えられた。正則化が新しいデータで役立つかは、学習データと分けて確認する。XGBoostでは一般にλが分岐選びにも影響するので、境界が同じなのは今回の観察結果。

## 3. Pythonの入力と実行出力

`X` は4行×1列、`y` は4件の正解。`fit` が木を学習し、`get_dump()[0]` が1本目の分岐と葉の補正値を文字列で返す。`predict(X)` が初期予測に補正を反映した4件の値を返す。XGBoost 3.4.1で実行した。以下の出力では浮動小数点の値を読みやすく丸めた。

```python
import numpy as np
from xgboost import XGBRegressor

X = np.array([[0], [1], [2], [3]])
y = np.array([0, 0, 2, 6])

for penalty in (0, 3):
    model = XGBRegressor(
        objective="reg:squarederror", base_score=2.0, n_estimators=1,
        max_depth=1, learning_rate=1.0, reg_lambda=penalty,
        tree_method="exact", n_jobs=1,
    )
    model.fit(X, y)
    print("lambda:", penalty)
    print(model.get_booster().get_dump()[0].strip())
    print("prediction:", model.predict(X).round(3).tolist())
```

```text
lambda: 0
0:[f0<2.5] yes=1,no=2,missing=1
	1:leaf=-1.33333337
	2:leaf=4
prediction: [0.667, 0.667, 0.667, 6.0]
lambda: 3
0:[f0<2.5] yes=1,no=2,missing=1
	1:leaf=-0.666666687
	2:leaf=1
prediction: [1.333, 1.333, 1.333, 3.0]
```

後から読み直す順は [決定木の分岐](2026-11-24-decision-tree-first-split.md#6件から分岐を作る) → [残差と負の勾配](./2026-11-24-gradient-boosting.md#なぜ木を足すと学習になるのか) → このページのL2正則化 → 未使用データでのモデル比較。
