---
title: "Project_HyperKit_A_toolkit_for_embedding_hypervisor_capabilities_EBOL_"
source_url: https://github.com/moby/hyperkit
download_date: 2026-09-07
---

# Project_HyperKit_A_toolkit_for_embedding_hypervisor_capabilities_EBOL_

来源: https://github.com/moby/hyperkit



   GitHub - moby/hyperkit: A toolkit for embedding hypervisor capabilities in your application · GitHub 

       Skip to content 

      Navigation Menu                         Sign in                Appearance settings          Platform          AI CODE CREATION            GitHub Copilot  Write better code with AI            GitHub Copilot app  Direct agents from issue to merge              MCP Registry  Integrate external tools          DEVELOPER WORKFLOWS          Actions  Automate any workflow              Codespaces  Instant dev environments              Issues  Plan and track work            Code Review  Manage code changes              Code Quality  Enforce quality at merge          APPLICATION SECURITY          GitHub Advanced Security  Find and fix vulnerabilities            Code security  Secure your code as you build            Secret protection  Stop leaks before they start          EXPLORE     Why GitHub      Documentation          Blog          Changelog          Marketplace          View all features               Solutions          BY COMPANY SIZE     Enterprises      Small and medium teams      Startups      Nonprofits         BY USE CASE     App Modernization      DevSecOps      DevOps      CI/CD      View all use cases               BY INDUSTRY     Healthcare      Financial services      Manufacturing      Government      View all industries                View all solutions               Resources          EXPLORE BY TOPIC     AI      Software Development      DevOps      Security      View all topics               EXPLORE BY TYPE     Customer stories      Events &amp; webinars      Ebooks &amp; reports      Business insights      GitHub Skills             SUPPORT &amp; SERVICES     Documentation          Customer support          Community forum      Trust center      Partners          View all resources               Open Source          COMMUNITY          GitHub Sponsors  Fund open source developers          PROGRAMS     Security Lab          Maintainer Community          GitHub Stars          Archive Program             REPOSITORIES     Topics      Trending      Collections             Enterprise          ENTERPRISE SOLUTIONS          Enterprise platform  AI-powered developer platform          AVAILABLE ADD-ONS          GitHub Advanced Security  Enterprise-grade security features              Copilot for Business  Enterprise-grade AI features            Premium Support  Enterprise-grade 24/7 support             Pricing               Search  /            Sign in       Sign up                Appearance settings          

         You signed in with another tab or window.  Reload  to refresh your session. 
         You signed out in another tab or window.  Reload  to refresh your session. 
         You switched accounts on another tab or window.  Reload  to refresh your session. 

  Dismiss alert 

       {{ message }} 

               Uh oh!

                There was an error while loading.  Please reload this page . 

        moby

     / 

       hyperkit 

       Public 

 Notifications
      You must be signed in to change notification settings 

 Fork
     336 

          Star
            3.7k 

         Code 

         Issues 
           47 

         Pull requests 
           6 

         Actions 

         Projects 

         Security and quality 
           0 

         Insights 

  Additional navigation options 

          Code

          Issues

          Pull requests

          Actions

          Projects

          Security and quality

          Insights

                                                  master                         Branches            Tags                                          Go to file              Code                 Open more actions menu           Latest commit         History           623 Commits                  623 Commits       Folders and files      Name    Name     Last commit message      Last commit date                 .circleci                .circleci                              dtrace                dtrace                              go                go                              ocaml                ocaml                              src                src                              test                test                              .gitignore                .gitignore                              CODINGSTYLE.md                CODINGSTYLE.md                              CONTRIBUTING.md                CONTRIBUTING.md                              Info.plist.in                Info.plist.in                              LICENSE                LICENSE                              MAINTAINERS                MAINTAINERS                              Makefile                Makefile                              README.md                README.md                              README.xhyve.md                README.xhyve.md                              TESTING.md                TESTING.md                              app.entitlements                app.entitlements                              config.mk                config.mk                              go.mod                go.mod                              go.sum                go.sum                              hyperkit.1                hyperkit.1                              hyperkit.opam                hyperkit.opam                              hyperkitrun.sh                hyperkitrun.sh                              xhyve_logo.png                xhyve_logo.png                       View all files           Repository files navigation              README            Contributing            BSD-2-Clause license           More  items                           HyperKit         

  HyperKit  is a toolkit for embedding hypervisor capabilities in your application. It includes a complete hypervisor, based on  xhyve / bhyve , which is optimized for lightweight virtual machines and container deployment.  It is designed to be interfaced with higher-level components such as the  VPNKit  and  DataKit . 
 HyperKit currently only supports macOS using the  Hypervisor.framework . It is a core component of Docker Desktop for Mac. 
  Requirements        

 OS X 10.10.3 Yosemite or later 
 a 2010 or later Mac (i.e. a CPU that supports EPT) 

  Reporting Bugs        
 If you are using a version of Hyperkit which is embedded into a higher level application (e.g.  Docker Desktop for Mac ) then please report any issues against that higher level application in the first instance. That way the relevant team can triage and determine if the issue lies in Hyperkit and assign as necessary. 
 If you are using Hyperkit directly then please report issues against this repository. 
  Usage        
   $ hyperkit -h

  Building        
   $ git clone https://github.com/moby/hyperkit
