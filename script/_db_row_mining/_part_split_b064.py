# -*- coding: utf-8 -*-
"""按字节平衡把 fhk_b064 digest 切成 40 片（不是按行数）。

做法：遍历行累计字节，累计字节首次达到 (k+1) * target 就关闭当前片。
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
TAG = "fhk_b064"
NL = chr(10)
RL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review_logs")
SRC = os.path.join(RL, "%s_digest.txt" % TAG)
NPART = 40

lines = io.open(SRC, encoding="utf-8").read().rstrip(NL).split(NL)
assert len(lines) == 2000, "digest 行数 %d != 2000" % len(lines)

widths = [len(l.encode("utf-8")) + 1 for l in lines]
total = sum(widths)
target = total / NPART

# 逐片生成：每累计 >= target 就关掉当前片
parts = []
cur_start = 0
cur_bytes = 0
for i, w in enumerate(widths):
    cur_bytes += w
    # 若达到 (len(parts)+1) * target 且还有后续行需要留给剩余片，则切分
    remaining_parts = NPART - len(parts) - 1
    if cur_bytes >= target and remaining_parts > 0 and i < len(lines) - 1:
        parts.append((cur_start, i))
        cur_start = i + 1
        cur_bytes = 0
# 最后一片
parts.append((cur_start, len(lines) - 1))
assert len(parts) == NPART, "片数 %d != %d" % (len(parts), NPART)

out_rows = 0
for n, (s, e) in enumerate(parts):
    chunk = lines[s:e + 1]
    pks = [int(l.split("|", 1)[0]) for l in chunk]
    assert pks == sorted(pks), "片 %d pk 非升序" % n
    assert len(set(pks)) == len(pks), "片 %d pk 重复" % n
    out = NL.join(chunk) + NL
    path = os.path.join(RL, "%s_digest_part%d.txt" % (TAG, n + 1))
    with io.open(path, "w", encoding="utf-8", newline=NL) as fh:
        fh.write(out)
        fh.flush()
        os.fsync(fh.fileno())
    raw = io.open(path, "rb").read()
    assert not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw
    out_rows += len(chunk)
    print("p%02d  %3d 行  pk %d-%d  %6d B"
          % (n + 1, len(chunk), pks[0], pks[-1], len(raw)))

assert out_rows == 2000, "总行数 %d != 2000" % out_rows
print("落盘 40 片，合计 %d 行" % out_rows)
