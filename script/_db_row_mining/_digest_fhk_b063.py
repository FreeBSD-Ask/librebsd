# -*- coding: utf-8 -*-
"""生成 fhk_b063 的 2000 封压缩摘要（40 路读手波的唯一输入）。

行格式（每封一行）:

  <pk>|<date[:10]>|<from_name[:40]>|<subject[:70]>|<正文压缩列[:420]>

口径（用 fhk_b044 落盘 digest 逐字节回算标定，2000/2000 全解；
b063 沿用并已实测，本批不改动）:
  1. 四个文本字段一律空白折叠 —— ' '.join(s.split())，连续空白并成一个空格；
  2. 字段内的 '|' 一律替换为 '/' —— 使每行恰好 4 个 '|'（即字段分隔符），
     解析用 split('|',4) 唯一且零正则。源正文里的 '|' 是真实内容，替换只为
     分隔符唯一，不删改信息；
  3. from_name 折叠后截 40 字；subject 折叠后截 70 字；正文折叠后截 420 字；
  4. subject 列为空时的回退：从正文首部逐行取 'Subject: ' 头行的值，
     字面照录、不做补全、不加注释（b044 pk 2544731 即此情形）。

正文压缩列口径必须与 _blind_fhk_b063.py 的 BLIND 判定**完全一致**
（同一折叠、同一 420 硬截断），否则 BLIND 清单与本 digest 会对不上。

关于 b044 的已知偏差（不影响本批口径，仅留痕）:
  b044 落盘 digest 的正文列并非一律 420 硬截断 —— 2000 行中 1841 行与本口径
  逐字节一致、1 行为 subject 回退、**158 行是全文**（未截断，其中 109 行属
  BLIND）。已交叉比对 BLIND/OWNVIS、有无引用块、行数、折叠长度、原始长度，
  均无法解释这 158 行的入选；其生成器亦不在盘上，无法复现。故本批一律按
  上述口径，由 BLIND 清单承担「420 窗口内看不到发帖人自有文字」的补偿。

只读源库。零正则、零反斜杠。
用法: C:/Python314/python.exe _digest_fhk_b063.py [输出路径]
      不带参数则写 review_logs/fhk_b063_digest.txt。
"""
import io
import json
import os
import sys

import duckdb

NL = chr(10)
CR = chr(13)
BOM = chr(0xFEFF)
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b063"
DB = (r"d:\librebsd\03-原始史料库\11-邮件列表史料"
      r"\01-freebsd\db\freebsd-hackers.duckdb")
# 库内序 124001-126000 -> pk 2582341 ~ 2584356，跨度 2016 缺 16（2582801/2583024/2583025/2583026/2583027/2583028/2583029/2583030/2583031/2583032/2583553/2583646/2583829/2583833/2583834/2583934），
# 端点区间 1996-08-17 ~ 1996-09-30（归档非按日期排序）
LO, HI = 2582341, 2584356
_BJ = json.load(io.open("_batch_fhk_b063.json", encoding="utf-8"))
assert (LO, HI) == (_BJ["pk_lo"], _BJ["pk_hi"]), "LO/HI 与 _batch_fhk_b063.json 不一致"
assert _BJ["n"] == 2000, "批次行数不符"
N_EXP = 2000
TRIM_F, TRIM_S, TRIM_B = 40, 70, 420


def fold(s):
    """空白折叠 + 字段内 '|' 换 '/'（保证分隔符唯一）。"""
    return " ".join((s or "").split()).replace("|", "/")


def subject_of(subject, body):
    """subject 列为空时从正文首部取 'Subject: ' 头行的值，字面照录。"""
    if subject and subject.strip():
        return fold(subject)
    for ln in (body or "").split(NL):
        t = ln.strip()
        if t[:8].lower() == "subject:" and len(t) > 8:
            return " ".join(t[8:].split()).replace("|", "/")
    return ""


out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RL, "%s_digest.txt" % TAG)

c = duckdb.connect(DB, read_only=True)
rows = c.execute(
    "SELECT CAST(id AS BIGINT), date, from_name, subject, body FROM messages "
    "WHERE CAST(id AS BIGINT) BETWEEN ? AND ? ORDER BY CAST(id AS BIGINT)",
    [LO, HI]).fetchall()
c.close()
assert len(rows) == N_EXP, "窗口行数 %d != %d" % (len(rows), N_EXP)

lines = []
n_fallback = 0
for pk, dt, frm, subj, body in rows:
    s = subject_of(subj, body)
    if not (subj and subj.strip()):
        n_fallback += 1
    lines.append("%d|%s|%s|%s|%s" % (
        pk, str(dt)[:10], fold(frm)[:TRIM_F], s[:TRIM_S], fold(body)[:TRIM_B]))

# ---- 写前门禁 ----
assert len(lines) == N_EXP, "输出行数 %d != %d" % (len(lines), N_EXP)
pkseq = [int(l.split("|", 1)[0]) for l in lines]
assert len(set(pkseq)) == N_EXP, "pk 有重复"
assert pkseq == sorted(pkseq), "pk 非严格升序"
assert (pkseq[0], pkseq[-1]) == (LO, HI), "pk 端点不符 %d ~ %d" % (pkseq[0], pkseq[-1])
bad_sep = [l for l in lines if l.count("|") != 4]
assert not bad_sep, "分隔符数 != 4: %s" % bad_sep[0][:80]
joined = NL.join(lines)
assert CR not in joined, "含 CR"
assert BOM not in joined, "含 BOM"
assert all(len(l.split("|", 4)[2]) <= TRIM_F for l in lines), "from 超 %d 字" % TRIM_F
assert all(len(l.split("|", 4)[3]) <= TRIM_S for l in lines), "subj 超 %d 字" % TRIM_S
assert all(len(l.split("|", 4)[4]) <= TRIM_B for l in lines), "正文超 %d 字" % TRIM_B

body_txt = NL.join(lines) + NL
with io.open(out, "w", encoding="utf-8", newline=NL) as f:
    f.write(body_txt)
    f.flush()
    os.fsync(f.fileno())

# ---- 回读校验 ----
raw = io.open(out, "rb").read()
assert not raw.startswith(b"\xef\xbb\xbf"), "文件首 BOM"
assert b"\r" not in raw, "含 CR"
assert len(raw) == len(body_txt.encode("utf-8")), "字节数不符"
back = io.open(out, encoding="utf-8").read().rstrip(NL).split(NL)
assert back == lines, "回读行序列与内存不一致"

n420 = sum(1 for l in lines if len(l.split("|", 4)[4]) == TRIM_B)
nshort = sum(1 for l in lines if len(l.split("|", 4)[4]) < TRIM_B)
w = [len(l.encode("utf-8")) for l in lines]
print("[写盘] %s" % out)
print("     %d 行 | pk %d ~ %d | 分隔符 4 个/行 | 回读逐位守恒"
      % (len(lines), LO, HI))
print("     正文恰 420 字 %d 行 / 天然不足 %d 行" % (n420, nshort))
print("     行宽 %d ~ %d 字节 | 文件 %d 字节" % (min(w), max(w), len(raw)))
print("     LF 行尾 | UTF-8 无 BOM | subject 回退 %d 行" % n_fallback)
