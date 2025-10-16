import pandas as pd

def read_csv_fallback(path):
    for enc in ("utf-8-sig","cp932","utf-8"):
        try:
            return pd.read_csv(path,encoding=enc)
        except UnicodeDecodeError:
            #次のエンコードでリトライ
            pass
        #ここまで来たら文字コードでは読めなかった
        raise UnicodeDecodeError("unknown", b"", 0, 0,"すべての文字コードで読めませんでした")
    
try:
    df = read_csv_fallback("week2/data/bad_encoding.csv")
    print(df.head())
except FileExistsError:
    print("ファイルが見つかりません。")
except UnboundLocalError:
    print("文字コードの問題で読み込めませんでした。")
    
    
        