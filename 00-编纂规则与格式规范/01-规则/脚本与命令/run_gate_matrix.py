# -*- coding: utf-8 -*-
"""门禁批量执行器（固定脚本，2026-11-17 立，工具类非门禁）。

用途：按分组增量跑全部判定程序，逐项记录退出码与输出尾迹（`results.jsonl` 按 id 断点续跑）。
节奏与退出码语义见 `流程规则/06-门禁体系.md`“门禁两档节奏与批量执行器”。
分组：G1 常备五件｜G2 规则与文档｜G3 工程与流程｜G4 目录页与 HTML｜G5 大纲与映射｜
      G6 数据库｜G7 复核套件与浏览器回归｜G8 条件面（批次上下文与域验证器）。

用法：
  python run_gate_matrix.py <G1..G8|all> [--force] [--out DIR]
  python run_gate_matrix.py --list
  python run_gate_matrix.py --selftest      # 表结构自检（id 唯一、分组合法、路径存在）

注意：
  * 重面（supplement／scan_invisible／tuhs／sidecar 全库扫／浏览器回归）单次 4—21 分钟，
    应后台分组执行；退出码 124 是**执行窗不足**，不是门禁结论——须单跑复验。
  * JS 运行时一律 bun（禁 npm／node 直呼），见 流程规则/02“JS 运行时与包管理器基线”。
"""
import argparse
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DIR05 = os.path.join(REPO, "05-卷册大纲", "目录")
TESTS = os.path.join(DIR05, "tests")
PY = r"C:\Program Files\Python315\python.exe"
BUN = "bun"

STATUS_OK, STATUS_FAIL, STATUS_ENV, STATUS_TIMEOUT = 0, 1, 2, 124


def p(name):
    return os.path.join(HERE, name)


