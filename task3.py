#2025-09-28 
#課題：CSVファイルを読み込み、合計金額を計算して表示する

#csvを書き込む

import csv 
with open("sample_2.csv","w",newline="",encoding="utf-8-sig") as f :
    writer = csv.DictWriter(f,fieldnames=["商品名","単価","数量"])
    writer.writeheader()
    writer.writerows([
        {"商品名":"ブドウ","単価":300,"数量":2},
        {"商品名":"いちご","単価":300,"数量":4},
        {"商品名":"もも","単価":400,"数量":2},
    ])

#csvを読み込み、合計金額を計算する

import csv
def to_int(s):
    return int(str(s).replace(",","").strip())

total= 0
with open("sample_2.csv","r",newline="",encoding="utf-8-sig") as f :
    reader =csv.DictReader(f)
    for row in reader:
        total += to_int(row["単価"]) * to_int(row["数量"])
print(f"合計金額: {total}円")