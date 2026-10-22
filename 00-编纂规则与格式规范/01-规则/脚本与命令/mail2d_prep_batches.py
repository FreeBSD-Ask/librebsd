# -*- coding: utf-8 -*-
"""批量预建/预处理邮件线批次（建 spec → dump → 补 pk_range → 容器行清单 → 拆 digest）。

用途：读手是瓶颈，预先备好 digest 可让其一到即派，避免串行等待。
幂等：已存在 spec 的 tag 跳过 new（除非 --force-new）；已存在的 digest 分件不重拆。

用法:
  C:/Python314/python.exe _prep_batches.py fhk_b003:4000:2000 fhk_b004:6000:2000 ...
  可附 --hosts 885,916,...  --lib freebsd-hackers
"""
import io
import json
import os
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
PYD = r"C:\Python314\python.exe"
RL = os.path.join(HERE, "review_logs")

# 并发写者（其他会话）会令 claim 库读锁抛 IOException —— 按本线约定重试（间隔 6 秒、至多 8 次）
RETRY_IO = ("IOException", "being used by another", "Could not set lock", "lock on file")

# 取位参时须同时跳过「带值旗标」及其值：--lib freebsd-hackers 里的值不以 -- 开头，
# 若按「不以 -- 开头即位参」过滤，该值会被当成 spec 喂给 split(":") 而崩
# （ValueError: not enough values to unpack）。历史坑，见 _H3_PROGRESS.md。
_LIB = ("--lib", "--hosts")
args = []
_i = 1
while _i < len(sys.argv):
    _a = sys.argv[_i]
    if _a in _LIB:
        _i += 2
        continue
    if _a.startswith("--"):
        _i += 1
        continue
    args.append(_a)
    _i += 1

LIB = "freebsd-hackers"
HOSTS = "885,916,986,10018,10110,1588,1648"
for i, a in enumerate(sys.argv):
    if a == "--lib":
        LIB = sys.argv[i + 1]
    if a == "--hosts":
        HOSTS = sys.argv[i + 1]


def run(cmd):
    r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return (r.stdout or "") + (r.stderr or "")


def run_retry(cmd, tries=8, wait=6.0):
    """执行并在此类并发锁错误上重试（其他会话正在写 claim 库时会发生）。"""
    out = ""
    for i in range(tries):
        out = run(cmd)
        if not any(k in out for k in RETRY_IO):
            return out
        print("  [锁冲突] 重试 %d/%d（%.0fs 后）" % (i + 1, tries, wait))
        time.sleep(wait)
    return out


for spec in args:
    tag, off, n = spec.split(":")
    sp_path = os.path.join(HERE, "_batch_%s.json" % tag)
    if not os.path.exists(sp_path):
        out = run_retry([PYD, "_mail2d_run_batch.py", "new", "--db", LIB, "--offset", off,
                         "--n", n, "--tag", tag, "--hosts", HOSTS,
                         "--note", "H3 线 %s 库内序 %s-%d" % (LIB, off, int(off) + int(n) - 1)])
        print(out.strip().splitlines()[-1] if out.strip() else out)
    else:
        print("[skip new] %s 已存在" % tag)
    # 标记「预建待判读」：本批 spec 已建、digest 已备，但**尚未判读落库**。
    # 台账构建器（_build_read_ledger.py）据此把该类 spec 排除出已读区间，
    # 否则深队列预建会把未来批次误计为已读、系统性高估覆盖率。
    # 判读落库后（review_logs/<tag>_claim_map.json 生成）自动转为已读，标记无需手工清除。
    if not os.path.exists(os.path.join(RL, "%s_claim_map.json" % tag)):
        _d = json.load(io.open(sp_path, encoding="utf-8"))
        if _d.get("queued") is not True:
            _d["queued"] = True
            io.open(sp_path, "w", encoding="utf-8", newline="\n").write(
                json.dumps(_d, ensure_ascii=False, indent=1) + "\n")
            print("  [queued] %s 标记为预建待判读" % tag)
    dg = os.path.join(RL, "%s_digest.txt" % tag)
    if not os.path.exists(dg):
        out = run([PYD, "_mail2d_run_batch.py", "dump", "--tag", tag])
        lo = hi = None
        for ln in out.splitlines():
            if ln.startswith("[pk区间"):
                lo, hi = [int(x) for x in ln.split("]")[1].replace(" ", "").split("~")]
        if lo is None:
            print("[dump 失败] %s\n%s" % (tag, out[-500:]))
            continue
        d = json.load(io.open(sp_path, encoding="utf-8"))
        d["pk_range"] = [lo, hi]
        io.open(sp_path, "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print("[dump] %s pk %s~%s" % (tag, lo, hi))
    else:
        print("[skip dump] %s 已有 digest" % tag)
    print("  " + run([PYD, "_list_container_pks.py", tag]).strip())
    parts = sorted(f for f in os.listdir(RL) if f.startswith("%s_digest_part" % tag))
    if not parts:
        print("  " + run([PYD, "_split_digest.py", tag, "4"]).strip().splitlines()[0])
    else:
        print("  [skip split] %s 已有 %d 分件" % (tag, len(parts)))
print("完成。")
