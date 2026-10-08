# -*- coding: utf-8 -*-
"""fhk_b074 叙述波素材生成：按裁定后候选切 50 份 narrpkg + 50 份正文包。

克隆自 _gen_narrpkg_b066.py，两处口径升级：
1. 库内序不再按 pk 线性外推（本批 pk span 2001 缺 1，线性外推在尾部最偏 11 位），
   改由源库 ROW_NUMBER() OVER (ORDER BY id) 实测取得，并按批断言 146001..148000。
2. 宿主全批单一带 885（_batch_fhk_b074.json hosts=[88.5]），故不再按年代分段
   分配片数，直接按候选顺序均分 50 份；每片打印年代画像供审计。

其余口径与 b066 完全一致：
1. 正文不做 replace(NL," ") 折行——折行会毁掉 `>` 引用块结构，
   使「引文里的话署给 FROM」这一主缺陷族在叙述层无法辨识。保留真实换行。
2. 超长正文做头+尾裁剪而非只截头：头部对齐 quote 语境，尾部保住作者签名
   与第三人称自述（签名的正文位置是判定署名归属的首要依据）。
   中段省略处显式打标记，不静默拼接。

只读两个库；不覆盖 review_logs/fhk_b074_claim_map.json（由
_verify_reg_fhk_b074.py 产出，此处仅核对不重写）。本脚本不推断任何裁定结论。
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
ANCHOR = "fhk_b074"
HOST = "885"
RN_LO, RN_HI = 146001, 148000      # 库内序窗口（offset 144000，左闭右闭）
PK_LO, PK_HI = 2604444, 2606444    # 实测 pk 端点（span 2011 缺 1）
PARTS = 50
BODYCAP = 2600
HEAD = 2100
TAIL = 500
CAND = os.path.join(RL, "fhk_b074_candidates.txt")
CMAP = os.path.join(RL, "fhk_b074_claim_map.json")


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
    assert (pks[0], pks[-1]) == (PK_LO, PK_HI), "pk 端点不符 %d..%d" % (pks[0], pks[-1])

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
    # 库内序由全表 ROW_NUMBER 实测取得，不按 pk 线性外推。
    body = {}
    rn = {}
    for i in range(0, len(pks), 200):
        seg = pks[i:i + 200]
        q = ("SELECT CAST(m.id AS BIGINT), m.from_name, m.subject, m.body, m.date, rn "
             "FROM messages m "
             "JOIN (SELECT CAST(id AS BIGINT) AS id2, "
             "ROW_NUMBER() OVER (ORDER BY CAST(id AS BIGINT) ASC) AS rn FROM messages) t "
             "ON CAST(m.id AS BIGINT) = t.id2 "
             "WHERE CAST(m.id AS BIGINT) IN (%s)") % ",".join("?" for _ in seg)
        for r in con.execute(q, seg).fetchall():
            pk, f2, s2, b2, d2, n2 = r
            b = b2 or ""
            if not b.strip():
                b = (f2 or "")
            body[int(pk)] = (f2 or "", s2 or "", clip(b), str(d2 or ""))
            rn[int(pk)] = int(n2)
    misspk = [pk for pk in pks if pk not in body]
    if misspk:
        raise SystemExit("源库缺 pk: %s" % misspk[:10])
    con.close()

    rnlo, rnhi = min(rn.values()), max(rn.values())
    print("库内序实测范围 %d..%d（批窗口 %d..%d）" % (rnlo, rnhi, RN_LO, RN_HI))
    assert rnlo >= RN_LO and rnhi <= RN_HI, "库内序越出批窗口"

    n = len(cands)
    base, rem = divmod(n, PARTS)
    sizes = [base + (1 if i < rem else 0) for i in range(PARTS)]
    assert sum(sizes) == n, "片内合计 %d != %d" % (sum(sizes), n)
    bands = []
    off = 0
    for i in range(PARTS):
        bands.append((HOST, cands[off:off + sizes[i]]))
        off += sizes[i]
    print("分件 %d 份 sizes=%d+%d x%d" % (
        len(bands), base, rem, rem if rem else 0))

    HEADER = (
        "署名归属规则（先读）：行首带 `>` 的是引用块，里面的话属于被引者，"
        "不得署给本封 FROM。本封作者只算 FROM 行 + 正文末尾自签 + 第一人称自述。"
        "正文中段的 `>` 块内人名与结论，一律不归给 FROM。"
    )
    for no, (hk, seg) in enumerate(bands, 1):
        assert hk == HOST
        npk, nb = [], []
        for pk, lvl, summ in seg:
            npk.append("%d|%s|%s" % (pk, lvl, summ))
            f, s, b, d = body[pk]
            nb.append("### PK %d ###" % pk)
            nb.append("===== 库内序 %d | PK %d | 等级 %s ====="
                      % (rn[pk], pk, lvl))
            nb.append("DATE: %s" % d)
            nb.append("FROM: %s" % f)
            nb.append("SUBJ: %s" % s)
            nb.append("摘要: %s" % summ)
            nb.append("")
            nb.append(b)
            nb.append("")
        nb.insert(0, HEADER)
        wr(os.path.join(RL, "fhk_b074_narrpkg_p%d.txt" % no), NL.join(npk) + NL)
        wr(os.path.join(RL, "fhk_b074_cands_body_p%d.txt" % no), NL.join(nb) + NL)
        yrs = {}
        for pk, _l, _s in seg:
            y = str(body[pk][3])[:4]
            yrs[y] = yrs.get(y, 0) + 1
        prof = " ".join("%s=%d" % kv for kv in sorted(yrs.items()))
        print("p%-3d 宿主 %s  %3d 条 | pk %d..%d | %s"
              % (no, hk, len(seg), seg[0][0], seg[-1][0], prof))

    assert no == PARTS, "份数不符"
    print("切片合计 %d == 候选 %d" % (sum(sizes), n))
    print("DONE")


if __name__ == "__main__":
    main()
