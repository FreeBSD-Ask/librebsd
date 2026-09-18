# -*- coding: utf-8 -*-
"""邮件库去重核验：消息级绝对重复 + msg_hash 跨列表/跨库碰撞"""
import sqlite3, os, sys, time

DBS = {
    'freebsd': '03-原始史料库/11-邮件列表史料/01-freebsd/freebsd_mail.db',
    'netbsd':  '03-原始史料库/11-邮件列表史料/02-netbsd/netbsd_mail.db',
    'openbsd': '03-原始史料库/11-邮件列表史料/03-openbsd/openbsd_mail.db',
    'dragonfly':'03-原始史料库/11-邮件列表史料/04-dragonfly/dragonfly_mail.db',
    'otherbsd':'03-原始史料库/11-邮件列表史料/06-other-bsd/other-bsd_mail.db',
    'usenet':  '03-原始史料库/11-邮件列表史料/07-usenet/usenet_mail.db',
}

def has_col(cur, t, col):
    return any(c[1] == col for c in cur.execute(f'PRAGMA table_info({t})').fetchall())

total_all = 0
report = {}
for name, path in DBS.items():
    if not os.path.exists(path):
        report[name] = 'MISSING'
        continue
    t0 = time.time()
    con = sqlite3.connect(path)
    cur = con.cursor()
    n = cur.execute('SELECT COUNT(*) FROM messages').fetchone()[0]
    total_all += n
    # 绝对重复：同 (list_id, message_id) 出现 >1 次
    abs_dup = cur.execute('SELECT COUNT(*) FROM (SELECT list_id, message_id FROM messages GROUP BY list_id, message_id HAVING COUNT(*)>1)').fetchone()[0]
    # 绝对重复涉及的行数
    abs_dup_rows = cur.execute('''SELECT COALESCE(SUM(c-1),0) FROM (
        SELECT COUNT(*) c FROM messages GROUP BY list_id, message_id HAVING COUNT(*)>1)''').fetchone()[0]
    # msg_hash 重复（跨列表，同库内）
    hash_dup_groups = cur.execute('SELECT COUNT(*) FROM (SELECT msg_hash FROM messages WHERE msg_hash IS NOT NULL AND msg_hash!=\'\' GROUP BY msg_hash HAVING COUNT(*)>1)').fetchone()[0]
    hash_dup_rows = cur.execute('''SELECT COALESCE(SUM(c-1),0) FROM (
        SELECT COUNT(*) c FROM messages WHERE msg_hash IS NOT NULL AND msg_hash!=\'\' GROUP BY msg_hash HAVING COUNT(*)>1)''').fetchone()[0]
    null_hash = cur.execute("SELECT COUNT(*) FROM messages WHERE msg_hash IS NULL OR msg_hash=''").fetchone()[0]
    null_msgid = cur.execute("SELECT COUNT(*) FROM messages WHERE message_id IS NULL OR message_id=''").fetchone()[0]
    con.close()
    report[name] = dict(n=n, abs_dup=abs_dup, abs_dup_rows=abs_dup_rows,
                        hash_dup_groups=hash_dup_groups, hash_dup_rows=hash_dup_rows,
                        null_hash=null_hash, null_msgid=null_msgid, sec=round(time.time()-t0,1))

print(f'{"库":<10}{"邮件数":>12}{"绝对重复组":>10}{"绝对重复行":>10}{"hash重复组":>10}{"hash重复行":>10}{"空hash":>8}{"空msgid":>8}  耗时')
for name, r in report.items():
    if r == 'MISSING':
        print(f'{name:<10}  MISSING')
    else:
        print(f'{name:<10}{r["n"]:>12}{r["abs_dup"]:>10}{r["abs_dup_rows"]:>10}{r["hash_dup_groups"]:>10}{r["hash_dup_rows"]:>10}{r["null_hash"]:>8}{r["null_msgid"]:>8}  {r["sec"]}s')
print(f'{"合计":<10}{total_all:>12}')

# 跨库 msg_hash 碰撞（同一封邮件跨项目列表，如 cross-post 到 freebsd+netbsd+usenet）
print('\n=== 跨库 msg_hash 碰撞 ===')
import hashlib
seen = {}
for name, path in DBS.items():
    if not os.path.exists(path): continue
    con = sqlite3.connect(path)
    cur = con.cursor()
    for (h,) in cur.execute("SELECT DISTINCT msg_hash FROM messages WHERE msg_hash IS NOT NULL AND msg_hash!=''"):
        seen.setdefault(h, []).append(name)
    con.close()
cross = {h: v for h, v in seen.items() if len(v) > 1}
print(f'跨库重复 msg_hash 组数: {len(cross)}')
from collections import Counter
c = Counter(tuple(sorted(v)) for v in cross.values())
for combo, cnt in c.most_common(20):
    print(f'  {cnt:>8}  {combo}')
