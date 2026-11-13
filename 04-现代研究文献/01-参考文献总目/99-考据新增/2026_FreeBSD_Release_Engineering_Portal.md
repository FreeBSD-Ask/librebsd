# FreeBSD Release Engineering（FreeBSD 官方文档）引用卡

> 用途：V71.1.6.3／1.6.4／1.6.5 内容补证（G8-S2 V71 b009）。

## 一、著录

FreeBSD Documentation Project. FreeBSD Release Engineering[EB/OL]. FreeBSD Documentation Portal, 2026-08-08[2026-11-13]. https://docs.freebsd.org/en/articles/freebsd-releng/.

- 责任者：FreeBSD Documentation Project（项目官方文档）
- 载体：HTML 文章；`source_tier=primary`（项目官方流程文档，机构自述）
- 访问日：2026-11-13
- 说明：文章描述 FreeBSD 发布工程流程（分支、冻结、合并与发版节奏）；引文照录，页面更新日 2026-08-08。

## 二、逐字引文（英文，未翻译）

主线与 stable 分支的合并等待：

> After a reasonable testing period, changes can then be merged to the stable/ branches. The default minimum timeframe before merging to stable/ branches is three (3) days.

stable 分支累积到发版：

> After several months, and the number of changes in the stable/ branch have grown significantly, it is time to release the next version of FreeBSD.

两年一次的 dot-zero 节奏：

> In between releases from the stable/ branches, approximately every two (2) years, a release will be cut directly from main.

代码冻结对提交的约束：

> The code freeze marks the point in time where all commits to the branch require explicit approval from the FreeBSD Release Engineering Team.

发布后向安全官的交接：

> Roughly two weeks following the release, the Release Engineer updates the Git repository changing the approver from the Release engineering team to the security officer for the releng/13.0 branch.

## 三、考据说明

- 三日最短等待是“合并窗口”的制度表述（1.6.5-A）；“several months”与“every two years”给出两套上游节奏（1.6.4-A、1.6.5-B）。
- 代码冻结期“explicit approval”说明窗口内的普通提交被阻断，是“积压”机制的原文依据（1.6.4-B）。
- 发布后两周交接给安全官，是三方分担中的“项目侧接力”（1.6.3-B）。
- 按 L3 采信：项目官方流程文档，非独立第三方；文中示例版本号（13.0）为文档写作时的示例，不作版本事实引用。
