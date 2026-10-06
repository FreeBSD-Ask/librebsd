# -*- coding: utf-8 -*-
"""p11 补单个尾 LF（幂等：已有尾 LF 则不动）。"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "review_logs", "fhk_b069_mount_narr_p11.tsv")

rb = open(P, "rb").read()
assert not rb.startswith(b"\xef\xbb\xbf"), "有 BOM"
assert b"\r" not in rb, "有 CR"
n_before = rb.count(b"\n")
if rb.endswith(b"\n"):
    print("已有尾 LF，跳过")
else:
    rb += b"\n"
    with io.open(P + ".tmpw", "w", encoding="utf-8", newline="") as fh:
        fh.write(rb.decode("utf-8"))
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(P + ".tmpw", P)
    print("补 1 个尾 LF")

rb2 = open(P, "rb").read()
print("bytes %d LF %d->%d tailLF %s rows %d"
      % (len(rb2), n_before, rb2.count(b"\n"), rb2.endswith(b"\n"),
         len([x for x in rb2.decode("utf-8").split("\n") if x.strip()])))
assert rb2.endswith(b"\n")
