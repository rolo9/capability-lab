# 二値分類の採用判断 — 2つのセンサーを使う

検索用の別名：分類、採用基準、ホールドアウト、holdout、二値分類、混同行列

## 比較前に決めた設計

模擬設備で、次の点検に回すべきケースを見つける。点検漏れを抑えつつ、正常な設備を点検に回す負担も抑えたい。本教材の合格条件は**再現率90%以上、誤検出率10%以下**。実運用の基準は点検能力や見逃しの損失から決める。

人工データを選んだのは、条件を満たす見込みのある事例で、分岐がどう改善につながるかを追うため。負荷と振動は独立に生成し、ともに高い場合に異常とする。高い状態の比率は各65%。測定値は低い状態で0〜0.4、高い状態で0.6〜1.0の範囲から生成する。ラベルは5%の確率で反転させ、測定値だけでは説明できない例を残す。これは教材用に設計した分布。

- 学習2,000件、検証1,000件、最終テスト1,000件。生成シードは順に11、22、33。最終テストは候補を決めるまで生成しない。
- 基準は深さ1の決定木、候補は深さ2。入力、データ、乱数、判定方法をそろえる。深さ1では1つの条件、深さ2では2条件の組み合わせを表現できる。
- 両モデルを検証し、事前条件を満たす最も浅いモデルを固定する。候補がなければ保留。候補があれば最終テストで同じ条件を一度確認し、両方を満たした場合に限り、この模擬条件の範囲で採用と判断する。

## 入力から予測までを1件ずつ追う

