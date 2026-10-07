# -*- coding: utf-8 -*-
"""删掉 fhk_b071 的重复记账行，并把 bookkeep 的幂等判据改成前缀匹配。

根因：_bookkeep_wave_fhk_b071.py 用
    SELECT COUNT(*) FROM entries WHERE summary=?  ["H3 fhk_b071"]
做幂等判断，但实际写入的 summary 是带尾巴的
    H3 fhk_b071 写回：freebsd-hackers 1321 块（L4=498/L3=823）入纲 1 宿主（...）
精确匹配永远不命中，于是第二次跑（narrative 修正后重验）又插了一条。
两条 summary 逐字节相同，created_at 相差约 10 分钟，均为本会话所写。

处理：保留先写的那条（id 2259），删掉后写的重复（id 2260）。
删除前逐字核对本会话两次运行打印的 summary，确认不是别人家的行。
"""
import duckdb
import io
import os

CG = r"d:\librebsd\01-项目管理\00-变更记录\changelog.duckdb"
KEEP, DROP = 2259, 2260
EXPECT = ("H3 fhk_b071 写回：freebsd-hackers 1321 块（L4=498/L3=823）"
          "入纲 1 宿主（CL-RM-408008~CL-RM-409328）")


def main():
    import time as _t
    con = None
    for _i in range(1, 241):
        try:
            con = duckdb.connect(CG)
            break
        except Exception as _e:
            print("  第 %d 次连接被占（%s），15s 后重试"
                  % (_i, str(_e).splitlines()[0][:56]), flush=True)
            _t.sleep(15)
    else:
        raise SystemExit("连接失败")
    try:
        rows = con.execute(
            "SELECT id, entry_order, summary FROM entries WHERE id IN (?,?)",
            [KEEP, DROP]).fetchall()
        assert len(rows) == 2, "候选行 %d 条，非 2 条" % len(rows)
        by = dict((r[0], r) for r in rows)
        assert by[KEEP][2] == by[DROP][2] == EXPECT, \
            "两条 summary 不一致或与预期不符:\n  %s\n  %s" % (by[KEEP][2], by[DROP][2])
        before = con.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
        con.execute("DELETE FROM entries WHERE id=? AND summary=?",
                    [DROP, EXPECT])
        con.execute("CHECKPOINT")
        after = con.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
        assert after == before - 1, "行数 %d -> %d，未减一" % (before, after)
        left = con.execute("SELECT COUNT(*) FROM entries WHERE summary=?",
                           [EXPECT]).fetchone()[0]
        assert left == 1, "删后仍存 %d 条同号摘要" % left
        ids = con.execute("SELECT id FROM entries WHERE id=%d OR id=%d"
                          % (KEEP, DROP)).fetchall()
        assert ids == [(KEEP,)], "残留行 %s" % ids
        print("before=%d after=%d | 保留 id=%d 删除 id=%d"
              % (before, after, KEEP, DROP))
    finally:
        con.close()
    print("DONE changelog 去重")


if __name__ == "__main__":
    main()