# (id, group, argv, cwd, timeout_s)
GATES = [
    # ---- G1 常备五件 ----
    ("standing_sync_baseline", "G1", [PY, p("sync_refactor2026_baseline.py"), "--check"], REPO, 480),
    ("standing_longline", "G1", [PY, p("_longline_status.py"), "--check"], REPO, 480),
    ("standing_gate_registry", "G1", [PY, p("audit_gate_registry.py")], REPO, 480),
    ("standing_sidecar", "G1", [PY, p("audit_sidecar_backup.py")], REPO, 1800),
    ("standing_rule_dup", "G1", [PY, p("audit_rule_dup.py")], REPO, 480),
    # ---- G2 规则与文档 ----
    ("rule_modality_selftest", "G2", [PY, p("audit_rule_modality.py"), "--selftest"], REPO, 480),
    ("rule_modality_diff", "G2", [PY, p("audit_rule_modality.py"), "--diff"], REPO, 480),
    ("proofread_forms_selftest", "G2", [PY, p("audit_proofread_forms.py"), "--selftest"], REPO, 480),
    ("proofread_forms_check", "G2", [PY, p("audit_proofread_forms.py")], REPO, 480),
    ("md_quote_glyphs", "G2", [PY, p("audit_md_quote_glyphs.py")], REPO, 1200),
    ("markdown_lint", "G2", [PY, p("audit_markdown_lint.py")], REPO, 480),
    ("md_bold_spacing", "G2", [PY, p("audit_md_bold_spacing.py")], REPO, 480),
    ("engineering_practice", "G2", [PY, p("audit_engineering_practice.py")], REPO, 480),
    # ---- G3 工程与流程 ----
    ("task_lifecycle", "G3", [PY, p("audit_task_lifecycle.py")], REPO, 480),
    ("supplement_selftest", "G3", [PY, p("audit_supplement_chain.py"), "--selftest"], REPO, 480),
    ("supplement_check", "G3", [PY, p("audit_supplement_chain.py"), "--check"], REPO, 1800),
    ("oaa_f1_check", "G3", [PY, p("oaa_remap_claims.py"), "--group", "F1", "--check"], REPO, 480),
    ("oaa_f2_check", "G3", [PY, p("oaa_remap_claims.py"), "--group", "F2", "--check"], REPO, 480),
    ("oaa_f3_check", "G3", [PY, p("oaa_remap_claims.py"), "--group", "F3", "--check"], REPO, 480),
    ("oaa_f4_check", "G3", [PY, p("oaa_remap_claims.py"), "--group", "F4", "--check"], REPO, 480),
    ("outline_writer_selftest", "G3", [PY, p("outline_writer.py"), "--selftest"], REPO, 480),
    # ---- G4 目录页与 HTML ----
    ("assemble_check", "G4", [PY, p("assemble_index.py"), "--check"], DIR05, 480),
    ("index_structure", "G4", [PY, p("audit_index_structure.py")], REPO, 900),
    ("seq_continuity", "G4", [PY, p("audit_sequence_continuity.py")], REPO, 480),
    ("xref_audit", "G4", [PY, p("xref_audit.py")], REPO, 480),
    ("note_xref", "G4", [PY, p("audit_note_xref.py")], REPO, 480),
    ("data_integrity", "G4", [PY, p("audit_data_integrity.py")], REPO, 480),
    ("embed_check", "G4", [PY, p("embed.py"), "--check"], DIR05, 480),
    ("page_assets", "G4", [PY, p("audit_page_assets.py")], REPO, 480),
    ("a11y", "G4", [PY, p("audit_a11y.py")], REPO, 1800),
    ("js_blockscope", "G4", [PY, p("audit_js_blockscope.py")], REPO, 480),
    ("server_contract", "G4", [PY, p("audit_server_contract.py")], REPO, 480),
    ("page_version_bump", "G4", [PY, p("audit_page_version_bump.py")], REPO, 480),
    ("fixture_freshness", "G4", [PY, p("audit_fixture_freshness.py")], REPO, 480),
    ("tri_negtest", "G4", [PY, os.path.join(TESTS, "tri_structure_negtest.py")], DIR05, 1800),
    ("outline_selfcheck", "G4", [PY, os.path.join(TESTS, "outline_selfcheck.py")], DIR05, 480),
    # ---- G5 大纲与映射 ----
    ("renumber_guard", "G5", [PY, p("audit_renumber_guard.py")], REPO, 480),
    ("silent_loss", "G5", [PY, p("audit_silent_loss_guard.py")], REPO, 480),
    ("anchor_pair_order", "G5", [PY, p("audit_anchor_pair_order.py")], REPO, 900),
    ("anchor_pairs_check", "G5", [PY, p("audit_anchor_pairs.py"), "--check"], REPO, 900),
    ("outline_dup", "G5", [PY, p("audit_outline_dup.py")], REPO, 900),
    ("outline_landing", "G5", [PY, p("audit_outline_landing.py")], REPO, 900),
    ("anchor_resolution", "G5", [PY, p("audit_anchor_resolution.py")], REPO, 480),
    ("evidence_labels", "G5", [PY, p("audit_evidence_level_labels.py")], REPO, 900),
    ("subsection_design", "G5", [PY, p("audit_subsection_design.py")], REPO, 480),
    ("title_consistency", "G5", [PY, p("audit_title_consistency.py"), "--check"], REPO, 480),
    ("title_term_forms", "G5", [PY, p("audit_title_term_forms.py")], REPO, 480),
    ("disk_terminology", "G5", [PY, p("audit_disk_terminology.py")], REPO, 900),
    # ---- G6 数据库 ----
    ("db_health", "G6", [PY, p("audit_databases.py")], REPO, 480),
    ("folder_db_integrity", "G6", [PY, p("audit_folder_db_integrity.py"), "--all", "--dry-run"], REPO, 900),
    ("provenance_dupes", "G6", [PY, p("audit_provenance_dupes.py")], REPO, 480),
    ("claimdb_guard", "G6", [PY, p("claimdb_guard.py"), "--db", "historical_claims"], REPO, 480),
    ("person_bio_integrity", "G6", [PY, p("audit_person_bio_integrity.py")], REPO, 480),
    # ---- G7 复核套件与浏览器回归 ----
    ("scan_invisible", "G7", [PY, p("scan_md_invisible.py")], REPO, 1800),
    ("browser_visual", "G7", [BUN, os.path.join(TESTS, "visual_regression.mjs"), "--headless"], DIR05, 1800),
    ("browser_matrix", "G7", [BUN, os.path.join(TESTS, "full_matrix_regression.mjs"), "--headless"], DIR05, 1800),
    ("browser_fullsize", "G7", [BUN, os.path.join(TESTS, "fullsize_regression.mjs"), "--headless"], DIR05, 1800),
    # ---- G8 条件面（批次上下文与域验证器） ----
    ("tag_ledger", "G8", [PY, p("audit_tag_ledger.py"), "--check"], REPO, 480),
    ("keyword_index", "G8", [PY, p("audit_keyword_index.py")], REPO, 900),
    ("guard_source_chars", "G8", [PY, p("guard_source_chars.py")], REPO, 480),
    ("mail2d_batch_selftest", "G8", [PY, p("audit_mail2d_batch.py"), "--selftest"], REPO, 480),
    ("mirror_ingest_audit", "G8", [PY, p("audit_mirror_ingest.py")], REPO, 480),
    ("oaa_batch_selftest", "G8", [PY, p("audit_oaa_batch.py"), "--selftest"], REPO, 480),
    ("tuhs_verify_sql", "G8", [PY, p("verify_tuhs_wiki_sql.py"), "--offline"], REPO, 900),
    ("tuhs_verify", "G8", [PY, p("verify_tuhs_wiki.py")], REPO, 1800),
]

