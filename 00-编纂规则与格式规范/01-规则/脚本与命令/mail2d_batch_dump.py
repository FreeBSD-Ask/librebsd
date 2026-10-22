# -*- coding: utf-8 -*-
"""邮件线通用批 dump（沿用本线 _gen_*_b*_survey.py 的 MAILDB/BATCH_OFF 口径）。

用法: C:/Python314/python.exe _mail2d_batch_dump.py <库名> <BATCH_OFF> [BATCH_N] [tag]
例:   C:/Python314/python.exe _mail2d_batch_dump.py freebsd-elastic 500 500 fe_b051

产出（落 script/_db_row_mining/）：
  <tag>_forread.txt            全文 dump（pk 升序）
  review_logs/<tag>_digest.txt pk|date|from|subject|body前420字（triage 视图）
  <tag>_heads.txt              ID/DATE/FROM/SUBJ 头（check/register 用）
只读源库。
"""
import glob
import io
import os
import re
import sys

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = r"d:\librebsd\03-原始史料库\11-邮件列表史料"

lib = sys.argv[1]
off = int(sys.argv[2])
n = int(sys.argv[3]) if len(sys.argv) > 3 else 500
tag = sys.argv[4] if len(sys.argv) > 4 else "%s_off%d" % (lib, off)

# 定位库文件（01-freebsd / 02-netbsd / 03-openbsd / 06-other-bsd）
cands = glob.glob(os.path.join(BASE, "*", "*", "%s.duckdb" % lib))
if not cands:
    sys.exit("未找到库文件: %s" % lib)
src = cands[0]
con = duckdb.connect(src, read_only=True)
tot = con.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
rows = con.execute(
    "SELECT id, date, from_name, from_email, subject, body FROM messages "
    "ORDER BY CAST(id AS BIGINT) ASC LIMIT ? OFFSET ?", [n, off]).fetchall()
con.close()
print("[dump] %s offset=%d n=%d 取到 %d 行（全库 %d）" % (lib, off, n, len(rows), tot))


def clean(s):
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "/").strip()


# 自有文本比例阈值（2026-09-24 主理人增补）：
#   own_ratio < FULL_RATIO 或全文 < FULL_MINCH 时，digest 直接内联不截断正文。
# 依据：420 字截断导致的臆造率单调上升（tk 段1 5.5% → 段2 22.6% → 段3 1181 条 = 23.6%），
# 任务书里的「不得因看不到后文断言原文无实质论述」属事后纪律，生成不了它没看到的内容。
# 这里把该判断前移到脚本：引用密／过短的封给全量正文，零额外人力。
FULL_RATIO = float(os.environ.get("FULL_RATIO", "0.30"))
FULL_MINCH = int(os.environ.get("FULL_MINCH", "200"))


def own_ratio(body):
    """去掉 '> 引用行' 后的字符数 / 总字符数。无引用返回 1.0。"""
    b = str(body or "")
    if not b.strip():
        return 0.0
    own = sum(len(ln) for ln in b.splitlines()
              if not ln.lstrip().startswith(">"))
    tot = sum(len(ln) for ln in b.splitlines())
    return (float(own) / tot) if tot else 0.0


SUBJ_RE = re.compile(r"(?im)^[>\s]*Subject:\s*(.+?)\s*$")


def subj_of(subj, body):
    """主题兜底：subject 字段为空时，从正文头部解析 `Subject:` 行。

    背景：个别库（如 port-alpha，6922 封中仅 7 封 subject 非空）把主题嵌在正文里
    （形如 `Body of article empty.\\nTo: ...\\nSubject: xxx\\n\\n...`），
    若不作兜底，digest 会整列丢失主题，读手失去关键信号。
    """
    s = str(subj or "").strip()
    if s:
        return s
    m = SUBJ_RE.search(str(body or "")[:1500])
    return m.group(1).strip() if m else ""


with io.open(os.path.join(HERE, "%s_forread.txt" % tag), "w", encoding="utf-8", newline="\n") as f:
    for i, (pk, dt, fn, fe, subj, body) in enumerate(rows, off):
        f.write("===== 序 %d | PK %s =====\nDATE: %s\nFROM: %s <%s>\nSUBJ: %s\n\n%s\n\n"
                % (i, pk, str(dt)[:10], fn, fe, subj_of(subj, body), body))
full_n, full_len = 0, []
with io.open(os.path.join(HERE, "review_logs", "%s_digest.txt" % tag), "w", encoding="utf-8", newline="\n") as f:
    trunc_n = 0
    for pk, dt, fn, fe, subj, body in rows:
        cb = clean(body)
        r = own_ratio(body)
        if r < FULL_RATIO or len(cb) < FULL_MINCH:
            f.write("%s|%s|%s|%s|%s\n" % (pk, str(dt)[:10], clean(fn)[:40],
                                           clean(subj_of(subj, body))[:70], cb))
            full_n += 1
            full_len.append(len(cb))
        else:
            f.write("%s|%s|%s|%s|%s\n" % (pk, str(dt)[:10], clean(fn)[:40],
                                           clean(subj_of(subj, body))[:70], cb[:420]))
            trunc_n += 1
with io.open(os.path.join(HERE, "%s_heads.txt" % tag), "w", encoding="utf-8", newline="\n") as f:
    for pk, dt, fn, fe, subj, body in rows:
        f.write("ID:%s | DATE:%s | FROM:%s | SUBJ:%s\n"
                % (pk, str(dt)[:10], clean(fn), clean(subj_of(subj, body))))
lo = rows[0][0] if rows else None
hi = rows[-1][0] if rows else None
print("[forread] %s_forread.txt" % tag)
print("[digest ] review_logs/%s_digest.txt" % tag)
if full_n:
    print("[full   ] %d 封内联全量正文（own_ratio<%.2f 或 < %d 字）平均 %d 字 / 最长 %d 字"
          % (full_n, FULL_RATIO, FULL_MINCH, sum(full_len) // full_n, max(full_len)))

if trunc_n and FULL_MINCH <= 200:
    print("[!! WARN] %d 封正文被截在 420 字（FULL_MINCH=%d 默认值）——"
          % (trunc_n, FULL_MINCH))
    print("[!! WARN] 判读依据可能已丢失。全量内联请加 "
          "FULL_MINCH=99999999 重跑（或直接走 _h1_resume.py --advance，"
          "它会自动注入）。")
print("[heads  ] %s_heads.txt" % tag)
print("[pk区间 ] %s ~ %s" % (lo, hi))
