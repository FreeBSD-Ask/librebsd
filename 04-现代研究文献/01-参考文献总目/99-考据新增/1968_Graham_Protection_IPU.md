# Protection in an Information Processing Utility（Graham 1968）

- 来源：https://multicians.org/graham-pipu.pdf
- 作者：Robert M. Graham
- 出处：Communications of the ACM, Vol. 11（multicians.org 扫描本）
- 访问日：2026-11-13
- 用途：Task 8.2 V01-S2 b015，V01.7.2.3 保护环与访问控制（D2 网页条目，1968 年同时代论文）
- 摘录说明：curl 取 PDF 后以 PyMuPDF 抽取文本；扫描 OCR 有断词（如 abil- ity）与误识（如 Indeedj），摘录时仅合并断词、不改字，误识原样保留并在提要注明

## 正文摘录（逐字，断词已合并）

"In a system where users may share data in working memory the ability to have more control over access is essential."

"What is needed is the ability to have a variety of access rights for each separate logical block of information (called a segment)."

"Current machines which have been modified for use in IPUs have hardware features which allow memory to be subdivided into a large number of parts called segments."

"If a program has any privileges it has all. If a program has any access, it has completely unrestricted access."

## 提要

Graham 1968 年记：在用户可共享工作内存数据的系统中，对访问施加更多控制是必要能力；所欠缺的是对每一个独立逻辑信息块（段）分别设定多种访问权限的能力；用于信息处理机（IPU）的改装机器已具备把内存细分为大量“段”的硬件特性。文中并批评既有机制的二值化——有特权即全有、有访问即全无限制——这正是段级权限划分要解决之处。
