# -*- coding: utf-8 -*-
"""全量入库：04-现代研究文献/03-文献下载/ 下所有未入库文件
- html/htm：提取正文（去 script/style/nav 等标签）-> references + fulltext native_text
- md/txt/srt/vtt：native_text
- pdf：文本层（有则入，无则跳过标记）
- epub：ebooklib 提取
- 幂等 + sha256/file_path/filename 去重
"""
import os, sqlite3, datetime, re, hashlib, sys

DB = "04-现代研究文献/05-参考文献全文数据库/references_fulltext.db"
BASE_DIR = "04-现代研究文献/03-文献下载"
BASE = "D:/librebsd"

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()

def extract_html_text(html):
    """提取网页正文：去 script/style/nav/header/footer/iframe 等"""
    # 去 script/style/nav 等块
    text = re.sub(r"<(script|style|nav|header|footer|iframe|form|aside|noscript)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    # 去注释
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    # 去标签
    text = re.sub(r"<[^>]+>", " ", text)
    # 去多余空白
    text = re.sub(r"\s+", " ", text)
    # 去常见导航词（保留正文）
    return text.strip()

def para_split(text):
    raw = [p.strip() for p in text.split("\n\n") if p.strip()]
    paras = []
    buf = ""
    for p in raw:
        p = " ".join(p.split())
        if len(p) < 40 and buf:
            buf += " " + p
            if len(buf) >= 40:
                paras.append(buf); buf = ""
        else:
            if buf:
                paras.append(buf); buf = ""
            paras.append(p)
    if buf:
        paras.append(buf)
    return paras

def extract_text(fp, low):
    """返回 (text, method) 或 None"""
    if low.endswith((".html", ".htm")):
        with open(fp, encoding="utf-8", errors="ignore") as f:
            raw = f.read()
        text = extract_html_text(raw)
        return (text, "native_text") if len(text) > 50 else None
    if low.endswith((".md", ".txt", ".srt", ".vtt")):
        with open(fp, encoding="utf-8", errors="ignore") as f:
            text = f.read()
        return (text, "native_text") if len(text.strip()) > 50 else None
    if low.endswith(".pdf"):
        import fitz
        fitz.TOOLS.mupdf_display_errors(False)
        doc = fitz.open(fp)
        text = ""
        for i in range(len(doc)):
            try:
                text += doc[i].get_text()
            except Exception:
                pass
        doc.close()
        return (text, "pymupdf_textlayer") if len(text.strip()) > 50 else None
    if low.endswith(".epub"):
        try:
            import ebooklib
            from ebooklib import epub
            book = epub.read_epub(fp)
            parts = []
            for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
                content = item.get_content().decode("utf-8", errors="ignore")
                parts.append(extract_html_text(content))
            text = "\n\n".join(p for p in parts if p)
            return (text, "pymupdf/ebooklib/mobi/xparse-ocr") if len(text) > 50 else None
        except Exception:
            return None
    return None  # 音频等其他格式

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    existing_fns = set()
    for (fn,) in cur.execute('SELECT filename FROM "references" WHERE filename IS NOT NULL'):
        existing_fns.add(fn)
    existing_paths = set()
    for (fp,) in cur.execute('SELECT file_path FROM "references" WHERE file_path IS NOT NULL'):
        existing_paths.add((fp or "").replace("\\", "/"))
    existing_shas = set()
    for (s,) in cur.execute('SELECT sha256 FROM "references" WHERE sha256 IS NOT NULL'):
        if s:
            existing_shas.add(s)

    # 收集未入库文件
    files = []
    for root, _, fs in os.walk(BASE_DIR):
        if "ocr" in root.split(os.sep) or "00-临时放置" in root or "10-无关文件" in root:
            continue
        for fn in fs:
            if fn.startswith("._"):
                continue
            low = fn.lower()
            if not low.endswith((".pdf", ".html", ".htm", ".md", ".txt", ".srt", ".vtt", ".epub")):
                continue
            rel = os.path.join(root, fn).replace("\\", "/")
            if fn in existing_fns or rel in existing_paths:
                continue
            files.append((os.path.join(root, fn), fn, rel))
    print(f"未入库文件: {len(files)}", flush=True)

    done = no_text = dup = fail = 0
    for i, (fp, fn, rel) in enumerate(files, 1):
        low = fn.lower()
        try:
            with open(fp, "rb") as f:
                head = f.read(4)
            if low.endswith(".pdf") and head != b"%PDF":
                fail += 1
                continue
            sha = sha256_file(fp)
            if sha in existing_shas:
                # sha256 重复：标记 reference_duplicates
                prim = cur.execute('SELECT id FROM "references" WHERE sha256=? LIMIT 1', (sha,)).fetchone()
                if prim:
                    cur.execute("INSERT OR IGNORE INTO reference_duplicates (primary_reference_id, duplicate_reference_id, duplicate_type, match_score, match_fields, merged_at, merged_by, merge_notes) VALUES (?,?,?,?,?,?,?,?)",
                                (prim[0], 0, "sha256", 1.0, "sha256", now, "full_ingest_20260808", f"sha256 dup for {fn}"))
                dup += 1
                continue
            res = extract_text(fp, low)
            if res is None:
                no_text += 1
                continue
            text, method = res
        except Exception as e:
            fail += 1
            continue
        # 建 references
        title = os.path.splitext(fn)[0].replace("_", " ").replace("-", " ")
        fmt = "html" if low.endswith((".html", ".htm")) else ("epub" if low.endswith(".epub") else "txt")
        cur.execute('''INSERT INTO "references" (title, author, year, format, file_path, filename, sha256, file_size, source_tier, created_at, updated_at, ocr_status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
            (title, "unknown", None, fmt, rel, fn, sha, os.path.getsize(fp), "primary", now, now, "verified"))
        rid = cur.lastrowid
        existing_shas.add(sha)
        existing_fns.add(fn)
        existing_paths.add(rel)
        # fulltext
        cur.execute("INSERT INTO fulltext (reference_id, content, char_count, extraction_method, extracted_at, encoding, line_ending) VALUES (?,?,?,?,?,?,?)",
                    (rid, text, len(text), method, now, "utf-8", "LF"))
        for blk in para_split(text):
            cur.execute("INSERT INTO fulltext_blocks (reference_id, block_index, block_type, block_level, block_content) VALUES (?,?,?,?,?)",
                        (rid, 0, "paragraph", 1, blk))
        done += 1
        if done % 100 == 0:
            con.commit()
            print(f"  进度 {done}/{i}", flush=True)
    con.commit()
    print(f"完成: 入库 {done}, 无文本/待OCR {no_text}, sha256重复 {dup}, 失败 {fail}", flush=True)
    con.close()

if __name__ == "__main__":
    main()
