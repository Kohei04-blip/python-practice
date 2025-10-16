# csv_reader_safe.py
# 使い方例:
#   python csv_reader_safe.py "week2/data/*.csv"

import sys, glob
import pandas as pd

ENCODINGS = ("utf-8-sig", "cp932", "utf-8")
REQUIRED_COLS = None  # 例: {"item","qty","price"} にすると必須列チェック

def read_csv_fallback(path):
    last_err = None
    for enc in ENCODINGS:
        try:
            return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError as e:
            last_err = e
            continue
    # 文字コードで読めず
    raise last_err if last_err else UnicodeDecodeError("unknown", b"", 0, 0, "encoding NG")

def main():
    if len(sys.argv) < 2:
        print("使い方: python csv_reader_safe.py \"week2/data/*.csv\"")
        sys.exit(1)

    pattern = sys.argv[1]
    files = glob.glob(pattern)
    if not files:
        print(f"[ERROR] パターンに一致するファイルがありません: {pattern}")
        sys.exit(2)

    read_ok, skipped, total_rows = 0, 0, 0

    for f in files:
        try:
            df = read_csv_fallback(f)

            # 空行・完全欠損を落とす（任意）
            df = df.dropna(how="all")

            # 必須列チェック（設定があれば）
            if REQUIRED_COLS and not REQUIRED_COLS.issubset(df.columns):
                missing = REQUIRED_COLS - set(df.columns)
                print(f"[SKIP] {f}: 必須列不足 → {missing}")
                skipped += 1
                continue

            print(f"[OK] {f}: {len(df)} 行 読み込み")
            read_ok += 1
            total_rows += len(df)

        except FileNotFoundError:
            print(f"[SKIP] {f}: ファイルが見つかりません")
            skipped += 1
        except UnicodeDecodeError:
            print(f"[SKIP] {f}: 文字コードの問題で読めません")
            skipped += 1
        except pd.errors.EmptyDataError:
            print(f"[SKIP] {f}: 空ファイル（データなし）")
            skipped += 1
        except Exception as e:
            print(f"[SKIP] {f}: 想定外エラー: {e}")
            skipped += 1

    print(f"=== 結果: 読めた={read_ok}, スキップ={skipped}, 合計行数={total_rows} ===")

if __name__ == "__main__":
    main()
