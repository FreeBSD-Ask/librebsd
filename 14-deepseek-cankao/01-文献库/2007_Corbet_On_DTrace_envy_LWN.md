---
title: "2007_Corbet_On_DTrace_envy_LWN.md"
source_url: https://lwn.net/Articles/244536/
download_date: 2026-09-08
note: manual_direct
---

# 2007_Corbet_On_DTrace_envy_LWN.md

来源: https://lwn.net/Articles/244536/

         

          On DTrace envy [LWN.net] 

             LWN .net 
             News from the source  

           Content     Weekly Edition    Archives    Search    Kernel    Security    Events calendar    Unread comments       LWN FAQ    Write for us    
   Edition     Return to the Front page    

          User:     
		  Password:          |

             |

                 Log in   /
                 Subscribe   /
                 Register  

 On DTrace envy 

 LWN.net needs you! 

Without subscribers, LWN would simply not exist.  Please consider
        signing up for a subscription  and helping
       to keep LWN publishing.

           By  Jonathan Corbet  August 7, 2007 

When Sun looks to highlight the strongest features of the Solaris operating
system, DTrace always appears near the top of the list.  Your editor
recently had a conversation with an employee of a prominent analyst firm
who was interested, above all else, in when Linux would have some sort of
answer to DTrace.  There is a common notion out there that tracing tools is
one place where Linux is significantly behind the state of the art.  So
your editor decided to take a closer look.

The Linux tool which is most similar to DTrace is  SystemTap .  This development is
supported by a number of high-profile companies, including Red Hat, Intel,
IBM, and Hitachi.  Most distributions have SystemTap packages somewhere in
their systems of repositories, making it readily available to Linux users.
DTrace supporters have been known to say that SystemTap is merely a  knock-off of
DTrace , and a badly-done one at that.  SystemTap proponents will
counter that it is an independent development which can hold its own.

Both tools are based on the insertion of probe points in the system
kernel.  Whenever a thread of execution hits one of those probe points,
some sort of action - as described in the tool's C-like language - is run.
That action can be as simple as printing a message, or it can be
significantly more complicated than that.

DTrace comes with a large set of pre-defined probe points wired into the
Solaris kernel - seemingly tens of thousands of them.  These points are  well documented  and
cover most of the kernel.  Some simple wildcarding is implemented for the
selection of multiple probe points.  It is claimed that the run-time
overhead of unused probe points is negligible.  [ Update : see the
comments for some useful clarification on the use of dynamic probe points
in DTrace.]

SystemTap, instead, does not depend on static probe points within the
kernel; that capability exists, but nobody has much interest in maintaining
all of those points.  Instead, SystemTap uses dynamic probes (implemented
with  kprobes ) which
are inserted into the kernel at run time.  A flexible language can enable
probes to be easily inserted anywhere in the kernel, with fairly complete
wildcard support which allows, for example, all functions within a source
file or subsystem to be instrumented with a single statement.  Unused probe
points do not exist at all, and so cannot affect system performance.

There are a couple of advantages to the DTrace approach.  The probe points
exist and can be easily found in the manuals; a SystemTap user, instead, is
required to have a certain amount of familiarity with the kernel source
code.  DTrace probe points are fixed at locations where it is known to be
safe to interrupt the execution of the kernel.  The SystemTap
documentation, instead, comes with warnings that placing probes in the
wrong places can cause system crashes and mutterings about the possibility of
implementing blacklists in the future.  The number of "wrong places"
appears to be quite small, but that is of limited comfort for an
administrator trying to observe the operation of a production system -
something which is supposed to be possible with either system.  There is a
set of predefined points provided in the "tapsets" packaged with SystemTap,
but it is small.

The "D" language provided with DTrace is more restricted than the SystemTap
language, though it does have a few features - like the ability to print
stack traces - which appear to be missing in SystemTap.  The D language has
no flow control or looping constructs.  Instead, the code associated with a
probe has a predicate expression determining whether that code is executed
when the probe is hit.  Thus each selected probe point can be thought of
as having a single, controlling " if " statement around it, with no
further flow control possible afterward.

SystemTap's language, instead, has conditionals, loops, and the ability to
define functions.  It also has, for those who like to live dangerously, the
ability to embed C code.  There are clear advantages to a more powerful
scripting language, but hazards as well: SystemTap must, for example, carry
extra code to keep infinite loops in scripts from bringing down the system.

D is, like Java, compiled to a special virtual machine and interpreted at
run time.  SystemTap, instead, compiles directly to C.  So SystemTap code
may execute more quickly, but D may benefit from the additional safety
checks which a virtual machine allows.

DTrace has the ability to work with user-space probes.  As with the kernel,
developers are required to insert the probe points before DTrace can use
them; it is not clear that large amounts of user-space code have been so
instrumented.  There is clear elegance to the idea, though, and this
capability may prove genuinely useful in the future as more applications
are equipped with probe points.  SystemTap does not currently have this
capability. 

In practice, simply getting SystemTap to work can be a challenge - even
when a distributor-supported package is available.  SystemTap is clearly
its own development which must be (somewhat painfully) integrated with a
specific kernel.  DTrace can be expected to simply work out of the box.  

And that is perhaps the biggest difference between the two tracing
systems.  SystemTap would appear to have all of the capabilities it really
needs to be a powerful system tracing tool - at least on the kernel side.
DTrace features which are missing -  speculative
tracing , for example - could certainly be added if there were demand
for it.  Evidently user-space tracing is in the works.  
But what SystemTap really needs is more basic than that.  What's missing is
the degree of maturity exhibited by DTrace.

SystemTap needs to simply work on most systems - and be usable by the
system administrators.  To a great extent, the "simply work" part is
something that the distributors must address.  Current SystemTap packages
as tested by your editor have the look of an edge-of-the-repository
afterthought.  They do not have the dependencies to bring in the needed
kernel information, requiring a fair amount of manual "what does it need
now?" administrative work.
Even then, performance is spotty at best; the SystemTap utilities just do
not have access to the sort of information (uncompressed kernel images, for
example) that they need to operate correctly.  Until an administrator can
simply tell the package management system to install SystemTap and expect
to have it work thereafter, it will be hard to convince anybody that we
have a mature tracing tool.

