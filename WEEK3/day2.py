from pathlib import Path
import csv
import pandas as pd

BASE = Path(__file__).resolve().parent  # 将来のための安定パス
csv_path = BASE / "sample_test_1.csv"

# 1) CSVを書き出す
with csv_path.open('w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'address'])
    writer.writeheader()
    writer.writerow({'name': '山田太郎', 'age': 20, 'address': '東京都'})

# 2) CSVを読み込む（パス文字列でOK）
df = pd.read_csv(csv_path, encoding='utf-8-sig')

# 3) 確認表示（headの“結果”を使う）
print(df.head())

    