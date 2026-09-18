# -*- coding: utf-8 -*-
"""WO-007：生成器幂等防护模块（idempotency guard）。
用途：任何向大纲 md 写入自动增补块（DATA_VERIFY_BLOCK / MAIL_MINE / DB_POINTS /
COL_SCAN / DEEP_ANALYSIS / PODCAST_REVIEW / ROW_MINE 等）的脚本，写入前必须调用
本模块的 ensure_absent() / has_block() 检查，已存在同名块则跳过或更新，禁止重复追加。
另提供 normalize_dbnames()：写盘前把旧库名（*.db）统一为现行 .duckdb（防再生）。

用法（生成器脚本内）：
    import sys; sys.path.insert(0, r'd:\\librebsd\\script\\_outline_audit_20260906')
    from wo007_idempotency import has_block, ensure_absent, normalize_dbnames

    t = open(path, encoding='utf-8').read()
    if has_block(t, 'DATA_VERIFY_BLOCK'):
        pass  # 已存在：跳过或走更新逻辑
    else:
        t = t + build_dvb_block(...)
    t = normalize_dbnames(t)
    open(path, 'w', encoding='utf-8', newline='\\n').write(t)
"""
import re

# 全部自动增补块的标记模式
BLOCK_MARKS = [
    "DATA_VERIFY_BLOCK", "MAIL_MINE", "DB_POINTS", "COL_SCAN",
    "DEEP_ANALYSIS", "PODCAST_REVIEW", "ROW_MINE", "MAIL_INSIGHT_SECTION",
    "DOUBT_PENDING_BLOCK", "NOISE_REF_CLEANUP", "dangan-", "DB_REF",
]

# 旧库名 → 新库名（词边界）
DB_MAP = [
    (re.compile(r"\billumos-gate\.db\b"), "illumos-gate.duckdb"),
    (re.compile(r"\blinux-kernel\.db\b"), "linux-kernel.duckdb"),
    (re.compile(r"\bbsd-derivatives\.db\b"), "bsd-derivatives.duckdb"),
    (re.compile(r"\bdragonfly\.db\b"), "dragonfly.duckdb"),
    (re.compile(r"\bopenbsd\.db\b"), "openbsd.duckdb"),
    (re.compile(r"\bnetbsd\.db\b"), "netbsd.duckdb"),
    (re.compile(r"\bfreebsd\.db\b"), "freebsd.duckdb"),
    (re.compile(r"\bdarwin\.db\b"), "darwin.duckdb"),
    # bsd_commits.db 无法静态映射到单库——显式要求调用方给 repo 参数
    (re.compile(r"\bbsd_commits\.db\b"), "REQUIRES_REPO_CONTEXT"),
]


def has_block(text: str, mark: str) -> bool:
    """text 中是否已存在 mark 标记的块（含 <!-- MARK --> 或 <!-- /MARK --> 形态）。

    ⚠️ b027 事故教训（2026-09-12）：本函数只匹配 `<!-- 紧跟 mark` 的形态，
    对 `<!-- ROW_MINE: db.messages.<pk> -->` 这类 mark 与注释开符之间还隔着
    "ROW_MINE: " 前缀的行内锚点，恒返回 False，曾导致写回脚本二跑重复追加。
    此类带行内前缀的锚点请改用 has_prefixed_block() / existing_pks()。
    """
    return bool(re.search(r"<!--\s*/?\s*" + re.escape(mark), text))


# 行内前缀型锚点（mark 之后紧跟 ":" 冒号再接键值，如 ROW_MINE: db.table.pk）
_PREFIXED_ANCHOR_RE = r"<!--\s*/?\s*{}\s*:\s*[\w.\-]+\s*-->"


def has_prefixed_block(text: str, mark: str) -> bool:
    """检测带冒号前缀的行内锚点块，如 `<!-- ROW_MINE: freebsd-hubs.messages.123 -->`。

    b027 事故教训固化（2026-09-12）：has_block 对此形态恒 False，二跑重复追加；
    本函数按 "<!-- MARK: ... -->" 通用形态匹配，供幂等预检使用。
    """
    return bool(re.search(_PREFIXED_ANCHOR_RE.format(re.escape(mark)), text))


def existing_pks(text: str, mark: str, source_prefix: str) -> set:
    r"""收集 text 中全部 `<!-- MARK: <source_prefix><pk> -->` 锚点的 pk 集合。

    例：existing_pks(t, "ROW_MINE", r"freebsd-hubs\.messages\.")
    供写回脚本过滤待写批次（已存在跳过、仅写缺失），实现真幂等。
    """
    pat = r"<!--\s*/?\s*" + re.escape(mark) + r"\s*:\s*" + source_prefix + r"(\d+)\s*-->"
    return set(re.findall(pat, text))


def all_blocks(text: str) -> list:
    """列出 text 中已存在的全部块标记。"""
    return [m for m in BLOCK_MARKS if has_block(text, m)]


def ensure_absent(text: str, mark: str, content: str = None) -> str:
    """幂等写入：若 mark 块已存在，原样返回 text（跳过）；
    不存在且给出 content 则追加 content；未给 content 仅返回原 text。
    返回 (new_text, appended_bool)。"""
    if has_block(text, mark):
        return text, False
    if content is not None:
        return text.rstrip("\n") + "\n\n" + content.rstrip("\n") + "\n", True
    return text, False


def normalize_dbnames(text: str, repo: str = None) -> str:
    """写盘前库名规范化。旧 *.db → *.duckdb；
    bsd_commits.db 需调用方给 repo（如 'freebsd'）才能映射，否则原样保留并交人工。"""
    for pat, new in DB_MAP:
        if new == "REQUIRES_REPO_CONTEXT":
            if repo:
                text = pat.sub(repo + ".duckdb", text)
            continue
        text = pat.sub(new, text)
    return text


def write_guard(path: str, new_text: str, repo: str = None):
    """写盘统一入口：normalize 库名 + 强制 UTF-8 无 BOM + LF。
    返回 (written_bool, guards_applied_desc)。"""
    applied = []
    if normalize_needed(new_text):
        new_text = normalize_dbnames(new_text, repo=repo)
        applied.append("dbnames")
    raw = new_text.encode("utf-8")
    if b"\r\n" in raw:
        new_text = new_text.replace("\r\n", "\n")
        applied.append("crlf")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_text)
    return True, applied


def normalize_needed(text: str) -> bool:
    return bool(re.search(r"\b\w+\.db\b", text) and ".duckdb" not in text.replace(".duckdb", "")) or \
           bool(re.search(r"\b(illumos-gate|linux-kernel|bsd-derivatives|dragonfly|openbsd|netbsd|freebsd|darwin|bsd_commits)\.db\b", text))
