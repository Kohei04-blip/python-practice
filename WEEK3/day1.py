# day1_path_check.py
from pathlib import Path

def main():
    # 1) 相対パスを作る（今日はテストとして "test.csv" を想定）
    p = Path("test.csv")

    # 2) 絶対パスに変換して表示
    abs_p = p.resolve()
    print("[ABS]", abs_p)

    # 3) 存在チェック（ファイルがなくてもOK：Falseが出れば正常）
    print("[EXISTS]", p.exists())

    # 4) 通常ファイルかどうか（ディレクトリではないか）
    print("[IS_FILE]", p.is_file())

    # 5) 親フォルダ、拡張子、名前
    print("[PARENT]", p.parent)
    print("[SUFFIX]", p.suffix)
    print("[NAME]", p.name)

if __name__ == "__main__":
    main()
