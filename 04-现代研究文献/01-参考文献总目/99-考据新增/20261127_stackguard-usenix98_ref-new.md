# 卡片草稿：StackGuard（USENIX Security 1998）

- 题名：StackGuard: Automatic Adaptive Detection and Prevention of Buffer-Overflow Attacks，第 3.1 节 Detecting Return Address Change Before Return
- 作者／机构：Crispin Cowan、Calton Pu、Dave Maier、Jonathan Walpole、Peat Bakke、Steve Beattie、Aaron Grier、Perry Wagle、Qian Zhang、Heather Hinton（Oregon Graduate Institute of Science & Technology 等）
- 出版者／站点：USENIX Association
- 出版年：1998（第七届 USENIX Security Symposium，1998 年 1 月 26—29 日，San Antonio, Texas）
- URL：https://www.usenix.org/legacy/publications/library/proceedings/sec98/full_papers/cowan/cowan_html/node5.html
- 引用格式（GB/T 7714-2015）：COWAN C, PU C, MAIER D, et al. StackGuard: automatic adaptive detection and prevention of buffer-overflow attacks[C]//Proceedings of the 7th USENIX Security Symposium. Berkeley, CA: USENIX Association, 1998. https://www.usenix.org/legacy/publications/library/proceedings/sec98/full_papers/cowan/cowan_html/node5.html [2026-11-27].
- 引文摘录："To be effective, detecting that the return address has been altered must happen before a function returns. StackGuard does this by placing a word next to the return address on the stack, as shown in Figure 2. When the function returns, it first checks to see that the canary word is intact before jumping to the address pointed to by the return address word."
- 备注：同文 PDF 抽取存在连字（ﬁ／ﬂ）与脚注插入，故引文以 USENIX 官方 HTML 节页为准；HTML 渲染中“placing a word”处原有一个 canary 链接被抽取器略去，引文照 HTML 快照逐字抄录。作者为 StackGuard 机制的设计者，按当事人论文定级。
