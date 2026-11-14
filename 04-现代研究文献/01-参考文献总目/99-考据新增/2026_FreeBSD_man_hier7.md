# hier(7) — FreeBSD 杂类手册页（文件系统层级索引）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=hier&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.1.1“源码树的目录分层”补证（D2 块）：产物目标树分离（D2 块，ref_id 见库）

## 抓取正文（节选）

```
			       sbin/	   local administration utilities
			       share/	   local architecture-independent files
			       share/doc/  local documentation
			       share/doc/freebsd/
					   articles, books, FAQ,  and  handbooks
					   available from the FreeBSD project
			       share/man/  local manual pages; see man(1)

		obj/	       architecture-specific  target  tree  produced  by
			       building FreeBSD from source; see build(7)
		ports/	       FreeBSD ports collection; see ports(7)
		sbin/	       system daemons and utilities meant for user  exe-
			       cution; see intro(8)
		share/	       architecture-independent files

			       atf/	   scripts  for  the  Automated  Testing
					   Framework; see ATF(7)
			       bhyve/	   bhyve(8) keyboard mappings
			       calendar/   system-wide calendar files; see  cal-
					   endar(1)
			       certs/	   TLS certificates for openssl(1)
			       dict/	   word lists; see look(1)

					   freebsd     FreeBSD-specific   terms,
						       proper names, and jargon
					   web2        words from Webster's Sec-
						       ond International

			       doc/	   miscellaneous documentation
			       dtrace/	   scripts for the Dynamic Tracing  Com-
					   piler; see dtrace(1)
			       examples/   various  examples  for users and pro-
					   grammers
			       firmware/   firmware images  loaded  by	userland
					   programs
			       games/	   ASCII text files used by BSD heritage
					   games, see intro(6)
			       keys/	   known trusted and revoked keys
```

## 引文摘录（空白已归一，供逐字核对）

sbin/ local administration utilities share/ local architecture-independent files share/doc/ local documentation share/doc/freebsd/ articles, books, FAQ, and handbooks available from the FreeBSD project share/man/ local manual pages; see man(1) obj/ architecture-specific target tree produced by building FreeBSD from source; see build(7) ports/ FreeBSD ports collection; see ports(7) sbin/ system daemons and utilities meant for user exe- cution; see intro(8) share/ architecture-independent files atf/ scripts for the Automated Testing Framework; see ATF(7) bhyve/ bhyve(8) keyboard mappings calendar/ system-wide calendar files; see cal- endar(1) certs/ TLS certificates for openssl(1) dict/ word lists; see look(1) freebsd FreeBSD-specific terms, proper names, and jargon web2 words from Webster's Sec- ond International doc/ miscellaneous documentation dtrace/ scripts for the Dynamic Tracing Com- piler; see dtrace(1) examples/ various examples for users and pro- grammers firmware/ firmware images loaded by userland programs games/ ASCII text files used by BSD heritage games, see intro(6) keys/ known trusted and revoked keys
