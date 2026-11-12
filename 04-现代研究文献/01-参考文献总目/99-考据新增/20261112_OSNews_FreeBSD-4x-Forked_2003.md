<!-- 网页存档｜来源：https://www.osnews.com/story/4058/freebsd-4x-forked-into-dragonfly/｜抓取：2026-11-12｜HTML 标签剥离与空白归一 -->

# FreeBSD 4.x Forked Into DragonFly（OSNews, 2003-07-17）

FreeBSD 4.x Forked Into DragonFly – OSnews
Popular Topics:
Home
Originals
Sponsorship
Submit News
Contact
Home
Originals
Sponsorship
Submit News
Contact
Popular Categories
Windows
Linux
Apple
General Development
Wireless
OS News
Hardware
macOS
Legal
Microsoft
Home
>
FreeBSD
>
FreeBSD 4.x Forked Into DragonFly
FreeBSD 4.x Forked Into DragonFly
Submitted by RJW & Jon
2003-07-17
FreeBSD
51 Comments
DragonFly
is an operating system and environment designed to be the logical continuation of the FreeBSD-4.x OS series. Prominent
former
FreeBSD developer Matthew Dillon is a major player in the development. According to the website, DragonFly gives “
the BSD base an opportunity to grow in entirely new direction from the one taken in the FreeBSD-5 series
.”
About The Author
Adam Scheinberg
Technology Executive • Web Developer • Father • Foodie • Music Snob • OS enthusiast
Follow me on Mastodon
@
[email protected]
51 Comments
2003-07-17 1:40 am
Anonymous
is this new direction?
2003-07-17 2:10 am
Anonymous
Well, apparently you didn’t even bother to check the website. I mean, I don’t care much about BSD and yet another fork is not something I give a damn about, but Dillon appears to address your concerns
http://www.dragonflybsd.org/Goals/
“> .
2003-07-17 2:38 am
Anonymous
“DragonFly” these *BSD people surely come up with cool names. Nothing beats “Darwin” sounds really mean – hehe.
But sadly the opensource OS with the most dumb looking mascot and the most dumb name rules the show.
2003-07-17 3:00 am
Anonymous
Another healthy fork of BSD? But how can this be? We all
know
BSD is dyi^h^h^h….<squelch />
2003-07-17 3:06 am
Anonymous
Care to explain about this?
http://www.osnews.com/comment.php?news_id=4035
2003-07-17 3:06 am
Anonymous
Another BSD…the more the merrier!!!
Keep up the good work all of you BSDs…you’re all great in your own ways!!!
2003-07-17 3:23 am
Anonymous
This was more than expected, especially with Matt Dillon comming into play
2003-07-17 3:25 am
Anonymous
It’s not dying, it’s resting.
2003-07-17 3:48 am
Anonymous
Who wants to start a “Linux is dying” crapflooding campaign? We’ll see how much they like it!
2003-07-17 3:56 am
Anonymous
Windows is dying
.
PS: Please mod down this “Xxx is dying” threads.
2003-07-17 3:57 am
Anonymous
It’s not dying. It’s… pining for the fjords.
2003-07-17 3:57 am
Anonymous
BSD’s been dying almost as long as Apple has
Yet BeOS lives…computer geeks are strange ones…LOL
(Disclaimer: not meant as a slam to any of the OSes mentioned, this is just a joke, I love ALL OSes in some form)
2003-07-17 3:59 am
Anonymous
There site’s “goals” page isn’t very helpful!
2003-07-17 4:02 am
Anonymous
I am not trying to start trouble but I need someone to clarify something for me. I have been reading all this press on Linux 2.6. What the features/improvements are for desktop and enterprise people, and then recently reading about how Linux will displace UNIX and other variants in the coming future (Not saying I believe this just putting it out there). But the counter argument to this is that Linux is missing a whole bunch of enterprise features that UNIX has (i.e. hot swappable CPU’s or something like that). Now my question is (By the way I am not claiming that Linux is superior or that BSD is or Solaris etc….) being that Linux is a UINX variant and it has so much popularity and momentum, why not just cease innovations/forking in these UNIX variants and just take what makes these UNIX variants so TECHNICALLY great and apply all your energies and make Linux what you want BSD to be. Basically why not just pool your resources and concentrate on one UNIX variant. I am not saying to abandon the others just maintain them until Linux is as powerful as other UNIX OS’s. Or if you wish you can forget Linux as an example and use BSD in place of Linux. Just curious.
2003-07-17 4:12 am
Anonymous
Forks exist because people have different ideas on what the focus should be, and one size fits all usually ends up fitting no one comfortably.
2003-07-17 4:16 am
Anonymous
I agree about the one size fits all problem but thier is not what 4 or 5 or 6 diff versions of BSD doesn’t this slow this downa bit
2003-07-17 4:16 am
Anonymous
The primary goal seems to be to move the kernel to a very microkernel-like message passing architecture. System calls have been replaced with messages sent from the userspace to the kernel. Messages are used to regulate the caching architecture. The locking model sounds quite interesting as well.
I’ll wish them luck, but this seems in many ways more ambitious than FreeBSD 5.x, and I don’t expect major headway to be made any time in the near future.
2003-07-17 4:21 am
Anonymous
1) Because UNIXs aren’t hemogenous. While the architecture of all thse UNIXs are similar, the actual code is different enough that its almost as much trouble to write a new piece of functionality from scratch as it is to port it from another UNIX.
2) Because not everyone has the same goals. There is no way to get the “ideal” system. There are trade-offs that make different systems more suitable for different tasks. For example, FreeBSD’s uniprocessor performance is still probably the best of the free UNIXs. But its SMP performance pales in comparison to Linux’s. Even something like kernel preemption (which made it into Linux 2.6) is controversial because the server people don’t want to give up throughput to allow the desktop people to have lower latency.
3) Because projects often need to approach something in different ways. DragonflyBSD, in this case, is a drastic rethinking of some core UNIX kernel algorithms. These sweeping changes could not have taken place within the FreeBSD project, because the FreeBSD project is expected to keep releasing stable OSs on a regular schedule, and already has its hands full with the 5.0 codebase.
4) Because people have an established interest in certain OSs.
Right now, IBM couldn’t just give everything up and move all their AIX developers to Linux. They’re contributing a lot of Linux developers, to be sure, and have committed to Linux being their UNIX in the future, but AIX customers will demand support for a long time to come.
5) Because software development just doesn’t work that way. A project has a certain number of participants that leads to optimal development speed. For OSS projects, this number is comparatively smaller than for large commercial projects, because organization is more of a burden in a distrubuted development environment. Once you get past this optimal number of developers, your productivity decreases, because of the coordination requirements between the people. This is also why OSS software tends to be composed of a number of small, independent modules, because that allows different projects to achieve maximum development efficiency. Its all a matter of parallelism (or lack thereof) in the development process. Tannebaum cites an apt quote in Modern Operating Systems — “It takes 9 months to bear a child, no matter how many women you assign to the job.”
2003-07-17 4:32 am
Anonymous
first thanks bascule for summing things up, cause the page did nothing for me in explaining it. There was no simple summary. Also looks like it was made in frontpage in a few minutes, but oh well.
I suppose this fork makes sense, but with what it sounds like their doing it sounds almost like there won’t be much BSD left in it when they are done. I think these forks are ok when they have a much differant goals then others and not a fork for the sack of forking to be cool and have your own OS.
Now how long till someone forks fbsd and intergrates 1 graphical system based on opengl to the core of it with one and only one define GUI, ala a OSX if you will. That would be a nice fork.
2003-07-17 4:34 am
Anonymous
Why in earth is Matt Damon starting a new BSD fork, i am telling you guys after he started thinking he could do intelligent movies he is megalomanic, Boycott Matt Damon !
2003-07-17 4:35 am
Anonymous
BTW this is yet another BSD fork based on the ego of a single hacker who couldn’t get along with the rest of the team. Well some people think OpenBSD is useful so this might not be a bad thing but still shouldn’t we rename the *BSDs into *EGOs.
Imagine if every Linux hacker who gets his patches rejected would start a fork…
2003-07-17 4:40 am
Anonymous
Hmmm. Sounds interesting. Unfortunately, a lot of the Goals section is over my head, not knowing BSD internals. The thing that the micro kernels got right (some would say the only thing) is message passing. It’s nice to see them moving towards better message passing, which IMO is a downfall of the classic unix API.
They talk about having threads move between CPUs as little as possible. I’d like to know how this would affect CPU load balancing on large machines running heavy-duty, multi-threaded programs.
2003-07-17 4:41 am
Anonymous
>ala a OSX if you will. That would be a nice fork.
Not exactly what you want but still very OSXy:
http://simplygnustep.sourceforge.net/
I’m really looking forward to this one.
2003-07-17 4:42 am
Anonymous
Also forks can end up being a good thing. FreeBSD has benefited from both OpenBSD and NetBSD. While I’m no OS expert I feel FreeBSD would not be as good as it is today without NetBSD and OpenBSD. Would the NetBSD people have been able to pursue their interests of portablility? Would stuff like OpenSSH exist if OpenBSD was never forked? No matter the reasons it was forked. The BSDs regularly merge stuff from one another that they find useful. What makes you think, that if the devs all worked under one roof that they would have been free to do what they wanted? Instead being forced code what the other devs felt were within the goals of FeeBSD. For that matter can’t what you asked be applied to anything? Why create any other chip architecture other than x86? Why have all those engineers waste millions of man hours developing PPC, Sparc, Alpha or Itanium? When they could devote all their skills and talent into making x86 the be all and end all of chips?
2003-07-17 4:47 am
Anonymous
Well said.
2003-07-17 5:03 am
Anonymous
Isn’t it sounds similar to Amiga’s stuff for the messaging layer? I think, I read Amiga somewhere about messaging layer, so I might be wrong.
2003-07-17 5:18 am
Anonymous
BTW this is yet another BSD fork based on the ego of a single hacker who couldn’t get along with the rest of the team.
Matt Dillon talked about forking 4.x way back when 5.x was in planning stages. He didn’t like the direction they were taking it. I don’t know that much about why he lost commit priveleges, nor do I care. But I think he’s doing this because he has some ideas he wants to work on and the FreeBSD project isn’t going the direction to allow that. I don’t think it’s purely an ego thing.
2003-07-17 5:48 am
Anonymous
You mean “EXACTLY my way or no way” isn’t an ego thing?! “Compromise” seems to be an unknown term in the *BSD world.
2003-07-17 6:13 am
Anonymous
Considering the amount of egos involved in the creation of the BSDs, having only four BSD is a strong indication that BSD developers indeed can compromise.
No, the important point is that the four BSDs pursue goals which are not just different, but in part simply incompatible, regardless of the egos involved, so that a separation of the different projects is necessary.
Not like Linux, where everybody and their dog seems to have their own distro just because they can.
2003-07-17 6:16 am
Anonymous
“Imagine if every Linux hacker who gets his patches rejected would start a fork… ”
I think in the Linux world you would do a distro. From what I gather the kernel’s and other parts of the OS in the most populair distro’s are not GNU standard and can differ a lot between the distro’s.
2003-07-17 6:30 am
Anonymous
You mean “EXACTLY my way or no way” isn’t an ego thing?! “Compromise” seems to be an unknown term in the *BSD world.
I don’t really know what you’re talking about. Like I said, I don’t really care. I’ve followed the FreeBSD lists for years, and I never knew him to say what you’ve quoted. Could be I wasn’t paying attention that closely. I also never said this new BSD isn’t an ego thing. Reread what I said. I said I don’t think it’s “purely” ego. But this is also about implementing new ideas.
2003-07-17 6:53 am
Anonymous
“Isn’t it sounds similar to Amiga’s stuff for the messaging layer? I think, I read Amiga somewhere about messaging layer, so I might be wrong.”
I found this comment on slashdot:
“Matt Dillon’s early background as an Amiga programmer is really showing through here. He’s basically proposing doing a piecewise conversion of BSD to an Amiga-style message-passing operating system.
He’s basically doing the reverse of what so many folks (NeXT, HURD) have done or tried to do.. not taking a microkernal and putting a UNIX layer over it, but taking a UNIX and scooping out the inside to replace it with a message-passing microkernal.
This will definitely be a fun one to watch. Go, Matt, go.”
Read the article here:
http://bsd.slashdot.org/article.pl?sid=03/07/16/217259&mode=nested&
…
2003-07-17 6:54 am
Anonymous
Slackware Linux is 10 years old!!!
Happy birthsday!!!
HAIL B0B!!!
http://www.slackware.com
Get the latest current and have fun!!!
2003-07-17 7:06 am
Anonymous
Has anyone used this??
http://templeofhate.com/tglaser/MirBSD/
2003-07-17 7:09 am
Anonymous
That link is something that crashes IE….
Internet Explorer sux anyway…lol…
2003-07-17 7:19 am
Anonymous
reading over his site, it seems very interesting indeed! and reading his diary page shows a lot of headway has been made already in regards to turning it in a lightweight kernel threading and message passing.
i think this will be one to keep an eye of, if it keeps going the way it is.
yes.. very interesting!
2003-07-17 7:40 am
Anonymous
for those that dont wade/chew through slashdot, here is a message from matt on the messaging.. pretty interesting.
———————-
There are many Amiga-like concepts incorporated into the model, and plenty of new stuff as well. The Amiga had a highly optimal messaging system oweing to the fact that it ran on such a slow cpu making every cycle golden. Two features have been taken from the Amgia I/O model. First, the idea that the target can choose to perform an operation synchronously or asynchronously entirely independant of the type of operation the client has requested. In the Amiga model the client passes a hint which the target may choose to act on or choose to ignore and so do we.
Another feature taken from the Amiga I/O model (for those who ever looked at the actual assembly code) is the ability to short-cut queueing operations. For example, if the target is able to execute a message synchronously regardless of what the client requested, the target can execute the message in the client’s context and return a synchronous result code without even bothering to queue the message (I/O request in Amiga terminology). Likewise, if the client wants to run an operation synchronously and the target decides to run it asynchronously the target doesn’t have to queue the message back to the client’s reply port when it is through, it simply wakes the (blocked) client up.
To make messaging truely efficient the ‘optimal’ case must have the lowest possible overhead. The Amiga model serves this requirement very nicely, making optimally handled messages take no more overhead then a subroutine call would take. This is extremely important in an MP design because queueing operations often require some sort of lock and being able to avoid a queueing operation in the optimal case is simply *HUGE*.
Consider the optimal syscall path given the above. If a syscall can run without blocking your syscall ‘message’ winds up costing no more then a traditional syscall would. After all, there is no point asynchronizing a syscall that can run without blocking, you only have one cpu for any given userland thread anyway so you can’t make things faster by switching out to handle something else and then back again. Yet in a traditional asynchronizing model like AIO, a great deal of effort and overhead is taken before you even know whether the I/O operation would block or not, making AIO expensive no matter how you cut it. The same goes with a select() based operation. And in a KSE style operation the expense occurs in having to maintain multiple kernel threads for system calls which are in-progress, instead of much smaller message structuers for system calls which are in-progress. The above Amiga-like features make it possible to encapsulate *ALL* system calls in messages, request asynchronous completion, yet still deal with synchronous completion in a manner which does not introduce a performance penalty
—————-
2003-07-17 8:22 am
Anonymous
All this microkernel talk reminds me of:
http://www.mklinux.org/
-magg
2003-07-17 11:40 am
Anonymous
Though I’m a NetBSD user, the texts on dragonflybsd.org deeply impressed me, since they describe exactly what needs to be done to make Unix into something better (IMHO).
This is very exciting. More power to Matt & Co.!!
2003-07-17 11:49 am
Anonymous
Nice to see Matt returning (in a sense) to his Amiga roots
I’ll be keeping an eye on this.
(For info, Matt wrote the DICE C development environment a fairly slick and professional but free/low-cost alternative to something like SAS/C or StormC.)
2003-07-17 11:50 am
Anonymous
This is the most interesting development for a long time. I am not a BSD user except on my firewall, but something like this might make me switch from Linux.
But this is a very radical change. Wouldn’t that require major userspace modifications?
I will keep an eye on this project.
2003-07-17 12:36 pm
Anonymous
I really like the mascot they chose. I think the Dragon fly represents the ultimate in speed and robustness, all the features that Matt is looking to incorporate into DragonFlyBSD.
As with all the Linuxes I am a firm believer that the reason why Linux isn’t more widely used and accepted (than it already is) is because there are so many of them to chose from, with little standards to unite them (packages, directory structure, etc). I hope this doesn’t become the case with the *BSDs because I feel that the BSDs are much more mature operating systems than Linux every will be and I hope that maturity isn’t lost.
I wish Matt luck!
– J
2003-07-17 12:40 pm
Anonymous
To everyone who was trying to “debunk” me… hello… I am on your side. It’s a joke. An attempt at irony, but never mind.
As I was trying to point out, another fork of BSD could be quite a healthy thing, giving certain people the opportunity to try some more radical changes that would never make it into the conservative FreeBSD code tree.
2003-07-17 1:35 pm
Anonymous
“Slackware Linux is 10 years old!!! ”
Slackware – the most BSD-like Linux around.
2003-07-17 2:25 pm
Anonymous
What if there’s a diaspora (say, for example, interstellar flight becomes a reality?) We ain’t all going to the same place.
When I see questions like these, I’m always reminded of the time QNX challenged the Linux developers to get Linux to run on a single floppy like they had done. On the advocacy page, I saw a lot of posts to the effect that taking the challenge wasn’t worthwhile. I answered it this way:
Linux is for everyone, and we can do with it what we will (within the limits of the licences, of course.) But it’s there for all of us. If something can be done, why *shouldn’t* we do it? Maybe we and the folks working on QNX can learn from each other.
Well, that was just before the Embedded Linux movement got going.
Anyway, I’d love to see another BSD fork. Hopefully, the developers in that new fork remain true to the idea of sharing ideas, too. If they take a direction that the current FreeBSD people won’t take, then later on both groups might be able to learn something from one another.
…and don’t forget, where there are forks, there are also merges. Think about corn.
2003-07-17 2:46 pm
Anonymous
…kinda looks like they’re going to build an OS that’s a cross between the mach unix system and NT.
I like some of the ideas,but I’m always skeptical of the hardware abstraction layer thingy. I happen to be into audio stuff (music composition, in particular.) For folks like me, there are always times when I want that “pedal-to-the-metal” performance that you can’t get with anything like a real-time OS. The Linux folks seem to be getting to the point where almost-real-time access is possible from user space (for applications like, for example, CSOUND, where I want to get a software synth to respond immediately o the keyboard, while at the same time running effects like echo and reverb.)
Musicians often don’t have a lot of money to spend; having this kind of bare-metal control in a free OS could be important to us.
2003-07-17 2:49 pm
Anonymous
“Nice to see Matt returning (in a sense) to his Amiga roots
I’ll be keeping an eye on this.”
Well…made a fool out of me! I guess if this guy has Amiga roots, I should be expecting to be a-rockin’ and a-rollin’ soon…..
2003-07-17 4:03 pm
Anonymous
So long as Dragonfly remains similar enough to the other *BSDs, it and the BSDs will benefit from each other. However, changing to a message-passing architecture for the VFS and other sys-calls strikes me as a very significant difference.
That’s not to say that Dragonfly diverging from the *BSDs is a bad thing. As long as the userland APIs remain similar (to either Linux or the FreeBSD’s), it will be able to benefit from Open Source packages , and the venue it presents for new ideas will help inspire the *BSDs (and Linux, I would hope) to better things. That kind of thing already helps both the *BSDs and Linux.
In fact, if Dragonfly does become successful, it should only help Linux by reminding the Linux community that there are successors chasing after it, should it falter.
B.T.W.: I use FreeBSD and Solaris professionally, and FreeBSD to manage a home network / file system with Samba and CUPs. The home FreeBSD box is an ancient Pentium/120Mhz CPU that serves files up quite nicely, and only takes a day to do a “make buildworld – mergemaster – make installworld – make kernel” sequence 😉
One Last Thing: The above seems very Pollyannish, doesn’t it.
2003-07-17 5:37 pm
Anonymous
I happen to be into audio stuff (music composition, in particular.) For folks like me, there are always times when I want that “pedal-to-the-metal” performance that you can’t get with anything like a real-time OS. The Linux folks seem to be getting to the point where almost-real-time access is possible from user space (for applications like, for example, CSOUND, where I want to get a software synth to respond immediately o the keyboard, while at the same time running effects like echo and reverb.
A HAL and a low-latency sound interface are not mutually exclusive.
Unfortunately FreeBSD’s sound API is essentially OSS, ensuring high latency until someone ports ALSA or the like.
If you want an OS with a good low-latency sound API and lots of great audio software like Cubase, ProTools, and Reason, might I suggest OS X? CoreAudio is the best sound interface implementation in existance.
Meanwhile in Windows, it seems that about 0.1% of the sound devices in the world have drivers that support ASIO…
2003-07-17 7:32 pm
Anonymous
I’ll answer your question with a question. Why don’t Ford, GM, Chrysler, Mercedes, Toytota, Nissan, etc all come together and make one car company?
They all make something with 4 wheels and takes people from place to place. So why have so many different ones?
Just think about that one, and when you come up with the answer then you’ll have the answer to your question. It might be a bad analogy, but it’s about as close as I can think of.
2003-07-21 1:32 am
Anonymous
I believe that this will be everything that the Hurd was ever meant to be, and significantly more featureful and robust “out of the box” so to speak. I have always had an interest in microkernels in general and of message passing specifically, and as a BSD lover, to have a message passing BSD kernel seems a dream come true.
The scalability, performance, stability, robustness and security potential that this new design offers is enough for me to switch from FreeBSD 5.x, something that I have long been awaiting for the many advances that it offers. This is truely a wonderful project!
Donate to OSNews
You can also:
Become a Patreon
Buy OSNews merch
Search OSNEWS
OSnews Accounts
Create Account
Login
Topics
Topics
Select Category
.NET
3D
Academic OSes
AMD
Amiga & AROS
Android
Apple
Benchmarks
BSD & Darwin
Bugs & Viruses
Clown car
Comics
Databases
Debian
Desktop environments
Editorial
Fedora Core
Finance
FreeBSD
Fuchsia
Games
Geek stuff
General Development
Genode
Gentoo
Gifts, Contests
Gnome
Google
Graphics
GTK+
Haiku
Hardware
Health
Humor
IBM
In the News
Intel
Internet
Internet Explorer
Java
KDE
Legacy OSes
Legal
Linspire
Linux
macOS
Mandriva, Mandrake, Lycoris
Microsoft
Mobile
Mono
Morphos
Mozilla, Gecko
Multimedia, AV
NetBSD
Novell and Ximian
Office
Open Source
OpenBSD
OpenStep, GNUstep
Opera
Oracle and SUN
Original OSNews Interviews
OS News
OS/2
PC-BSD
Podcasts
Privacy, Security
QNX
Qt
ReactOS
Red Hat
Redox OS
Retro computing
RISC OS
Rumors
SCO
Servo
SGI and IRIX
SkyOS
Slackware, Slax
Solaris
Sponsor
SuSE, openSUSE
Syllable, AtheOS
Technofascism
Ubuntu
Unix
Wayland
Web 2.0
Windows
Wireless
Xfce
Zeta
Related Posts
FreeBSD 5.2.1 RC Available
February 1, 2004 •
22
Comments
Interview: FreeBSD Foundation Director Sam Leffler
February 17, 2007 •
10
Comments
FreeBSD made major gains in laptop support this year
December 21, 2025 •
4
Comments
Poll: FreeBSD’s Popularity
August 29, 2004 •
228
Comments
FreeBSD 5.1 Release Schedule; Bluetooth Stack Update
May 2, 2003 •
20
Comments
Popular Posts
The Ubuntu 26.04 Rust sudo is not compatible with standard sudo
November 5, 2026 •
41
Comments
Microsoft claims it’s optimising Windows for 8GB of RAM
October 5, 2026 •
38
Comments
“I can’t believe PowerShell is actually good”
October 22, 2026 •
38
Comments
Sam Altman wants to take your RAM
November 2, 2026 •
32
Comments
Oldest GUI application that still runs on Windows 11
October 26, 2026 •
27
Comments
Popular Posts (Last 3 Years)
Is 2024 the year of Windows on the desktop?
June 20, 2024
Apple intentionally kills web applications for EU users in iOS 17.4 onward to spite its EU users
February 15, 2024
Made O’Meter helps you easily and quickly avoid American products
March 6, 2025
Codeberg’s programmer user base overwhelmingly votes to ban slopcoded projects from its platform
July 22, 2026
Why do I not use “AI” at OSNews?
February 15, 2026
About OSnews
OSnews Privacy Statement
© OSnews Inc. All Rights Reserved.
OSnews and the OSnews logo are trademarks of OSnews.
Theme Customizations by
Adam Scheinberg
Proudly powered by
Wordpress
Reader comments are owned by the poster.
We are not responsible for them in any way.
All trademarks, icons, and logos shown or mentioned in this web site are the property of their respective owners.
Reproduction of OSnews stories is permitted only with explicit authorization from OSnews.
Reproductions must be properly credited.
Important Links
OSnews Privacy Statement
Sponsorship
OSnews on Mastodon
Notice to Bulk Emailers
Contact OSNews
Trans rights are human rights
From the Archives
From the Archives
Select Month
November 2026 (14)
October 2026 (54)
September 2026 (39)
August 2026 (50)
July 2026 (71)
June 2026 (62)
May 2026 (70)
April 2026 (46)
March 2026 (57)
February 2026 (63)
January 2026 (62)
December 2025 (53)
November 2025 (52)
October 2025 (50)
September 2025 (72)
August 2025 (74)
July 2025 (67)
June 2025 (57)
May 2025 (68)
April 2025 (66)
March 2025 (61)
February 2025 (49)
January 2025 (64)
December 2024 (57)
November 2024 (59)
October 2024 (56)
September 2024 (62)
August 2024 (80)
July 2024 (70)
June 2024 (82)
May 2024 (105)
April 2024 (127)
March 2024 (105)
February 2024 (70)
January 2024 (82)
December 2023 (71)
November 2023 (93)
October 2023 (140)
September 2023 (155)
August 2023 (109)
July 2023 (90)
June 2023 (41)
May 2023 (38)
April 2023 (45)
March 2023 (29)
February 2023 (27)
January 2023 (37)
December 2022 (32)
November 2022 (37)
October 2022 (40)
September 2022 (37)
August 2022 (41)
July 2022 (34)
June 2022 (41)
May 2022 (33)
April 2022 (36)
March 2022 (35)
February 2022 (29)
January 2022 (41)
December 2021 (38)
November 2021 (47)
October 2021 (49)
September 2021 (40)
August 2021 (50)
July 2021 (39)
June 2021 (50)
May 2021 (34)
April 2021 (37)
March 2021 (50)
February 2021 (48)
January 2021 (37)
December 2020 (41)
November 2020 (39)
October 2020 (51)
September 2020 (35)
August 2020 (41)
July 2020 (43)
June 2020 (42)
May 2020 (46)
April 2020 (48)
March 2020 (60)
February 2020 (44)
January 2020 (51)
December 2019 (39)
November 2019 (49)
October 2019 (54)
September 2019 (50)
August 2019 (51)
July 2019 (61)
June 2019 (47)
May 2019 (55)
April 2019 (66)
March 2019 (69)
February 2019 (48)
January 2019 (76)
December 2018 (36)
November 2018 (63)
October 2018 (80)
September 2018 (64)
August 2018 (71)
July 2018 (85)
June 2018 (108)
May 2018 (124)
April 2018 (57)
March 2018 (36)
February 2018 (31)
January 2018 (40)
December 2017 (36)
November 2017 (41)
October 2017 (38)
September 2017 (40)
August 2017 (41)
July 2017 (49)
June 2017 (53)
May 2017 (55)
April 2017 (41)
March 2017 (60)
February 2017 (47)
January 2017 (62)
December 2016 (56)
November 2016 (60)
October 2016 (44)
September 2016 (41)
August 2016 (51)
July 2016 (51)
June 2016 (40)
May 2016 (42)
April 2016 (42)
March 2016 (46)
February 2016 (39)
January 2016 (41)
December 2015 (47)
November 2015 (47)
October 2015 (55)
September 2015 (62)
August 2015 (69)
July 2015 (80)
June 2015 (66)
May 2015 (71)
April 2015 (87)
March 2015 (88)
February 2015 (85)
January 2015 (96)
December 2014 (68)
November 2014 (88)
October 2014 (45)
September 2014 (47)
August 2014 (49)
July 2014 (56)
June 2014 (56)
May 2014 (56)
April 2014 (55)
March 2014 (55)
February 2014 (45)
January 2014 (54)
December 2013 (49)
November 2013 (40)
October 2013 (48)
September 2013 (50)
August 2013 (64)
July 2013 (76)
June 2013 (70)
May 2013 (89)
April 2013 (87)
March 2013 (84)
February 2013 (72)
January 2013 (96)
December 2012 (71)
November 2012 (59)
October 2012 (88)
September 2012 (92)
August 2012 (91)
July 2012 (96)
June 2012 (107)
May 2012 (132)
April 2012 (131)
March 2012 (104)
February 2012 (89)
January 2012 (89)
December 2011 (84)
November 2011 (99)
October 2011 (75)
September 2011 (78)
August 2011 (114)
July 2011 (93)
June 2011 (97)
May 2011 (122)
April 2011 (84)
March 2011 (118)
February 2011 (116)
January 2011 (161)
December 2010 (102)
November 2010 (109)
October 2010 (113)
September 2010 (104)
August 2010 (121)
July 2010 (118)
June 2010 (119)
May 2010 (145)
April 2010 (137)
March 2010 (150)
February 2010 (124)
January 2010 (130)
December 2009 (118)
November 2009 (137)
October 2009 (148)
September 2009 (170)
August 2009 (151)
July 2009 (173)
June 2009 (158)
May 2009 (166)
April 2009 (173)
March 2009 (169)
February 2009 (166)
January 2009 (172)
December 2008 (116)
November 2008 (114)
October 2008 (118)
September 2008 (100)
August 2008 (103)
July 2008 (181)
June 2008 (131)
May 2008 (109)
April 2008 (147)
March 2008 (143)
February 2008 (160)
January 2008 (151)
December 2007 (109)
November 2007 (132)
October 2007 (152)
September 2007 (153)
August 2007 (188)
July 2007 (186)
June 2007 (169)
May 2007 (195)
April 2007 (215)
March 2007 (205)
February 2007 (265)
January 2007 (278)
December 2006 (242)
November 2006 (251)
October 2006 (331)
September 2006 (331)
August 2006 (348)
July 2006 (284)
June 2006 (281)
May 2006 (299)
April 2006 (293)
March 2006 (350)
February 2006 (307)
January 2006 (383)
December 2005 (296)
November 2005 (360)
October 2005 (422)
September 2005 (309)
August 2005 (322)
July 2005 (353)
June 2005 (325)
May 2005 (254)
April 2005 (293)
March 2005 (315)
February 2005 (277)
January 2005 (273)
December 2004 (257)
November 2004 (306)
October 2004 (290)
September 2004 (285)
August 2004 (273)
July 2004 (321)
June 2004 (333)
May 2004 (305)
April 2004 (354)
March 2004 (345)
February 2004 (336)
January 2004 (324)
December 2003 (282)
November 2003 (257)
October 2003 (289)
September 2003 (315)
August 2003 (206)
July 2003 (246)
June 2003 (247)
May 2003 (238)
April 2003 (277)
March 2003 (227)
February 2003 (237)
January 2003 (238)
December 2002 (196)
November 2002 (216)
October 2002 (200)
September 2002 (198)
August 2002 (187)
July 2002 (171)
June 2002 (141)
May 2002 (134)
April 2002 (137)
March 2002 (148)
February 2002 (137)
January 2002 (127)
December 2001 (110)
November 2001 (114)
October 2001 (108)
September 2001 (54)
August 2001 (22)
OSnews
Copyright © 2026.
© OSnews Inc · Theme by
Adam Scheinberg
