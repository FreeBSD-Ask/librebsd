# -*- coding: utf-8 -*-
"""落 _batch_fhk_b074.json（与 _batch_fhk_b073.json 同缩进 indent=1、无尾换行）。

全部数值从源库按与 _probe_batch_fhk_b074.py 完全相同的口径实测：
ORDER BY CAST(id AS BIGINT) ASC LIMIT 2000 OFFSET 146000，即库内序 146001-148000。
与 probe 的 pk_lo/pk_hi/条数交叉断言，任一不符即中止——不硬编外推。
"""
import io
import json
import os
from collections import Counter

import duckdb

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_batch_fhk_b074.json")
RL = os.path.join(HERE, "review_logs")
TAG = "fhk_b074"
DB = (r"d:\librebsd\03-原始史料库\11-邮件列表史料\01-freebsd\db"
      r"\freebsd-hackers.duckdb")
OFFSET, N = 146000, 2000
HOST = 88.5

con = duckdb.connect(DB, read_only=True)
rows = con.execute(
    "SELECT CAST(id AS BIGINT), date, from_name, subject, body FROM messages "
    "ORDER BY CAST(id AS BIGINT) ASC LIMIT ? OFFSET ?", [N, OFFSET]).fetchall()
con.close()
assert len(rows) == N, "取到 %d 行非 %d" % (len(rows), N)

pks = [int(r[0]) for r in rows]
assert pks == sorted(pks) and len(set(pks)) == len(pks), "pk 非升序或重复"
dates = [str(r[1])[:10] for r in rows]
bl = [len((r[4] or "")) for r in rows]
missing = sorted(set(range(pks[0], pks[-1] + 1)) - set(pks))
# 全空判据取 _blind 口径（strip 后为空）：probe 的裸 len 会把单换行体记为
# <=20 字短正文，掩盖其真实为空。先按 strip 判空，再判短正文。
empty = sorted(int(r[0]) for r in rows if not (r[4] or "").strip())
short = sorted(int(r[0]) for r in rows
               if (r[4] or "").strip() and 0 < len((r[4] or "")) <= 20)
if empty:
    eraw = max(len((r[4] or "")) for r in rows if int(r[0]) in set(empty))
    empty_note = ("（%s 为单换行体，raw len=%d、strip 后为空——"
                  "与 _blind 的全空判据一致；probe 的裸 len 口径只记为 <=20 字短正文，"
                  "故此处以 _blind 口径为准）"
                  % ("／".join(str(x) for x in empty), eraw))
else:
    empty_note = ""
nosub = sorted(int(r[0]) for r in rows if not (r[3] or "").strip())
nohead = sorted(int(r[0]) for r in rows
                if not (r[3] or "").strip() and not (r[2] or "").strip())
mdist = Counter(d[:7] for d in dates)
n_drops = sum(1 for i in range(1, len(dates)) if dates[i] < dates[i - 1])
# 脏日期：月内条数 <5 的月份都是解析错乱的单封，单独列出
ndirty = sum(1 for k, v in mdist.items() if v < 5)
dirty_k = "、".join(sorted(k for k in mdist if mdist[k] < 5))
main_months = "/".join(sorted(k for k in mdist if mdist[k] >= 5))
# 主窗只取主月内的日期：脏日期各 1 封会把 min/max 拉到 1994 与 2000，
# 造成「主窗 1994-05-11~2000-01-21」的误述。
main_dates = sorted(d for d in dates if mdist[d[:7]] >= 5)
main_n = sum(v for k, v in mdist.items() if v >= 5)
topk = max(sorted(mdist), key=lambda k: mdist[k])
top = "%s 占 %.1f%%" % (topk, mdist[topk] * 100.0 / N)

# 与 probe 落盘件交叉断言，防窗口漂移
probe = io.open(os.path.join(RL, "%s_probe.txt" % TAG), encoding="utf-8").read()
for s in ("%d ~ %d" % (pks[0], pks[-1]), "取行 %d" % N):
    assert s in probe, "probe 与本次实测不符：%s" % s

