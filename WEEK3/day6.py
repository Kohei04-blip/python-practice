# day6_encoding_error_repro.py
from pathlib import Path
import pandas as pd
from pandas.errors import EmptyDataError, ParserError

BASE = Path(__file__).resolve().parent
csv_path = BASE / "sample_cp932.csv"

def make_cp932_csv(path: Path) -> None:
    data = {
        "名前": ["山田太郎", "鈴木花子", "佐藤次郎"],
        "年齢": [28, 34, 22],
        "職業": ["エンジニア", "デザイナー", "マーケター"],
    }
    df = pd.DataFrame(data)
    # cp932(Shift-JIS)で保存
    df.to_csv(path, index=False, encoding="cp932")
    print(f"[MAKE] 書き出し完了: {path}（encoding=cp932）")

def read_as_utf8_then_observe_error(path: Path) -> None:
    print("[READ] encoding='utf-8' で読み込みを試します（エラー再現が目的）")
    try:
        df = pd.read_csv(path, encoding="utf-8")
        # ここに来たら想定外（本来はUnicodeDecodeErrorのはず）
        print("[WARN] 予想外：エラーが出ずに読み込めました。先頭5行：")
        print(df.head())
    except UnicodeDecodeError as e:
        print(f"[OK] 期待通り UnicodeDecodeError を捕捉：{e}")

        # Day7 への布石：cp932 での再読み込み
        print("[RETRY] encoding='cp932' で再読み込みします…")
        try:
            df_cp = pd.read_csv(path, encoding="cp932")
            print("[OK] cp932 での再読み込み成功。先頭5行：")
            print(df_cp.head())
        except Exception as e2:
            print(f"[ERROR] cp932 でも読めませんでした：{type(e2).__name__}: {e2}")

if __name__ == "__main__":
    make_cp932_csv(csv_path)
    read_as_utf8_then_observe_error(csv_path)
