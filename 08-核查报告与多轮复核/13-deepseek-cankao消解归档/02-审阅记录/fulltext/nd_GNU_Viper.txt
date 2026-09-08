---
title: "Viper"
source_url: https://www.gnu.org/software/emacs/manual/html_node/viper/
download_date: 2026-09-07
---

# Viper

来源: https://www.gnu.org/software/emacs/manual/html_node/viper/

 

 Top (Viper Is a Package for Emacs Rebels) 

  Viper  &para;   

 We believe that one or more of the following statements are adequate
descriptions of Viper:

 Viper Is a Package for Emacs Rebels;
it is a VI Plan for Emacs Rescue
and/or a venomous VI PERil.

 Technically speaking, Viper is a Vi emulation package for Emacs.  It
implements all Vi and Ex commands, occasionally improving on them and
adding many new features.  It gives the user the best of both worlds: Vi
keystrokes for editing combined with the power of the Emacs environment.

 Viper emulates Vi at several levels, from the one that closely follows Vi
conventions to the one that departs from many of them.  It has many
customizable options, which can be used to tailor Viper to the work habits
of various users.
This manual describes Viper, concentrating on the differences from Vi and
new features of Viper.

 Viper, formerly known as VIP-19, was written by Michael Kifer.  It is based
on VIP version 3.5 by Masahiko Sato and VIP version 4.4 by Aamod Sane.
About 15% of the code still comes from those older packages.

 Viper is intended to be usable without reading this manual; the defaults
are set to make Viper as close to Vi as possible.  At startup, Viper will
try to set the most appropriate default environment for you, based on
your familiarity with Emacs.  It will also tell you the basic GNU Emacs window
management commands to help you start immediately.

 Although this manual explains how to customize Viper, some basic
familiarity with Emacs Lisp is a plus.

 It is recommended that you read the Overview node.  The other nodes may
be visited as needed.

 Comments and bug reports are welcome.
 kifer@cs.stonybrook.edu  is the current address for Viper bug reports.
Please use the Ex command  :submitReport  for this purpose.

 Copyright &copy; 1995&ndash;2026 Free Software Foundation, Inc.

 Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with the Front-Cover Texts being &ldquo;A GNU Manual&rdquo;,
and with the Back-Cover Texts as in (a) below.  A copy of the license
is included in the section entitled &ldquo;GNU Free Documentation License&rdquo;.

 (a) The FSF&rsquo;s Back-Cover Text is: &ldquo;You have the freedom to copy and
modify this GNU manual.&rdquo;

 Table of Contents 

    1 Overview of Viper 

      1.1 Emacs Preliminaries  
      1.2 Loading Viper  
      1.3 States in Viper 

        1.3.1 Emacs State  
        1.3.2 Vi State  
        1.3.3 Insert State  
        1.3.4 Replace State  

      1.4 The Minibuffer  
      1.5 Multiple Files in Viper  
      1.6 Unimplemented Features  

    2 Improvements over Vi 

      2.1 Basics  
      2.2 Undo and Backups  
      2.3 History  
      2.4 Macros and Registers  
      2.5 Completion  
      2.6 Improved Search  
      2.7 Abbreviation Facilities  
      2.8 Movement and Markers  
      2.9 New Commands  
      2.10 Useful Packages  

    3 Customization 

      3.1 Rudimentary Changes  
      3.2 Key Bindings  
      3.3 Packages that Change Keymaps  
      3.4 Viper Specials  
      3.5 Vi Macros  

    4 Commands 

      4.1 Groundwork  
      4.2 Text Handling 

        4.2.1 Move Commands  
        4.2.2 Marking  
        4.2.3 Appending Text  
        4.2.4 Editing in Insert State  
        4.2.5 Deleting Text  
        4.2.6 Changing Text  
        4.2.7 Search and Replace  
        4.2.8 Yanking  
        4.2.9 Undoing  

      4.3 Display  
      4.4 File and Buffer Handling  
      4.5 Mapping  
      4.6 Shell Commands  
      4.7 Options  
      4.8 Emacs Related Commands  
      4.9 Mouse-bound Commands  

    Appendix A GNU Free Documentation License  
    Acknowledgments  
    Key Index  
    Function Index  
    Variable Index  
    Package Index  
    Concept Index  

Next:  Overview of Viper  &nbsp; [ Contents ][ Index ] 


