from csv import DictReader
from pathlib import Path
from statistics import mean

csv_path = Path(__file__).with_name("measurements.csv")
with csv_path.open(encoding="utf-8", newline="") as file:
    rows = list(DictReader(file))

observations = []
for row in rows:
    temperature = int(row["temperature_c"])
    reference = int(row["reference_g"])
    reading = int(row["reading_g"])
    offset = reading - reference
    observations.append((temperature, offset))

print(f"測定1: {observations[0][0]} ℃、ずれ {observations[0][1]:+d} g")

all_offsets = [offset for temperature, offset in observations]
print(f"全体: {len(all_offsets)} 件、平均 {mean(all_offsets):+.1f} g")

for target_temperature in (20, 25, 30):
    offsets = [
        offset
        for temperature, offset in observations
        if temperature == target_temperature
    ]
    print(
        f"{target_temperature} ℃: {offsets}、"
        f"平均 {mean(offsets):+.1f} g、範囲 {max(offsets) - min(offsets)} g"
    )
