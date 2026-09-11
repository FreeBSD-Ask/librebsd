---
chapter: 第 298 章
id: CH298
volume: 第15卷-许可证哲学与法律分析
---

# 第 298 章 gnu操作系统史诞生与工具链构建

## 要点

- linux-kernel 代码仓库共 1,474,341 次提交（1970-01-01 至 2026-08-24；起点系时区边界记录），39,865 位贡献者（contributors 表行数）
| 组合 | 兼容性 | 说明 |
|---|---|---|
| GPLv3 ↔ Apache-2.0 | ✅ 兼容 | Apache-2.0 项目可并入 GPLv3（单向） |
| GPLv3 ↔ GPLv2 | ⚠ 有条件 | “GPLv2 or later” 可升级；“GPLv2 only” 不兼容 v3 |
| GPLv2 ↔ Apache-2.0 | ❌ 不兼容 | Apache-2.0 专利条款与 GPLv2 冲突 |
| LGPL ↔ GPL | ✅ 兼容 | LGPL 库可并入 GPL 项目（§6 可重新许可） |
| LGPL-3.0 → GPLv3 | ✅ 可升级 | LGPLv3+ 可升级为 GPLv3，反之不可 |
| MPL-2.0 ↔ GPL/Apache | ✅ 兼容 | MPL-2.0 文件级 copyleft 可并入 |
| EPL ↔ GPL | ❌ 不兼容 | EPL-1.0 明确不兼容 GPL |
| CDDL ↔ GPL | ❌ 不兼容 | CDDL 与 GPL 互斥 |
| OpenSSL 双许可 ↔ GPL | ❌ 不兼容 | 广告条款残留——LibreSSL fork 动因 |

（表源：298.7.2 许可证兼容性矩阵）


## 史料

- [DB:references_fulltext:chapter_matches:chmatch_3984] 卷“第15卷-许可证哲学与法律分析”第 298 章，匹配置信度 folder，原因：folder 第296章
- [DB:bsdnow_podcast:outline_mappings:om_10484] BSD Now 第 665 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10548] BSD Now 第 654 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10585] BSD Now 第 646 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10647] BSD Now 第 637 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_10779] BSD Now 第 617 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11153] BSD Now 第 571 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11216] BSD Now 第 563 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11367] BSD Now 第 546 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11446] BSD Now 第 536 期，匹配 CH298 章，关联度 1.0
- [DB:bsdnow_podcast:outline_mappings:om_11545] BSD Now 第 526 期，匹配 CH298 章，关联度 1.0

## 史观

(待人工回填——详见子节文件史观/辨析字段)

## 辨析

- 贡献者高度集中——Top 1 贡献者 Linus Torvalds 占比 33.2%，需考量‘个人主导’与‘社区协作’的叙事张力
- 许可证兼容性是单向的（如 GPLv3 ↔ Apache-2.0 仅 Apache→GPLv3 可行）；引用须以 FSF 官方列表为准 [考据完成：2026-08-04]

## 文献

- FSF License List；各许可证文本 ［A］<!-- NEWREF:2411 -->

