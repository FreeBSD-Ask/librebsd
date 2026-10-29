# -*- coding: utf-8 -*-
"""
第二十件门禁：重构静默丢失守卫（audit_silent_loss_guard.py）

背景（88 号文 §五.6 新增建议 P1 ／ spec converge-all-remaining-tasks SubTask 1.3 残余）：
  2026-09-19→09-20 重构中 4 个整章静默消失（BSD 数据库服务器生态／邮件系统与反垃圾战争／
  BSD 在科研计算中的角色／自由概念史），系 88 号文以“三时点比对法”抓出。
  本件将该法固化为门禁判据：早期目录载体中的每一章，其章题（整题或核心词段）须在现行
  内容源残留，或在豁免登记表中有登记（合法改题／主题归并／待裁定），否则 FAIL。

三时点载体：
  T1（最早）：仓内快照 `08-核查报告与多轮复核/重构2026/data/outline-t1-20261011.txt`——
             2026-10-11 时点 67 卷 483 章（取自提交 c7ced9322）。
             **2026-10-29 重定基线**：原载体为 Git 提交 305b320（2026-09-18，36 卷 321 章），
             该对象在历史重写后被 gc 清除、无引用可达，远端按 SHA 取回失败；故固化为仓内快照。
             窗口由“09-19→今”收窄为“10-11→今”，09-19→10-11 段已由 88 号文当年逐条甄别覆盖。
  T3（现行）：data/outline.txt
  （T2 中间时点 09-20 prebak 已不在盘；本件以 T1↔T3 两端比对承载 88 判据——判据实质
    为“曾为章、现为零承接”。初版实跑 326 章得候选 34，逐条语义甄别（2026-10-09）：
    UI 面板 3 条判据过滤、合法改题/归并 27 条入豁免表（各带去向北键）、F 组待裁定 4 条
    入豁免表（92 号文 L608）；2026-10-29 重定基线批另增 2 条。）

豁免登记表（有意识的选择，非遗漏；每条含去向北键，北键消失＝豁免腐烂 FAIL）：
  改题/归并类：watch 键为现行承接章题或其区分词；watch 键在现行 outline 消失 → 豁免腐烂。
  F 组待裁定类：无 watch 键（尚未回写，92 号文 L608 登记在案；回写落卷后应改判并删豁免）。

用法：python audit_silent_loss_guard.py [--early PATH|GIT:<commit>:<path>] [--outline PATH]
退出码：0=PASS，1=FAIL。
"""
import argparse
import io
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# T1 早期载体（2026-10-29 重定基线）：原以 Git 提交 305b320（2026-09-18 22:57，36 卷 321 章）
# 为唯一长期取证载体。2026-10-29 实测该对象在历史重写后被 gc 清除：无任何引用可达，
# 远端按 SHA 取回亦失败（origin 仅 main 与两标签）。故改为**仓内快照**：
# 2026-10-11 时点、67 卷 483 章（取自提交 c7ced9322 的同路径文件），
# 使判据在全新克隆与 CI 中可复现（原 GIT: 形态仍保留，可用 --early 显式指定）。
# 判据窗口影响：“09-19→今”收窄为“10-11→今”；09-19→10-11 段的丢失已由 88 号文当年
# 逐条语义甄别覆盖（本件豁免表即其产物），本次重定基线批新增 2 条承接豁免。
DEFAULT_EARLY = os.path.join(REPO, "08-核查报告与多轮复核", "重构2026", "data",
                             "outline-t1-20261011.txt")
DEFAULT_OUTLINE = os.path.join(REPO, "05-卷册大纲", "目录", "data", "outline.txt")

# index.html 工具面板 h3（非章，判据过滤；面板标题变化不影响判定）
UI_PANELS = ("跨卷关联图谱", "时间线视图", "结构修订史")

