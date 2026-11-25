from csv import DictReader
from pathlib import Path
from statistics import mean

csv_path = Path(__file__).resolve().parents[1] / "01-observations" / "measurements.csv"
with csv_path.open(encoding="utf-8", newline="") as file:
    rows = list(DictReader(file))

temperatures = [int(row["temperature_c"]) for row in rows]
offsets = [int(row["reading_g"]) - int(row["reference_g"]) for row in rows]
temperature_mean = mean(temperatures)
offset_mean = mean(offsets)

temperature_diffs = [temperature - temperature_mean for temperature in temperatures]
offset_diffs = [offset - offset_mean for offset in offsets]
cross_sum = sum(dx * dy for dx, dy in zip(temperature_diffs, offset_diffs))
square_sum = sum(dx ** 2 for dx in temperature_diffs)
slope = cross_sum / square_sum

constant_predictions = [offset_mean for temperature in temperatures]
line_predictions = [offset_mean + slope * dx for dx in temperature_diffs]

constant_sse = sum((actual - predicted) ** 2 for actual, predicted in zip(offsets, constant_predictions))
line_sse = sum((actual - predicted) ** 2 for actual, predicted in zip(offsets, line_predictions))

print(f"測定1: {temperatures[0]} ℃、実測 {offsets[0]:+d} g、"
      f"平均の予測 {constant_predictions[0]:+.1f} g、直線の予測 {line_predictions[0]:+.1f} g")
print(f"平均温度: {temperature_mean:g} ℃、平均のずれ: {offset_mean:g} g")
print(f"傾き: {cross_sum:g} / {square_sum:g} = {slope:+.2f} g/℃")
print(f"二乗和: 平均 {constant_sse:g} g²、直線 {line_sse:g} g²")
