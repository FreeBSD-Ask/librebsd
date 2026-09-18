# -*- coding: utf-8 -*-
"""261 万邮件 → raw_source(namespace='mail') 全量登记（幂等，INSERT OR IGNORE）"""
import sqlite3, os, time, datetime

DBS = {
    'freebsd': '03-原始史料库/11-邮件列表史料/01-freebsd/freebsd_mail.db',
    'netbsd':  '03-原始史料库/11-邮件列表史料/02-netbsd/netbsd_mail.db',
    'openbsd': '03-原始史料库/11-邮件列表史料/03-openbsd/openbsd_mail.db',
    'dragonfly':'03-原始史料库/11-邮件列表史料/04-dragonfly/dragonfly_mail.db',
    'otherbsd':'03-原始史料库/11-邮件列表史料/06-other-bsd/other-bsd_mail.db',
    'usenet':  '03-原始史料库/11-邮件列表史料/07-usenet/usenet_mail.db',
}
TARGET = '04-现代研究文献/historical_claims.db'

def date_precision(d):
    if not d: return 'unknown'
    d = d.strip()
    if len(d) >= 10: return 'day'
    if len(d) >= 7:  return 'month'
    if len(d) >= 4:  return 'year'
    return 'unknown'

def main():
    tcon = sqlite3.connect(TARGET)
    tcon.execute('PRAGMA journal_mode=WAL')
    tcon.execute('PRAGMA synchronous=NORMAL')
    tcur = tcon.cursor()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    total_inserted = 0
    total_seen = 0
    per_db = {}
    for dbn, path in DBS.items():
        if not os.path.exists(path):
            print(f'[skip] {dbn} 不存在')
            continue
        scon = sqlite3.connect(path)
        scur = scon.cursor()
        # 取列名索引
        cols = [c[1] for c in scur.execute('PRAGMA table_info(messages)').fetchall()]
        ci = {c: i for i, c in enumerate(cols)}
        batch = []
        n_seen = 0
        t0 = time.time()
        # 流式读取（避免一次载入 12GB freebsd 全量）
        for row in scur.execute('SELECT * FROM messages'):
            rid = row[ci['id']]
            msg_hash = row[ci['msg_hash']] or ''
            subject = row[ci['subject']]
            from_name = row[ci['from_name']]
            from_email = row[ci['from_email']]
            date = row[ci['date']]
            author = None
            if from_name and from_email:
                author = f'{from_name} <{from_email}>'
            elif from_email:
                author = from_email
            elif from_name:
                author = from_name
            source_id = f'SRC-mail:{dbn}:{rid}'
            # 精简登记：title/author/tier_basis/acquired_at/acquisition_method/legacy_status 置空
            # （派生自邮件库，可通过 source_db+local_pk 取回；避免 2.6M 行冗余 bloat）
            batch.append((
                source_id, 'mail', path, 'messages', str(rid), msg_hash, None,
                'mailing_list', 'email', 2, None, date, date_precision(date),
                None, None, None, None, 1, 1, 0,
                None, None, None, None, None,
                'U', None, 0, 0, None, now, now,
            ))
            n_seen += 1
            if len(batch) >= 5000:
                tcur.executemany('''INSERT OR IGNORE INTO raw_source
                    (source_id, namespace, source_db, source_table, local_pk, content_hash, title,
                     source_type, carrier, source_layer, tier_basis, source_date, date_precision,
                     author, author_entity, organization, org_entity, first_hand, contemporary, retrospective,
                     provenance_url, provenance_commit, provenance_archive, acquired_at, acquisition_method,
                     reliability_grade, reliability_rationale, banned_source, doubt_flag, legacy_status, created_at, updated_at)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', batch)
                total_inserted += tcur.rowcount
                batch = []
        if batch:
            tcur.executemany('''INSERT OR IGNORE INTO raw_source
                (source_id, namespace, source_db, source_table, local_pk, content_hash, title,
                 source_type, carrier, source_layer, tier_basis, source_date, date_precision,
                 author, author_entity, organization, org_entity, first_hand, contemporary, retrospective,
                 provenance_url, provenance_commit, provenance_archive, acquired_at, acquisition_method,
                 reliability_grade, reliability_rationale, banned_source, doubt_flag, legacy_status, created_at, updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', batch)
            total_inserted += tcur.rowcount
        tcon.commit()
        per_db[dbn] = n_seen
        total_seen += n_seen
        scon.close()
        print(f'[ok] {dbn}: {n_seen} 行, 耗时 {round(time.time()-t0,1)}s')
    tcon.commit()
    # 校验
    mail_cnt = tcur.execute("SELECT COUNT(*) FROM raw_source WHERE namespace='mail'").fetchone()[0]
    print(f'\n=== 完成 ===')
    print(f'读取总行数: {total_seen}')
    print(f'实际 INSERT (rowcount 累加): {total_inserted}')
    print(f'raw_source namespace=mail 现有: {mail_cnt}')
    tcon.close()

if __name__ == '__main__':
    main()