# 豁免登记表：章题核心词 -> (watch 键或 None, 理由, 登记出处)
# watch 键非 None：现行 outline 须仍含该键（豁免防腐烂）；None：F 组待裁定（静态豁免）
EXEMPTS = {
    # —— 改题类（watch＝现行承接章题区分词；证据＝2026-10-09 残留实测）——
    "电子计算机时代的形成": ("电子计算机", "改题：现行卷一“电子计算机的诞生”", "C-12 批甄别"),
    "虚拟内存与地址空间": ("虚拟内存", "主题归并：现行“虚拟内存”12 处", "C-12 批甄别"),
    "贝克莱与伯克利市": ("伯克利", "改题：现行“伯克利”56 处（贝克莱译名归并）", "C-12 批甄别"),
    "分裂之后的共同遗产": ("共同遗产", "改题：现行“共同遗产”2 处", "C-12 批甄别"),
    "卷末史料与研究方法": ("史料与方法", "改题与终归：原“卷末史料与方法”章（卷40）经 157/155 批并入卷七十五各卷史料交代汇编（原 E-3 题面统一 T1.3，id=2320）", "C-12 批甄别·155 批复核"),
    "安全模型与系统加固": ("安全模型", "改题：现行“安全模型”11 处", "C-12 批甄别"),
    "技术专题史料总目": ("史料总目", "改题：现行“史料总目”1 处", "C-12 批甄别"),
    "代码审计方法论与默认安全原则": ("代码审计", "改题：现行“代码审计”9 处", "C-12 批甄别"),
    "可移植性与平台支持": ("可移植性", "改题：现行“可移植性”34 处", "C-12 批甄别"),
    "用户态与上游差异": ("用户态", "改题：现行“用户态”7 处", "C-12 批甄别"),
    "代码共享与上游关系": ("代码共享", "改题：现行“代码共享”4 处", "C-12 批甄别"),
    "分化轴的四象限": ("分化轴", "改题：现行“分化轴”17 处（四象限模型并入比较史章族）", "C-12 批甄别"),
    "工程哲学的横向对照": ("横向比较", "改题：横向对照系改“横向比较”49 处", "C-12 批甄别"),
    "符号与仪式的横向对照": ("符号与仪式", "改题：现行“符号与仪式”1 处（横向比较系）", "C-12 批甄别"),
    "共同体与治理文化的横向对照": ("治理文化", "改题：现行“治理文化”4 处（横向比较系）", "C-12 批甄别"),
    "价值与许可证观的横向对照": ("横向比较", "改题：横向比较系（主题入卷三十五价值观对照章族）", "C-12 批甄别"),
    "争议与神话的横向对照": ("横向比较", "改题：横向比较系（主题入卷三十五争议对照章族）", "C-12 批甄别"),
    "比较的方法论与判据": ("历史前提", "改题：现行卷三十四第 1 章“比较史的历史前提与共同基线”", "C-12 批甄别"),
    "自由的不对称与商业闭源：取而不回的结构与案例": ("商业闭源", "改题：现行“取而不回”1 处", "C-12 批甄别"),
    "合规认证作为形式主义的制度化": ("形式主义", "改题：现行“形式主义”1 处", "C-12 批甄别"),
    "许可证选择的代际差异": ("版权治理", "主题归并：现行卷三十九“BSD 项目的许可证政策与版权治理”等三章", "C-12 批甄别"),
    "利益分配分析的总结：自由分配是否对称": ("利益分配", "改题：现行“利益分配”1 处", "C-12 批甄别"),
    "许可证与治理的交叉：基金会的版权管理": ("版权治理", "题面归并：现行“许可证政策与版权治理”", "C-12 批甄别"),
    "低密度地区与跨区域细目": ("低密度", "改题：现行“低密度”2 处", "C-12 批甄别"),
    "镜像站生态：志愿者基础设施的物质史": ("镜像站", "改题：现行“镜像站”8 处", "C-12 批甄别"),
    "六十年分离聚合的分期总览": ("分离聚合", "归并：现行卷五十六“六十年分离聚合模型的历史解释”", "C-12 批甄别"),
    "分期划分的说明": ("分离聚合", "归并：同上（分期说明并入该章）", "C-12 批甄别"),
    "偶然性节点考：关键转折点的反事实标注": ("反事实", "改题：现行“反事实”2 处", "C-12 批甄别"),
    "基石与声名：丹尼斯·里奇与史蒂夫·乔布斯的对照": ("乔布斯", "改题：现行“乔布斯”1 处（声名分配章）", "C-12 批甄别"),
    "被记住者名录：人物志作为记忆装置": ("人物志", "改题：现行“人物志”1 处", "C-12 批甄别"),
    "记忆史方法论：记忆变形五类型与本书的自我限制": ("记忆变形", "改题：现行“记忆变形”1 处（记忆研究章）", "C-12 批甄别"),
    # —— F 组（2026-10-22 151 号文批：四条改判删豁免——F-13 回写落卷 5.7、F-12 由 8.5/13.7 承载、F-14 由 12.7/12.8 承载、F-15 由 9.3/6.5/1.6 承载，核心词段皆有残留）——
    # —— P92 门禁同步（2026-10-21）：74 卷重排后的改题／归并承接 ——
    "小型机产业的兴衰与终局": ("主机与小型机产业的格局与兴衰", "改题：现行卷3 第2章", "P92 门禁同步"),
    "网络代码的作者与署名": ("网络代码的作者群", "改题：现行卷27 4.1", "P92 门禁同步"),
    "开源治理的制度化：从企业采纳到开源办公室": ("开源治理的组织化", "改题：现行卷31 第2章", "P92 门禁同步"),
    "安全机制的架构适配": ("多架构内核安全机制一致性", "归并：现行卷42 2.13", "P92 门禁同步"),
    "虚拟化与现代运行环境": ("虚拟化与运行环境", "改题：现行卷38 第10章", "P92 门禁同步"),
    "宽松许可证的类型与许可证兼容性": ("许可证兼容", "归并：现行卷56 5.8／5.10", "P92 门禁同步"),
    "合规数据与法律史方法": ("自动化合规数据", "归并：现行卷59 5.2", "P92 门禁同步"),
    # —— 2026-10-29 T1 重定基线批（窗口 10-11→今；2 条改题/归并承接，用户 2026-10-29 批准）——
    "卷末史料与方法": ("书目述评", "改题＋外迁：28 号文书评挂靠改造后章级题名取消，述评改为编号小节挂靠宿主章，全文外迁 12-重构大纲书目述评/", "T1 重定基线批"),
    "习俗与仪式": ("习俗", "改题/归并：现行“传言、都市传说与习俗”三章（卷十一/卷二十九/卷六十三）与“符号与仪式”横向比较章承接", "T1 重定基线批"),
    # —— UI 面板模板串（非章题，静态豁免）——
    "ui.search.title": (None, "UI 面板模板串，非章题", "P92 门禁同步"),
    "ui.graph.h3": (None, "UI 面板模板串，非章题", "P92 门禁同步"),
    "ui.tl.h3": (None, "UI 面板模板串，非章题", "P92 门禁同步"),
    "ui.rv.h3": (None, "UI 面板模板串，非章题", "P92 门禁同步"),
}

