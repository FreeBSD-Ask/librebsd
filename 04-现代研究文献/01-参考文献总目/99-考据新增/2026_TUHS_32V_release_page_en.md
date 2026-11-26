# TUHS 32V 发行页引用卡

> 用途：V12.4.3 节（BSD 虚拟内存：设计思想与实现机制）五题内容补证（V12 补证批 b051）。TUHS 档案页（机构档案，二手权威）。

## 一、著录

The Unix Heritage Society. 32V[EB/OL]. TUHS Archive（utree 索引页）[2026-11-26]. https://www.tuhs.org/cgi-bin/utree.pl?file=32V.

- 责任者：The Unix Heritage Society（档案维护方）
- 载体：网页索引页（32V 档案目录说明；文件来自 Unix Archive 的 32V 文件夹，Keith Bostic 捐赠）
- `source_tier=secondary_authoritative`（档案机构说明；L3 公开文献记载）
- 访问日：2026-11-26（curl 直取，Mozilla UA 放行）

## 二、逐字引文（英文，未翻译）

32V 移植者与出处（4.3.3B／4.3.5A）：

> 32V Unix was a port of 7th Edition Unix to the VAX by John Reiser and Tom London of Bell Labs.

32V 未用 VAX 虚存、仅换入换出（4.3.2B／4.3.4B）：

> Although 32V provided a Version 7 Unix environment on the VAX, it did not use the virtual memory capability of the VAX hardware, and only provided swapping of running processes.

谱系地位（4.3.6A，商业 Unix 与 BSD 的共同祖先）：

> Despite this, 32V is essentially the original ancestor of all the commercial Unix derivatives and the BSD varieties.

档案来源与捐赠（备选）：

> The files here come from the 32V folder in the Unix Archive, and were donated by Keith Bostic.

## 三、考据说明

1. 32V 页给出三件硬事实：移植者为 Bell 实验室的 John Reiser 与 Tom London（署名分工）；32V 未使用 VAX 虚存硬件能力、只提供进程换入换出（与 3BSD 首加请求调页形成对照）；32V 是商业 Unix 与 BSD 变体的共同祖先（谱系）。
2. 与 TUHS 3BSD 页（ref11236）“3BSD 自 32V 派生、首加虚存／页面置换／按需分页”句并置，构成“32V 无虚存—3BSD 首加虚存”的实现路线对照。
3. L3 纪律：档案机构说明用于版本与技术定位；虚存实现细节须与当事人记述（ref1575 块 7）交叉。
4. 禁引核查：TUHS 公开档案页，`banned_source=0`。
