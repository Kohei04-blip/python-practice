# step4_loop_many.py
import glob, pandas as pd

def read_csv_fallback(path):
    for enc in ("utf-8-sig", "cp932", "utf-8"):
        try:
            return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError("unknown", b"", 0, 0, "encoding NG")

files = glob.glob("week2/data/*.csv")
read_ok, skipped = 0, 0

for f in files:
    try:
        df = read_csv_fallback(f)
        print(f"[OK] {f} 行数={len(df)}")
        read_ok += 1
    except FileNotFoundError:
        print(f"[SKIP] {f}: 見つかりません")
        skipped += 1
    except UnicodeDecodeError:
        print(f"[SKIP] {f}: 文字コードNG")
        skipped += 1
    except Exception as e:
        print(f"[SKIP] {f}: 想定外のエラー: {e}")
        skipped += 1

print(f"=== 結果: 読めた={read_ok}, スキップ={skipped} ===")
