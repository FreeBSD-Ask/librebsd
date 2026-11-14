# USENIX 2001 FREENIX kqueue 论文页卡：完整论文的轨道刊载

> 用途：V67.2.3.1“kqueue 设计文档的会议首发”内容补证（V67 补证批 b017，第二源）。

## 一、著录

Jonathan Lemon. Kqueue: A generic and scalable event notification facility[EB/OL]. 2001[2026-11-14]. https://www.usenix.org/legacy/events/usenix01/freenix01/lemon.html.

- 责任者：Jonathan Lemon（FreeBSD Project）
- 载体：2001 FREENIX 轨道论文摘要页（web；USENIX legacy 存档）
- `source_tier=primary`（学会官方存档页，一手）
- 访问日：2026-11-14

## 二、逐字引文（英文，未翻译）

标题与作者行：

> Kqueue: A generic and scalable event notification facility
> Jonathan Lemon, FreeBSD Project

页头：

> 2001 FREENIX Track Technical Program - Abstract

全文链接：full_papers/lemon/lemon.pdf（PDF 已另行下载，104,951 B）。

## 三、摘要逐字（英文，未翻译；b019 批补录）

> Applications running on a UNIX platform need to be notified when some activity occurs on a socket or other descriptor, and this is traditionally done with the select() or poll() system calls. However, it has been shown that the performance of these calls does not scale well with an increasing number of descriptors. These interfaces are also limited in the respect that they are unable to handle other potentially interesting activities that an application might be interested in, these might include signals, file system changes, and AIO completions. This paper presents a generic event delivery mechanism, which allows an application to select from a wide range of event sources, and be notified of activity on these sources in a scalable and efficient manner. The mechanism may be extended to cover future event sources without changing the application interface.

（摘要由页面正文提取；与 PDF 版摘要一致，连字归一同 PDF 卡说明。）

## 三、核对记录

- 论文页属 2001 FREENIX 轨道技术议程——题面“2001 年 FREENIX 轨道再出完整论文”直证；轨道属 2001 USENIX 年会（6 月 25–30，波士顿，见技术议程页 technical.html）。
- 摘要首句以 select()／poll() 的不可扩展性为问题起点（2.3.2 题面），本批未取，留姊妹题。
- 论文 PDF 全文 grep “bsdcon” 零命中——论文本身不自证 BSDCon 2000 早版；早版事实由 ref K（作者自述）承担。
- 条目细节（Kernel 分场 2001-06-29、主席 Drew Gallatin）见 technical.html 议程页，卡内核对记录，本批引文面取论文页页头。
