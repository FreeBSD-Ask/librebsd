# -*- coding: utf-8 -*-
"""
挖（dig）：按章节从 6 邮件库定向抽取候选邮件。
用法: python extract_candidates.py --ch 2 [--top 60] [--out ...]
"""
import sqlite3, json, os, re, sys, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
KW_PATH = os.path.join(ROOT, '05-卷册大纲', 'chapter_keywords.json')
DBS = {
    'freebsd':  ('03-原始史料库/11-邮件列表史料/01-freebsd/freebsd_mail.db', 'freebsd'),
    'netbsd':   ('03-原始史料库/11-邮件列表史料/02-netbsd/netbsd_mail.db', 'netbsd'),
    'openbsd':  ('03-原始史料库/11-邮件列表史料/03-openbsd/openbsd_mail.db', 'openbsd'),
    'dragonfly':('03-原始史料库/11-邮件列表史料/04-dragonfly/dragonfly_mail.db', 'dragonfly'),
    'otherbsd': ('03-原始史料库/11-邮件列表史料/06-other-bsd/other-bsd_mail.db', 'otherbsd'),
    'usenet':   ('03-原始史料库/11-邮件列表史料/07-usenet/usenet_mail.db', 'usenet'),
}
EN_TOK = re.compile(r'[A-Za-z][A-Za-z0-9._+-]{2,}')

def derive_terms(entry):
    terms = []
    for kw in entry.get('keywords', []):
        if kw and kw.strip():
            terms.append(kw.strip())
    # 从 title/subs 提取英文 token（长度>=3 且非纯通用词）
    text = entry.get('title', '') + ' ' + ' '.join(entry.get('subs', []))
    for t in EN_TOK.findall(text):
        t = t.lower()
        if len(t) >= 3 and t not in ('the','and','for','with','from','that','this','was','are','not','com','org','net','edu','http','https','www'):
            terms.append(t)
    # 去重保序
    seen = set(); out = []
    for t in terms:
        if t not in seen:
            seen.add(t); out.append(t)
    return out

def fts_query(term):
    # FTS5 短语安全：纯字母数字直接加引号
    t = re.sub(r'[^A-Za-z0-9._+-]', '', term)
    return f'"{t}"'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ch', type=int, required=True)
    ap.add_argument('--top', type=int, default=80, help='每 term 每库最多候选')
    ap.add_argument('--out', type=str, default=None)
    args = ap.parse_args()

    with open(KW_PATH, encoding='utf-8') as f:
        kw = json.load(f)
    entry = kw.get(str(args.ch))
    if not entry:
        print(f'章节 {args.ch} 不在 chapter_keywords.json 中'); sys.exit(1)
    terms = derive_terms(entry)
    print(f'章节 {args.ch}: {entry["title"]} ({entry["volume"]})')
    print(f'派生搜索词 ({len(terms)}): {terms[:40]}')

    candidates = {}  # msg_hash -> row dict
    for term in terms:
        q = fts_query(term)
        for dbn, (relpath, proj) in DBS.items():
            abspath = os.path.join(ROOT, relpath)
            if not os.path.exists(abspath):
                continue
            con = sqlite3.connect(abspath)
            cur = con.cursor()
            try:
                rows = cur.execute(f"""
                    SELECT m.id, m.list_id, m.message_id, m.subject, m.from_name, m.from_email,
                           m.date, m.year, m.body, m.msg_hash
                    FROM messages_fts f JOIN messages m ON m.id = f.rowid
                    WHERE messages_fts MATCH ?
                    ORDER BY m.year IS NULL, m.year ASC, m.id ASC
                    LIMIT ?""", (q, args.top)).fetchall()
            except Exception as e:
                rows = []
            con.close()
            for r in rows:
                rid, list_id, mid, subj, fname, femail, date, year, body, mhash = r
                key = mhash or f'{dbn}:{rid}'
                if key in candidates:
                    continue  # msg_hash 去重（跨库跨列表 repost）
                candidates[key] = dict(db=dbn, proj=proj, rid=rid, list_id=list_id,
                                       message_id=mid, subject=subj, from_name=fname,
                                       from_email=femail, date=date, year=year,
                                       body=body, msg_hash=mhash, term=term)
    # 排序：按 year 升序（最早期最可能有起源/首现证据）
    clist = sorted(candidates.values(), key=lambda x: (x['year'] is None, x['year'] or 0, x['db']))
    print(f'候选邮件总数（msg_hash 去重后）: {len(clist)}')

    if args.out is None:
        outdir = os.path.join(ROOT, 'script', '_staging', 'mailmine', 'candidates')
        os.makedirs(outdir, exist_ok=True)
        args.out = os.path.join(outdir, f'ch{args.ch:03d}.md')

    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(f'# 章节 {args.ch} 候选邮件（{entry["title"]}）\n\n')
        f.write(f'> 卷：{entry["volume"]} ｜ 候选数：{len(clist)} ｜ 搜索词：{"、".join(terms[:40])}\n\n')
        for i, c in enumerate(clist, 1):
            subj = (c['subject'] or '(无主题)')[:120]
            fname = c['from_name'] or ''
            femail = c['from_email'] or ''
            author = f'{fname} <{femail}>' if fname or femail else '(未知)'
            body = (c['body'] or '')
            body = re.sub(r'\s+', ' ', body)[:900]
            f.write(f'## [{i}] {subj}\n\n')
            f.write(f'- 库: {c["db"]} ｜ 列表id: {c["list_id"]} ｜ 日期: {c["date"] or "?"} (year {c["year"]}) ｜ 作者: {author}\n')
            f.write(f'- message_id: {c["message_id"]}\n')
            f.write(f'- source_id: `SRC-mail:{c["db"]}:{c["rid"]}` ｜ msg_hash: {c["msg_hash"]}\n')
            f.write(f'- 命中词: {c["term"]}\n\n')
            f.write(f'```text\n{body}\n```\n\n')
    print(f'已写入: {args.out}')

if __name__ == '__main__':
    main()
