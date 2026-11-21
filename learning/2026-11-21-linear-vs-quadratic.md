# 線形回帰に2次項を足すと何が変わるか

検索用の別名：多項式回帰、2次回帰、非線形変換、評価誤差、MAE

[ロードマップ](../ROADMAP.md#現在地と再開点)の統計的機械学習。前回の[平均と線形回帰](2026-11-21-mean-vs-linear.md)では、入力を使う価値を見た。今回は、入力を馬力に固定し、関係を直線に限る場合と曲がれる場合を比較する。

## 復習の問い

直線と2次式はどちらも最小二乗法で学習できる。コードでは何が増え、出力の形はどう変わるか。全体のMAEが改善しても、用途によって直線を選ぶのはどんな場合か。

## 教材の説明

$y=a+bx$ に $cx^2$ を足すと、馬力の位置によって予測値の変化の大きさが変わる。学習時には $b$ と $c$ を一緒に決める。学習と評価で同じ変換を使う。 [ISLP第3章の非線形変換](https://islp.readthedocs.io/en/stable/labs/Ch3-linreg-lab.html#non-linear-transformations-of-the-predictors)

## 実行で確認した事実

元データは[出典・利用形態を記録したISLP Auto](2026-11-21-mean-vs-linear.md#公開データの出典と利用形態)。入力は馬力、予測対象は燃費。1979年型以前の307台で学習し、1980年型以降の85台で比較した。85 hpは誤差を読み分けるために置いた区切りで、運用閾値の根拠は持たせていない。

| 評価対象 | 台数 | 直線のMAE | 2次式のMAE |
| --- | ---: | ---: | ---: |
| 全体 | 85 | 7.249 mpg | 6.548 mpg |
| 85 hp未満 | 52 | 8.414 mpg | 6.832 mpg |
| 85 hp以上 | 33 | 5.415 mpg | 6.100 mpg |

全体の改善は85 hp未満の改善で生まれた。85 hp以上が主用途なら、この比較では直線が優位。実習では前回と同じ評価データを再利用した。これを見て手法を選ぶ場合、採用に向けた最終評価には、その用途を代表する別のデータが必要。

## コードと再実行

[固定版Auto.csv](https://github.com/intro-stat-learning/ISLP/blob/46fb7dfaa39a41c007c627cc6a90dba3a88e5b2c/ISLP/data/Auto.csv)と同じ場所で、下の検証コードを実行する。scikit-learnを使う場合は、馬力を1列の入力 `X_train` と `X_eval` にして、下の `degree` がモデルの形を変える箇所になる。ライブラリ例の実行は未確認。上の数値は、折りたたみ内の標準Pythonによる最小二乗の実行結果。

```python
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

model = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    LinearRegression(),
)
model.fit(X_train, y_train)
prediction = model.predict(X_eval)
```

<details>
<summary>実行したPythonコードと出力</summary>

```python
from csv import DictReader
from pathlib import Path
from statistics import mean

with Path("Auto.csv").open() as file:
    points = [(int(r["year"]), float(r["horsepower"]), float(r["mpg"]))
              for r in DictReader(file)]

# 馬力の単位を100 hpにそろえ、学習データの平均を原点にする。
train = [(hp, mpg) for year, hp, mpg in points if year < 80]
test = [(hp, mpg) for year, hp, mpg in points if year >= 80]
center = mean(hp for hp, _ in train)
x = [(hp - center) / 100 for hp, _ in train]
y = [mpg for _, mpg in train]
x2 = [value ** 2 for value in x]
x2_mean, y_mean = mean(x2), mean(y)
z = [square - x2_mean for square in x2]
dy = [value - y_mean for value in y]

def dot(left, right):
    return sum(a * b for a, b in zip(left, right))

# 最小二乗。直線は x だけ、2次式は x と x² の係数を同時に求める。
xx, xz, zz = dot(x, x), dot(x, z), dot(z, z)
xy, zy = dot(x, dy), dot(z, dy)
linear_slope = xy / xx
det = xx * zz - xz ** 2
quadratic_slope = (xy * zz - zy * xz) / det
curvature = (zy * xx - xy * xz) / det

for name, rows in [
    ("all", test),
    ("under 85 hp", [(hp, mpg) for hp, mpg in test if hp < 85]),
    ("85 hp and up", [(hp, mpg) for hp, mpg in test if hp >= 85]),
]:
    scaled = [(hp - center) / 100 for hp, _ in rows]
    actual = [mpg for _, mpg in rows]
    line = [y_mean + linear_slope * x for x in scaled]
    curve = [y_mean + quadratic_slope * x + curvature * (x ** 2 - x2_mean)
             for x in scaled]
    mae = lambda predictions: mean(abs(p - y) for p, y in zip(predictions, actual))
    print(f"{name}: n={len(rows)}, linear={mae(line):.3f}, quadratic={mae(curve):.3f}")
```

```text
all: n=85, linear=7.249, quadratic=6.548
under 85 hp: n=52, linear=8.414, quadratic=6.832
85 hp and up: n=33, linear=5.415, quadratic=6.100
```

</details>
