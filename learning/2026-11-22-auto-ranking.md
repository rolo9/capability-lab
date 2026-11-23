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

**順位付けを改善する目的では、馬力の2次化を優先しない。** 実測値に近づいても選抜結果が変わらず、馬力が同じ車も区別できなかった。選抜方法の改善を検討する場合は、試験前に取得できるという前提で、馬力だけの線形回帰に車重を1列加える。データ分割と10台の試験枠をそろえ、馬力順の基準を上回るか、見逃しがどの車で入れ替わるかを見る。車重の効果はこの時点では仮説。

ここで候補を絞る。採用を判断する段階では、必要な検出水準とその理由を先に定め、選び終えた候補を用途に合う未使用データで確認する。この85台はその確認に使わない。

## 分析設計の見直し — モデルを変えるか、試験枠を増やすか

試験前の判断は「誰を測るか」と「何台測るか」の二つ。見逃しを減らしたいなら、選び方を変える効果を、直接測定を増やす効果と比べる。今回は順位を馬力の大きい順、評価対象を前回の85台、正解を実測燃費の悪い10台に固定し、検査枠だけを変えた。15台と20台は比較用の仮定。

| 試験枠 | 拾えた台数 | 見逃し | 無作為選抜で拾える期待台数 |
| --- | ---: | ---: | ---: |
| 10台 | 5 | 5 | 1.18 |
| 15台 | 6 | 4 | 1.76 |
| 20台 | 8 | 2 | 2.35 |

無作為選抜では各枠が対象車に当たる確率は10/85なので期待台数は枠数×10/85。これは「手掛かりなし」の参考。運用を変える判断には現在使える選び方と比較する。ここでは馬力順をその基準の例とした。たとえば「見逃しは最大2台」と仮定すると、検討した枠では20台で届いた。10枠が固定なら、次の候補にはこの開発データ上で3台分の改善が必要になる。試験費用、見逃しの影響、モデルの運用費用が実際に分かれば、どちらを検討する価値が高いかを決められる。見逃し2台は比較の読み方を示す例で、実用上の合格条件は未設定。

この計算には85台すべての実測がある。運用で選んだ車しか測らないと、残りの車を何台見逃したかは観測できない。新しい集団で検出割合そのものを確認するなら、まず候補選びと切り離した検証用の一群で全車を測る設計を検討する。実際に試験を追加する判断と、評価のために正解データを集める判断には、それぞれ目的がある。

10枠が固定され、あと3台拾うことに価値があるという条件で、次に車重を加える意味が生まれる。馬力の2乗は同じ情報から曲線を作る列で、同じ馬力の2台の区別には使えない。車重は試験前に取得できれば別の情報になる。追加の候補はまずこの仮説に絞る。同じ10枠で比較し、改善が見えた候補を独立したデータで確認する。

<details>
<summary>試験枠を変えた実行コード</summary>

固定版の `Auto.csv` と同じディレクトリで、下を `budget.py` として保存し `python budget.py` を実行する。Python標準ライブラリのみ。各出力行は試験枠、拾えた台数、見逃した台数、無作為選抜の期待台数の順。

```python
from csv import DictReader
from itertools import accumulate

with open("Auto.csv", encoding="utf-8", newline="") as file:
    cars = [row for row in DictReader(file) if int(row["year"]) >= 80]

# sorted は同点で元の行順を保つ。
actual = sorted(range(len(cars)), key=lambda i: float(cars[i]["mpg"]))
target = set(actual[:10])
priority = sorted(range(len(cars)), key=lambda i: -int(cars[i]["horsepower"]))
hits = list(accumulate(i in target for i in priority))

for budget in (10, 15, 20):
    found = hits[budget - 1]
    print(budget, found, 10 - found, round(budget * 10 / len(cars), 2))

print("Target ranks:", [rank for rank, i in enumerate(priority, 1) if i in target])
```

</details>

## 車重を加えて10枠で見逃しが減るか

10枠が固定され、車重は試験前に分かると仮定した。前回の見逃しに馬力が低めで重い車が含まれていたので、「馬力に車重を足すと、その車たちを拾い、10枠全体でも改善する」と仮説を立てた。1979年型以前307台で係数を求め、すでに結果を見た1980年型以降85台で比較。基準は馬力順で、前回の馬力だけの線形回帰と同じ10台を選ぶ。対象・試験枠・実測燃費が悪い10台という定義は前回と共通。順位の同点はCSVの行順で決めた。

