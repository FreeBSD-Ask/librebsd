# 细粒度分析第三轮（fine3b）· 待应用补丁说明

**生成时间**：2026-08-04 03:04（GMT+8）
**状态**：补丁包已构建完毕，因 `05-卷册大纲` 全树被外部进程写锁拦截，待锁释放后一键应用。

---

## 一、本轮"全做"交付内容

用户要求两件事全部完成：
- **(A) 标志特性拆章**：把 NetBSD / OpenBSD / DragonFly / Linux 的标志性特性，像 FreeBSD 那样拆到更具体的技术章。
- **(B) commit_files 体量对比**：补充代码增删规模流动分析。

### (A) 拆章清单（14 章 + 具体特性）

| 章 | 项目 | 拆入特性 |
| --- | --- | --- |
| ch194（OpenBSD-3x 的 pf 防火墙引入） | OpenBSD | pf防火墙 |
| ch198（OpenBSD 安全框架） | OpenBSD | pledge/unveil |
| ch199（OpenBSD 安全框架续） | OpenBSD | pledge/unveil |
| ch200（OpenSSH） | OpenBSD | OpenSSH |
| ch186（NetBSD 与同时期 OS 比较） | NetBSD | kqueue |
| ch182（NetBSD-2.0 的 SMP） | NetBSD | SMP/多核 |
| ch188（NetBSD-10.0 现代硬件） | NetBSD | ARM |
| ch181（NetBSD-9.0 与 ZFS） | NetBSD | ZFS |
| ch220（DragonFly HAMMER1） | DragonFly | HAMMER |
| ch223（DragonFly HAMMER2） | DragonFly | HAMMER |
| ch218（DragonFly LWKT/SMP） | DragonFly | SMP/多核 |
| ch114（Linux eBPF） | Linux | eBPF |
| ch118（Linux KVM） | Linux | KVM |
| ch130（Linux GPU/DRM） | Linux | GPU/DRM |

> 注：DragonFly HAMMER 此前已在 ch104（基础章）出现，本轮进一步在 ch220/ch223（HAMMER1/2 专章）深化；LWKT 实际映射为 DragonFly 的"SMP/多核"特性（ch218）。

### (B) 跨项目文件级变更体量对比（注入 ch254）

- **重要数据说明**：本批数据库 `commit_files` 表的 `additions`/`deletions` 行数列**全为空**（9 个库合计约 6300 万行，入库时未采集行级增删）。
- **替代方案**：以文件级 `status` 占比（A=新增文件 / M=修改 / D=删除）作为代码改动体量的可用代理指标。
- **关键规律**（已聚合验证）：
  - NetBSD 删除占比异常高（57.3% D）——大规模重构/清理特征明显
  - Linux / OpenZFS 修改主导（91.7% / 85.7% M）——成熟项目的增量修补
  - BSD 衍生项目新增占比突出（21.7% A）——外围创新活跃
  - DragonFly / illumos 新增占比高（24.6% / 29.1% A）——年轻项目的快速扩张

---

## 二、锁诊断（环境级，非脚本问题）

- **现象**：对 `05-卷册大纲` 下跨多卷、多章的 `概述.md` 做 `r+` 打开均返回 `PermissionError: [Errno 13] Permission denied`；但目录可新建临时文件，ACL 显示有写权限。
- **结论**：外部进程（疑似 Git 后台索引 / 云同步 / 文件监控）以共享读锁持有整棵大纲树，阻塞所有文件级写入。
- **原则**：未 kill 任何进程，不强行突破锁。采用"补丁包 + 重放脚本"交付，待锁释放后一键落地。

---

## 三、交付物清单

| 文件 | 说明 |
| --- | --- |
| `script/gitrepo_fine3_patch_20260804.json` | 补丁包：14 章深化块（含子标记）+ ch254 status 对比块 |
| `script/_apply_fine3_patch_20260804.py` | 重放脚本：Glob 动态解析路径 + 幂子等幂 + FINE/GITREPO 块挂载 |
| `script/apply_fine3_report_20260804.json` | 最近一次应用尝试报告（15 项全部 LOCKED_WRITE） |

---

## 四、一键应用命令（锁释放后执行）

```bash
cd D:/librebsd
python3 script/_apply_fine3_patch_20260804.py
```

脚本行为：
1. 用 Glob 动态解析每章真实路径（不依赖卷名硬编码，避免错配）。
2. 对每个章检查子标记（如 `<!-- FINE_SP_openbsd_194 v20260804 -->`）是否已存在 —— 已存在则跳过（幂等）。
3. 将块注入到该章已有的 `GITREPO_FINE_BLOCK` / `GITREPO_BLOCK` 内；若无则文末新建 FINE 块。
4. 输出 `apply_fine3_report_20260804.json` 汇总（APPLIED / SKIPPED / LOCKED 计数）。

应用成功后，建议执行后复核（独立重算 tech_features 标记一致性 + 确认新块落地 + 既有块完好），对应 Task #23。