GROUPS = ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8")
ENV = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")


def load_done(path):
    done = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    done.add(json.loads(line)["id"])
                except Exception:
                    pass
    return done


def cmd_selftest():
    """表结构自检：id 唯一、分组合法、脚本路径存在、超时为正。"""
    bad = []
    ids = [g[0] for g in GATES]
    if len(ids) != len(set(ids)):
        bad.append("id 重复")
    for gid, grp, argv, cwd, to in GATES:
        if grp not in GROUPS:
            bad.append("%s 分组非法 %s" % (gid, grp))
        if to <= 0:
            bad.append("%s 超时非法" % gid)
        target = argv[1]
        if target.endswith(".py") or target.endswith(".mjs"):
            if not os.path.exists(target):
                bad.append("%s 目标不存在：%s" % (gid, target))
        if not os.path.isdir(cwd):
            bad.append("%s cwd 不存在" % gid)
    print("表项 %d 个；问题 %d 个" % (len(GATES), len(bad)))
    for b in bad:
        print("  FAIL " + b)
    print("自检：%s" % ("PASS" if not bad else "FAIL"))
    return 0 if not bad else 1


def cmd_list():
    cur = None
    for gid, grp, argv, cwd, to in GATES:
        if grp != cur:
            print("== %s" % grp)
            cur = grp
        print("  %-26s %ss" % (gid, to))
    print("合计 %d 项" % len(GATES))
    return 0


def main():
    ap = argparse.ArgumentParser(description="门禁批量执行器（工具类非门禁；节奏见 流程规则/06）")
    ap.add_argument("group", nargs="?", default="all", help="G1..G8 或 all")
    ap.add_argument("--force", action="store_true", help="忽略既有 results.jsonl 全量重跑")
    ap.add_argument("--out", default=None, help="结果目录（默认本脚本目录）")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return cmd_selftest()
    if a.list:
        return cmd_list()
    if a.group not in GROUPS + ("all",):
        print("[exit 2] 分组非法：%s（可用 %s／all）" % (a.group, "／".join(GROUPS)))
        return 2
    outdir = a.out or HERE
    results = os.path.join(outdir, "results.jsonl")
    done = set() if a.force else load_done(results)
    ran = 0
    for gid, grp, argv, cwd, to in GATES:
        if a.group not in ("all", grp):
            continue
        if gid in done:
            continue
        t0 = time.time()
        try:
            proc = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=to, env=ENV)
            code, out = proc.returncode, (proc.stdout or b"") + (proc.stderr or b"")
            tail = out.decode("utf-8", errors="replace")[-4000:]
        except subprocess.TimeoutExpired:
            code, tail = STATUS_TIMEOUT, "TIMEOUT after %ss（执行窗不足，非门禁结论；须单跑复验）" % to
        rec = {"id": gid, "group": grp, "exit": code, "dur_s": round(time.time() - t0, 1),
               "tail": tail, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
        with open(results, "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("[%s] %s exit=%s %ss" % (grp, gid, code, rec["dur_s"]), flush=True)
        ran += 1
    print("本批实跑 %d 项；结果 %s" % (ran, results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