前回の[6件で最初の分岐を手計算した実習](2026-11-24-decision-tree-first-split.md#6件から分岐を作る)では、1つの質問でデータを左右に分けた。今回は、その質問を**予測1件につき最大何回できるか**を変える。分岐の終点を葉ノード（leaf node）と呼ぶ。 [決定木の用語表](2026-11-24-decision-tree-first-split.md#専門資料で使う用語)

### 1. データを作り、入力と正解に分ける

`X_train, y_train = make_data(2000, 11)` は入力2列×2,000件と、正解2,000件を返す。実際に出力した先頭の1件は次のとおり。

```text
first training row: [0.9696842336094917, 0.7862600280399094] True
```

入力の順は負荷、振動。最後の `True` は点検対象という正解で、予測に渡す2つの測定値とは別に持つ。検証・最終テストも同じ形で、各1,000件。

### 2. 深さが違うと何を質問できるか

`fit(X_train, y_train)` は学習済みの決定木を返す。どの列をどこで分けるかはデータから決まる。`export_text(model, ...)` がその分岐を文字列で返す。以下は実行出力（境界の表示は丸め）。

```text
|--- vibration <= 0.60
|   |--- class: False
|--- vibration >  0.60
|   |--- class: True

|--- vibration <= 0.60
|   |--- vibration <= 0.39
|   |   |--- class: False
|   |--- vibration >  0.39
|   |   |--- class: False
|--- vibration >  0.60
|   |--- load <= 0.40
|   |   |--- class: False
|   |--- load >  0.40
|   |   |--- class: True
```

前半の深さ1は、振動の質問1回で判定する。後半の深さ2は、高振動側で負荷をもう1回質問できる。たとえば上の先頭行は振動0.786と負荷0.970なので、深さ2では質問を2回通って `True` になる。一方、仮に振動0.8・負荷0.2なら、深さ1は振動だけで `True`、深さ2は負荷まで見て `False` になる。深さ2は経路ごとの質問回数の上限。全体の質問数は2を超え得る。

### 3. 予測から集計表を作る

`model.predict(X_valid)` は検証の1,000件に対して `True/False` を1,000個返す。`confusion_matrix` は正解と順番に突き合わせて2×2に数える。深さ2の検証では `[[535, 23], [24, 418]]`。上の行は正常、下の行は異常。左列は点検に回さない、右列は回す。 [混同行列の復習](2026-11-23-digit-classification.md#分類の基礎--混同行列)

`evaluate` はこの表を `(TN, FP, FN, TP) = (535, 23, 24, 418)` の順に取り出し、事前条件の合否 `True` と一緒に返す。下の結果表は、各回の件数を `results` に集め、コード末尾で `418/(418+24)` などを計算してMarkdownの表として出力したもの。

## 検証で選び、最終テストで判断する

| 評価 | 深さ上限 | 再現率 | 誤検出率 | 条件 |
| --- | ---: | ---: | ---: | --- |
| 検証 | 1 | 428/442 (96.8%) | 227/558 (40.7%) | 未達 |
| 検証 | 2 | 418/442 (94.6%) | 23/558 (4.1%) | 合格 |
| 最終テスト | 2 | 403/434 (92.9%) | 18/566 (3.2%) | 合格 |

深さ2では、検証上の見逃しは14件から24件に増えたが、誤検出は227件から23件に減った。最終テストでも事前条件を両方満たしたため、模擬条件で採用と判断した。モデルの深さや合格条件は最終テストの前後で変更していない。実機で使うには、実機データでの確認が必要。

`export_text` で学習した決定木の分岐を確認した。予測を変える条件は「振動が境界を超え、かつ負荷が境界を超える」。低振動側にも分岐が1つ入ったが、両方の葉ノード（leaf nodes）が正常判定なので、予測は変わらない。表示される境界値は丸められる。

## Pythonと復習

`make_data` が入力2列と正解を作る。`fit` が分岐を学習し、`predict` が各件を分類する。`confusion_matrix` がTN・FP・FN・TPを返す。深さが小さい順に比較して最初の合格候補を固定し、その後にだけシード33で最終テストを生成する。

振り返るときは「検証で決めたことと、最終テストで確かめたこと」を一言ずつ説明する。点検漏れの影響が大きい別の設備では、同じ基準を使う前に何を確認するかも考える。

```python
from random import Random

from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, export_text

def make_data(size, seed):
    rng = Random(seed)
    X, y = [], []
    for _ in range(size):
        load_high = rng.random() < 0.65
        vibration_high = rng.random() < 0.65
        X.append([
            rng.uniform(0.6, 1.0) if high else rng.uniform(0.0, 0.4)
            for high in (load_high, vibration_high)
        ])
        y.append((load_high and vibration_high) ^ (rng.random() < 0.05))
    return X, y

def evaluate(model, X, y):
    tn, fp, fn, tp = confusion_matrix(
        y, model.predict(X), labels=[False, True]
    ).ravel()
    recall = tp / (tp + fn)
    false_positive_rate = fp / (fp + tn)
    passed = recall >= 0.90 and false_positive_rate <= 0.10
    return (tn, fp, fn, tp), passed

X_train, y_train = make_data(2000, 11)
X_valid, y_valid = make_data(1000, 22)
print('first training row:', X_train[0], y_train[0])
selected = None
results = []
for depth in (1, 2):
    model = DecisionTreeClassifier(max_depth=depth, random_state=11)
    model.fit(X_train, y_train)
    counts, passed = evaluate(model, X_valid, y_valid)
    results.append(("検証", depth, counts, passed))
    print(export_text(model, feature_names=["load", "vibration"]))
    if passed and selected is None:
        selected = model

if selected is None:
    print("Hold: no candidate")
else:
    X_test, y_test = make_data(1000, 33)
    counts, passed = evaluate(selected, X_test, y_test)
    results.append(("最終テスト", selected.max_depth, counts, passed))

print("| 評価 | 深さ上限 | 再現率 | 誤検出率 | 条件 |")
print("| --- | ---: | ---: | ---: | --- |")
for stage, depth, (tn, fp, fn, tp), passed in results:
    positives = tp + fn
    negatives = fp + tn
    status = "合格" if passed else "未達"
    print(f"| {stage} | {depth} | {tp}/{positives} ({tp/positives:.1%}) "
          f"| {fp}/{negatives} ({fp/negatives:.1%}) | {status} |")
```
