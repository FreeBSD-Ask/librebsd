<!-- 网页存档｜来源：https://lists.freebsd.org/pipermail/freebsd-hackers/2003-July/002102.html｜抓取：2026-11-13｜exa 服务端渲染，HTML 标签剥离 -->

# Announcing DragonFly BSD!（freebsd-hackers，2003-07-16）

发件人：Matthew Dillon（dillon at apollo.backplane.com）；时间：Wed Jul 16 12:42:08 PDT 2003；列表：freebsd-hackers。

## 抓取正文（节选）

```
			    Announcing DragonFly BSD!
			   http://www.dragonflybsd.org/

    Hello everyone!  For the last few months I have been investigating
    and then working on a new approach to the BSD kernel.  This has snowballed
    into a far more ambitious project which is now ready for wider 
    participation.

    It is the intent of this project to take over development of the 4.x tree,
    to move kernel development along an entirely new path towards SMP, and
    to completely rewrite the packaging and distribution system.  We
    eventually intend to backport many FreeBSD-5 features into the new tree,
    but that is not where the initial focus will be.

    The preliminary 'proving' work I have done is now available on the new
    DragonFly site.  You can access it through cvsup or browse it through
    ftp.  This proving work involved implementing much of the earlier UP->SMP
    converstion work that was done when 5.x first branched, but under an
    entirely new mutex-free light weight kernel threading infrastructure.
    It includes the LWKT system, interrupt threads, and pure threads for
    system processes amoung other things.

    For obvious reasons the codebase will only run on i386 for now, and ports
    to other platforms will not happen until the MD infrastructure is cleaned
    up and finalized.  I considered starting with a 5.x base but it is simply
    too heavily mutexed, it was actually faster to start with 4.x and move
    forward rather then to start with 5.x and move backwards.

    I have both UP and SMP builds working in the current codebase.  I believe
    it proves out the core concepts quite nicely and there is much
    more work coming down the pipeline.

    The site is:

	http://www.dragonflybsd.org/

    Hopefully my T1 can handle the cvsup load.  Eventually I'll colocate
    some boxes to deal with that issue.

    For the next few months the project is going to concentrate on low
    level kernel development.  There are still a number of big ticket items
    that have to be accomplished, primarily in converting the I/O path to
    using VM Object/range lists, before work can branch out into other areas.
    I expect the project to start fairly slowly but then for momentum to
    build.

    Anyone interested in working on or discussing the project is welcome!  I
    have created a mailing list server and newsgroup forums and I am working
    on web-accessibility to same for passive listeners.  I will be posting
    periodic updates to freebsd-hackers as well.

    Again, the site is below.  It contains a great deal of documentation
    and other information.  I even have a mascot!  And, hopefully, it will
    all work from outside my LAN :-)

	http://www.dragonflybsd.org/

							-Matt
```

## 用途注记

Task 8.2 G5 · V50.1.3.2“项目意图的三项声明”P2 联网补证（D2 块；公告原文为当事人一手记录）。