$ cd hyperkit
$ make

 The resulting binary will be in  build/hyperkit  
 To enable qcow support in the block backend an OCaml  OPAM  development
environment is required with the qcow module available. A
suitable environment can be setup by installing  opam  and  libev 
via  brew  and using  opam  to install the appropriate libraries: 
   $ brew install opam libev
$ opam init
$ eval `opam env`
$ opam pin add qcow.0.11.0 git://github.com/mirage/ocaml-qcow -n
$ opam pin add qcow-tool.0.11.0 git://github.com/mirage/ocaml-qcow -n
$ opam install uri qcow.0.11.0 conduit.2.1.0 lwt.5.3.0 qcow-tool mirage-block-unix.2.12.0 conf-libev logs fmt mirage-unix prometheus-app

 Notes: 

  opam config env  must be evaluated each time prior to building
hyperkit so the build will find the ocaml environment. 

 Any previous pin of  mirage-block-unix  or  qcow 
should be removed with the commands: 
  $ opam update
$ opam pin remove mirage-block-unix
$ opam pin remove qcow  

  Tracing        
 HyperKit defines a number of static DTrace probes to simplify investigation of
performance problems. To list the probes supported by your version of HyperKit,
type the following command while HyperKit VM is running: 
    $ sudo dtrace -l -P 'hyperkit$target' -p $(pgrep hyperkit)

 Refer to scripts in dtrace/ directory for examples of possible usage and
available probes. 
  Relationship to xhyve and bhyve        
 HyperKit includes a hypervisor derived from  xhyve , which in turn
was derived from  bhyve . See the  original xhyve
README  which incorporates the bhyve README. 
 We try to avoid deviating from these upstreams unnecessarily in order
to more easily share code, for example the various device
models/emulations should be easily shareable. 
  Reporting security issues        
 The maintainers take security seriously. If you discover a security issue,
please bring it to their attention right away! 
 Please  DO NOT  file a public issue, instead send your report privately to
 security@docker.com . 
 Security reports are greatly appreciated and we will publicly thank you for it.
We also like to send gifts—if you're into Docker schwag, make sure to let
us know. We currently do not offer a paid security bounty program, but are not
ruling it out in the future. 
                 About   A toolkit for embedding hypervisor capabilities in your application   Resources         Readme          BSD-2-Clause license     Contributing         Contributing          Activity          Custom properties     Stars         3.7k  stars    Watchers         86  watching    Forks          336    forks      Report repository       Releases          Packages        Used by        Contributors        Languages                                 

   Footer 

        &copy; 2026 GitHub,&nbsp;Inc.

       Footer navigation 

             Terms 

             Privacy 

               Security 

               Status 

             Community 

             Docs 

             Contact 

      Manage cookies

        Do not share my personal information

    You can’t perform that action at this time.


