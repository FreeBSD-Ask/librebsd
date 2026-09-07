---
title: "J_In-kernel_WireGuard_is_on_its_way_to_FreeBSD_and_the_pfSense_router_"
source_url: https://arstechnica.com/gadgets/2021/03/in-kernel-wireguard-is-on-its-way-to-freebsd-and-the-pfsense-router/
download_date: 2026-09-07
---

# J_In-kernel_WireGuard_is_on_its_way_to_FreeBSD_and_the_pfSense_router_

来源: https://arstechnica.com/gadgets/2021/03/in-kernel-wireguard-is-on-its-way-to-freebsd-and-the-pfsense-router/

 

   In-kernel WireGuard is on its way to FreeBSD and the pfSense router - Ars Technica 

  Skip to content

     Ars Technica home 

            Sections

                Forum

                  Subscribe

                Search

                    AI

                    Biz &amp; IT

                    Cars

                    Culture

                    Gaming

                    Health

                    Policy

                    Science

                    Security

                    Space

                    Tech

                  Feature

                  Reviews

            AI

            Biz &amp; IT

            Cars

            Culture

            Gaming

            Health

            Policy

            Science

            Security

            Space

            Tech

      Forum

        Subscribe

           Story text 

           Size 

   Small 
   Standard 
   Large 

 Width
       * 

   Standard 
   Wide 

 Links 

   Standard 
   Orange 

     * Subscribers only  
    &nbsp;&nbsp; Learn more 

            Pin to story

       Theme 

                HyperLight

                Day & Night

                Dark

                System

       Search 

    Sign In

            Sign in dialog...

      Sign in

    strange bedfellows

      In-kernel WireGuard is on its way to FreeBSD and the pfSense router

      WireGuard probably won&#8217;t make it into 13.0-RELEASE, but 13.1 seems very likely.

    Jim Salter

  –

  Mar 15, 2021 6:39 pm

     |   

    188

      FreeBSD is getting its own in-kernel WireGuard module in the near future, thanks to a sponsored code contribution from Netgate, followed by additional code and review from Jason Donenfeld and several FreeBSD and OpenBSD developers.

          Credit:

          WireGuard / Jim Salter

      FreeBSD is getting its own in-kernel WireGuard module in the near future, thanks to a sponsored code contribution from Netgate, followed by additional code and review from Jason Donenfeld and several FreeBSD and OpenBSD developers.

          Credit:

          WireGuard / Jim Salter

       Text
        settings 

             Story text 

           Size 

   Small 
   Standard 
   Large 

 Width
       * 

   Standard 
   Wide 

 Links 

   Standard 
   Orange 

     * Subscribers only  
    &nbsp;&nbsp; Learn more 

            Minimize to nav

           This morning, WireGuard founding developer Jason Donenfeld  announced  a working, in-kernel implementation of his WireGuard VPN protocol for the FreeBSD 13 kernel. This is great news for BSD folks—and users of BSD-based routing appliances and distros such as  pfSense  and  opnSense . 
 If you&#8217;re not familiar with WireGuard, it establishes connections more quickly than traditional VPNs like OpenVPN. It&#8217;s also, in our personal experience, overwhelmingly more reliable when managing large numbers of connections. Your author used to spend several hours a month shelling into machines and manually re-establishing broken OpenVPN tunnels, even  after  writing watchdog scripts to attempt to detect and re-establish them automatically—tearing it all out and replacing this several-hundred-machine-monitoring network with WireGuard-based infrastructure cut that down to &#8220;zero hours per month.&#8221; 
 In addition to performance and reliability, WireGuard brings modern protocols, versioned crypto that literally cannot be set up incorrectly, and a far cleaner, lighter codebase than most competitors—Linus Torvalds once declared it &#8220;a work of art&#8221; by comparison to OpenVPN and IPSec. 
 Politics in the kernel 
 Although WireGuard  landed  in the Linux kernel first, its inclusion in FreeBSD&#8217;s kernel has long been on the general roadmap. In February 2020, FreeBSD developer Matt Macy pushed the first WireGuard-related  commit  to FreeBSD. Macy&#8217;s work was directly commissioned by Netgate, the company behind the BSD-based pfSense router distribution. 
 After nearly a year&#8217;s work, Macy&#8217;s port was  imported  to the kernel scheduled for FreeBSD 13.0-RELEASE, which is expected to launch in 15 days. Unfortunately, there was a problem—after WireGuard&#8217;s own Jason Donenfeld reviewed it alongside several FreeBSD and OpenBSD developers, it was judged  unready  for prime time: 
  I imagined strange Internet voices jeering, “this is what gives C a bad name!” There were random sleeps added to “fix” race conditions, validation functions that just returned true, catastrophic cryptographic vulnerabilities, whole parts of the protocol unimplemented, kernel panics, security bypasses, overflows, random printf statements deep in crypto code, the most spectacular buffer overflows, and the whole litany of awful things that go wrong when people aren’t careful when they write C.  

          This, understandably, presented a major problem for Donenfeld—although the WireGuard protocol itself is open source, there is more to a project than its code. Much of what propelled WireGuard&#8217;s meteoric rise in the first place is its brevity and code correctness, as assessed by Linux founder Linus Torvalds and reflected by the project&#8217;s reliability and lack of major flaws since becoming popular. A less than stellar implementation in FreeBSD could damage WireGuard&#8217;s brand—possibly irrevocably. 
 This left the FreeBSD port caught between a rock and a hard place—Donenfeld believed that the Netgate-sponsored code wasn&#8217;t ready for public consumption, but Netgate had already  announced  WireGuard support in the upcoming pfSense 2.5. 
 Mindful of Netgate&#8217;s exposed position, Donenfeld reached out to core FreeBSD developers Kyle Evans and Matt Dunwoodie, and the three dug in for a mad, week-long sprint to bring the problematic code up to par. Donenfeld describes one part of the process: 
  &#8230; there were 40,000 lines of optimized crypto implementations pulled out of the Linux kernel compat module but not really wired up correctly, and mangled beyond repair with mazes of Linux→FreeBSD ifdefs. I wound up replacing this with an 1,800 line file,  crypto.c , containing all of the cryptographic primitives needed to implement WireGuard.  
 This is very much in-line with Donenfeld&#8217;s usual coding  modus operandus —the reason WireGuard on Linux is 4,000 lines of code to OpenVPN&#8217;s 400,000 has much to do with stripping out inherited cruft and replacing it with just enough tightly focused code to do the job. 
 Unfortunately for Netgate, neither its sponsored code nor the week-long sprint by Donenfeld, Dunwoodie, and Evans seem likely to make it into FreeBSD 13.0. Presented with one deeply flawed port and another massively rushed overhaul, the FreeBSD team will most likely disable the WireGuard module entirely for 13.0-RELEASE and revisit for 13.1-RELEASE.

 Past controversy and present development 
 This collaboration clearly wasn&#8217;t all smooth sailing. Donenfeld expressed some frustration concerning Netgate&#8217;s failure to reach out to him directly, and—once he&#8217;d discovered their commissioned port—a perceived lack of interest in working together with him: 
  They didn&#8217;t bother reaching out to the project. That&#8217;s okay, I figured, I&#8217;ll reach out and see if I can help and coordinate. What followed over the next year was a series of poor communications – messages unanswered, code reviews ignored, that kind of thing. [&#8230;] at some point, whatever code laying around got merged into the FreeBSD tree and the developer tasked with writing it moved on.  
 This is a fairly typical open source conflict of interest—project A hires developer B to do x hours of work, but related project C says it takes x*2 hours of work to do it right. With good lines of communication and a minimum of ego, there&#8217;s usually a way to resolve this kind of conflict—but a  problematic history  like Netgate&#8217;s can easily damage those lines of communication. 
 Despite the back and forth, this port should be considered a classic success story for open source software development. Netgate&#8217;s initial developer commission got the ball rolling for an extremely valuable addition to the FreeBSD kernel. That commission in turn attracted interest and major follow-on work from both WireGuard and FreeBSD core developers, and it will eventually result in a high-quality, reliable WireGuard port for FreeBSD&#8217;s users—as well as Netgate&#8217;s. 

     Related Stories 

            WireGuard VPN review: A new type of VPN offers serious advantages

            Fewer lines of code, simpler setup, and better algorithms make a strong case.

            WireGuard VPN makes it to 1.0.0—and into the next Linux kernel

            It's a good day for WireGuard users—DKMS builds will soon be behind us.

    Listing image:

      WireGuard / Jim Salter

                  Jim Salter

       Former Technology Reporter 

                  Jim Salter

       Former Technology Reporter 

      Jim is an author,  podcaster , mercenary sysadmin,  coder , and father of three—not necessarily in that order.

    188 Comments

    Comments

     Forum view 

      Loading comments...

 Prev story  

            Next story           

        Most Read 

                 1. 
                 Tesla’s Cybercab has been deployed, and it’s already under investigation 

                 2. 
                 German company becomes first in Europe to launch fully commercial orbital rocket 

                 3. 
                 Nearly impossible? How Fairphone built the ethical, repairable Fairphone Gen 6+ 

                 4. 
                 Farmed salmon may not be as nutritious as it once was, new research suggests 

                 5. 
                 OpenAI agents discussed ways to escape their sandbox on public wiki 

       Customize 

         Ars Technica has been separating the signal from
          the noise for over 25 years. With our unique combination of
          technical savvy and wide-ranging interest in the technological arts
          and sciences, Ars is the trusted source in a sea of information. After
          all, you don’t need to know everything, only what’s important. 

         More
          from Ars

           About Us  
  Staff Directory  
  Ars Newsletters  
  General FAQ  
  Posting Guidelines  
  AI Policy  
  RSS Feeds  

         Contact 
           Contact us  
  Advertise with us  
  Reprints  

            Manage Preferences

      © 2026 Condé Nast. All rights reserved. Use of and/or
      registration on any portion of this site constitutes acceptance of our  User Agreement  and
       Privacy Policy and
        Cookie Statement  and  Ars
        Technica Addendum  and  Your
        California Privacy Rights . Ars Technica may earn compensation on
      sales from links on this site.  Read our
        affiliate link policy . The material on this site may not be
      reproduced, distributed, transmitted, cached or otherwise used, except
      with the prior written permission of Condé Nast.  Ad
        Choices 

 
