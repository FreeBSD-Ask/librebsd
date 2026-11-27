# 卡片草稿：OpenBSD elf(5) 的 PT_GNU_RELRO 定义

- 题名：elf(5) — format of ELF executable binary files
- 作者／机构：OpenBSD Project（man 页作者 Jeroen Ruigrok van der Werven）
- 出版者／站点：man.openbsd.org
- 出版年：2022（页脚 OpenBSD-current March 31, 2022）
- URL：https://man.openbsd.org/elf.5
- 引用格式（GB/T 7714-2015）：OpenBSD Project. elf(5): format of ELF executable binary files[EB/OL]. OpenBSD-current, 2022-03-31. https://man.openbsd.org/elf.5 [2026-11-27].
- 引文摘录："The array element specifies the location and size of a part of the memory image of the program that should be made read-only once all immediate relocation processing for the file has been performed."
- 备注：引文为 PT_GNU_RELRO 条目正文；同页 PT_OPENBSD_RANDOMIZE 条目另行说明该随机化区域可与 RELRO 重叠并在置为只读前填充随机数据。
