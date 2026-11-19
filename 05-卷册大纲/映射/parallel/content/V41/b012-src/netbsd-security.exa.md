# Security and NetBSD（exa 实取快照）

fetched: 2026-11-19 via exa web_fetch（curl SSL exit 35，同 b012 预备件口径）
url: https://netbsd.org/security/

---

Security and NetBSD

Security issues in NetBSD are handled by three groups: the Security Team, the Security Alert Team, and the Security Officer. These groups investigate, document and update code in response to newly reported security issues.

The NetBSD source tree contains several millions of lines of code written by many different people and organizations with varying styles and quality. Given the rate of change and the amount of human resources available, it is not possible to manually verify every line of code for correctness. To compensate for that the NetBSD Foundation utilizes modern tools and techniques to automatically detect and manually correct bugs as soon as they appear.

Specifically, the NetBSD source tree is periodically analyzed by two separate code scanners to maintain and improve code quality: Coverity - a commercial code scanner, and Brainy - a private code scanner developed by a NetBSD developer.

Several security features are available in NetBSD, including IPsec, a homegrown firewall (NPF), a file integrity system (Veriexec), a kernel authorization framework (kauth(9)), disk encryption (CGD), among others.

In terms of exploit mitigations, NetBSD supports a good number of modern features: W^X (in both userland and the kernel), Userland ASLR, Kernel ASLR, SMEP, SMAP, and a variety of other internal kernel bug detection features. Support for these mitigations sometimes depends on the capabilities of the hardware.

Some advanced internal bug detection features are enabled only during the development process, because they are too costly from a performance point of view. This allows for good quality insurance during development, and at the same time avoids performance overhead in the stable releases.

Other classic secure network services are available, such as SSH (OpenSSH) and Kerberos 5 (Heimdal). All services default to their most secure settings, and no services are enabled by default for new installations.

## Reporting a Security Problem

To report a security problem in NetBSD, please contact the Security Alert Team: <security-alert@NetBSD.org>.

## Security Advisories

When serious security problems in NetBSD are discovered and corrected, we issue a security advisory, describing the problem and containing a pointer to the fix. These are announced to our netbsd-announce mailing list and our security-announce mailing list as well as to various other mailing lists and websites. In addition, they are archived on this site as well as provided as an RSS feed.

Security issues are fixed as soon as possible, and the fixes are propagated to the stable branches as fast as possible. However, when a vulnerability is found during a code audit, or when several other issues are likely to be spotted and fixed in the near future, the security team may delay the release of a Security Advisory, so that one unique, comprehensive Security Advisory covering several vulnerabilities can be issued. Communication with vendors and other distributions shipping the same code may also cause these delays.
