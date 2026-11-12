# FreeBSD geli(8) 手册页（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=geli&sektion=8&manpath=FreeBSD+15.1-RELEASE+and+Ports.quarterly
- 抓取日期：2026-11-12
- 抓取方式：exa 服务端渲染（本机直连该站超时）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.1.6.2“GELI 的密钥层级”补证（D2 块，ref_id 见库）

## 抓取正文（节选）

```
GELI(8) 		     System Manager's Manual		      GELI(8)

NAME
     geli -- control utility for the cryptographic GEOM class

SYNOPSIS
     To compile GEOM_ELI into your kernel, add the following lines to your
     kernel configuration file:

	   device crypto
	   options GEOM_ELI

     Alternatively, to load the GEOM_ELI module at boot time, add the following
     line to your loader.conf(5):

	   geom_eli_load="YES"

DESCRIPTION
     The geli utility is used to configure encryption on GEOM providers.

     The following is a list of the most important features:

	   *   Utilizes  the  crypto(9) framework, so when there is crypto hard-
	       ware available, geli will make use of it automatically.
	   *   Supports  many  cryptographic  algorithms   (currently	AES-XTS,
	       AES-CBC, and Camellia-CBC).
	   *   Can  optionally	perform data authentication (integrity verifica-
	       tion) utilizing	one  of  the  following  algorithms:  HMAC/SHA1,
	       HMAC/RIPEMD160, HMAC/SHA256, HMAC/SHA384 or HMAC/SHA512.
	   *   Can  create  a  User  Key from up to two, piecewise components: a
	       passphrase entered via prompt or read from one or more passfiles;
	       a keyfile read from one or more files.
	   *   Allows encryption of the root partition.  The user is  asked  for
	       the passphrase before the root filesystem is mounted.
```

## 说明

节选 NAME／SYNOPSIS（编译与模块装载段）与 DESCRIPTION 特性清单前五项；主密钥／用户密钥派生细节与其余选项未引。抓取件保留手册页原始换行与缩进。
