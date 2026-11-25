# ref-fbsd-handbook-mac 登记卡（V61 b016 新登记：FreeBSD Handbook《Mandatory Access Control》章）

- **来源**：The FreeBSD Project. Mandatory Access Control[EB/OL]. FreeBSD Handbook, Chapter 19[2026-11-25]. https://docs.freebsd.org/en/books/handbook/mac/.
- **性质**：FreeBSD 官方手册 MAC 章（MAC 与 DAC 的分野、可装载策略模块与 MLS 组合、root 约束的实际边界），official_doc 类。
- **取文途径**：docs.freebsd.org 经 curl 直取全文（133 507 字节 HTML，剥标签后 57 669 字节，2026-11-25）。
- **四键查重**：source_url（docs.freebsd.org/en/books/handbook/mac/，库内无命中）；题名（库内无命中）——新登记。
- **tier 依据**：official_doc／source_tier=primary；块内 claim 取 L3（官方手册文书）。
- **用途**：V61 b016（2.5.3 叠加顺位、2.5.4 策略组合、2.5.5 超级用户上限）。

## 逐字引文池（供本批取用，均取自上述 Handbook 章正文；空白归一照录）

1. [2.5.3 用] This is in contrast to the default security mechanism of Discretionary Access Control (DAC) where enforcement is left to the discretion of users.
2. [2.5.4 用] Perhaps the best use of the policy modules is to load several security policy modules at a time in order to provide a MLS environment.
3. [2.5.5 用] The root user can still change the security enforcement and edit its configuration files.

- 原页 19.1 节含弯撇号（如 `UNIX®`、章节交叉引用 “Access Control Lists”），引文池三条均为无特殊引号的陈述句；空白按归一连续照录。
