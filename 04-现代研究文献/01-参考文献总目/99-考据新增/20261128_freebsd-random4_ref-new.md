# 卡片草稿：FreeBSD random(4) 熵设备

- 题名：random(4) — the entropy device
- 作者／机构：The FreeBSD Project（Mark R V Murray 等携功）
- 出版者／站点：man.freebsd.org（FreeBSD 15.1-RELEASE）
- 出版年：2025（页脚 FreeBSD 15.1 August 28, 2025）
- URL：https://man.freebsd.org/cgi/man.cgi?query=random&sektion=4&manpath=FreeBSD+15.1-RELEASE
- 引用格式（GB/T 7714-2015）：FreeBSD Project. random(4) — the entropy device[EB/OL]. FreeBSD 15.1-RELEASE, 2025-08-28. https://man.freebsd.org/cgi/man.cgi?query=random&sektion=4&manpath=FreeBSD+15.1-RELEASE [2026-11-28].
- 引文摘录："The kern.random.harvest.mask bitmask is used to select the possible entropy sources."
- 引文摘录二："The generator will start in an unseeded state, and will block reads until it is seeded for the first time."
- 引文摘录三："A random device appeared in FreeBSD 2.2. ... In FreeBSD 11.0, the Fortuna algo- rithm was introduced as the default. In FreeBSD 12.0, Yarrow was removed entirely."
- 引文摘录四："The kern.random.nist_healthtest_enabled tunable can be used to enable the entropy source health tests outlined in section 4 of NIST Special Publica- tion 800-90B."
- 引文摘录五："... FreeBSD auto- matically saves some entropy data in /boot/entropy for the loader(8) to provide to the kernel."
- 备注：HISTORY 载 Yarrow（5.0）→Fortuna（11.0 默认）→Yarrow 移除（12.0）；本批 2.11 五题引文均出自该页；快照由 tvly extract --extract-depth advanced 取得，DESCRIPTION／HISTORY／SECURITY CONSIDERATIONS 各节齐。
