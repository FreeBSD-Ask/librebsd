---
title: "W_postfix_Architecture_Overview_EBOL_2026-07-19"
source_url: http://www.postfix.org/
download_date: 2026-09-07
---

# W_postfix_Architecture_Overview_EBOL_2026-07-19

来源: http://www.postfix.org/

 

 The Postfix Home Page 

 QUICK LINKS 

      Home   

      Announcements   

  Non-English Info    -->

      Feature overview    

      Web sites (text)   

      Download (source)   

      Mailing lists   

      Press and Interviews   

      Documentation   

      Howtos and FAQs    -->

      Add-on Software   

      Packages and Ports   

      Becoming a mirror site   

  The Postfix Home Page 

    All programmers are optimists   -- Frederick P.
Brooks, Jr.    

  First of all, thank you for your interest in the Postfix project.

  What is Postfix? It is  Wietse Venema's  mail
server that started life at  IBM
research  as an alternative to the widely-used  Sendmail  program.  After eight
years at Google,  Wietse continues to maintain Postfix .  

  Postfix attempts to be fast, easy to administer, and secure.
The outside has a definite Sendmail-ish flavor, but the inside is
completely different.   

  Newsflash  

  SMTP Smuggling Attack: an email spoofing attack was published
a few days before Christmas 2023, before people had an opportunity
to update their Postfix and other mail systems. Updates are now
available for all supported Postfix stable releases. More at   smtp-smuggling.html .   

  A recent twitter post reveals the existence of an exploit for Postfix,
in a collection of what appear to be NSA break-in tools.  

https://twitter.com/JulianAssange/status/850870683831648256 

  This is an exploit for Postfix 2.0 - 2.2, for a bug that was
fixed 11 years ago in Postfix 2.2.11 and later.  

  There was a memory corruption bug in a Postfix workaround for
a Sendmail bug (CERT advisory CA-2003-07, remote buffer overflow
in Sendmail when message headers contain lots of comment text before
or after an email address).  

  Technical details: the Postfix strip_address() function, which 
removes large comments from a mail header, called the printable()
function on a string that wasn't null-terminated. This caused the
printable() function to scribble past the end of malloc()ed memory,
corrupting the memory heap.  

  Running the exploit against Postfix versions less than 11 years
old results in odd-looking email messages in the super-user's
mailbox, and warning messages in the maillog file (warning: stripping
too many comments from address: &lt;long character string&gt;).

 As of July 2015, all supported Postfix releases have new TLS
default settings that no longer enable export-grade ciphers, and
no longer enable the SSLv2 and SSLv3 protocols. These ciphers and
protocols have little if any legitimate use today, and have instead
become a vehicle for downgrade attacks.  See the  announcement  for more.

 Logjam Attack: this has mostly the same countermeasure as FREAK:
disable EXPORT ciphers on the SMTP server side, as described under
the next bullet.  

 FREAK Attack: To protect vulnerable clients execute as root
" postconf smtpd_tls_exclude_ciphers=EXPORT; postfix reload ".
This command removes EXPORT ciphers with opportunistic as well as
mandatory TLS.  The impact of this attack was already low because
each Postfix SMTP server process computes its own own "ephemeral"
RSA key and terminates after a limited time.  

 GHOST Attack: Postfix does not call gethostbyname() since 2005.
There is no Postfix code that invokes this function unless Postfix
is specifically built for operating systems from more than 10 years
ago (this requires the compile-time option " -DNO_IPV6 ").

-->
  About this website  

  This website has information about the Postfix source code
distribution. Built from source code, Postfix can run on UNIX-like
systems including AIX, BSD, HP-UX, Linux, MacOS X, Solaris, and
more.  

  Postfix is also distributed as ready-to-run code by operating
system vendors, appliance vendors, and other providers.  Their
versions may have small differences with the software that is
described on this website.   


