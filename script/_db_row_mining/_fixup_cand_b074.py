# -*- coding: utf-8 -*-
"""fhk_b074 读手产物看护补丁：外科修正已落盘分件的确认缺陷，不动合格行。

数据驱动、可重跑（幂等）：
  (a) 缺末行 LF -> 补一个 LF；
  (b) sweep_blind：BLIND 清单内的候选一律整行删除（口径与门禁一致，b071 起沿用）；
  (c) pk 重写：以数字开头的摘要补主体名前缀（读手漏写 subject=FROM 的英文昵称），
      改写时只保留 420 字窗口内可见的 FROM 自有文字，看不到的一律不写（删而非改，
      禁止臆造断言）。

本批门禁实际报出的缺陷：
  [B] 12 条 BLIND 泄漏（p02 1 条、p13 2 条、p18 9 条）-> sweep_blind 整行删除
  [T] 2 条以数字开头（2605304 p18、2605763 p27）-> REWRITE 补主体名

用法: python _fixup_cand_b074.py
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b074"
N = 40
MIN_SUM, MAX_SUM = 20, 80

# 片号 -> {pk: 新摘要}
# 两条均以数字开头，违反 [T] 门禁；同时读手漏了 subject=FROM 前缀。
# 改写只依据 420 字窗口内 FROM 自有文字：
#   2605304 FROM Julian Elischer，正文自有句可见
#     「I have resurected an old project of mine that I did in 1988... It's CBASIC
#       (yes CP/M's C-BASIC) to UNIC/C translater. It ran in production for years.
#       I've decided to get it up on FreeBSD.. (now that the original owners have
#       sold the business and written off the software」-> 全部可考据。
#   2605763 FROM tcobb，正文自有句可见至「It doesn't require particularl」即被截断，
#     「It doesn't require particularl[y]...」之后不可见 -> 读手原摘要里的「负载不高也
#     触发」属截断处推断，按删而非改处理，予以去除。
REWRITE = {
    18: {
        2605304: ("Julian Elischer：把 1988 年做过的 CBASIC 转 UNIC/C 转换器搬上 "
                  "FreeBSD，原持有公司已出售业务并注销该软件"),
    },
    27: {
        2605763: ("tcobb：2.2.6 配 DPT RAID 控卡约每三天 panic 报 biodone buffer "
                  "not busy，据其查无补丁可修"),
    },
}
# 片号 -> 整行删除的 pk（读手判定错，非 BLIND 口径）
DELETE = {}


def patch(k):
    rw, dl = REWRITE.get(k, {}), DELETE.get(k, set())
    if not rw and not dl:
        return
    p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
    raw = io.open(p, "rb").read()
    lines = [l for l in raw.decode("utf-8").split("\n") if l.strip()]
    seen = [l.split("|", 1)[0] for l in lines]
    for pk in sorted(rw):
        assert MIN_SUM <= len(rw[pk]) <= MAX_SUM, \
            "重写摘要越界 %d 字: %s" % (len(rw[pk]), rw[pk])
    for pk in sorted(rw):
        if str(pk) not in seen:
            print("  [跳过] p%d pk %d 已无原文（补丁已应用）" % (k, pk))
    for pk in sorted(dl):
        if str(pk) not in seen:
            print("  [跳过] p%d pk %d 已删除（补丁已应用）" % (k, pk))
    out, rew, drp = [], [], []
    for ln in lines:
        pk, lvl, s = ln.split("|", 2)
        pk = int(pk)
        if pk in dl:
            drp.append(pk)
            continue
        if pk in rw:
            out.append("%d|%s|%s" % (pk, lvl, rw[pk]))
            rew.append(pk)
        else:
            out.append(ln)
    txt = "\n".join(out) + "\n"
    with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
        fh.flush()
        os.fsync(fh.fileno())
    rb = io.open(p, "rb").read()
    assert rb == txt.encode("utf-8") and not rb.startswith(b"\xef\xbb\xbf")
    print("[p%-2d] 重写 %s | 删除 %s | %d -> %d 行 | %d B"
          % (k, " / ".join(str(x) for x in rew) or "无",
             " / ".join(str(x) for x in drp) or "无",
             len(lines), len(out), len(rb)))


def sweep_blind():
    """BLIND 口径对齐：门禁一律不收 BLIND 行，整行删除（可重跑幂等）。"""
    blind = set()
    bf = io.open(os.path.join(RL, "_blind_%s.txt" % TAG), encoding="utf-8")
    for ln in bf:
        s = ln.strip()
        m = re.match(r"^p(\d+)\s+([\d/]+)\s*$", s)
        if m:
            for x in m.group(2).split("/"):
                if x:
                    blind.add(int(x))
    bf.close()
    total = 0
    for k in range(1, N + 1):
        p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
        if not os.path.exists(p):
            continue
        raw = io.open(p, "rb").read()
        lines = [l for l in raw.decode("utf-8").split("\n") if l.strip()]
        keep, drp = [], []
        for ln in lines:
            pk = int(ln.split("|", 1)[0])
            if pk in blind:
                drp.append(ln)
            else:
                keep.append(ln)
        if not drp:
            continue
        txt = "\n".join(keep) + "\n"
        with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(txt)
            fh.flush()
            os.fsync(fh.fileno())
        total += len(drp)
        print("[p%-2d] 删 BLIND 行 %d 条 -> 余 %d 行"
              % (k, len(drp), len(keep)))
        for d in drp:
            print("        删: %s" % d)
    print("[sweep_blind] BLIND 清单 %d 条，共删候选 %d 条" % (len(blind), total))


def ensure_final_lf():
    for k in range(1, N + 1):
        p = os.path.join(RL, "%s_candidates_p%d.txt" % (TAG, k))
        if not os.path.exists(p):
            continue
        raw = io.open(p, "rb").read()
        if not raw.endswith(b"\n"):
            with io.open(p, "ab") as fh:
                fh.write(b"\n")
                fh.flush()
                os.fsync(fh.fileno())
            print("[LF] p%-2d 补末行 LF -> %d B" % (k, len(raw) + 1))


if __name__ == "__main__":
    for k in sorted(REWRITE) + sorted(DELETE):
        patch(k)
    sweep_blind()
    ensure_final_lf()
