# audit.log(5) — FreeBSD 文件格式手册页（BSM 审计日志格式）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=audit.log&sektion=5
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.5.2.2“审计日志的记录格式”补证（D2 块）：BSM 令牌流定性（D2 块，ref_id 见库）

## 抓取正文（节选）

```
AUDIT.LOG(5)		       File Formats Manual		    AUDIT.LOG(5)

NAME
     audit -- Basic Security Module (BSM) file format

DESCRIPTION
     The  audit  file  format is based on Sun's Basic Security Module (BSM) file
     format, a token-based record stream to represent system audit  data.   This
     file format is both flexible and extensible, able to describe a broad range
     of  data  types, and easily extended to describe new data types in a moder-
     ately backward and forward compatible way.

     BSM token streams typically begin and end with a "file" token,  which  pro-
     vides  time stamp and file name information for the stream; when processing
     a BSM token stream from a stream as opposed to a single file  source,  file
     tokens  may  be seen at any point between ordinary records identifying when
     particular parts of the stream begin and end.  All other tokens will appear
     in the context of a complete BSM audit record, which begins with a "header"
     token, and ends with a "trailer" token, which describe  the  audit  record.
     Between  these  two  tokens  will	appear a variety of data tokens, such as
     process information, file path names, IPC object information,  MAC  labels,
     socket information, and so on.

     The  BSM  file  format  defines specific token orders for each record event
     type; however, some variation may occur depending on the  operating  system
     in use, what system options, such as mandatory access control, are present.

     This  manual page documents the common token types and their binary format,
     and is intended for reference purposes only.  It is recommended that appli-
     cation programmers use the libbsm(3) interface to read  and  write  tokens,
     rather than parsing or constructing records by hand.

   File Token
     The  "file"  token is used at the beginning and end of an audit log file to
     indicate when the audit log begins and ends.  It  includes  a  pathname  so
     that,  if concatenated together, original file boundaries are still observ-
     able, and gaps in the audit log can be identified.  A "file" token  can  be
```

## 引文摘录（空白已归一，供逐字核对）

AUDIT.LOG(5) File Formats Manual AUDIT.LOG(5) NAME audit -- Basic Security Module (BSM) file format DESCRIPTION The audit file format is based on Sun's Basic Security Module (BSM) file format, a token-based record stream to represent system audit data. This file format is both flexible and extensible, able to describe a broad range of data types, and easily extended to describe new data types in a moder- ately backward and forward compatible way. BSM token streams typically begin and end with a "file" token, which pro- vides time stamp and file name information for the stream; when processing a BSM token stream from a stream as opposed to a single file source, file tokens may be seen at any point between ordinary records identifying when particular parts of the stream begin and end. All other tokens will appear in the context of a complete BSM audit record, which begins with a "header" token, and ends with a "trailer" token, which describe the audit record. Between these two tokens will appear a variety of data tokens, such as process information, file path names, IPC object information, MAC labels, socket information, and so on. The BSM file format defines specific token orders for each record event type; however, some variation may occur depending on the operating system in use, what system options, such as mandatory access control, are present. This manual page documents the common token types and their binary format, and is intended for reference purposes only. It is recommended that appli- cation programmers use the libbsm(3) interface to read and write tokens, rather than parsing or constructing records by hand. File Token The "file" token is used at the beginning and end of an audit log file to indicate when the audit log begins and ends. It includes a pathname so that, if concatenated together, original file boundaries are still observ- able, and gaps in the audit log can be identified. A "file" token can be
