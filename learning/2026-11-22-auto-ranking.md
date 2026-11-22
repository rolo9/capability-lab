# 予測誤差が減っても、試験に回す10台は変わるか

検索用の別名：予測モデルの評価、MAE、ランキング、上位10件、特徴量選択

[ロードマップ](../ROADMAP.md#予測モデルを作り使えるかを判断する流れ)の統計的機械学習。工程1〜2で用途と比較方法を決め、工程3〜4で同じデータに候補を当て、次の変更を選ぶ。実際の自動車試験を想定した採用判断は保留。

## 問いと前提

燃費試験の枠が85台のうち10台分だけあり、実測燃費が低い車を優先したいと仮定する。試験前に分かる車両仕様から燃費を推定し、予測mpgが低い順に10台を選ぶ。主指標は、実測mpgが低い10台のうち何台を選べたか。MAEは、85台全体で予測値が実測値にどの程度近かったかを読む補助指標にする。10台は試験枠で、この段階の採用基準は設けていない。

復習では、MAEと拾えた台数のどちらが目的を直接測るかを、結果を見る前に説明する。別のケースで、上位だけ処理する仕事と全件に数値予測を使う仕事を比べ、何を指標にすべきか考える。

## 教材の説明

線形回帰は馬力の列を使い、2次回帰は同じ馬力から作った馬力の2乗を列に加える。どちらも学習データの残差平方和を小さくする係数を求める。コードでは `PolynomialFeatures` が列を作り、`LinearRegression.fit` が係数を求める。その後、`predict` の出力を並べ替えて試験の対象を決める。 [ISLP第3章の非線形変換](https://islp.readthedocs.io/en/stable/labs/Ch3-linreg-lab.html#non-linear-transformations-of-the-predictors)

## 実行で確認した事実

[固定版Auto.csv](https://github.com/intro-stat-learning/ISLP/blob/46fb7dfaa39a41c007c627cc6a90dba3a88e5b2c/ISLP/data/Auto.csv)を使用。 [出典と利用形態](2026-11-21-mean-vs-linear.md#公開データの出典と利用形態)。[前回](./2026-11-21-linear-vs-quadratic.md)と同じく1979年型以前307台で学習し、結果を見たことのある1980年型以降85台で開発中の診断を行った。学習・評価データ、入力の馬力、試験枠を固定し、馬力の2乗を加えるかだけを変えた。

| 候補 | 実測の低燃費10台のうち選べた台数 | 85台のMAE |
| --- | ---: | ---: |
| 線形回帰 | 5 / 10 | 7.249 mpg |
| 2次回帰 | 5 / 10 | 6.548 mpg |
| 馬力の大きい順（比較用） | 5 / 10 | — |

3通りとも選んだ10台は同じ。評価範囲の48〜132 hpでは、予測mpgが馬力とともに下がる。2次式の折り返しは193.59 hpで、この範囲の外にある。予測値の間隔が変わっても、順位は変わらなかった。

選抜の最後の1枠で100 hpの2台が同点だった。全候補でCSVの行順を使った結果は5台。もう一方を選ぶ規則なら両モデルとも4台になる。実測側の境界は10位24.3 mpg、11位25.0 mpgで同点はなかった。見逃した5台は85〜92 hp。たとえば85 hp・3,465 lbの車は実測17.6 mpgだったが、132 hpの車は32.7 mpgでも優先された。

## 今回の判断と次に確かめること

**順位付けを改善する目的では、馬力の2次化を優先しない。** 実測値に近づいても選抜結果が変わらず、馬力が同じ車も区別できなかった。次は試験前に取得できるという前提で、馬力だけの線形回帰に車重を1列加える。データ分割と10台の試験枠をそろえ、馬力順の基準を上回るか、見逃しがどの車で入れ替わるかを見る。車重の効果はこの時点では仮説。

ここで候補を絞る。採用を判断する段階では、必要な検出水準とその理由を先に定め、選び終えた候補を用途に合う未使用データで確認する。この85台はその確認に使わない。

## 本人の予想と解釈

- 実行前の予想：
- 結果を見ての解釈：

## コードと再実行

Python 3.12.14、scikit-learn 1.8.0で実行。Macでは同じバージョンのscikit-learnが使えるPython環境で、固定版CSVをダウンロードし、以下を `rank.py` として保存して `python rank.py /path/to/Auto.csv` を実行する。Macでの再実行は未確認。変えた箇所は `degree`。CSVの行番号はヘッダーを1行目として数える。

<details>
<summary>実行コードを表示</summary>

```python
from csv import DictReader
from statistics import mean
import sys

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

with open(sys.argv[1], encoding="utf-8", newline="") as file:
    rows = list(DictReader(file))
train = [i for i, row in enumerate(rows) if int(row["year"]) < 80]
dev = [i for i, row in enumerate(rows) if int(row["year"]) >= 80]
hp = [int(row["horsepower"]) for row in rows]
mpg = [float(row["mpg"]) for row in rows]
X_train = [[hp[i]] for i in train]
X_dev = [[hp[i]] for i in dev]
y_train = [mpg[i] for i in train]
budget = 10

def order(scores):
    # 同点ならCSVで先に現れる行を優先。予測の同点を実測燃費で解消しない。
    return sorted(dev, key=lambda i: (scores[i], i))

actual_order = order(mpg)
actual = set(actual_order[:budget])
print(f"train={len(train)}, development={len(dev)}")
print("Actual MPG at ranks 10 and 11:", [mpg[i] for i in actual_order[9:11]])
picks = {}
for degree in (1, 2):
    model = make_pipeline(
        PolynomialFeatures(degree=degree, include_bias=False),
        LinearRegression(),
    )
    model.fit(X_train, y_train)
    predictions = dict(zip(dev, model.predict(X_dev)))
    ordered = order(predictions)
    selected = set(ordered[:budget])
    picks[degree] = selected
    mae = mean(abs(predictions[i] - mpg[i]) for i in dev)
    print(f"degree={degree}: hits={len(selected & actual)}/{budget}, MAE={mae:.3f}")
    print("  HP at ranks 10 and 11:", [hp[i] for i in ordered[9:11]])
    print("  Picked (CSV row, hp, mpg):", [(i + 2, hp[i], mpg[i]) for i in ordered[:budget]])
    print("  Missed (CSV row, hp, mpg):", [(i + 2, hp[i], mpg[i]) for i in sorted(actual - selected)])
    if degree == 2:
        slope, curvature = model[-1].coef_
        print(f"  Turning point: {-slope / (2 * curvature):.2f} hp")

horsepower_only = sorted(dev, key=lambda i: (-hp[i], i))
print("Development horsepower range:", min(hp[i] for i in dev), max(hp[i] for i in dev))
print("Both models pick the same set:", picks[1] == picks[2])
print("Same set as sorting by horsepower:", set(horsepower_only[:budget]) == picks[1])

print("At the selection cutoff (CSV row, hp, mpg, weight):",
      [(i + 2, hp[i], mpg[i], int(rows[i]["weight"])) for i in dev if hp[i] == 100])
print("Missed cars' weights (CSV row, lb):",
      [(i + 2, int(rows[i]["weight"])) for i in sorted(actual - picks[1])])
```

</details>
