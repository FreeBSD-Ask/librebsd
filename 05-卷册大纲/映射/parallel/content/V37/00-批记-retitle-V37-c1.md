# V37 批记 retitle-V37-c1（第 1 章 65 题改题＋迁移）

- **批次**：`retitle-V37-c1`｜2026-11-27｜G4 全责线（162 v5.0 组四）
- **范围**：第 1 章“FreeBSD 存储体系：从 4.2BSD FFS 到 OpenZFS 时代（1993–2026）”13 节 65 题全数重拟；58 件 filled（迁移保块零内容改）＋7 件 skeleton，改名保状态，H1 同步。
- **拟题依据**：节题构式＋thesis＋实义锚（柱面组／超级块／UFS1／UFS2／inode／软更新／fsck／GEOM／provider／CAM／SCSI／ATA／NVMe／RAID／GELI／ZFS／OpenZFS／CDDL／GPL／devfs／mdconfig／tmpfs／sendfile／VFS／vnode／Gibbs／i386／13.x）。

## 一、分布自检（章级 65 题）

| 指标 | 实测 | 判据 |
| ---- | ---- | ---- |
| 冒号 | 0 | 六规则 1 |
| 问句 | 0 | 六规则 5 |
| 题长 | 8—17 字（去空格）；8—12 字 38 席（58.5%） | 六规则 2 burstiness＋C8e |
| 含“的”题 | 0/65 | 六规则 4＋C8d |
| 三并列 | 1（1.6.5 换盘经降级、重建与校验） | 六规则 3 |
| 尾簇 | 全卷 ≤3（预检改 10 题尾词后复检 0 超限） | C8b |
| 构式 | 逐节各异（13 节各 5 席） | 六规则 6 |

## 二、预检与返工

- **尾簇预检**：首稿 7 簇超限（校验×4、对照×4、接入×4、维护×4、惯例×4、决策×4、节点×4），落盘前改 7 题尾词；复检 0 超限。
- **C8e 预检**：首稿 8—12 字 41/65（63.1%），加长 3 题后 38/65（58.5%），全卷 8—12 字比 87.8%→87.8%（旧题存量主导，卷级待后续章批继续压降）。
- **呈审件**：`title-design/retitle/V37-c1-呈审-20261127.md`（逐题旧题→新题＋分布自检）。

## 三、迁移与再生

- **台账**：`title-design/V37.tsv`、`design/V37.tsv`、`design/fragments/V37.tsv` 各 65 行标题改；`design/V37-C2.tsv` 同步 129 行；`title.ok`／`land.ok` 重签（ledger 指纹 `2973c6a389c66350…`）；`approvals` 追加一行（supersedes 前批准指纹 `d764a071665193e5`）。
- **树件**：65 件改名＋H1 同步；58 件 filled 保块零内容改；7 件 skeleton 改名保状态。
- **再生**：`premerge_keyguard` PASS → `merge_subsections --vols 37`（outline 65 行改）→ `assemble_index`；SUMMARY V37 卷块 65 行改。

## 四、门禁（2026-11-27 实测）

- 第三十九件：47 项 FAIL 0（C8b／C8e 均 PASS；V37 零）。
- 第四十一件：FAIL 2＝V01 他线（CP/M 全角）；V37 0。
- 第三十七件 19/19 PASS；第三十八件 3/3 PASS；第三十五件 exit 0（V37 零）；第三十四／三十三件 PASS。
- 第二十四件 V37 0（他线 8 处）；第二十八件 0。
- 下一页：ch1 填充批（7 题：1.10.4／1.10.5／1.11.5／1.13.2—1.13.5）；章骨架清零后与 ch13 一并进入三章批队列（继 ch2）。
