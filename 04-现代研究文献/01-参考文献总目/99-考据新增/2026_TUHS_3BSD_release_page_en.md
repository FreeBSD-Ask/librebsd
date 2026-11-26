# TUHS 3BSD 发行页引用卡

> 用途：V12.4.1 节（UNIX／32V 与 Berkeley 的 VAX 计算环境）五题内容补证（V12 补证批 b049）。TUHS 档案页（机构档案，二手权威／L5 档案标识）。

## 一、著录

The Unix Heritage Society. 3BSD[EB/OL]. TUHS Archive（utree 索引页）[2026-11-26]. https://www.tuhs.org/cgi-bin/utree.pl?file=3BSD.

- 责任者：The Unix Heritage Society（档案维护方）
- 载体：网页索引页（3BSD 档案目录说明；文件来自 3bsd.tar.gz，Kirk McKusick 捐赠）
- `source_tier=secondary_authoritative`（档案机构说明，非当事人证词；L5 档案标识用于版本与来源判定）
- 访问日：2026-11-26（curl 直取，Mozilla UA 放行）

## 二、逐字引文（英文，未翻译）

VAX 平台首发（4.1.1B）：

> 3BSD was the first Berkeley Software Distribution to run on the 32-bit VAX platform.

32V 派生与虚存首发（4.1.2B／4.1.3B）：

> Derived from 32V, 3BSD was the first Unix system to add virtual memory, page replacement and demand paging to Unix.

档案来源与捐赠（4.1.5B／4.1.6A）：

> The files here come from 3bsd.tar.gz, and were donated by Kirk McKusick.

延伸阅读指向（4.1.6 备选）：

> For more information about 3BSD, see Twenty Years of Berkeley Unix by Kirk McKusick.

## 三、考据说明

1. TUHS 档案页是 3BSD 版本身份（首个 VAX 发行、32V 派生、虚存／页面置换／按需分页首发）的机构性表述，与 McKusick《Twenty Years of Berkeley Unix》（ref1575 全文块）互证。
2. 档案实体（3bsd.tar.gz）由 Kirk McKusick 捐赠——档案出处链的终点在案，可用于 4.1.6“装机叙述的档案出处”。
3. L5 纪律：档案机构说明用于版本与来源判定；技术史细节（如虚存实现）须与当事人记述（ref1575 块 7）交叉。
4. 禁引核查：TUHS 公开档案页，`banned_source=0`。
