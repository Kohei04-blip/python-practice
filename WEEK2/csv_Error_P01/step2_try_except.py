#何もないデータを読み込んだ時
import pandas as pd 
try:
    df = pd.read_csv("WEEK2/data/missing.csv")
    print(df.head())
    
except FileNotFoundError:
    print("ファイルが見つかりません。名前を確認してください。")
   
 