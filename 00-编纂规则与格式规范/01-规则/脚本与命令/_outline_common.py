# -*- coding: utf-8 -*-
"""H 线（mail2d）大纲写入公共件 —— **阶段二后为参考件／键空间层**。

现行写入链（2026-10-22 阶段二起）
--------------------------------
大纲回写一律走固定脚本 `00-编纂规则与格式规范/01-规则/脚本与命令/outline_writer.py`
（ADR-0010 执行件）；宿主权威＝`claim_map.hosts`。本件保留供历史批内脚本
（`_outline_b0NN.py`／`_bookkeep_b0NN.py`／`_merge_*_narr.py`）复跑与键空间参考，
并承载 `frozen_hosts()` 承重冻结判据。

宿主解析（现行布局：卷／章目录／节目录／小节 `.md`；**键空间为卷内口径**——本件默认只索引 VOL10）
----------------------------------------------------
- **递归**解析（旧版一层 `listdir` 在目录化后返回 0 条，见 TD-015）。
- `key` ＝ 小节文件名首个 `-` 前的数字前缀，**保点**：`216.5.33-….md` → `216.5.33`
  （旧制「去点」压平会把 `097.1.11` 与 `097.11.1` 映射成同一键——2026-10-22 实测全库 102 组撞键（卷05 内 58 组），故改保点）；
  `value` ＝ 相对**卷目录**的路径（`216.5-…/216.5.33-….md`）。
- **键空间已变**：旧批 narr 键（如 `1975`＝旧的 `197.5-….md`）在新布局不可解析；
  新链以 `claim_map.hosts` 为宿主权威，narr 键仅用于 multi 消歧（经 `--host-map`）。

承重冻结（显式名单＋承重参考）
------------------------------
旧硬编码 `BANS = {19410,19411,19412,19413}` 随 155 批重编号失效（实测其继任
`213.13-openbsd2x期邮件列表史料实录第四辑200103起` 仍为 1,406 refs）。现行口径：

- **生效面＝显式名单**：`BANS`（宿主键）与 `BANS_PATHS`（节相对路径），默认均为空
  ——旧四节已随重编号消失，且现行轮转按专题路由，重节恰是主题枢纽，故不作自动硬冻结
  （自动冻结会误挡 ob_b024 式合法专题路由，如 216.5／210.1）。
- **承重参考**：`section_refs()`／`frozen_sections(min_refs)` 现取各节 refs（节＝承重口径，
  与旧冻结点同层）；`承重参考阈值` 默认 2000，仅用于报告与人工决策，不进 whitelist。
- 主理人如要求恢复硬冻结：把目标节路径写入 `BANS_PATHS` 即可（`whitelist()` 自动扣除）。
"""
import os
import re

ROOT = r"d:\librebsd\05-卷册大纲"
VOL10 = r"第10卷-openbsd的历史"

# 显式禁写名单（生效面）：宿主键与节相对路径；默认空（旧 19410–19413 已随重编号消失）
BANS = set()
BANS_PATHS = set()

# 承重参考阈值（仅报告，不进 whitelist）：旧冻结点 194.13 实测 1,406 refs，现行节级 2,000 起报
FROZEN_MIN_REFS = 2000

_SKIP_STEM = re.compile(r"^index$|概述")
_KEY_RE = re.compile(r"^\d+(\.\d+)*$")
_REF_RE = re.compile(r"<!-- ROW_MINE:")
_CACHE = {}


def host_index():
    """{host_key: 相对卷目录的节文件路径}；递归现行「卷／章／节目录／小节 md」布局。"""
    if "index" in _CACHE:
        return dict(_CACHE["index"])
    out = {}
    base = os.path.join(ROOT, VOL10)
    for d, _dirs, files in os.walk(base):
        files.sort()
        for f in files:
            if not f.endswith(".md"):
                continue
            stem = f[:-3]
            if _SKIP_STEM.search(stem):
                continue
            pref = stem.split("-", 1)[0]
            if not _KEY_RE.match(pref):
                continue
            key = pref
            rel = os.path.relpath(os.path.join(d, f), base).replace(os.sep, "/")
            out[key] = rel
    _CACHE["index"] = dict(out)
    return out


def host_refs():
    """{host_key: 该小节文件的 ROW_MINE 块计数}（读盘一次，进程内缓存）。"""
    if "refs" in _CACHE:
        return dict(_CACHE["refs"])
    base = os.path.join(ROOT, VOL10)
    refs = {}
    for key, rel in host_index().items():
        p = os.path.join(base, rel.replace("/", os.sep))
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                refs[key] = len(_REF_RE.findall(fh.read()))
        except OSError:
            refs[key] = 0
    _CACHE["refs"] = dict(refs)
    return refs


def section_refs():
    """{节相对路径: 该节全部小节文件的 ROW_MINE 合计}——承重口径按**节**计（旧冻结点即节）。"""
    if "srefs" in _CACHE:
        return dict(_CACHE["srefs"])
    out = {}
    for key, rel in host_index().items():
        sec = "/".join(rel.split("/")[:2])      # 章目录/节目录
        out[sec] = out.get(sec, 0) + host_refs()[key]
    _CACHE["srefs"] = dict(out)
    return out


def frozen_sections(min_refs=FROZEN_MIN_REFS):
    """承重冻结节（refs ≥ min_refs，数据驱动；重编号／重排后自动跟随）。"""
    return sorted(s for s, n in section_refs().items() if n >= min_refs)


def frozen_paths(min_refs=FROZEN_MIN_REFS):
    """冻结节的卷相对路径前缀集合（写入前按 claim_map.hosts 路径前缀比对）。"""
    return frozen_sections(min_refs)


def frozen_hosts(min_refs=FROZEN_MIN_REFS):
    """承重参考：refs ≥ 阈值的节内全部宿主键（仅报告；是否冻结由 BANS_PATHS 决定）。"""
    fz = set(frozen_sections(min_refs))
    return sorted(k for k, rel in host_index().items()
                  if "/".join(rel.split("/")[:2]) in fz)


def whitelist():
    """可路由宿主键＝全部键 − 显式 BANS／BANS_PATHS（承重参考不自动扣除）。"""
    fz = set(BANS)
    if BANS_PATHS:
        idx = host_index()
        fz |= {k for k, rel in idx.items()
               if any(rel == p or rel.startswith(p + "/") for p in BANS_PATHS)}
    return sorted(set(host_index()) - fz)
