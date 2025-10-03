def main() :
    filename = input("ファイル名を記入してください：").strip()
    
    try :
        with open(filename,"r",encoding="utf-8") as f :
            context = f.read()
            print("ファイル名：")
            print(context)
    
    except FileNotFoundError :
        print(f"ファイルが見つかりません：",{filename})
        
    except PermissionError :
        print(f"権限が見つかりません：",{filename})
        
    except UnicodeDecodeError :
        print("文字コードの問題で読み込みませんでした。")
    
    except Exception as e :
        print("予期せぬエラーが起きました:",e)
        
    finally :
        print("処理終了")

if __name__ == "__main__" :
    main()