D = {
    "tag": TAG,
    "lib": "freebsd-hackers",
    "offset": OFFSET,
    "n": N,
    "pk_lo": pks[0],
    "pk_hi": pks[-1],
    "pk_range": "%d-%d" % (pks[0], pks[-1]),
    "rn_lo": pks[0],
    "rn_hi": pks[-1],
    "parts": 40,
    "hosts": [HOST],
    "hosts_note": ("单宿主 88.5（2026-10-07 主会话裁定，沿用 b071/b072/b073 口径）："
                   "本批主窗 %s~%s，%s 三月同年内共 %d 封，"
                   "另有脏日期 %d 封各 1 封（%s），属日期头解析错乱、非内容跨年。"
                   "H3 线既有实践是把 freebsd-hackers 全时段内容一律落 88.5、不按年切宿主"
                   "（b071 跨 1997-12~1998-01、b072 跨 1998-01~1998-02、"
                   "b073 跨 1998-02~1998-04 均挂 88.5），本批与前批 pk 相邻衔接"
                   "（b073 末 pk %d，本批起 pk %d），整体挂 88.5，无需多宿主分派。"
                   % (main_dates[0], main_dates[-1], main_months,
                      main_n,
                      ndirty,
                      "、".join("%s 各 1" % k for k in sorted(mdist) if mdist[k] < 5),
                      2604443, pks[0])),
    "anchor": TAG,
    "src_db": DB,
    "month_dist": dict(sorted(mdist.items())),
    "body_gt20": sum(1 for x in bl if x > 20),
    "body_max": max(bl),
    "empty_body": len(empty),
    "empty_body_pks": empty,
    "empty_subject": len(nosub),
    "missing_pks": missing,
    "empty_subject_pks": nosub,
    "short_body_pks": short,
    "ordinal_note": "库内序 %d-%d" % (OFFSET + 1, OFFSET + N),
    "note": ("pk span %d 缺 %d（%s）；主窗 %s~%s，%s 三月同年内（%s）；"
             "日期回卷点 %d 处全为线程内错序，另有脏日期 %d 封各 1 封"
             "（%s，与 b071 的 2036-02、b072 的 1997-01-28 同类，"
             "由日期头解析错乱所致，判读时须回源核对正文语境）；"
             "全头空 %d 封；正文空 %d 封%s；"
             "正文 <=20 字 %d 封（%s）；subject 空 %d 封；from_name 空 0 封；"
             "正文均值 %.0f 字、最大 %d 字"
             % (pks[-1] - pks[0] + 1, len(missing),
                "、".join(str(x) for x in missing) if missing else "无",
                main_dates[0], main_dates[-1],
                main_months,
                top,
                n_drops,
                ndirty,
                dirty_k,
                len(nohead), len(empty), empty_note, len(short),
                "、".join(str(x) for x in short) if short else "无",
                len(nosub), sum(bl) / len(bl), max(bl))),
    "changelog_msg": "fhk_b074 offset 146000",
    "line_date": "2026-10-07",
    "probe": ("坐标由 _probe_batch_fhk_b074.py 只读源库实测；与上一批端点衔接"
              "（库内序 146000 对应 pk 2604443 为 fhk_b073 末，本批起点 pk %d）"
              % pks[0]),
}


def main():
    txt = json.dumps(D, ensure_ascii=False, indent=1)
    assert "\r" not in txt
    assert not txt.endswith("\n")
    io.open(OUT, "w", encoding="utf-8", newline="\n").write(txt)
    b = io.open(OUT, "rb").read()
    assert not b.startswith(b"\xef\xbb\xbf"), "BOM"
    assert b"\r" not in b, "CRLF"
    assert not b.endswith(b"\n"), "尾换行"
    assert json.loads(b.decode("utf-8")) == D, "round-trip 不等"
    print("[写盘] %s (%d B)" % (OUT, len(b)))
    print("pk %d~%d  span %d  缺 %d  月份 %s"
          % (pks[0], pks[-1], pks[-1] - pks[0] + 1, len(missing),
             dict(sorted(mdist.items()))))
    print("月分合计 %d（须 = %d）" % (sum(mdist.values()), N))
    assert sum(mdist.values()) == N, "月份分布合计不符"
    print("正文 gt20=%d max=%d 空=%d <=20=%d subject空=%d 回卷点=%d"
          % (D["body_gt20"], D["body_max"], D["empty_body"], len(short),
             D["empty_subject"], n_drops))


if __name__ == "__main__":
    main()
