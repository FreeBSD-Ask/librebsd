# 库内登记脚本（T008，脚本豁免）：备份＋新增列＋幂等写入＋复核日志。
# 用法: --apply | --verify-idempotent | --rollback --ids 1,2 | --restore-file <相对路径>
import csv
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

import duckdb

ROOT = Path(r"D:\librebsd")
DB = ROOT / "04-现代研究文献/06-存疑数据库/doubts_standalone.duckdb"
STG = ROOT / "script/_staging/pilot_samples_20260930"
SNAP = STG / "snapshots"
OUTLINE = ROOT / "05-卷册大纲"
MANIFEST = STG / "landed_manifest.json"
REVIEW_ACTION = "pilot_dual_marker_20260930"
REVIEWER = "main-agent+先导样本执行"
BAK_DB = ROOT / "12-数据库备份/doubts_standalone.prebak-pilot-20260930.duckdb"


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def backup(con):
    if not BAK_DB.exists():
        con.close()
        shutil.copy2(DB, BAK_DB)
        print(f"文件级备份: {BAK_DB.name} ({BAK_DB.stat().st_size} 字节)")
        con = duckdb.connect(str(DB))
    con.execute("""CREATE TABLE IF NOT EXISTS doubts_to_resolve_bak_20260930
                   AS SELECT * FROM doubts_to_resolve""")
    n = con.execute("SELECT count(*) FROM doubts_to_resolve_bak_20260930").fetchone()[0]
    print(f"表级备份: doubts_to_resolve_bak_20260930（{n} 行）")
    return con


def apply(con, manifest):
    con.execute("""ALTER TABLE doubts_to_resolve
                   ADD COLUMN IF NOT EXISTS dual_marker_id VARCHAR""")
    writes = 0
    for s in manifest:
        if s.get("db_landed") is False:
            continue
        marker = s["marker"]
        did = str(s["id"])
        cur = con.execute("SELECT dual_marker_id FROM doubts_to_resolve WHERE id = ?",
                          [did]).fetchone()
        if cur is None:
            raise SystemExit(f"id {did} 不存在")
        if cur[0] != marker:
            con.execute("UPDATE doubts_to_resolve SET dual_marker_id = ? WHERE id = ?",
                        [marker, did])
            writes += 1
    logs = 0
    for s in manifest:
        if s.get("db_landed") is False:
            continue
        did = str(s["id"])
        exists = con.execute(
            "SELECT count(*) FROM doubt_review_log WHERE doubt_id = ? AND review_action = ?",
            [did, REVIEW_ACTION]).fetchone()[0]
        if not exists:
            con.execute("""INSERT INTO doubt_review_log
                           (id, doubt_id, review_round, reviewer_model, review_action,
                            review_notes, reviewed_at)
                           VALUES (?, ?, '0', ?, ?, ?, ?)""",
                        [f"pilot-{did}-{REVIEW_ACTION}", did, REVIEWER, REVIEW_ACTION,
                         f"先导样本双轨落标：磁盘侧内嵌 {s['marker']} 于 {s['file']}；"
                         f"库侧 dual_marker_id 已写入；交叉核准与去重判定见执行记录",
                         datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
            logs += 1
    print(f"本轮新写入: dual_marker_id 更新 {writes} 行；doubt_review_log 新增 {logs} 行")
    return writes + logs


def rollback(con, ids):
    for did in ids:
        con.execute("UPDATE doubts_to_resolve SET dual_marker_id = NULL WHERE id = ?", [str(did)])
        con.execute("""DELETE FROM doubt_review_log
                       WHERE doubt_id = ? AND review_action = ?""", [str(did), REVIEW_ACTION])
        print(f"已回退 id {did}: dual_marker_id=NULL，复核日志行已删")
    n = con.execute("""SELECT count(*) FROM doubts_to_resolve
                       WHERE dual_marker_id IS NOT NULL""").fetchone()[0]
    print(f"回退后 dual_marker_id 非空行数: {n}")


def restore_file(rel):
    snap = SNAP / rel.replace("/", "__")
    assert snap.exists(), f"无快照: {rel}"
    dst = OUTLINE / rel
    cur = dst.read_bytes()
    old = snap.read_bytes()
    if cur == old:
        print(f"已与快照一致（无需恢复）: {rel}")
    else:
        dst.write_bytes(old)
        print(f"已从快照恢复: {rel}（改后 {len(cur)} 字节 -> 恢复为 {len(old)} 字节）")
        assert dst.read_bytes() == old, "恢复后与快照不一致"
        print("恢复后 diff 为空")


if __name__ == "__main__":
    manifest = load_manifest()
    if "--rollback" in sys.argv:
        ids = [int(x) for x in
               sys.argv[sys.argv.index("--ids") + 1].split(",")]
        con = duckdb.connect(str(DB))
        rollback(con, ids)
    elif "--restore-file" in sys.argv:
        restore_file(sys.argv[sys.argv.index("--restore-file") + 1])
    else:
        con = duckdb.connect(str(DB))
        con = backup(con)
        n = apply(con, manifest)
        if "--verify-idempotent" in sys.argv:
            print(f"幂等复跑新增写入 = {n}（应为 0）")
    con.close()
    print("RC=0")
