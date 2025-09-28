#2025-09-27 
#課題：CSVファイルを読み込み、合計金額を計算して表示する

#1.何もない状態から、PythonでCSVファイルを生成する

#CSVライブラリをインポート
import csv
#header配列にデータ代入
header = ['ID','num']
#body配列にデータ代入
body = [
        ['cherry',50],
        ['strawberry',90],
        ['peach',350],
    ]
#sample.csvファイルを書き込みで開いてfというオブジェクトで利用
with open('sample.csv','w') as f:
    
    #writerオブジェクトにfオブジェクトを書き込む準備
    writer = csv.writer(f)
    #header配列を1行目に書き込む
    writer.writerow(header)
    #body配列を2行目以降に書き込む
    writer.writerows(body)
#ファイルを閉じる
f.close()

#2.CSVファイルの読み込み

import csv
#sample.csvという名前のCSVファイルをrという指定で読み込むためにopenメソッドで開く
file = open('sample.csv','r')
#csv.readerで読み込み、dataオブジェクトに代入
data = csv.reader(file)
#dataオブジェクトの中身を1行ずつrowに取り出し、さらにrowの中身を1列ずつcolに取り出して表示
for row in data:
    #rowの中身を1列ずつcolに取り出して表示
    for col in row:
        #colの中身を表示
        print(col,end=',')
    #1行表示したら改行
    print()
#ファイルを閉じる
file.close()

#3.CSVファイルの合計金額を計算して表示

import pandas as  pd

#sample.csvという名前のCSVファイルを読み込む
df = pd.read_csv('sample.csv')
#num列の合計を計算してtotalに代入
total = df['num'].sum()
#合計金額を表示
print('合計金額:',total)
#合計金額: 490 



