import pandas as pd

try :
    df = pd.read_csv('sa.csv')
    print(df.head())

except FileNotFoundError :
    print("ファイルが見つかりません")
    