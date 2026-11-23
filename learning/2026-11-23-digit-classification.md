# 二値分類 — 手書き数字の「8」を確認に回す

検索用の別名：分類、二値分類、再現率、誤検出率、混同行列、分類のしきい値

[ロードマップ](../ROADMAP.md#現在の実習と次の再開点)の統計的機械学習。前の回帰では燃費のような数値を推定した。今回は画像1枚ごとに「確認に回す・回さない」を決める。

## 問いと前提

手書き数字の画像から「8」を見つけて人の確認に回す。教材上、優先するのは本物の8の見逃しを減らすこと。全件を確認に回すと人の負担が増えるので、比較前に「8を80%以上拾う」「8以外を誤って回す割合は10%以下」の両方を条件に置いた。数値は教材用の設定。実運用では見逃しの影響と確認の処理能力から決める。

復習では、すべてを「8ではない」とする方法がなぜ全体正解率では高く見えるかを説明する。別のケースで、他クラスが増えたときに、人が確認する総件数を把握するには何を数えるべきかを考える。

## 教材の説明

画像の64個の値は、8×8に並ぶ各区画のインクの量を表す。学習用の画像だけから、「8」と「それ以外」の平均画像を1枚ずつ作る。各マスの差を二乗して足すと、画像同士の距離を数値にできる。「それ以外への距離 − 8への距離」が大きい画像ほど、8の平均画像に相対的に似ている。ここでは学習側の8以外のうち、上位10%を上限に通す点数をしきい値にした。ちょうど境界の画像は送らない。

再現率の分母は本物の8、誤検出率の分母は8以外。人に回す総件数は、拾った8と誤って送ったものの合計。

## 実行で確認した事実

[scikit-learn 1.8.0 同梱データ](https://github.com/scikit-learn/scikit-learn/blob/1.8.0/sklearn/datasets/data/digits.csv.gz)を利用。元データは Alpaydin・Kaynak の [UCI Optical Recognition of Handwritten Digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits)（DOI 10.24432/C50P49、CC BY 4.0）。同梱版は元データの一部。元データはリンクで参照し、CSVの複製は配置しない。各行の最後の値が正解の数字で、残り64個を画像として利用した。gzipファイルのSHA-256は `09f66e6debdee2cd2b5ae59e0d6abbb73fc2b0e0185d2e1957e9ebb51e23aa22`。

数字ごとにシード8で混ぜ、先に学習1074枚・比較359枚・最終確認364枚に分けた。この分割は画像単位。未知の書き手への性能を主張するなら、書き手が重複しない分割が別途必要。

| 方法 | 8を拾う | 8を見逃す | 8以外を誤って回す | 8以外を回さない |
| --- | ---: | ---: | ---: | ---: |
| 何も回さない | 0 | 35 | 0 | 324 |
| 2枚の平均画像で比較 | 28 | 7 | 24 | 300 |

何も回さない場合でも、全体正解率は324/359（90.3%）。平均画像方式は再現率28/35（80.0%）、誤検出率24/324（7.4%）で、比較用データでは両条件を満たした。人に回る画像は52枚で、うち24枚は8以外。次は学習で決まった方式と境界を固定して、今回スコアを計算しなかった364枚でも両条件を満たすか一度確認する。

## 本人の予想と解釈

- 実行前の予想：
- 結果を見ての解釈：

## コードと再実行

Apple Silicon MacのPython 3.9.6で実行。上記の固定版gzipファイルと下のコードを同じ場所に置き、コードを `digits.py` として `python3 digits.py digits.csv.gz` で実行できる。`score` が距離の差を返し、`threshold` が確認に回す水準を決める。scikit-learnでは同梱データを `load_digits()`、4種類の件数を `confusion_matrix(y_true, y_pred, labels=[False, True])`（結果は `[[TN, FP], [FN, TP]]`）で扱える。実行は標準Python版。

<details>
<summary>実行したPythonコード</summary>

```python
import csv
import gzip
import random
from statistics import mean
from sys import argv

with gzip.open(argv[1], "rt", newline="") as file:
    rows = [list(map(int, row)) for row in csv.reader(file)]

# 各数字を別々に混ぜ、60/20/20に分ける。
rng = random.Random(8)
train, valid, final = [], [], []
for digit in range(10):
    group = [row for row in rows if row[-1] == digit]
    rng.shuffle(group)
    n = len(group)
    train.extend(group[:3*n//5])
    valid.extend(group[3*n//5:4*n//5])
    final.extend(group[4*n//5:])

positive = [row[:-1] for row in train if row[-1] == 8]
negative = [row[:-1] for row in train if row[-1] != 8]
eight = [mean(column) for column in zip(*positive)]
other = [mean(column) for column in zip(*negative)]

def distance(pixels, template):
    return sum((a - b)**2 for a, b in zip(pixels, template))

def score(pixels):
    return distance(pixels, other) - distance(pixels, eight)

# 学習側の「8以外」で上位10%までが通る境界。境界と同点なら送らない。
negative_scores = sorted((score(row) for row in negative), reverse=True)
threshold = negative_scores[len(negative_scores)//10]
print("split:", len(train), len(valid), len(final))
print("threshold:", round(threshold, 2))
for label, rule in [("send none", lambda pixels: False),
                    ("templates", lambda pixels: score(pixels) > threshold)]:
    counts = {"TP": 0, "FN": 0, "FP": 0, "TN": 0}
    for row in valid:
        send = rule(row[:-1])
        key = ("TP" if send else "FN") if row[-1] == 8 else ("FP" if send else "TN")
        counts[key] += 1
    print(label, counts)
```

</details>
