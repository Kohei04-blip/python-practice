## try-except文の練習

a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("0では割れません！")
finally:
    print("処理が終わりました")
    

##類題

##問1:文字を数字に変換する

try:
    a =int(input("数字を入力してください："))
    number = a * 2
    print(number)
except ValueError:
    print("数字を入力してください！")
finally:
    print("処理終了")
    
##問2:リストの中身を取り出す

fruits = ["apple", "banana", "orange"]
try:
    a = int(input("何番目のフルーツを表示しますか？:"))
    print(fruits[a])
except IndexError:
    print("その番号はありません")
finally:
    print("終わり")

##問3:ファイルを開いて読む

# problem3_file_open.py
def main():
    fname = input("ファイル名を入力してください：").strip() # strip()で余分な空白を削除
    if not fname:
        print("ファイル名が空です。もう一度やり直してください。") # 入力が空の場合というチェック
        return

    try:
        with open(fname, "r", encoding="utf-8") as f:
            first_line = f.readline().rstrip("\n") # 1行目を読み込み、改行コードを削除
            if first_line == "":
                print("ファイルは空のようです（1行目がありません）。")
            else:
                print("1行目：", first_line)

    except FileNotFoundError:
        print(f"ファイルが見つかりません：{fname}")
    except PermissionError:
        print(f"ファイルを開く権限がありません：{fname}")
    except UnicodeDecodeError:
        print("文字コードの問題で読み込めませんでした。encoding を cp932 などに変えて再実行してください。")
    except Exception as e:
        print("想定外のエラーが発生しました：", e)
    finally:
        print("終了")

if __name__ == "__main__":
    main()
