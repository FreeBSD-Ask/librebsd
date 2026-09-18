# -*- coding: utf-8 -*-
"""
落库（write）：读取精炼 JSON，写入 evidence / claim / claim_evidence / source_chapter。
用法: python write_claims.py --json <refined.json>
"""
import sqlite3, json, sys, os, argparse, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
TARGET = os.path.join(ROOT, '04-现代研究文献', 'historical_claims.db')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', required=True)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    with open(args.json, encoding='utf-8') as f:
        data = json.load(f)
    vol = data['vol']; ch = data['ch']
    claims = data['claims']
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    con = sqlite3.connect(TARGET)
    cur = con.cursor()
    n_ev = n_cl = n_ce = n_sc = 0
    for c in claims:
        cid = c['claim_id']
        evids = []
        for ev in c.get('evidence', []):
            eid = ev['evidence_id']
            src = ev['source_id']
            cur.execute('''INSERT OR IGNORE INTO evidence
                (evidence_id, source_id, anchor, quote, quote_lang, fact_text, evidence_kind,
                 event_date, event_date_precision, confidence, extracted_by, extraction_review, legacy_refs, created_at, updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (eid, src, ev.get('anchor'), ev.get('quote'), ev.get('quote_lang','en'),
                 ev.get('fact_text'), ev.get('evidence_kind','quote'),
                 ev.get('event_date'), ev.get('event_date_precision','day'),
                 ev.get('confidence', 0.8), 'llm:agent', 'pending',
                 json.dumps({'mail_mine': True, 'ch': ch, 'vol': vol}, ensure_ascii=False), now, now))
            n_ev += cur.rowcount
            evids.append((eid, ev.get('role','supporting'), ev.get('strength','strong')))
            # source_chapter 挂钩
            cur.execute('''INSERT OR IGNORE INTO source_chapter (source_id, vol, ch, sec, link_type)
                           VALUES (?,?,?,?,?)''', (src, vol, ch, '', 'used'))
            n_sc += cur.rowcount
        # claim
        cur.execute('''INSERT OR IGNORE INTO claim
            (claim_id, claim_text, claim_type, time_start, time_end, time_precision,
             evidence_level, wording_gate, status, parent_claim_id, impact_subtype,
             linked_arrow_id, controversy_id, created_by, reviewed_by, created_at, updated_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
            (cid, c['claim_text'], c['claim_type'], c.get('time_start'), c.get('time_end'),
             c.get('time_precision','unknown'), c.get('evidence_level'), c.get('wording_gate'),
             c.get('status','supported'), c.get('parent_claim_id'), c.get('impact_subtype'),
             c.get('linked_arrow_id'), c.get('controversy_id'), 'llm:agent', None, now, now))
        n_cl += cur.rowcount
        # claim_evidence
        for eid, role, strength in evids:
            cur.execute('''INSERT OR IGNORE INTO claim_evidence (claim_id, evidence_id, role, strength, disposition, search_log_ref, created_at)
                           VALUES (?,?,?,?,?,?,?)''', (cid, eid, role, strength, None, None, now))
            n_ce += cur.rowcount
    con.commit()
    if args.dry_run:
        print('[dry-run] 不提交')
        con.rollback()
    else:
        print(f'写入完成: evidence +{n_ev}, claim +{n_cl}, claim_evidence +{n_ce}, source_chapter +{n_sc}')
    con.close()

if __name__ == '__main__':
    main()
