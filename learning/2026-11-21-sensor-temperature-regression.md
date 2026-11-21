# 温度でセンサーのずれを予測できるか

検索用の別名：単回帰、線形回帰、最小二乗、ベースライン、学習データと評価データ、MAE

現在地は[統計から機械学習への入口](../ROADMAP.md#現在地と再開点)。

## 答えを見る前に考える

同じ100 gのおもりを、同じ重量センサーで量る架空の実験。表示値から100 gを引いた値を「ずれ」とする。1日目の記録は次のとおり。

| 温度 | 20 ℃ | 25 ℃ | 30 ℃ |
| --- | ---: | ---: | ---: |
| ずれ | −2 g | ＋1 g | ＋1 g |

別の日に22 ℃と28 ℃で測る。**温度で予測を変える方がよさそうか、それとも1日目の平均で十分そうか。そう考えた理由は？** 最初の実習では、ここでHiroさんの回答を待つ。

復習するときは、**学習データに直線がよく合ったとして、別の日にも使えるかをどう確かめるか**を先に考える。

## 教材の説明

[ISLP Python版](https://www.statlearning.com/) 第2章は学習誤差と評価誤差、第3章は単回帰と最小二乗を扱う。基準モデルは1日目のずれの平均を返す。単回帰は1日目の残差の二乗和が最小になる傾きと切片を求める。どちらが別の日に役立つかは、同じ評価行で予測と記録の差の絶対値を平均して比べる（MAE、単位はg）。

## 実行で確認した事実

<details>
<summary>答え合わせと元資料</summary>

- 元データは架空の[学習用CSV](../data/sensor-temperature/train.csv)と[評価用CSV](../data/sensor-temperature/evaluation.csv)。評価用のずれは予測を出した後に読む。
- 温度を予測に使うかを変える。評価日、評価行、真の重量、センサー、指標をそろえる。評価する温度は学習データの範囲内。
- [Notebook](../notebooks/sensor-temperature-regression.ipynb)で、平均と `DummyRegressor`、最小二乗と `LinearRegression`、22 ℃での式と `predict` を照合する。
- 実習の評価表・MAE・図はNotebookの「3. 別の日で評価する」に出力される。Hiroさんの実行結果と復習用の図へのリンクは、実習後に追記する。

</details>

## 採用条件を決めた追加検証

実習上の運用条件として、21・25・29 ℃で測定し、**絶対誤差が1.00 g以内の測定が90％以上**なら採用候補とする。両方が通ればMAEの小さい手法を選ぶ。この条件は検証用の仮定であり、実機の仕様値ではない。3〜6日目の[架空の採用判定用CSV](../data/sensor-temperature/adoption-check.csv)を用意し、両モデルを再学習せず、同じ12件に適用した。1日目で決めた予測は平均が0 g、線形回帰が `0.30 × 温度 − 7.50` g。

| 方法 | MAE | 最大絶対誤差 | 許容内 | 90％基準 |
| --- | ---: | ---: | ---: | --- |
| 平均 | 0.56 g | 1.30 g | 10/12（83.3％） | 未達 |
| 線形回帰 | 0.36 g | 1.10 g | 10/12（83.3％） | 未達 |

**この条件では両方とも採用保留。** 線形回帰の平均誤差は小さいが、6日目は実測のずれがほぼゼロで、21 ℃と29 ℃の予測がどちらも1.10 g外れた。平均を使う方法は4日目の21 ℃と5日目の29 ℃で許容範囲を超えた。90％を満たすには12件中11件以上が必要。条件を満たすモデルを探す場合は、この結果を参考に候補を見直し、最終判定にはまた別の日のデータを使う。

<details>
<summary>採用判定を再実行するPythonコード</summary>

リポジトリのルートで実行する。係数は最初のNotebookで確認した値に固定している。

```python
from csv import DictReader
from decimal import Decimal as D
from pathlib import Path
from statistics import mean

limit = D("1.00")
required_rate = D("0.90")
path = Path("data/sensor-temperature/adoption-check.csv")
rows = list(DictReader(path.read_text().splitlines()))
for name, predict in {
    "mean": lambda t: D("0"),
    "linear": lambda t: D("0.30") * t - D("7.50"),
}.items():
    errors = [abs(predict(D(row["temperature_c"])) - D(row["offset_g"])) for row in rows]
    passed = sum(error <= limit for error in errors)
    failures = [(row["day"], row["temperature_c"]) for row, error in zip(rows, errors) if error > limit]
    print(f"{name}: MAE={mean(errors):.2f} g, max={max(errors):.2f} g, within limit={passed}/{len(rows)}, pass={D(passed)/len(rows) >= required_rate}, failures={failures}")
```

</details>

## Hiroさん自身の予想と解釈

- 実行前の予想
- 実行後の解釈

## 別のケースで判断する

同じ機種の**別の個体**に、この補正式を使ってよいか。「使う」「見送る」「追加で確かめる」から選び、今回のデータがその判断をどこまで支えるかを説明する。復習では、元の記録に戻れるか、考え方を自分で説明できるか、初見のケースで理由付きで判断できるかを確認する。

## Macで再実行する

最新版を取得した作業フォルダで、Docker Desktop起動後に `make up`、次に `make jupyter` を実行する。旧コンテナが動いている場合は、Notebookを保存してから `make down` で止めて起動し直す。[実習Notebook](../notebooks/sensor-temperature-regression.ipynb)を開き、番号順にセルを実行する。

「2. 22 ℃の予測を1行で書く」の `prediction_22 = None` を、傾き・切片・`temperature_c` を使う式に書き換える。照合が通ったら評価セルで表と図を確認する。最後に、図を根拠にした解釈を記録する。