STOP_PREFIX = re.compile(r"^第\s*\d+\s*章\s*")


def extract_chapter_titles_early(html):
    titles = []
    for m in re.findall(r"<h3[^>]*>([^<]{4,120})</h3>", html):
        t = m.replace("&amp;", "&").strip()
        if any(p in t for p in UI_PANELS):
            continue  # 工具面板，非章
        titles.append(STOP_PREFIX.sub("", t))
    return titles


def core_words(title):
    t = STOP_PREFIX.sub("", title)
    segs = re.split(r"[：:，,、（）()\[\]／/·—\s]+", t)
    return [s for s in segs if len(s) >= 2]


def extract_chapter_titles_outline(text):
    return [STOP_PREFIX.sub("", m).strip()
            for m in re.findall(r"^##\s*第\s*\d+\s*章\s*(.+?)\s*$", text, re.M)
            if m.strip()]


def load_early(spec):
    if spec.startswith("GIT:"):
        parts = spec[4:].split(":", 1)
        if len(parts) != 2:
            raise SystemExit("--early GIT:<commit>:<path> 形制错误")
        commit, path = parts
        r = subprocess.run(["git", "show", "%s:%s" % (commit, path)],
                           cwd=REPO, capture_output=True)
        if r.returncode != 0:
            raise SystemExit("git show 失败：%s" % r.stderr.decode("utf-8", "replace")[:300])
        return r.stdout.decode("utf-8", "replace")
    if not os.path.isfile(spec):
        raise SystemExit("T1 载体缺失：%s（旁路副本已按 2026-10-23 封禁令清除，"
                         "请用 --early GIT:<commit>:<path> 指向 Git 历史）" % spec)
    return io.open(spec, encoding="utf-8").read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--early", default=DEFAULT_EARLY)
    ap.add_argument("--outline", default=DEFAULT_OUTLINE)
    args = ap.parse_args()

    early_text = load_early(args.early)
    outline = io.open(args.outline, encoding="utf-8").read()
    if "<h3" in early_text:
        titles = extract_chapter_titles_early(early_text)
    else:
        titles = extract_chapter_titles_outline(early_text)

    print("=" * 72)
    print("第二十件：重构静默丢失守卫（88 号文三时点比对法固化）")
    print(f"  T1 早期载体：{os.path.relpath(args.early, REPO) if os.path.isfile(args.early) else args.early}（章 {len(titles)}）")
    print(f"  T3 现行内容源：{os.path.basename(args.outline)}")
    print("-" * 72)

    # 豁免防腐烂：watch 键须仍在现行
    for kw, (watch, reason, src) in EXEMPTS.items():
        if watch and watch not in outline:
            print(f"  [FAIL] 豁免腐烂：核心词“{kw}”的去向键“{watch}”已在现行内容源消失——请复核该豁免（{src}）")
            sys.exit(1)

    suspect = []
    exempted_ok = []
    for t in titles:
        words = core_words(t)
        if t in outline or any(w in outline for w in words):
            continue
        hit_kw = next((kw for kw in EXEMPTS if kw in t), None)
        if hit_kw:
            exempted_ok.append((t, hit_kw))
        else:
            suspect.append(t)

    print(f"  三时点比对：早期 {len(titles)} 章 → 疑零承接 {len(suspect)} 章；豁免在案 {len(exempted_ok)} 章（豁免表 {len(EXEMPTS)} 条，防腐烂校验通过）")
    for t in suspect:
        print(f"    [未豁免疑丢失]“{t}”")

    if suspect:
        print(f"第二十件：FAIL——{len(suspect)} 章曾为章、现行零承接且未豁免（须登记或回写）")
        sys.exit(1)
    print("第二十件：PASS——无未豁免的静默丢失章（88 三时点比对法固化判据）")
    sys.exit(0)


if __name__ == "__main__":
    main()
