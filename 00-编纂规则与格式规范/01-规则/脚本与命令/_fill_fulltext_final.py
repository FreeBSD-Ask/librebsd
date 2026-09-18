# -*- coding: utf-8 -*-
"""final 补齐 fulltext v2：子进程隔离 + 30 秒超时，处理剩余无 fulltext 记录
- PDF：文本层提取（子进程，超时保护）
- HTML/TXT：native_text
- 跳过：无文件、lit、CAJ、无文本层
"""
import os, sqlite3, datetime, re, subprocess, sys

DB = "04-现代研究文献/05-参考文献全文数据库/references_fulltext.db"
BASE = "D:/librebsd"

PDF_WORKER = r'''import fitz, sys, os
fitz.TOOLS.mupdf_display_errors(False)
p = sys.argv[1]
doc = fitz.open(p)
t = ""
for i in range(len(doc)):
    try: t += doc[i].get_text()
    except Exception: pass
doc.close()
print("TEXT_START")
print(t)
print("TEXT_END")
'''

def resolve(fp):
    if not fp:
        return None
    p = fp.replace("\\", "/")
    c1 = os.path.join(BASE, p)
    if os.path.exists(c1):
        return c1
    c2 = os.path.join(BASE, "04-现代研究文献/03-文献下载", p)
    if os.path.exists(c2):
        return c2
    return None

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

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = cur.execute('''SELECT r.id, r.filename, r.file_path FROM "references" r
        WHERE NOT EXISTS (SELECT 1 FROM fulltext f WHERE f.reference_id=r.id)
        AND r.filename NOT LIKE 'SFU_PUPS_%'
        AND r.filename NOT LIKE '%.caj'
        ORDER BY r.id''').fetchall()
    print(f"待处理: {len(rows)}", flush=True)
    done = no_file = no_text = fail = 0
    for i, (rid, fn, fp) in enumerate(rows, 1):
        real = resolve(fp)
        if not real:
            no_file += 1
            continue
        low = fn.lower()
        try:
            if low.endswith((".html", ".htm", ".txt")):
                with open(real, encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                if low.endswith((".html", ".htm")):
                    text = re.sub(r"<[^>]+>", " ", text)
                    text = re.sub(r"\s+", " ", text)
                method = "native_text"
                if len(text.strip()) < 50:
                    no_text += 1
                    continue
            else:
                # PDF 子进程提取（超时 30s）
                r = subprocess.run([sys.executable, "-c", PDF_WORKER, real],
                                   capture_output=True, text=True, timeout=30)
                out = r.stdout or ""
                if "TEXT_START" not in out:
                    fail += 1
                    continue
                text = out.split("TEXT_START", 1)[1].split("TEXT_END", 1)[0]
                method = "pymupdf_textlayer"
                if len(text.strip()) < 50:
                    no_text += 1
                    continue
        except subprocess.TimeoutExpired:
            fail += 1
            continue
        except Exception as e:
            fail += 1
            continue
        cur.execute('''INSERT INTO fulltext (reference_id, content, char_count, extraction_method, extracted_at, encoding, line_ending)
            VALUES (?,?,?,?,?,?,?)''', (rid, text, len(text), method, now, "utf-8", "LF"))
        for blk in para_split(text):
            cur.execute('''INSERT INTO fulltext_blocks (reference_id, block_index, block_type, block_level, block_content)
                VALUES (?,?,?,?,?)''', (rid, 0, "paragraph", 1, blk))
        done += 1
        if done % 50 == 0:
            con.commit()
            print(f"  进度 {done}/{i}", flush=True)
    con.commit()
    print(f"完成: 写入 {done}, 无文件 {no_file}, 无文本层 {no_text}, 失败 {fail}", flush=True)
    con.close()

if __name__ == "__main__":
    main()
