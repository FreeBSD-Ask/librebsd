---
title: "draft-schoen-intarea-unicast-lowest-address_EBOL_2026-07-19"
source_url: https://datatracker.ietf.org/doc/draft-schoen-intarea-unicast-lowest-address/
download_date: 2026-09-07
---

# draft-schoen-intarea-unicast-lowest-address_EBOL_2026-07-19

来源: https://datatracker.ietf.org/doc/draft-schoen-intarea-unicast-lowest-address/



        draft-schoen-intarea-unicast-lowest-address-08 - Unicast Use of the Lowest Address in an IPv4 Subnet

         Skip to main content 

                    Datatracker

            Groups

     By area/parent 

            Apps &amp; Realtime

            General

            Internet

            Ops &amp; Management

            Routing

            Security

            Web and Internet Transport

          IESG  

            IAB

            IRTF

            IETF LLC

            RFC Editor

            Other

             Active AGs 

             Active Areas 

             Active Directorates 

             Active IAB Workshops 

             Active Programs 

             Active RAGs 

             Active Teams 

     New work 

            Chartering groups

            BOFs

            BOF Requests

     Other groups 

            Concluded groups

            Non-WG lists

            Documents

            Search

            Recent I-Ds

            Submit an Internet-Draft

        RFC streams

            IAB

            IRTF

            ISE

            Editorial

        Subseries

            STD

            BCP

            FYI

            Meetings

            Agenda

            Materials

            Floor plan

            Registration

            Important dates

            Request a session

            Session requests

            Upcoming meetings

            Upcoming meetings

            Past meetings

            Past meetings

            Meeting proceedings

            Other

            IPR disclosures

            Liaison statements

            IESG agenda

            NomComs

            Downref registry

            Statistics

                    I-Ds/RFCs

                    Meetings

            API Help

            Release notes

            System status

            Report a bug

                User

                    Sign in

                    Password reset

                    Preferences

                New account

        List subscriptions

                    IETF Lists

                IRTF Lists

                    IAB Lists

                    RFC-Editor Lists

                        Report a bug

                            Sign in

                             Javascript disabled?  Like other modern websites, the IETF Datatracker relies on Javascript.
                            Please enable Javascript for full functionality.

    Unicast Use of the Lowest Address in an IPv4 Subnet

     draft-schoen-intarea-unicast-lowest-address-08 

                Status

                Email expansions

                History

     Versions: 

                            00

                            01

                            02

                            03

                            04

                            05

                            06

                            07

                            08

        This document is an Internet-Draft (I-D).
        Anyone may submit an I-D to the IETF.
        This I-D is  not endorsed by the IETF  and has  no formal standing  in the
         IETF standards process .

         Document 
         Type 

     Expired Internet-Draft 
    (individual)

                    Expired &amp; archived

         Authors 

                  Seth David Schoen   
                    ,

                  John IETF Gilmore   
                    ,

                  David M. Täht   
                    ,

                  Michael J. Karels   

         Last updated 

            2025-12-25

                 (Latest revision 2025-06-23) 

                 Replaces 

                             draft-schoen-intarea-lowest-address 

            RFC stream

                (None)

                Intended RFC status

                        (None)

            Formats

                   txt

                   html

                   xml

                   htmlized

                   bibtex

                   bibxml

                    Stream

                        Stream state

                         (No stream defined) 

                        Consensus boilerplate

                            Unknown

                        RFC Editor Note

                                (None)

                        IESG

                            IESG state

                                Expired

                            Telechat date

                                    (None)

                            Responsible AD

                                    (None)

                            Send notices to

                                    (None)

                Email authors

                IPR

                References

                Referenced by

                Nits

                Nits v3

                Search email archive

                      This Internet-Draft is no longer active. A copy of
                    the expired Internet-Draft is available in these formats:  

                   txt

                   html

                   xml

                   htmlized

                   bibtex

                   bibxml

                        Abstract

                           With ever-increasing pressure to conserve IP address space on the
   Internet, it makes sense to consider where relatively minor changes
   can be made to fielded practice to improve numbering efficiency.  One
   such change, proposed by this document, is to increase the number of
   unicast addresses in each existing subnet, by redefining the use of
   the lowest-numbered (zeroth) host address in each IPv4 subnet as an
   ordinary unicast host identifier, instead of as a duplicate segment-
   directed broadcast address.

                        Authors

                              Seth David Schoen   

                              John IETF Gilmore   

                              David M. Täht   

                              Michael J. Karels   

                        (Note: The e-mail addresses provided for the authors of this Internet-Draft may no longer be valid.)

                 IETF 
                 IESG 
                 IAB 
                 IRTF 
                 IETF LLC 
                 IETF Trust 
                 RFC Editor 
                 IANA 
                 Privacy Statement 

                         About IETF Datatracker 

                            Version 12.74.0
                            (release - 9578423)

                     System Status 

                        Report a bug:
                         GitHub 

                             Email 


