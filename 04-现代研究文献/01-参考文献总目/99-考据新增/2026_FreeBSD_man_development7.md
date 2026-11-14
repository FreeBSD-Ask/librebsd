# development(7) — FreeBSD 杂类手册页（开发过程导引）（网页抓取件）

- 来源 URL：https://man.freebsd.org/cgi/man.cgi?query=development&sektion=7
- 抓取日期：2026-11-14
- 抓取方式：curl 直取 `format=ascii` 纯文本版（本机直连该站可用）
- 页面版本：FreeBSD 15.1-RELEASE and Ports.quarterly
- 用途：Task 8.2 G4 · V37.6.1.1“源码树的目录分层”／V37.6.7.1“发布工程的职责分区”补证（D2 块）：src 构成两层＋CI 核查（D2 块，ref_id 见库）

## 抓取正文（节选一）

```

     https://docs.FreeBSD.org/en/books/fdp-primer/

     Ports,  described	further  in ports(7), are the way to build, package, and
     install third party software.  To read more, see:

     https://docs.FreeBSD.org/en/books/porters-handbook/

     The last one, src, revolves around the source code  for  the  base  system,
     consisting  of  the kernel, and the libraries and utilities commonly called
     the world.

     The Committer's Guide, describing topics relevant to all committers, can be
     found at:

     https://docs.freebsd.org/en/articles/committers-guide/

     FreeBSD src development takes place in the project-hosted	Git  repository,
     located at:

     https://git.FreeBSD.org/src.git

     The push URL is:

     ssh://git@gitrepo.FreeBSD.org/src.git

     There is also a list of public, read-only Git mirrors at:

     https://docs.FreeBSD.org/en/books/handbook/mirrors/#external-mirrors

     The  `main'  Git branch represents CURRENT; all changes are first committed
     to CURRENT and then usually cherry-picked back to STABLE, which  refers  to
     Git branches such as `stable/14'.	Every few years a new STABLE is branched
     from  CURRENT, with an incremented major version number.  Releases are then
     branched off STABLE and numbered with consecutive	minor  numbers	such  as
     `releng/14.3'

     The  layout  of  the source tree is described in its README.md file.  Build
```

## 抓取正文（节选二）

```

     https://reviews.FreeBSD.org

     Or Github:

     https://github.com/freebsd

     To check the latest FreeBSD build and test status	of  CURRENT  and  STABLE
     branches, the continuous integration system is at:

     https://ci.FreeBSD.org

FILES
     /usr/src/CONTRIBUTING.md		    FreeBSD contribution guidelines
     /usr/src/tools/tools/git/git-arc.sh    Phabricator review tooling
     /usr/ports/devel/freebsd-git-devtools  Phabricator review tooling as a port

EXAMPLES
     Apply a patch from Github pull #1234, using devel/gh:

	   gh pr checkout 1234

     Apply a patch from Phabricator review D1234, using git-arc(1):

	   git arc patch -c D1234

     Apply a manually downloaded git-format-patch(1), draft.patch, from Bugzilla
     or mail:

	   git am draft.patch

     Apply a manually downloaded patch, draft.diff, from Bugzilla or mail:

	   git apply draft.diff

SEE ALSO
     git(1),  git-arc(1),  witness(4),	build(7), hier(7), ports(7), release(7),
     tests(7), locking(9), style(9)
```

## 引文摘录（空白已归一，供逐字核对）

https://docs.FreeBSD.org/en/books/fdp-primer/ Ports, described further in ports(7), are the way to build, package, and install third party software. To read more, see: https://docs.FreeBSD.org/en/books/porters-handbook/ The last one, src, revolves around the source code for the base system, consisting of the kernel, and the libraries and utilities commonly called the world. The Committer's Guide, describing topics relevant to all committers, can be found at: https://docs.freebsd.org/en/articles/committers-guide/ FreeBSD src development takes place in the project-hosted Git repository, located at: https://git.FreeBSD.org/src.git The push URL is: ssh://git@gitrepo.FreeBSD.org/src.git There is also a list of public, read-only Git mirrors at: https://docs.FreeBSD.org/en/books/handbook/mirrors/#external-mirrors The `main' Git branch represents CURRENT; all changes are first committed to CURRENT and then usually cherry-picked back to STABLE, which refers to Git branches such as `stable/14'. Every few years a new STABLE is branched from CURRENT, with an incremented major version number. Releases are then branched off STABLE and numbered with consecutive minor numbers such as `releng/14.3' The layout of the source tree is described in its README.md file. Build

https://reviews.FreeBSD.org Or Github: https://github.com/freebsd To check the latest FreeBSD build and test status of CURRENT and STABLE branches, the continuous integration system is at: https://ci.FreeBSD.org FILES /usr/src/CONTRIBUTING.md FreeBSD contribution guidelines /usr/src/tools/tools/git/git-arc.sh Phabricator review tooling /usr/ports/devel/freebsd-git-devtools Phabricator review tooling as a port EXAMPLES Apply a patch from Github pull #1234, using devel/gh: gh pr checkout 1234 Apply a patch from Phabricator review D1234, using git-arc(1): git arc patch -c D1234 Apply a manually downloaded git-format-patch(1), draft.patch, from Bugzilla or mail: git am draft.patch Apply a manually downloaded patch, draft.diff, from Bugzilla or mail: git apply draft.diff SEE ALSO git(1), git-arc(1), witness(4), build(7), hier(7), ports(7), release(7), tests(7), locking(9), style(9)
