# pdf_merge_safe.py
# 依存: pip install pypdf

from __future__ import annotations
import argparse
import glob
from pathlib import Path
from typing import List

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError

def gather_inputs(patterns: List[str]) -> List[Path]:
    files: List[Path] = []
    seen = set()
    for p in patterns:
        expanded = glob.glob(p) if any(ch in p for ch in "*?[]") else [p]
        for path_str in expanded:
            path = Path(path_str)
            if path.suffix.lower() != ".pdf":
                continue
            if path.exists() and path.is_file() and path not in seen:
                files.append(path)
                seen.add(path)
    return files

def read_pages_safely(pdf_path: Path) -> int | None:
    try:
        reader = PdfReader(str(pdf_path))
        if getattr(reader, "is_encrypted", False):
            try:
                ok = reader.decrypt("")
                if not ok and ok != 1:
                    print(f"[SKIP] 暗号化の解除に失敗: {pdf_path.name}")
                    return None
            except Exception:
                print(f"[SKIP] 暗号化の解除に失敗: {pdf_path.name}")
                return None
        return len(reader.pages)
    except FileNotFoundError:
        print(f"[SKIP] 見つかりません: {pdf_path}")
    except PdfReadError:
        print(f"[SKIP] 破損/不正なPDFです: {pdf_path.name}")
    except Exception as e:
        print(f"[SKIP] 想定外エラー({pdf_path.name}): {e}")
    return None

def merge_pdfs(inputs: List[Path], output: Path) -> None:
    writer = PdfWriter()
    ok_files = 0
    skipped = 0
    total_pages = 0

    for pdf in inputs:
        pages = read_pages_safely(pdf)
        if pages is None:
            skipped += 1
            continue
        try:
            reader = PdfReader(str(pdf))
            if getattr(reader, "is_encrypted", False):
                try:
                    ok = reader.decrypt("")
                    if not ok and ok != 1:
                        print(f"[SKIP] 暗号化PDFを結合できません: {pdf.name}")
                        skipped += 1
                        continue
                except Exception:
                    print(f"[SKIP] 暗号化PDFを結合できません: {pdf.name}")
                    skipped += 1
                    continue

            for i in range(len(reader.pages)):
                writer.add_page(reader.pages[i])
            ok_files += 1
            total_pages += len(reader.pages)
            print(f"[OK] 追加: {pdf.name}（{len(reader.pages)}ページ）")
        except PdfReadError:
            print(f"[SKIP] 読込エラー: {pdf.name}")
            skipped += 1
        except Exception as e:
            print(f"[SKIP] 想定外エラー({pdf.name}): {e}")
            skipped += 1

    output.parent.mkdir(parents=True, exist_ok=True)

    if ok_files == 0:
        print("[ERROR] 結合できるPDFがありませんでした。出力は作成しません。")
        return

    try:
        with open(output, "wb") as f:
            writer.write(f)
        print(f"=== 完了: {ok_files}ファイル結合 / スキップ{skipped} / 合計{total_pages}ページ ===")
        print(f"出力: {output}")
    except PermissionError:
        print(f"[ERROR] 出力先に書き込めませんでした: {output}")
    except Exception as e:
        print(f"[ERROR] 出力時の想定外エラー: {e}")

def main():
    parser = argparse.ArgumentParser(description="PDFを安全に結合（壊れていてもスキップ）")
    parser.add_argument("--input", nargs="+", required=True,
                        help="入力PDFパターンまたはファイル群（例: 'week2/pdfs/*.pdf'）")
    parser.add_argument("--output", required=True,
                        help="出力PDF（例: week2/output/merged.pdf）")
    args = parser.parse_args()

    inputs = gather_inputs(args.input)
    if not inputs:
        print("[ERROR] 入力PDFが見つかりませんでした。パス/パターンを確認してください。")
        return

    merge_pdfs(inputs, Path(args.output))

if __name__ == "__main__":
    main()
