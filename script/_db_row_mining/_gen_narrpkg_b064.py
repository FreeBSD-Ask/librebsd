# -*- coding: utf-8 -*-
"""fhk_b064 叙述波素材生成：按裁定后候选切 50 份 narrpkg + 50 份正文包。

输入：review_logs/fhk_b064_candidates.txt （pk|L|摘要，已裁定）
      源库 freebsd-hackers.duckdb         （DATE/FROM/SUBJ/body）
      claims 库 historical_claims.duckdb  （anchor='fhk_b064' -> pk2claim）
输出：review_logs/fhk_b064_narrpkg_p1..p50.txt
      review_logs/fhk_b064_cands_body_p1..p50.txt

与 _gen_narrpkg_b054.py 的口径完全一致，仅批次坐标不同：
1. 正文不做 replace(NL," ") 折行——折行会毁掉 `>` 引用块结构，
   使「引文里的话署给 FROM」这一主缺陷族在叙述层无法辨识。保留真实换行。
2. 超长正文做头+尾裁剪而非只截头：头部对齐 quote 语境，尾部保住作者签名
   与第三人称自述（签名的正文位置是判定署名归属的首要依据）。
   中段省略处显式打标记，不静默拼接。

只读两个库；不覆盖 review_logs/fhk_b064_claim_map.json（由
_claimmap_fhk_b064.py 产出，此处仅核对不重写）。本脚本不推断任何裁定结论。
本批候选实测跨年两段（_claimmap_fhk_b064.py）：1996-12=113、1997-01=176，
合计 289。年份一律取源库 date 实测值，不按批次声明；BANDS 两段
（1996 二十份 + 1997 三十份，宿主均 885），与 b062 单段克隆版不同。
"""
import io
import json
import os
import sys
import time

import duckdb

sys.stdout.reconfigure(encoding="utf-8")
NL = chr(10)
HERE = os.path.dirname(os.path.abspath(__file__))
RL = os.path.join(HERE, "review_logs")
SRC = r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db\freebsd-hackers.duckdb"
HC = r"d:\librebsd\04-现代研究文献\historical_claims.duckdb"
ANCHOR = "fhk_b064"
LIBBASE = 128000         # 台账 offset（库内序 126001-128000）
PK0 = 2584357            # 库内序 126001 对应的 pk
PARTS = 50
BODYCAP = 2600
HEAD = 2100
TAIL = 500
CAND = os.path.join(RL, "fhk_b064_candidates.txt")
CMAP = os.path.join(RL, "fhk_b064_claim_map.json")

# 候选年分布实测：本批 pk 2584357-2586358 对应 1997-04-01 至 1997-04-26，
# 单一日历月，无跨年；main() 内按源库 date 实测断言，不采信此处注释。
# 宿主裁定 885 = 88.5「FreeBSD 2.x 开发者群体与核心团队代际（1994–1997）」，
# 落在 885 覆盖年内，故单带写宿主 885，全部 50 份归 1997。
BANDS = [("1997", "885", 50)]


def rd(p, tries=40):
    last = None
    for _ in range(tries):
        try:
            with io.open(p, encoding="utf-8", errors="replace") as f:
                return f.read()
        except Exception as e:
            last = repr(e)
            time.sleep(0.4)
    raise SystemExit("read fail %s last=%s" % (p, last))


def wr(p, s, tries=40):
    """整块构建后 os.replace，写后回读断言。"""
    tmp = p + ".tmpw"
    with io.open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(s)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)
    for _ in range(tries):
        try:
            with io.open(p, encoding="utf-8", errors="replace", newline="") as f:
                if f.read().rstrip("\n") == s.rstrip("\n"):
                    return
        except Exception:
            pass
        time.sleep(0.5)
    raise SystemExit("writeback mismatch " + p)


def clip(b):
    """超长正文：留头与尾，中段显式标记省略，不改一个字。"""
    if len(b) <= BODYCAP:
        return b
    dropped = len(b) - HEAD - TAIL
    return b[:HEAD] + NL + "[…中段省略 %d 字符…] %s" % (dropped, b[len(b) - TAIL:])


