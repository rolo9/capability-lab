# 平均と線形回帰の違いを見分ける

検索用の別名：単回帰、線形回帰、ベースライン、合成データ、MAE、時系列分割

[ロードマップ](../ROADMAP.md#現在地と再開点)の統計から機械学習への入口。[先行したセンサー実習](2026-11-21-sensor-temperature-regression.md)を踏まえ、入力を使う価値がどんな条件で生まれるかを確かめる。

## 教材の説明

学習データの平均を返す方法は、入力が変わっても予測を変えない。単回帰は、学習点に対する残差の二乗和が最小になる直線を作る。評価では、学習に使っていない同一のデータで平均絶対誤差（MAE）を比べる。[ISLP Python版](https://www.statlearning.com/)の第2章は学習と評価、第3章は最小二乗と単回帰を扱う。

## 結果を見る前に決めた合成データの構造

温度とずれの関係を `ずれ = 傾き × (温度 − 25) + ノイズ` と置く。傾きが0.30の条件では入力が予測に役立つと見込み、傾きが0の条件では平均を上回る理由が乏しいと見込む。変えるのは傾きだけ。温度、学習・評価の分け方、乱数シード42、各行のノイズと指標をそろえる。想定した違いを見せる教材として設計した。

## 実行で確認した事実

| データ | 分け方 | 平均のMAE | 線形回帰のMAE |
| --- | --- | ---: | ---: |
| 合成・傾きあり | 学習18件／評価15件 | 0.720 g | 0.221 g |
| 合成・傾きなし | 学習18件／評価15件 | 0.215 g | 0.221 g |
| 公開Auto | 1979年型以前307台／1980年型以降85台 | 11.040 mpg | 7.249 mpg |

合成データでは傾きの有無だけで、直線を使う価値が変わった。公開Autoは[ISLPのデータ説明](https://intro-stat-learning.github.io/ISLP/0.4.1/datasets/Auto.html)にある実測データ。馬力を入力、燃費を予測値とし、新しい年式でも過去の関係が使えるかを確認するため年式で分割した。今回の分割では平均に対して改善した。用途に合わせた許容誤差と、その用途を代表する評価データがあれば採用の判断に進める。

## 再実行する

[固定版のAuto.csv](https://github.com/intro-stat-learning/ISLP/blob/46fb7dfaa39a41c007c627cc6a90dba3a88e5b2c/ISLP/data/Auto.csv)を作業フォルダに保存し、同じ場所で次のPythonコードを実行する。合成データはコード内の生成式と固定シードから再生成する。平均と単回帰は[センサーNotebook](../notebooks/sensor-temperature-regression.ipynb)で用いた計算と同じ。

```python
from csv import DictReader
from pathlib import Path
from random import Random
from statistics import mean

def compare(label, train, test):
    xs, ys = zip(*train)
    x_mean, y_mean = mean(xs), mean(ys)
    slope = sum((x - x_mean) * (y - y_mean) for x, y in train) / sum(
        (x - x_mean) ** 2 for x in xs
    )
    intercept = y_mean - slope * x_mean
    mean_error = mean(abs(y - y_mean) for x, y in test)
    linear_error = mean(abs(y - (intercept + slope * x)) for x, y in test)
    print(f"{label}: train={len(train)}, test={len(test)}, "
          f"slope={slope:.3f}, mean MAE={mean_error:.3f}, linear MAE={linear_error:.3f}")

rng = Random(42)
train_x = [20, 22, 24, 26, 28, 30] * 3
test_x = [21, 23, 25, 27, 29] * 3
train_noise = [rng.uniform(-0.35, 0.35) for _ in train_x]
test_noise = [rng.uniform(-0.35, 0.35) for _ in test_x]
for true_slope in (0.30, 0.0):
    train = [(x, true_slope * (x - 25) + e) for x, e in zip(train_x, train_noise)]
    test = [(x, true_slope * (x - 25) + e) for x, e in zip(test_x, test_noise)]
    compare(f"synthetic slope={true_slope:.2f}", train, test)

with Path("Auto.csv").open() as file:
    auto = [(int(row["year"]), float(row["horsepower"]), float(row["mpg"]))
            for row in DictReader(file)]
assert len(auto) == 392
train = [(hp, mpg) for year, hp, mpg in auto if year < 80]
test = [(hp, mpg) for year, hp, mpg in auto if year >= 80]
compare("Auto, model year split", train, test)
```

```text
synthetic slope=0.30: train=18, test=15, slope=0.310, mean MAE=0.720, linear MAE=0.221
synthetic slope=0.00: train=18, test=15, slope=0.010, mean MAE=0.215, linear MAE=0.221
Auto, model year split: train=307, test=85, slope=-0.128, mean MAE=11.040, linear MAE=7.249
```