### 計算と出力

線形回帰に車重を1列足すと、燃費の予測は「基準の燃費＋馬力の寄与＋車重の寄与」になる。最小二乗法で2つの係数を同時に学び、推定mpgが低い順に10台を選ぶ。実行した式では、馬力が同じ場合、車重1,000 lb増に対し予測値が約5.38 mpg下がった。これはモデル上の差であり、車重を操作したときの因果効果を測った値ではない。scikit-learnでは、馬力と車重の2列を `X_train` にすると `LinearRegression().fit(X_train, y_train)` がこの当てはめを担う。実行したのは標準Python版。

| 選び方 | 拾えた台数 | 見逃し |
| --- | ---: | ---: |
| 馬力順 | 5 | 5 |
| 馬力＋車重の線形回帰 | 5 | 5 |

選抜した6台が入れ替わり、実測燃費が悪い車を3台拾い直した一方、馬力順で拾っていた別の3台を落とした。たとえば85 hp、3,465 lb、17.6 mpgの車を拾ったが、112 hp、2,835 lb、22.0 mpgの車を落とした。判定対象を10台全体で見た結果、拾った台数は同じだった。

### 判断

今回の指標では馬力順を上回る根拠が得られず、車重を使う候補はこの段階で採用保留。次の設計上の論点は、見逃しを一律に数えるのか、特に悪い車の見逃しに重みを付けるのか。用途の側で決める。基準や候補を固めた後の確認には、別の未使用データが必要。今回の85台は開発中の診断に使用した。

<details>
<summary>Macで実行したPythonコード</summary>

Apple Silicon Mac、Python 3.9.6の標準ライブラリのみで実行。固定版CSVを取得し、下記を `weight.py` として保存して `python3 weight.py Auto.csv` を実行する。

```python
import csv
from statistics import mean
from sys import argv

with open(argv[1], newline="", encoding="utf-8") as file:
    cars = list(csv.DictReader(file))

train = [car for car in cars if int(car["year"]) < 80]
dev = [car for car in cars if int(car["year"]) >= 80]
target = set(sorted(range(len(dev)), key=lambda i: float(dev[i]["mpg"]))[:10])

# 係数の単位を100 hp、1000 lbにする。平均は学習用データだけで求める。
hp = [float(car["horsepower"]) / 100 for car in train]
weight = [float(car["weight"]) / 1000 for car in train]
mpg = [float(car["mpg"]) for car in train]
hp_mean, weight_mean, mpg_mean = mean(hp), mean(weight), mean(mpg)
x = [v - hp_mean for v in hp]
z = [v - weight_mean for v in weight]
y = [v - mpg_mean for v in mpg]

def dot(a, b):
    return sum(left * right for left, right in zip(a, b))

xx, xz, zz = dot(x, x), dot(x, z), dot(z, z)
xy, zy = dot(x, y), dot(z, y)
# 最小二乗の連立方程式を解く。
det = xx * zz - xz ** 2
hp_coef = (xy * zz - zy * xz) / det
weight_coef = (zy * xx - xy * xz) / det

def predict(car):
    return (mpg_mean
            + hp_coef * (float(car["horsepower"]) / 100 - hp_mean)
            + weight_coef * (float(car["weight"]) / 1000 - weight_mean))

indices = range(len(dev))
baseline = set(sorted(indices, key=lambda i: -int(dev[i]["horsepower"]))[:10])
candidate = set(sorted(indices, key=lambda i: predict(dev[i]))[:10])
print("train, development:", len(train), len(dev))
print("coefficients:", hp_coef, weight_coef)
print("hits:", len(baseline & target), len(candidate & target))
for label, subset in [
    ("added", candidate - baseline), ("removed", baseline - candidate),
    ("missed", target - candidate),
]:
    print(label, [(dev[i]["horsepower"], dev[i]["weight"], dev[i]["mpg"],
                   round(predict(dev[i]), 2), i in target) for i in sorted(subset)])
```

</details>

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