def main():
    rows = [l.rstrip("\n") for l in rd(CAND).split("\n") if l.strip()]
    cands = []
    for l in rows:
        pk, lvl, summ = l.split("|", 2)
        cands.append((int(pk), lvl, summ))
    cands.sort()
    pks = [c[0] for c in cands]
    print("候选存活 %d 条 | pk %d..%d | 唯一 %d"
          % (len(cands), pks[0], pks[-1], len(set(pks))))
    assert len(set(pks)) == len(pks), "pk 不唯一"
    assert pks == sorted(pks), "非升序"

    cm = json.load(io.open(CMAP, encoding="utf-8"))
    claim_map = {int(k): v["claim_id"] for k, v in cm.items()}
    assert len(claim_map) == len(pks), "claim_map %d != 候选 %d" % (len(claim_map), len(pks))
    miss = set(pks) - set(claim_map)
    assert not miss, "claim_map 缺 pk: %s" % sorted(miss)[:5]
    assert set(claim_map) == set(pks), "claim_map 多出 pk: %s" % (
        sorted(set(claim_map) - set(pks))[:5])
    print("claim_map 对账 %d 条 | 序号 %s..%s" % (
        len(claim_map),
        min(claim_map.values(), key=lambda x: int(x.rsplit("-", 1)[1])),
        max(claim_map.values(), key=lambda x: int(x.rsplit("-", 1)[1]))))

    con = duckdb.connect(SRC, read_only=True)
    body = {}
    # 单 PK 查询在本机约 0.96s，874 条逐条要 14 分钟；按 200 条分块 IN 批查。
    for i in range(0, len(pks), 200):
        seg = pks[i:i + 200]
        for r in con.execute(
            "SELECT CAST(id AS BIGINT), from_name, subject, body, date FROM messages"
            " WHERE CAST(id AS BIGINT) IN (%s)"
            % ",".join("?" for _ in seg), seg).fetchall():
            pk, f2, s2, b2, d2 = r
            b = b2 or ""
            if not b.strip():
                b = (f2 or "")
            body[int(pk)] = (f2 or "", s2 or "", clip(b), str(d2 or ""))
    misspk = [pk for pk in pks if pk not in body]
    if misspk:
        raise SystemExit("源库缺 pk: %s" % misspk[:10])
    con.close()

    n = len(cands)
    ymap = {str(body[pk][3])[:4] for pk in pks}
    got = {yr: [c for c in cands if str(body[c[0]][3])[:4] == yr]
           for yr, _, _ in BANDS}
    miss_y = sorted(ymap - set(got))
    assert not miss_y, "年代带未覆盖: %s" % miss_y
    bands = []
    for yr, hk, nparts in BANDS:
        seg = sorted(got[yr])
        assert len(seg) >= nparts, "带 %s 仅 %d 条不足 %d 份" % (yr, len(seg), nparts)
        base, rem = divmod(len(seg), nparts)
        sizes = [base + (1 if i < rem else 0) for i in range(nparts)]
        off = 0
        for i in range(nparts):
            bands.append((yr, hk, seg[off:off + sizes[i]]))
            off += sizes[i]
    sizes = [len(b[2]) for b in bands]
    assert sum(sizes) == n, "带内合计 %d != %d" % (sum(sizes), n)
    print("年段画像: " + " ".join(
        "%s=%d" % (yr, sum(1 for c in cands if str(body[c[0]][3])[:4] == yr))
        for yr, _, _ in BANDS))
    print("分件 %d 份 sizes=%s" % (len(bands), sizes))

    HEADER = (
        "署名归属规则（先读）：行首带 `>` 的是引用块，里面的话属于被引者，"
        "不得署给本封 FROM。本封作者只算 FROM 行 + 正文末尾自签 + 第一人称自述。"
        "正文中段的 `>` 块内人名与结论，一律不归给 FROM。"
    )
    for no, (yr, hk, seg) in enumerate(bands, 1):
        npk, nb = [], []
        for pk, lvl, summ in seg:
            npk.append("%d|%s|%s" % (pk, lvl, summ))
            f, s, b, d = body[pk]
            nb.append("### PK %d ###" % pk)
            nb.append("===== 库内序 %d | PK %d | 等级 %s ====="
                      % (LIBBASE + (pk - PK0), pk, lvl))
            nb.append("DATE: %s" % d)
            nb.append("FROM: %s" % f)
            nb.append("SUBJ: %s" % s)
            nb.append("摘要: %s" % summ)
            nb.append("")
            nb.append(b)
            nb.append("")
        nb.insert(0, HEADER)
        wr(os.path.join(RL, "fhk_b064_narrpkg_p%d.txt" % no), NL.join(npk) + NL)
        wr(os.path.join(RL, "fhk_b064_cands_body_p%d.txt" % no), NL.join(nb) + NL)
        print("p%-3d 年 %s  宿主 %s  %2d 条 | pk %d..%d"
              % (no, yr, hk, len(seg), seg[0][0], seg[-1][0]))

    assert no == sum(x[2] for x in BANDS), "份数不符"
    print("切片合计 %d == 候选 %d" % (sum(sizes), n))
    print("DONE")


if __name__ == "__main__":
    main()