On the development side, there should be an extensive set of
well-documented trace points which can be used without having to go into
the kernel source.  Digging deeply into the system in a flexible way is
always going to require a certain amount of skill, but SystemTap all but
requires its users to be kernel hackers.  The hard work of making a tool
which can match - and, in places, exceed - DTrace has been done.  What
remains is a large (but relatively straightforward) job: making this tool
usable by a much wider set of system administrators.  Until that is done,
DTrace envy will remain with us.  
             Index entries for this article  
              Kernel    SystemTap   
               Kernel    Tracing   

              to post comments

        Factual errors about DTrace 

        Posted Aug 7, 2007 18:50 UTC (Tue)
                               by  cajal  (guest, #4167)
                              [ Link ] (8 responses)

      I'd like to correct several factual errors about DTrace in this article. 

DTrace does not depend upon static probes in the kernel. In fact, the "D" in DTrace stands for dynamic; DTrace uses dynamic probing. It does allow developers to add statically defined probe points, and the Solaris kernel does have many statically defined probes. 

But it is inaccurate to state that DTrace depends on static probes. In fact, the overwhelming majority of the in-kernel probes on Solaris are dynamic (they're provided by the function boundary tracing (fbt) DTrace provider). This is where most of the "tens of thousands" of in-kernel DTrace probes come from (they're tracing kernel function entry and return points). In userspace, the pid provider allows probes to be dynamically inserted at arbitrary offsets in a program. 

The D language does have (limited) control flow: It has the ternary operator.  

Concerning user-space probes, it is not required that application developers insert DTrace probe points before DTrace can use them. The pid provider, which I mentioned above, can trace user-space function entry and return (as well as at any arbitary offset within an application). However, it is possible for developers to insert static probes points into their applications. There are several examples of this: 

* PostgreSQL 8.2 ( http://www.postgresql.org/docs/8.2/interactive/dynamic-tr... ) 
* Sun's Java 6 ( http://java.sun.com/javase/6/docs/technotes/guides/vm/dtr... ) 
* mod_dtrace for Apache ( http://prefetch.net/projects/apache_modtrace/ ) 
* Ruby ( https://dtrace.joyent.com/projects/ruby-dtrace/wiki/Ruby+... ) 
* X.org 7.3 ( http://wiki.x.org/wiki/Releases/7.3 ) 
* PHP ( http://pecl.php.net/package/DTrace ) 
* Sendmail ( http://mail.opensolaris.org/pipermail/dtrace-discuss/2006... ) 
* Python  
( http://blogs.sun.com/levon/entry/python_and_dtrace_in_build ) 

Granted, the last two are still experimental. 

        static probes 

        Posted Aug 7, 2007 19:24 UTC (Tue)
                               by  fuhchee  (guest, #40059)
                              [ Link ] (6 responses)

       &gt; DTrace does not depend upon static probes in the kernel.  

That is true at a certain level, but almost all of the interesting 
data that is gathered comes from providers other than fbt, and these 
are implemented with static probes.  Check out the dtt code. 

In linux, the closest thing we have are markers, which are slowly 
making their way through LKML for upstream inclusion.  Systemtap 
already interfaces to these effortlessly. 

        static probes 

        Posted Aug 7, 2007 20:57 UTC (Tue)
                               by  bcantrill  (guest, #31087)
                              [ Link ] (5 responses)

 DTrace does not depend upon static probes in the kernel. 

That is true at a certain level, but almost all of the interesting
data that is gathered comes from providers other than fbt, and these
are implemented with static probes. Check out the dtt code.

That's a pretty gutsy assertion from someone who, to the best of my knowledge, has never used DTrace.  (Because it was not explicit in his comment, Frank Ch. Eigler -- a.k.a. fuhchee -- is the SystemTap lead at Red Hat.)  And indeed, you're falling prey to a bit of a logical fallacy:  we invented SDT/USDT because it allowed scripts to not have to rely on the implementation, and as the DTraceToolkit wishes to avoid depending on the implementation, it has of course implemented everything in terms of SDT/USDT; looking at the scripts in the DTraceToolkit is therefore  not  representative (necessarily, anyway) of how people  use  DTrace.

So how  do  people use DTrace?  When first looking at a problem with DTrace, much investigation does indeed start with probes from SDT- and USDT-provided probes -- but it often finishes with probes from  fbt  and  pid .  That is, one often descends from the most abstract ("Why are we doing I/O?") through to the implementation ("Why is  FT_New_Face  inducing I/O?  That font should be cached!")  So it's not one or the other -- one needs both methodologies to be able to comprehensively instrument the system, and that is why we have taken both approaches in DTrace.

        static probes 

        Posted Aug 7, 2007 22:15 UTC (Tue)
                               by  fuhchee  (guest, #40059)
                              [ Link ] (2 responses)

       &gt; That's a pretty gutsy assertion   

And a correct one, as we seem to be in vigorous agreement.  Many scripts 
use the static probes, especially the ones one might use to start analyzing 
a problem.  There is nothing wrong with "depending" on static probes in this 
sense, so I don't see why you would object. 

 &gt; from someone who, to the best of my knowledge, has never used DTrace.   

The best of your knowledge needs to get better. 

        Vigorous disagreement 

        Posted Aug 7, 2007 22:34 UTC (Tue)
                               by  bcantrill  (guest, #31087)
                              [ Link ] (1 responses)

      Frank, you write:

 That's a pretty gutsy assertion 

And a correct one, as we seem to be in vigorous agreement.

No, no we're not -- not at all.  You wrote this:

...but almost all of the interesting
data that is gathered comes from providers other than fbt, and these
are implemented with static probes.

That is  wrong , and I am not in agreement with it whatsoever.   It's wrong in two dimensions.  The first being that "all...interesting data comes from providers other than fbt"; as I said (clearly, I thought)  fbt  and  pid  often are used as an investigation proceeds from the symptoms of a suboptimal system to the root-causes of that suboptimality in the implementation.  So it's a gross mischaracterization to dismiss their role in DTrace.  The second way in which your statement is incorrect is the implication that "providers other than fbt ... are implemented with static probes."  This shows complete ignorance of the  pid  provider, which can instrument any instruction in any running process, and is the workhorse of user-level instrumentation.

You also write:

 from someone who, to the best of my knowledge, has never used DTrace. 

The best of your knowledge needs to get better.

Fair enough; allow me to rephrase:  "someone who, if they have used DTrace at all, appears to have learned nothing from the experience."  Better?

        Please don't misquote 

        Posted Aug 12, 2007 18:49 UTC (Sun)
                               by  felixfix  (subscriber, #242)
                              [ Link ] 

      Your credibility in this argument just took a big dive.  fuhchee said "almost all of the interesting data" and you left out the "almost", which changes the meaning considerably.  Besides which, you yourself say "much investigation does indeed start with probes from SDT- and USDT-provided probes -- but it often finishes with probes from fbt and pid" which certainly implies that a majority of investigations begin with SDT and USDT, which also implies that SDT and USDT are "more" used than  anything else.  Maybe "almost all" is an exageration of "most", but leaving out the "almost" is a misquote twisting his words to match your thoughts. 

        static probes 

        Posted Aug 8, 2007 8:06 UTC (Wed)
                               by  njs  (subscriber, #40338)
                              [ Link ] (1 responses)

      Not the interrupt the Flame-War of the Titans, but... 

When Frank sez "almost all of the interesting data that is gathered comes from providers other than fbt", I don't think he's saying "no-one ever uses fbt".  (Nor is he trying to estimate total number of in-production probe hits on different providers or anything like that.)  He's replying to a claim that static probes are irrelevant, or uninteresting, or at least not as important as the original article claimed.  Maybe cajal didn't mean his comment that way, but it certainly can be read that way. 

Based on that, to me it basically sounds like Frank is saying "static providers are critical to dtrace's usability in practice", and you're saying "no, no, static providers are only critical to do initial investigation of problems so you can figure out how to deploy the other parts of dtrace".  These are not exactly contradictory statements.  I can't imagine trying to do anything with dtrace without relying on proc, sched, io, even if I used fbt and pid too. 

So cajal's comment does seem a bit misleading, and it seems fair to correct that part of it. 

(FTR, I haven't used dtrace either, just envied it intensely.) 

        static probes 

        Posted Aug 8, 2007 13:22 UTC (Wed)
                               by  cajal  (guest, #4167)
                              [ Link ] 

      I was responding to the original article's claim that "SystemTap, instead, does not depend on static probe points within the kernel". That claim implies that DTrace depends on static probe points in the kernel. I was only trying to point out that DTrace provides both dynamic and static trace points (since, as Bryan points out, both are needed). 

        Very, very experimental Perl DTrace support 

        Posted Aug 16, 2007 8:39 UTC (Thu)
                               by  richdawe  (subscriber, #33805)
                              [ Link ] 

      Alan Burlison from Sun wrote some experimental support for DTrace in Perl and blogged about it at &lt; http://blogs.sun.com/alanbur/entry/dtrace_and_perl &gt;. I've reproduced his work -- I have a patch &lt; http://rich.phekda.org/perl-dtrace/ &gt;, which needs some more work. 

        On DTrace envy 

        Posted Aug 7, 2007 18:55 UTC (Tue)
                               by  bcantrill  (guest, #31087)
                              [ Link ] 

      First, thanks for what is largely an accurate comparison -- it's especially gratifying to see understanding of (and appreciation for) the design decisions that we made in DTrace around safety.  One very important correction, however:  DTrace does  not  rely solely on programmer insertion of probes.  In the kernel, DTrace can instrument every function entry and return  without any programmer involvement whatsoever  (which is the reason that tens of thousands of probes exist on any system -- there are two for most kernel functions).  At user level, DTrace goes one better and can instrument every instruction in every process -- again  without programmer involvement .

Now, all of that said, DTrace  benefits  from programmer involvement:  programmers may add static points of instrumentation that export the semantics of the system instead of its implementation.  As a concrete example, there are three functions in the Solaris kernel in which we enqeue a thread to run:   setkpdq ,  setfrontdq  and  setbackdq .  An expert in Solaris internals could therefore determine when a thread is scheduled to run with the following DTrace fragment:

setkpdq:entry,
setfrontdq:entry,
dispdeq:entry
{
        printf("%s scheduled to run...\n", args[0]->t_procp->p_user.u_comm);
}

This doesn't (or didn't) require any changes to the Solaris kernel itself, which is good.  But this also requires knowing quite a bit about the implementation of Solaris:  where threads are enqueued to run, what the thread structure looks like, etc.  And it's brittle:  if we change the kernel's implementation, the script is broken.

To address these shortcomings, we added a statically-defined tracing (SDT) provider, the  sched  provider, which makes available higher-level semantics.  When rephrased in terms of  sched , the above becomes:

sched:::enqueue
{
        printf("%s scheduled to run...\n", args[1]->pr_fname);
}

This is something that is simpler to understand, and represents stable, documented abstractions -- and we can change the kernel without breaking the script. 

While originally a kernel-level notion, we brought this same technology to user-land, with what we call user-level statically-defined tracing (USDT). USDT allows one to instrument, say, one's Ruby, Python, Java, JavaScript, etc. in terms of the language instead of the implementation; the reader is directed to google + [language of choice] + "I'm feeling lucky" for details.

Anyway, thanks again for the careful look at DTrace.  And if anyone finds themselves suffering from excessive DTrace envy, you might want to chime in on  Adam's blog  about how a Linux port could be made possible...

        Minor factual errors regarding systemtap 

        Posted Aug 7, 2007 19:44 UTC (Tue)
                               by  fuhchee  (guest, #40059)
                              [ Link ] (4 responses)

Here are some nits to correct in the body of the otherwise well-done article.  I'm a systemtap developer.

It is true that systemtap relies on dynamic probes almost exclusively.  Since these are expressed in terms of functions / source code lines, they indeed rely on an understanding of the kernel.  We are well aware that this is too much for an ordinary user, which is why from day 1, systemtap has included a  "tapset"  facility.  This method allows kernel experts to encode their knowledge about subsystems into higher level probe points, so that end-user scripts can refer to higher level abstractions.  So, a knowledgeable person can  probe kernel.function("sys_open")  and look at local variables or parameters; a less knowledgeable one can rely on the automatic tapset searching and  probe syscall.open .  Such higher level tapset probes are intended to allay the "must be a kernel hacker" worry, and are generally documented accordingly.

The documentation not only mutters about a blacklist.  There are kernel-side and systemtap-side blacklists.  (There exists a similar blacklist in dtrace for analogous low-level kernel code.)  While these are actively maintained, they are not complete, thus the caution in the docs.

Regarding the relative safety of a virtual-machine-based interpreter versus the compiled-in checks of systemtap, as far as we can see, it's a toss-up.  One can consider the systemtap method to be equivalent to  inlining  all the same checks that the virtual machine would do.  All the  difficult  areas of safety assurance come from other places - the runtime, the choice of probe points.

Regarding the difficulty of getting started with systemtap due to its installation requirements, we agree, and are working on improving this aspect.  Similarly, we are aware of the need for more polish, fuller documentation, a bigger library of samples.  Our small group is working on these things, and would appreciate community assistance.  All of our work (code, bugs, documents, mailing lists) have been in the open since day 1.

Let me finish off with a plug at a  systemtap-dtrace comparison page .  We have invited Adam Leventhal from Sun to help edit it to keep us all honest.

        Minor factual errors regarding systemtap 

        Posted Aug 7, 2007 21:19 UTC (Tue)
                               by  ahl  (guest, #40497)
                              [ Link ] 

      As I've conveyed to you privately, I appreciate the invitation to edit your comparison, but I thought  
my role was limited to rectifying inaccuracies. I'll be happy to add some material to make the  
comparison more complete e.g. stack backtraces, tracing Ruby, Perl, Python, Java, JavaScript, PHP,  
etc. -- all of which are absent from SystemTap in its current form. I had though that would be  
overstepping my role. 

        Minor factual errors regarding systemtap 

        Posted Aug 7, 2007 21:20 UTC (Tue)
                               by  oak  (guest, #2786)
                              [ Link ] (1 responses)

      A colleague did a quick/ad-hoc test of the recent ARM port of Systemtap  
and a single Systemtap syscall probe seems to have about as much  
performance hit for the system as the whole LTT(ng) thing.  Does this  
result sound right (LTT uses static probe points whereas Systemtap uses  
dynamic kprobe + has its own overhead on top of that)? 

        Minor factual errors regarding systemtap 

        Posted Aug 7, 2007 22:10 UTC (Tue)
                               by  fuhchee  (guest, #40059)
                              [ Link ] 

       &gt; [on ARM a] single Systemtap syscall probe seems to have about as much  
 &gt; performance hit for the system as the whole LTT(ng) thing.   

Please post some details to the mailing list. 

 &gt; Does this result sound right (LTT uses static probe points whereas Systemtap  
 &gt; uses dynamic kprobe + has its own overhead on top of that)?  

Yes, dynamic probes are significantly costly than static probe points, 
but overall cost is a function that includes rate-of-hits and other 
quantities.  Note that the LTT static probe points will be transparently 
exploitable from systemtap once this part of LTT is merged upstream, 
and this should greatly reduce the performance differences. 

        DTrace blacklist? 

        Posted Aug 7, 2007 21:25 UTC (Tue)
                               by  bcantrill  (guest, #31087)
                              [ Link ] 

The documentation not only mutters about a blacklist. There are kernel-side and systemtap-side blacklists.  (There exists a similar blacklist in dtrace for analogous low-level kernel code.)   (Emphasis added) 

What are you referring to?  We dynamically decide what can be safely instrumented; there is no "blacklist of functions" to maintain in DTrace.  This is not to say that we can instrument every function, just that we determine whether or not we can safely instrument a function on-the-fly.  And   I might add that because of our safety-centric architecture, there are very few contexts that one cannot safely instrument...

        On DTrace envy 

        Posted Aug 7, 2007 19:53 UTC (Tue)
                               by  ncm  (guest, #165)
                              [ Link ] (1 responses)

      It's excellent work like this that makes me keep renewing my subscription. 

        On DTrace envy 

        Posted Aug 9, 2007 1:58 UTC (Thu)
                               by  lysse  (guest, #3190)
                              [ Link ] 

      What he said. 

        On DTrace envy 

        Posted Aug 7, 2007 20:32 UTC (Tue)
                               by  prasadav  (guest, #46636)
                              [ Link ] (3 responses)

      Jonathan, thanks for taking an objective look at the tracing tools and giving your informed opinion. I would like to give few clarifications mainly from SystemTap point of view.  

On the documentation SystemTap does provide a manual pages that explains the probe points available in the tapsets so one doesn't have to read the source code. I agree we can improve the documentation and we are addressing this issue and you will see detailed language reference manual soon on the website.  

SystemTap language does support static markers. The static marker infrastructure in the kernel is currently undergoing review in LKML and we are expecting that to make to mainline soon. Once it makes to mainline SystemTap will exploit that.  

We designed SystemTap to be flexible yet safe to make it usable to wide variety of audience. SystemTap also provides predefined probe points that are safe to probe. An administrator can limit to only these probe points without worrying about safety. SystemTap also provides ability for a developer or support person to place probes anywhere using advanced guru mode hence the warnings of safety. I agree with you that bundled tapsets contain limited probe points and needs enhancement and work is in progress.  

Safety is one of the most important considerations in all of our design decisions. The generated code also has safety checks very similar to what a virtual machine provides.  

I agree with you that SystemTap provides feature rich language including ability to print stack trace using backtrace() construct.  

SystemTap project is very young (2.5 years) and it is still work in progress. We have come a long way in this short amount of time due to our flexible architecture but I agree with you that we need to focus making it usable to administrators of all levels.  

        On DTrace envy 

        Posted Aug 7, 2007 21:26 UTC (Tue)
                               by  ahl  (guest, #40497)
                              [ Link ] (2 responses)

SystemTap project is very young (2.5 years) and it is still work in progress. We have come a long 
way in this short amount of time due to our flexible architecture but I agree with you that we need 
to focus making it usable to administrators of all levels. 

By way of comparison, DTrace was being used in production a bit more than a year after 
development started, and it integrated after being in development for less than two years (it has, of 
course, evolved since then).

        On DTrace envy 

        Posted Aug 7, 2007 23:36 UTC (Tue)
                               by  clugstj  (subscriber, #4020)
                              [ Link ] (1 responses)

      Not really a fair comparison unless we are told how much much effort has been expended on each project, not just how much time. 

        On DTrace envy 

        Posted Aug 8, 2007 0:21 UTC (Wed)
                               by  ahl  (guest, #40497)
                              [ Link ] 

      Fair point: 

I'm a member of the DTrace team. Development started with two people in October 2001; I joined about 6 months later. We integrated into Solaris in September 2003 so the original effort took about 5.5 man years of work. From 2003-2005 (when Solaris 10 shipped), the focus for the three of us continued to be DTrace, but we had several other projects on the side as well. 

        On DTrace envy 

        Posted Aug 7, 2007 20:40 UTC (Tue)
                               by  dw  (guest, #12017)
                              [ Link ] (24 responses)

      I can't help but think this is a knee jerk reaction to the (from my limited perspective) excellent post on Adam Leventhal's blog. There are certain things about that entry not covered here, such as the seemingly blatant plagiarism present in the "Red Hat Summit 2007" slides. 

Can anyone mention a single good reason DTrace can't be lifted as-is, name kept and everything, into the Linux kernel? The Sun people seem to be pushing for this while the Linux people seem intriguingly silent on the issue. 

Personally after reading that post and the various things it links to, I'd say DTrace is the better and more rigorously designed system. 

        On DTrace envy 

        Posted Aug 7, 2007 20:49 UTC (Tue)
                               by  corbet  (editor, #1)
                              [ Link ] (12 responses)

      This article has been in the works for a couple of weeks, and was not motivated by Adam's posting.  And, yes, there's issues he raises there that I did not address - I was talking about the two technologies, not other bits of associated silliness.

As for putting DTrace into Linux - read the comments on Adam's posting.  The GPL/CDDL incompatibility is something that Sun designed in; it cannot be wished away.  If Sun were to dual-license DTrace under GPLv2, the situation would be different.

        Drag-n-drop DTrace into Linux Kernel? 

        Posted Aug 7, 2007 22:34 UTC (Tue)
                               by  pr1268  (guest, #24648)
                              [ Link ] (11 responses)

        &gt; If Sun were to dual-license DTrace under GPLv2, the situation would be different.  

 Does there seem to be any indications that this could happen sometime in the future?  I'm not trying to immediately discount SystemTap; but rather, I'm curious if Sun would/could be so persuaded. 

 Thank you, Jon, for a wonderful article.  Your research articles always seem to get the liveliest discussions! :-) 

        Drag-n-drop DTrace into Linux Kernel? 

        Posted Aug 8, 2007 17:17 UTC (Wed)
                               by  madscientist  (subscriber, #16861)
                              [ Link ] (1 responses)

      A really interesting twist to this would be GPLv3. 

There was some talk this past spring that Sun was looking at GPLv3 as a worthy successor for or alternative to CDDL.  If Sun really does relicense OpenSolaris (and hence XFS and DTrace) under GPLv3 (or dual license it), I wonder if that's the "killer app" that would get the Linux kernel devs to re-examine the GPLv2 / GPLv3 issue.  The buzz is that Linus and Co. are not as disdainful of the final GPLv3 draft as they were of some earlier versions, but that the effort involved with relicensing was widely seen as a waste of time with no real benefit. 

Personally I doubt it would change anything on the Linux side; the people who would have to make this decision and do much of the work don't really seem to care much about DTrace (at least). 

        Drag-n-drop DTrace into Linux Kernel? 

        Posted Aug 9, 2007 8:59 UTC (Thu)
                               by  nsoranzo  (guest, #34668)
                              [ Link ] 

       &gt; There was some talk this past spring that Sun was looking at GPLv3 as a worthy successor for or alternative to CDDL. If Sun really does relicense OpenSolaris (and hence XFS and DTrace) under GPLv3 (or dual license it)  

Obviously you mean ZFS, not XFS... 

Nicola 

        Drag-n-drop DTrace into Linux Kernel? 

        Posted Aug 8, 2007 20:22 UTC (Wed)
                               by  khim  (subscriber, #9252)
                              [ Link ] 

        Does there seem to be any indications that this could happen sometime in the future?  

 Today there are no need for this: the parts of DTrace which can be easily lifted are already reimplemented in SystemTap, the stuff that remains is important, but tied to Solaris too tightly to be easily lifted... 

        DTrace real port 

        Posted Aug 9, 2007 10:25 UTC (Thu)
                               by  man_ls  (guest, #15091)
                              [ Link ] (7 responses)

      I'm surprised that nobody has asked the question, so it is probably an obvious stupidity. Anyway there it goes.

Why bother to port? Why not reimplement  everything  (including the kernel modules) and put it under GPLv2? Building a compatible implementation shouldn't require that much effort, even to the point where DTrace scripts can be shared (that is, those which are not too tightly coupled to Solaris internals).

        DTrace real port 

        Posted Aug 9, 2007 15:47 UTC (Thu)
                               by  bcantrill  (guest, #31087)
                              [ Link ] (1 responses)

      Good luck with that. 

        DTrace real port 

        Posted Aug 10, 2007 23:13 UTC (Fri)
                               by  man_ls  (guest, #15091)
                              [ Link ] 

      Is there any specific problem you see with this approach? Not that it is an easy task, but after all there is a working implementation with source code to study. It would probably be easier than working around the limitations you people have exposed in SystemTap, wouldn't it?

        dtrace clone 

        Posted Aug 10, 2007 14:48 UTC (Fri)
                               by  fuhchee  (guest, #40059)
                              [ Link ] (4 responses)

      There are several obstacles.  Rewriting the code is a relatively small part.  Merging upstream is huge and controversial.  There may also be legal (patent) barriers. 

        dtrace clone 

        Posted Aug 10, 2007 23:09 UTC (Fri)
                               by  man_ls  (guest, #15091)
                              [ Link ] (3 responses)

      Merging upstream has to be done with SystemTap too. Is there any reason why it would be harder with a dtrace clone?

And patent trouble has not stopped kernel developers before...

        dtrace clone 

        Posted Aug 11, 2007 20:53 UTC (Sat)
                               by  fuhchee  (guest, #40059)
                              [ Link ] 

       &gt; Merging upstream has to be done with SystemTap too.  

Not as much as one might think.  Systemtap relies only on existing 
externalized kernel interfaces and hooks - no changes just on our 
account.  That's not to say it wouldn't be nice to get some extra 
interfaces/hooks, or to offload some version drift maintenance to other 
folks.  It means that we can work toward their development and upstream 
inclusion gradually, without blocking the rest of the work. 

        dtrace clone 

        Posted Aug 11, 2007 22:09 UTC (Sat)
                               by  dlang  (guest, #313)
                              [ Link ] (1 responses)

      please name anything in the kernel that has been put in if there is any doubt about the legality of it. 

the license and patent status of dtrace is very much a reason for it not being considered (in fact, due to these issues most of the kernel developers don't even look at it to avoid any accusations of them being tainted) 

        dtrace clone 

        Posted Aug 12, 2007 12:13 UTC (Sun)
                               by  man_ls  (guest, #15091)
                              [ Link ] 

      As you probably know, any non-trivial piece of code probably infringes on a lot of patents. That hasn't stopped kernel developers from improving the kernel, and rightly so. Maybe the situation with specific patents is different.

        On DTrace envy 

        Posted Aug 7, 2007 21:36 UTC (Tue)
                               by  ahl  (guest, #40497)
                              [ Link ] 

      Thank you for the kind words about my blog post. And, Jon, I think you did a terrific job with your 
analysis, and create a very balanced conversation.

Regarding a DTrace port to Linux, that was the subject of my follow-on blog post which you can 
find  here . In it, I put 
forth a hypothetical DTrace port which I believe conforms to all relevant licenses.

        On DTrace envy 

        Posted Aug 7, 2007 21:53 UTC (Tue)
                               by  tfheen  (subscriber, #17598)
                              [ Link ] (9 responses)

       Can anyone mention a single good reason DTrace can't be lifted as-is, name  kept and everything, into the Linux kernel? The Sun people seem to be pushing for this while the Linux people seem intriguingly silent on the issue. 

 DTrace is licenced under the CDDL, the Linux kernel is licenced under the GPLv2.  Those two licences are incompatible, so any wholesale lifting of DTrace into Linux would give you a result which is (legally) undistributable. 

 Given that Linux has so many contributors, it is for all practical purposes impossible to change the licence or add an exception allowing linking with the CDDL.  Sun owns (afaik) the copyright to DTrace and could with a sufficient effort relicence DTrace under the GPLv2 which would allow lifting the code into Linux, barring any technical difficulties. 

 Note that I am in no way saying that GPL is better or worse than the CDDL; they are just incompatible due to the GPL's requirement on "no further restrictions" and the CDDL's patent termination clauses.  Also please note that I am in no way saying that Sun  should  relicence DTrace, only that if they want it to end up in the Linux kernel, as-is, relicencing is probably the easiest way to make that happen. 

        On DTrace envy 

        Posted Aug 8, 2007 13:07 UTC (Wed)
                               by  paulj  (subscriber, #341)
                              [ Link ] (8 responses)

        DTrace is licenced under the CDDL, the Linux kernel is licenced under the GPLv2. Those two licences are incompatible, so any wholesale lifting of DTrace into Linux would give you a result which is (legally) undistributable. 

It's pretty simple.

a) Follow AHL's recipe (see his blog, linked to several times in this article)

That gets you GPLed reimplementation of certain DTrace bits for the linux kernel (perfectly redistributable) and CDDLed DTrace bits for the linux kernel (which a user is perfectly entitled to download and combine together with the GPLed bits - many Linux users already have long availed of this right to download and install completely  proprietary  Linux modules from their distributions repositories).

For 100%-shiny-white redistribution, you need:

b) Linux kernel developers to state they're fine with redistribution of CDDLed Linux kernel modules together with GPLed kernel and/or modules (remember, they're both free software licences).

If the bulk of Linux devs of significance do so, then the problem is solved.

        On DTrace envy 

        Posted Aug 8, 2007 13:32 UTC (Wed)
                               by  paulj  (subscriber, #341)
                              [ Link ] 

      "If the bulk of Linux devs of significance do so, then the problem is solved." 

Hmm, I should re-state that, as in the above form it allows for possibly morally-bankrupt situations (e.g. some developers objecting, but who do not have resources to take action), which wasn't my intention. So: 

"If no Linux kernel developers object, then there is no problem". 

        On DTrace envy 

        Posted Aug 8, 2007 17:12 UTC (Wed)
                               by  madscientist  (subscriber, #16861)
                              [ Link ] (5 responses)

       &gt; That gets you GPLed reimplementation of certain DTrace bits for the linux  
 &gt; kernel (perfectly redistributable)  

While it is redistributable, I should point out that as described there's very little chance that those changes will ever be accepted into the mainline kernel.  Linus et.al. have a long standing, and firm, position that no code will be accepted (even if it's perfectly legal GPL code) into the mainline kernel if its only purpose is to enable proprietary modules of one sort or another. 

Of course, there's no reason why individual distributors like Red Hat, SuSE, Debian, etc. couldn't apply that patch themselves to their kernel packages, but this becomes a pain. 

Of course, another option would be for the DTrace port to use existing, generic kernel facilities or, if none such exist, work on getting them added.  This would be a lot more work, I expect. 

        On DTrace envy 

        Posted Aug 8, 2007 17:28 UTC (Wed)
                               by  JoeBuck  (subscriber, #2330)
                              [ Link ] (4 responses)

      In this case, that's not the purpose; DTrace is free software, not proprietary software, even though the license isn't compatible.  Furthermore SystemTap could use the same hooks.

        On DTrace envy 

        Posted Aug 8, 2007 19:30 UTC (Wed)
                               by  ahl  (guest, #40497)
                              [ Link ] (2 responses)

      That's a very interesting point. I wonder if Linus et al. would object to hooks for an  open source  component, and, if they did, what the grounds for those objections would be.

        On DTrace envy 

        Posted Aug 9, 2007 11:47 UTC (Thu)
                               by  paulj  (subscriber, #341)
                              [ Link ] 

       I don't want to sound too humbugish about attribution, but that was  my  point with  "(remember, they're both free software licences)"  from my point b) (get linux devs to agree CDDLed Dtrace modules are ok). Any points about potential odd-standards are implied in that (particularly as I had already referred to proprietary modules earlier in my post, highlighted in bold too to make it obvious..).

:)

        On DTrace envy 

        Posted Aug 9, 2007 19:55 UTC (Thu)
                               by  bfields  (subscriber, #19510)
                              [ Link ] 

       I wonder if Linus et al. would object to hooks for an open source component, and, if they did, what the grounds for those objections would be. 

 That sort of thing has always met a lot of resistance.  Currently any in-kernel API can be changed as long as you take care to fix up all the in-tree users.  Obviously that makes certain kinds of changes much easier.
And having in-tree users for API's makes those API's easier to understand and maintain.

        On DTrace envy 

        Posted Aug 8, 2007 21:30 UTC (Wed)
                               by  madscientist  (subscriber, #16861)
                              [ Link ] 

      You're right, I misspoke.  I wonder about ahl's point as well: is the Linux devs' position that they shouldn't create special hooks for code that is not GPL-compatible, and hence stands no chance of ever being integrated with the mainline kernel?  Or is it only binary blobs they don't like?  They really push hard the goal of getting everything promoted up to the mainline kernel. 

Of course if it's the case that the in-kernel hooks can be made generic between SystemTap (et.al.) and DTrace, then it doesn't matter anyway. 

        On DTrace envy 

        Posted Aug 29, 2007 20:06 UTC (Wed)
                               by  renox  (guest, #23785)
                              [ Link ] 

       &gt; Follow AHL's recipe (see his blog, linked to several times in this article)  

Well AHL's "recipe" is the one followed by FreeBSD I think to use DTrace and they won't integrate DTrace in FreeBSDv7 because some of them have doubts about the legality of linking BSD code with CDDL headers. 

The issue would be of course the same for the Linux kernel. 

Is the legal issue real or not? Some say yes, some say no, I have really no clue.. 

Hopefully this legal mess will be cleared at some point, otherwise maybe Sun could relicense just the header under the BSD license to clear this mess once for all? 

        On DTrace envy 

        Posted Aug 7, 2007 22:51 UTC (Tue)
                               by  bgregg  (guest, #46639)
                              [ Link ] 

      Great article. I have some points to add from by background as a customer using DTrace, writing most of the scripts in the DTraceToolkit, and more recently joining Sun. 

 making this tool usable by a much wider set of system administrators   

This is also important with DTrace, which I've helped encourage by creating a collection of scripts called the DTraceToolkit  DTraceToolkit  (inspired by the SE Toolkit), which also contains man pages, example files, notes, and a list of one-liners. It would be great if regular sysadmins wrote their own scripts, but if they don't have the time or skill to do that, then using the DTraceToolkit is better than not using DTrace. People can also use the scripts and one-liners in the toolkit as examples from which to learn DTrace. 

Another way to reach a larger audience for DTrace is the  DTrace Topics wiki , where I hope to write documentation specific to different roles (sysadmin, DBA, etc). This is in addition to the Dynamic Tracing Guide on docs.sun.com, which (DTrace aside) is an example of outstanding technical documentation. 

   SystemTap's language, instead, has conditionals, loops, and the ability to define functions.   

Loops keep being mentioned as a feature of SystemTap's language, perhaps as it's a well known programming construct from other languages. If you write a few hundred DTrace scripts, you'll discover that loops aren't actually that important - perhaps 1 in 40 scripts that I write I think that loops would be nice, then use a workaround. If they did become more important, I imagine they could be added after carefully addressing safety concerns. 

As for functions: again, sounds nice, but write a few hundred DTrace programs and note how many times you wanted them. Most DTrace scripts are short, a dozen lines or so; and the DTrace providers make concise abstractions available that shouldn't need too much digging to get to what you want (such as needing functions or loops). There are also workarounds for functions, such as using #defines.  

So not having loops or functions would, for other languages, be a big deal. It isn't really the case here, at least in my experience. 

  DTrace has the ability to work with user-space probes.   

This is a big deal; it is allowing providers to be created for languages such as Java, JavaScript, Ruby, Python, etc, and is what makes DTrace complete. DTrace is about observing your application as it runs and interacts with the system libraries, syscalls, kernel and device drivers - the entire software stack. This means if a customer has a performance issue, almost anywhere, DTrace can find it. This is the miracle solution to performance disputes - the application developers, database vendor and os vendor can all use the same tool and see the same numbers. 

A while back I wrote a  JavaScript DTrace provider , and now with much help from engineers at both Sun and Mozilla, we are looking at how best this could be made a permanent part of Mozilla. Great for JavaScript developers on either Solaris or MacOS, and Linux too - if it ports DTrace. 

        On DTrace envy 

        Posted Aug 8, 2007 0:30 UTC (Wed)
                               by  davem  (guest, #4154)
                              [ Link ] (6 responses)

      Built-in predefined trace points are a great tradeoff for a system 
whose pace of development is as glacial as Solaris's is. 

This same tradeoff simply does not traslate to the pace at which the 
linux kernel core innards are changing.  Any predefined trace points 
are going to have their placement and semantics change on a week to week 
if not a day to day basis.  It wouldn't help users at all. 

        On DTrace envy 

        Posted Aug 8, 2007 2:06 UTC (Wed)
                               by  bgregg  (guest, #46639)
                              [ Link ] 

        Any predefined trace points are going to have their placement and semantics change on a week to week if not a day to day basis. It wouldn't help users at all.  

I'm not sure I follow. That last sentence makes no sense to me at all. 

The vast majority of people I've met (and also taught DTrace to), either don't have the time to browse kernel source and figure things out, or the assumed programming knowledge to do so. For example, if you had an NFS server latency issue and no stable probes, how many regular users would be able to pick their way through the NFS code, plus the TCP/IP stack code, plus the filesystem cache code, plus the disk driver code (or abstractions), and finally be able to point to the source of the latency? This would span around 300,000 lines of kernel code (in Solaris). 

Stable probes allow users to trace complex systems without spending weeks untangling the code, or needing the programming background to understand the kernel. It also allows them to write stable scripts that will work for years to come. So, if the code is changing on a day to day basis, then there is an even  greater  need for these stable probes - if customers are expected to use the facility. 

  whose pace of development is as glacial as Solaris's is  

Much of the kernel does change frequently, such as the TCP/IP code. A couple of years ago I wrote some dynamic probe based scripts to monitor TCP traffic (tcpsnoop, etc), which have broken several times during those years due to kernel changes. It's a pain for customers trying to use them, and me trying to maintain them. The solution? I've written stable TCP/IP providers for Solaris (not yet putback), which will allow scripts similar to tcpsnoop to be both simple to write and robust. 

        On DTrace envy 

        Posted Aug 8, 2007 4:49 UTC (Wed)
                               by  comay  (guest, #46649)
                              [ Link ] 

       whose pace of development is as glacial as Solaris's is. 

Although I'm sure the number of commits into the Linux kernel source base is larger than that of OpenSolaris, to call the pace of development of OpenSolaris "glacial" is misleading.  Have you taken a

 look 

at the commits going into the OS/Net consolidation to see the changes taking place?

Of course, it might be interesting to break down the reason for all of the various commits taking place in both projects.  How many are new features and other enhancements?  How many are due to earlier changes introducing a regression or not being complete?

        On DTrace envy 

        Posted Aug 8, 2007 8:20 UTC (Wed)
                               by  njs  (subscriber, #40338)
                              [ Link ] (3 responses)

      I don't understand this.  The "predefined trace points" that DTrace provides are things like "thread blocked waiting on IO", "thread resumed after waiting on IO", "cpu went idle", "module was loaded", "page was swapped out".  Sure Linux changes really fast, but... is it going to stop having threads that block on IO, cpus that go idle, modules that get loaded, and pages that get swapped out?  Of course there is some work in maintaining high-level trace points like these as the actual code implementing the high-level events changes, but I don't see how it's an unreasonable amount of work, given the benefits. 

Right now on Linux there is no way to take an app and profile its disk seeks in the same way that oprofile lets us profile its i-cache misses; on Solaris dtrace makes it trivial, including userspace stack traces (another oprofile feature, so still a fair comparison). 

        On DTrace envy 

        Posted Aug 10, 2007 19:08 UTC (Fri)
                               by  oak  (guest, #2786)
                              [ Link ] (2 responses)

       &gt; Right now on Linux there is no way to take an app and profile its disk   
seeks in the same way that oprofile lets us profile its i-cache misses; 

Disk seeks can already be done, just not at the kernel side (what's cached  
and what's not).  There was a demonstration in GUADEC 2007 about a new  
(yet to be released) Valgrind extension which catches both file accesses  
(open etc) AND accesses to memory mapped files.  As Valgrind is a CPU  
simulator, it can catch these.  You can then have another tool that maps  
these file/mmap accesses to the actual disk geometry.  There was also UI  
for visualizing this. 

        Be careful of the implicit context 

        Posted Aug 29, 2007 20:18 UTC (Wed)
                               by  renox  (guest, #23785)
                              [ Link ] (1 responses)

      Sorry but 'can be done' is very different from 'can be done usefully' i.e. with DTrace a sysadmin can do the disk profile on a live production system, AFAIK Valgrind cannot do this.. 

Note that I'm not criticising Valgrind which is a very useful tool, just that the great selling point of DTrace is that it can do systemic tracing on live production system, so sure you can do many things with CPU simulators but it's quite out of topic/context.. 

        Be careful of the implicit context 

        Posted Mar 6, 2008 20:41 UTC (Thu)
                               by  oak  (guest, #2786)
                              [ Link ] 

IOgrind has been released a while ago.  Its advantage over live system 
profiling is that the results are deterministic whereas live system 
performance measurements can (according to Meeks) differ as much as 10% 
(on Linux) from run to run.  On a properly designed system, you don't 
(anymore) find that large bottlenecks, they are smaller.

If the bottlenecks are larger, I would assume one could catch them even 
with strace (just strace all applicable processes at the same time).

            Copyright &copy; 2007, Eklektix, Inc. 
            This article may be redistributed under the terms of the
               Creative
              Commons CC BY-SA 4.0  license 
            Comments and public postings are copyrighted by their creators. 
            Linux  is a registered trademark of Linus Torvalds 


