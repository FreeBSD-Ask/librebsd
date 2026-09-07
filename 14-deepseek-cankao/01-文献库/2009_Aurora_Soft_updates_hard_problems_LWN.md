---
title: "2009_Aurora_Soft_updates_hard_problems_LWN.md"
source_url: https://lwn.net/Articles/339337/
download_date: 2026-09-08
note: manual_direct
---

# 2009_Aurora_Soft_updates_hard_problems_LWN.md

来源: https://lwn.net/Articles/339337/

         

          Soft updates, hard problems [LWN.net] 

             LWN .net 
             News from the source  

           Content     Weekly Edition    Archives    Search    Kernel    Security    Events calendar    Unread comments       LWN FAQ    Write for us    
   Edition     Return to the Kernel page    

          User:     
		  Password:          |

             |

                 Log in   /
                 Subscribe   /
                 Register  

 Soft updates, hard problems 

 Did you know...? 

LWN.net is a subscriber-supported publication; we rely on subscribers
       to keep the entire operation going.  Please help out by  buying a subscription  and keeping LWN on the
       net.

            July 1, 2009 
            This article was contributed by Valerie Aurora 

If a file system discussion goes on long enough, someone will bring up
soft updates eventually, usually in the form of, "Duhhh, why are you
Linux people so stupid?  Just use soft updates, like BSD!"  Generally,
there will be no direct reply to this comment and the conversation
will flow silently around it, like a stream around an inky black
boulder.  Why is this?  Is it pure NIH (Not Invented Here) on the part
of Linux developers (and Solaris and OS X and AIX and...) or is there
something deeper going on?  Why are soft updates so famous and yet so
seldom implemented?  In this article, I will argue that soft updates
are, simply put, too hard to understand, implement, and maintain to be
part of the mainstream of file system development - while
simultaneously attempting to explain how soft updates work.  Oh, the
irony!

 Soft updates: The view from 50,000 feet 

Soft updates is one of a family of techniques for maintaining on-disk
file system consistency.  The basic problem is that a file system
doesn't always get shut down cleanly - think power outage or operating
system crash - and if this happens in the middle of an update to the
file system (say, deleting a file), the on-disk state of the file
system may be inconsistent (corrupt).  The original solution to this
problem was to run  fsck  on the entire file system to find and
correct inconsistencies; ext2 is an example of a file system that uses
this approach. (Note that this use of  fsck  - to recover from
an unclean shutdown - is different from the use of  fsck  to
check and repair a file system that has suffered corruption through
some other cause.)  

The  fsck  approach has obvious drawbacks
(excessive time, possible lost data), so file system developers have
invented new techniques.  The most popular and well-known is that of
logging or journaling: before we begin writing out the changes to the
file system, we write a short description of the changes we are about
to make (a journal entry) to a separate area of the disk (the
journal).  If the system crashes in the middle of writing out the
changes, we simply finish up the changes by replaying the journal
entry at the next file system mount.

Soft updates, instead, takes a two-step approach to crash recovery.  First, we
carefully order writes to disk so that, at the time of a crash (or any
other time), the
only inconsistencies are ones in which a file system structure is
marked as allocated when it is actually unused.  Second, at the next
boot after the crash,  fsck  is run in the background on a file
system snapshot (more on that later) to find and free file system
structures that are wrongly marked as allocated.  Basically, soft
updates orders writes to the disk so that only relatively harmless
inconsistencies are possible, and then fixes them in the background by
checking and repairing the entire file system.  The benchmark results
are fairly stunning: in common workloads, performance is often
within 5% of that of BSD's memory-only file system.  The older version
of FFS, which used synchronous writes and foreground  fsck  to
provide similar reliability, often runs 20-30% slower than the
in-memory file system.

 Step 1: Update dependencies 

The first part of implementing soft updates is figuring out how to
order the writes to the disk so that after a crash, the only possible
errors are inodes and blocks erroneously marked as allocated (when
they are actually free).  First, the authors lay out some rules to
follow when writing changes to disk in order to accomplish this goal.
From the paper:

   Never point to a structure before it has been initialized
  (e.g., an inode must be initialized before a directory entry
  references it). 

   Never re-use a resource before nullifying all previous pointers
  to it (e.g., an inode's pointer to a data block must be nullified
  before that disk block may be re-allocated for a new inode). 

   Never reset the old pointer to a live resource before the new
  pointer has been set (e.g., when renaming a file, do not remove the
  old name for an inode until after the new name has been written). 

Pairs of changes in which one change must to be written to disk before
the next change can be written, according to the above rules, are
called  update dependencies .  For some more examples of update
dependencies, take the case of writing to the first block in a file
for the first time.  The first update dependency is that the block
bitmap, which records which blocks are in-use, must be written to show
that the block is in use before the block pointer in the inode is set.
If a crash were to occur at this point, the only inconsistency would
be one bit in the block bitmap showing a block is allocated when it
isn't actually.  This is a resource leak, and must be fixed
eventually, but the file system can operate correctly with this error
as long as it doesn't run out of blocks.

The second update dependency is that the data in the block itself must
be written before the block pointer in the inode can be set (along
with the increase in the inode size and the associated timestamp
updates).  If it weren't, a crash at this point would result in
garbage appearing in the file - a potential security hole, as well, if
that garbage came from a previously written file.  Instead, a crash
would result in a leaked block (marked as allocated when it isn't)
that happens to contain the data from the attempted write.  As a
result, the write to the bitmap and the write of the data to the block
must complete (in any order) before the write that updates the inode's
block pointer, size, and timestamps.

These rules about ordering of writes aren't new for soft updates; they
were originally created for writes to a "normal" FFS file system.  In
the original FFS code, ordering of writes is enforced with synchronous
writes - that is, the ongoing file system operation (create, unlink,
etc.) waits for each ordered write to hit disk before going on to the
next step.  While the write is in progress, the operating system
buffer containing the disk block in question is locked.  Any other
operation needing to change that buffer has to wait its turn.  As a
result, many metadata operations progress at disk speed (i.e.,
murderously slowly).

 Step 2: Efficiently satisfying update dependencies 

So far, we have determined that synchronous writes on locked buffers
are a slow, painful way of enforcing the ordering of writes to the
file system.  But synchronous writes are overkill for most file system
operations; other than  fsync() , we generally don't want a
guarantee that the result has been written to stable storage before
the system call returns, and as we've seen, the file system code
itself usually only cares about the order of writes, not when they
complete.  What we want is a way to record changes to metadata, along
with the associated ordering constraints, and then schedule the actual
writes at our leisure.  No problem, right?  We'll just add a couple of
pointers to each in-memory buffer containing metadata, linking it to
the blocks it has come before and after.

Turns out there is a problem: cyclical dependencies.  We have to write
to the disk in block-size units, and each block can potentially
contain metadata affected by more than one metadata operation.  If two
different operations affect the same blocks, it can easily result in
conflicting requirements: operation A requires that block 1 be written
before block 2, and operation B requires that block 2 be written
before block 1.  Now you can't write out any changes without violating
the ordering constraints.  What to do?

Most people, at this point, decide to use journaling or copy-on-write
to deal with this problem.  Both techniques group related changes into
transactions - a set of writes that must take effect all at once - and
write them out to disk in such a manner that they take effect
atomically.  But if you are Greg Ganger and Yale Patt, you come up
with a scheme to record individual modifications to blocks (such as
the update to a single bit in a bitmap block) and their relationships
to other individual changes (that change requires this other change to
be written out first).  Then, when you write out a block, you lock it
and iterate through the records of individual changes to this block.
For each individual change whose dependencies haven't yet been
satisfied, you undo that change to the block, and then write out the
resulting block.  When the write is done, you re-apply the changes
(roll forward), unlock, and continue on your way until the next write.
The write you just completed may have satisfied the update
dependencies of other blocks, so now you can go through the same
process (lock, roll back, write, roll forward, unlock) for those
blocks.  Eventually, all the dependencies will be satisfied and
everything will be written to disk, all without running into any circular
dependencies.  This, in a nutshell, is what makes soft updates unique.

 Recording changes and dependencies 

So what does a record of a metadata change, and its corresponding
update dependencies, actually look like at the data structure level?
First, there are twelve (as of the 1999 paper) distinct structures to
record the different types of dependencies:

  Structure  Dependency tracked  
  bmsafemap  block/inode bitmaps  
  inodedep  inode  
  allocdirect  blocks referenced by direct block pointers  
  indirdep  indirect block  
  allocindir  blocks referenced by indirect block pointers  
  pagedep  directory entry add/remove  
  mkdir  new directory creation  
  dirrem  directory removal  
  freefrag  fragment to be freed  
  freeblks  block to be freed  
  freefile  inode to be freed  

Each kind of dependency-tracking structure includes pointers that
allow it to be linked into lists attached to the buffers containing
the relevant on-disk structures.  These lists are what the soft
updates code traverses during the roll-back and roll-forward
operations on a block being written to disk.  Each dependency
structure has a set of state flags describing the current status of
the dependency.  The flags indicate whether the dependency is
currently applied to the associated buffer, whether all of the writes
it depends on have completed, and whether the update described by the
dependency tracking structure itself has been written to disk.  When
all three of these flags are set (the update is applied to the
in-memory buffer, all its dependent writes are completed, and the
update is written to disk), the dependency structure can be thrown
away.

Page 7 of the  1999
soft updates paper [PDF]  begins the descriptions of
specific kinds of update dependency structures and their relationships
to each other.  I've read this paper at least 15 times, and each time
I when get to page 7, I'm feeling pretty good and thinking, "Yeah,
okay, I must be smarter now than the last time I read this because I'm
getting it this time," - and then I turn to page 8 and my head
explodes.  Here's the first figure on that page:

And that's only the figure from the left-hand column.  An only
slightly less complex spaghetti-gram occupies the right-hand column.
This goes on for six pages, describing each specific kind of update
dependency and its progression through various lists associated with
buffers and file system structures and, most importantly, other update
dependency structures.  You find yourself struggling through paragraphs like:

Figure 10 shows the structures involved in renaming a file. [Figure 10
looks much like the figure above.] The dependencies follow the same
series of steps as those for adding a new file entry, with two
variations.  First, when a roll-back of an entry is needed because its
inode has not yet been written to disk, the entry must be set back to
the previous inode number rather than zero.  The previous inode number
is stored in a  dirrem  structure.  The DIRCHG flag is set in
the  diradd  structure so that the roll-back code knows to use
the old inode number stored in the  dirrem  structure.  The
second variation is that, after the modified directory entry is
written to disk, the  dirrem  structure is added to the work
daemon's  tasklist  list so that the link count of the old
inode will be decremented as described in Section 3.9.

Say that three times fast!

The point is not that the details of soft updates are too complex for
mere humans to understand (although I personally wouldn't bet
against Greg Ganger being superhuman).  The point is that this
complexity reflects a lack of generality and abstraction in the design
of soft updates as a whole.  In soft updates, every file system
operation must be individually analyzed for write dependencies, every
on-disk structure must have a custom-designed dependency tracking
structure, and every update operation must allocate one of these
structures and hook itself into the web of other custom-designed
dependency tracking structures.  If you add a new file system feature,
like extended attributes, or change the on-disk format, you have to
start from scratch and reason out the relevant dependencies, design a
new structure, and write the roll-forward/roll-back routines.  It's
fiddly, tedious work, and the difficulty of doing it correctly doesn't
make it any better a use of programmer staff-hours.

Contrast the highly operation-specific design of soft updates to the
transaction-style interface used by most journaling and copy-on-write
file systems.  When you begin a logical operation (such as a file
create), you create a transaction handle.  Then, for each on-disk
structure you have to modify, you add that buffer to the list of
buffers modified by this transaction.  When you are done, you close
out the transaction and hand it off to the journaling (or COW)
subsystem, which figures out how to merge it with other transactions
and write them out to disk properly.  The user of the transaction
interface only has to know how to open, close, and add blocks to a
transaction, while the transaction code only has to know which blocks
are part of the same transaction.  Adding a new write operation
requires no special knowledge or analysis beyond remembering to add
changed blocks to the transaction.

The lack of generalization and abstraction shows up again when the
combination of update dependency ordering and the underlying disk
format poke out and cause strange user-visible behavior.  The most
prominent example shows up when removing a directory; following the
rules governing update dependencies means that a directory's ".."
entry can't be removed until the directory itself is recorded as
unlinked on the disk.  Chains of update dependencies sometimes
resulted in up to two minutes of delay between the return
of  rmdir() , and the corresponding decrement of the parent
directory's link count.  This can break, among other things, a simple
recursive " rm -rf ".  The fix was to fake up a second link
count that is reported to userspace, but the real problem was a
too-tight coupling between on-disk structures, the system to maintain
on-disk consistency, and the user-visible structures.  Long chains of
update dependencies cause problems elsewhere, during unmount
and  fsync()  in particular.

 Fsck and the snapshot 

But wait, there's more!  The second stage of recovery for soft updates
is to run  fsck  after the next boot, in the background using a
snapshot of the file system metadata.  File system snapshots in FFS
are implemented by creating a sparse file the same size as the file
system - the snapshot file.  Whenever a block of metadata is altered,
the original data is first copied to the corresponding block in the
snapshot file.  Reads of unaltered blocks in the snapshot redirect to
the originals.  Online  fsck  runs on the snapshot of the file
system metadata, finding leaked blocks and inodes.  Once it completes,
 fsck  uses a special system call to mark these blocks and
inodes as free again.

Online fsck implemented in this manner has severe limitations.  First,
recovery from a crash still requires reading and processing the
metadata for the entire file system - in the background, certainly,
but that's still a lot of
I/O. ( Freeblock
scheduling  piggybacks low-priority I/O, like that of a
background  fsck , on high-priority foreground I/O so that it
interferes as little as possible with "real" work, but that's cold
comfort.) Second, it's not actually a full file system check and
repair, it's just a scan for leaked blocks and inodes - expected
inconsistencies.  The whole concept of running  fsck  on a
snapshot file whose blocks are allocated from the same file system
assumes that the file system is not corrupted in a way that leaves
blocks marked as free when they are actually allocated.

 Conclusion 

Conceptually, soft updates can be explained concisely - order writes
according to some simple rules, track updates to metadata blocks,
roll-back updates with unsatisfied dependencies before writing the
block to disk, then roll-forward the updates again.  But when it come
to implementation, only programmers with deep, encyclopedic knowledge
of the file system's on-disk format can derive the correct ordering
rules and construct the associated data structures and web of
dependencies.  The close coupling of on-disk data structures and their
updates and the user-visible data structures and their updates results
in weird, counter-intuitive behavior that must be covered up with
additional code.

Overall, soft updates is a sophisticated, insightful, clever idea - and
an evolutionary dead end.  Journaling and copy-on-write systems are
easier to implement, require less special-purpose code, and demand far
less of the programmer writing to the interface.

             Index entries for this article  
              Kernel    Filesystems   
               Kernel    Soft updates   
               GuestArticles    Aurora (Henson), Valerie   

              to post comments

        Soft updates, hard problems 

        Posted Jul 2, 2009 7:12 UTC (Thu)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] (26 responses)

Wow... Humans computed those dependence graphs?  Yipe!  This feels a little like the "sufficient thrust" principle was applied:  With sufficient thrust, any pig will fly. 

I've programmed in assembly language on VLIW computers (and still do from time to time).  These computers allow you to schedule many instructions in parallel, but you have to take into account their resource usage, their latencies, and most importantly the dependences[*] between instructions.  For short programs (10s of instructions), this isn't too difficult to do.  For anything non-trivial, it very, very quickly gets unmanageable for a human. 

That's why we use code generation tools that know about the architecture and can compute and track the dependence chains for the programmer.  The programmer may still be picking the individual instructions, but the tool computes the actual dependence edges. 

And, when it comes time to enhance the architecture, the tool itself needs to be reconfigured.  Rather than manually write all the new rules, it makes more sense to provide higher level descriptions of how the features all relate, and let the tool figure out how to apply that to new code.  (This can be invaluable when exploring different potential tweaks to a CPU architecture.) 

I see this as a direct analog to the dependence discovery one needs to do on a filesystem to implement soft-updates, at least based on Valerie's description above. 

It seems like it ought to be possible to describe the on-disk format in some higher level form that allows a tool to work out the dependences between various updates automatically, dramatically improving the maintainability of the filesystem.  If nothing else, it seems like it ought to reduce the chance of error. 

Is the argument that the filesystem is fairly static, and therefore it's not worth the cost of building the tool the first time?  That could be short sighted.  For one, such a tool may open the way for another level filesystem optimization that focuses on reorganizing things to achieve different objectives:  reduce the depth of dependence chains, or minimizing the number of rewrites to sectors, or what-have-you.  Depending on the type of media you're writing to, different objectives become more or less important.  Rewrites are a bigger issue on SSDs due to wear leveling concerns, but seeking for reads is "free."  etc. etc. etc. 

[*]Yes, "dependences", not "dependencies."  Flip open a copy of Hennessy and Patterson if you disagree...  Call me a curmudgeon.  ;-)   

        Soft updates, hard problems 

        Posted Jul 2, 2009 7:16 UTC (Thu)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] (15 responses)

PS.  The dependencies vs. dependences thing isn't meant to be a dig at Valerie, since actually she's in very good company with folks that prefer proper English to the bastardized version that I learned when learning computer architecture.  :-)  My footnote was meant more as a "don't make fun of me because I talk funny and prefer it that way." 

Thank you for the well written article. 

        Soft updates, hard problems 

        Posted Jul 2, 2009 12:05 UTC (Thu)
                               by  rsidd  (guest, #2582)
                              [ Link ] (14 responses)

Not just "folks that prefer proper English": I'm pretty sure the more common term in mathematics, too, is "dependency" (as in "dependency graph") and not "dependence".  Cf. any number of well-known textbooks. 

        dependencies 

        Posted Jul 3, 2009 20:19 UTC (Fri)
                               by  giraffedata  (guest, #1954)
                              [ Link ] (12 responses)

(as in "dependency graph")

Well, it's logical in that sense.  The problem would be saying that the graph shows dependencies.

I think of dependency like connectivity and functionality, two other words computer people widely misuse because they find longer words sound smarter.  Connectivity is the degree or quality of being connected, so that a mesh network has more connectivity than a star.  But "I have connectivity to Chicago" is nonsense.  It's "I have a connection to Chicago."  Similarly, functionality is the degree or quality of being functional, so "I'm improving the functionality of the word processor" sensible, but "I'm adding undelete functionality" is not.  (It's "I'm adding undelete function").

So I think dependency is the degree or quality of being dependent.  A graph that shows how things depend on other things shows dependency.  But an instance of A depending upon B is dependence.

That's apparently not a traditional use of "dependency" -- traditionally, I think it just doesn't exist.  I just find it a logical construction of the word.

        dependencies 

        Posted Jul 3, 2009 20:31 UTC (Fri)
                               by  nix  (subscriber, #2304)
                              [ Link ] (10 responses)

"I'm adding undelete function" sounds desperately ungrammatical to me: at  
the very least it's missing an article. 

"I'm adding an undelete function" is grammatical but does *not* mean the  
same thing as 'I'm adding undelete functionality" (one has definite  
number, the other does not). 

Your statement about 'connectivity' is also nonsense: your  
sample "ungrammatical" sentence is perfectly grammatical. 

        dependencies 

        Posted Jul 3, 2009 22:00 UTC (Fri)
                               by  giraffedata  (guest, #1954)
                              [ Link ] (9 responses)

"I'm adding undelete function" sounds desperately ungrammatical to me:
at
the very least it's missing an article.

You don't recognize "function" as a mass noun?  Form follows function?  Some function is too costly provide?  Which half of the function shall we leave out?

You're right that "I have connectivity to Chicago" is grammatically correct, and it isn't nonsense as I said.  It's just a nonsensical phrasing for a statement that I have a connection, when there are plainer ways to phrase it.  Like saying that what distinguishes a window from a door is that a window has transparency.

        dependencies 

        Posted Jul 3, 2009 22:37 UTC (Fri)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] (8 responses)

        Time flies like an arrow; fruit flies like a banana.  -- Groucho Marx 
 Gotta love the chameleon-like nature of certain words in English.  "Function" is such a word.  In a computer context, it's use pretty much boils down to one of three of its many potential meanings: 
  A mathematical construct, such as f(x) = x 2 . 
 A self contained piece of code (in some sense modeled after the mathematical construct). 
 A synonym for the word "role."  
 In all three cases, the noun is not a mass noun.  It makes sense to use an article with "function" in the original example, regardless of which of the two senses ("piece of code" or "role") were intended. 
 Even in your example, "Form follows function," "function" does not act as a mass noun.  In that example, there is an implied "its" in front of both "form" and "function:"  "(Its) form follows (its) function."  And "its" can be replaced with any possessive:  "Fred's form follows Fred's function."  "The iPhone's form follows the iPhone's function." 
 And here we see that the "form follows function" example is bogus.  I imagine Forrest Gump would take no issue with "iPhone's form follows iPhone's function," but most people would be more comfortable saying "The iPhone's form follows the iPhone's function." 
 Here's a better test.  When there's "many" of something, we use "many" if it's a counting noun, and "much" if it's a mass noun.  ("Many chairs" vs. "much furniture.") So, by means of a concrete example:   Would you say complicated, overreaching software has: 
  Too much function. 
 Too much functionality. 
 Too many functions.   I reckon the latter two are accepted more widely than the first. 
 Remind me what this had to do with filesystems again?  I must thoroughly apologize for having highlighted the obscure trivia of "dependences" vs. "dependencies." 

        dependencies 

        Posted Jul 4, 2009 2:33 UTC (Sat)
                               by  giraffedata  (guest, #1954)
                              [ Link ] (7 responses)

      Hmm.  "Too much function" sounds perfectly fine to me, but maybe it's just something I made up.  I see the dictionary doesn't mention anything close to that meaning.  It also doesn't cover other uses I'm sure I've heard around the engineering world, like "we're testing function this week and performance next week," or "is the patch just for maintainability, or does it affect function?"

And with "form follows function," I don't see how an implied "its" fits in there.  I think an architect might well say, "I used to think just about form, but now I spend most of my time worrying about function."

But even if a certain feature of a device can't be considered a "piece of function," I can't see how it could be considered a "piece of functionality" either.

        dependencies 

        Posted Jul 4, 2009 2:48 UTC (Sat)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] (6 responses)

       At the very least,  "piece of functionality"  has nearly 100k hits on Google, generally referring individual features of a product or device.  In contrast,  "piece of function"  only gets 14,500, and most of those that I looked at are phrases where "function" modifies something else--ie. "piece of function  noun ". 
 *shrug* 

        dependencies 

        Posted Jul 4, 2009 3:30 UTC (Sat)
                               by  giraffedata  (guest, #1954)
                              [ Link ] (2 responses)

      Sure, but popularity is irrelevant to the point I'm making.  In fact, I mentioned in my first post that "functionality" is widely used this way - it's why I thought it was worth mentioning.  "Dependency" is quite a bit more popular than "dependence" in computer science discussions, but still wrong.  Other phrasings that are in majority use but wrong: IDE to mean ATA, DB-9 to mean DE-9, RJ45 to mean the 8 position modular connector we use with Ethernet.  "Could care less" to mean couldn't care less, gridlock to mean slow traffic, exponential growth to mean fast growth, steep learning curve to mean shallow learning curve.

        dependencies 

        Posted Jul 4, 2009 9:18 UTC (Sat)
                               by  SiB  (subscriber, #4048)
                              [ Link ] (1 responses)

 &gt; Sure, but popularity is irrelevant to the point I'm making.  

Language is supposed to serve people, not the other way.  What people use and understand defines language, not the dictionary.  The dictionary is supposed to record how people use language.  Language evolves.  Dictionaries need to follow that change. Popularity is all that matters.  (I'm not a native English speaker, but what I said should apply to all languages in use.) 

        dependencies 

        Posted Jul 4, 2009 18:12 UTC (Sat)
                               by  giraffedata  (guest, #1954)
                              [ Link ] 

Sure, but popularity is irrelevant to the point I'm making.

Language is supposed to serve people, not the other way. What people use and understand defines language, not the dictionary. 

I agree, but I don't know why you bring it up.  While I made the statement above about popularity, I didn't say anything about dictionaries except to say that the dictionary  doesn't  support my usage of "function."

Popularity is all that matters

 Language serves people best by being logical, consistent, precise, and easily expressive.  Those are not implied by popularity -- the number of people using a particular phrasing.  When one chooses between two phrasings to write, the relative number of times one has heard one or the other should be a fairly minor factor.

        dependencies 

        Posted Jul 4, 2009 12:12 UTC (Sat)
                               by  ajf  (guest, #10844)
                              [ Link ] (2 responses)

       At the very least, "piece of functionality" has nearly 100k hits on Google 

... and  definately  has nearly 14 million.

        dependencies 

        Posted Jul 4, 2009 12:26 UTC (Sat)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] (1 responses)

...many of which are people complaining that it's to be spelled "definitely," which incidentally gets nearly 10x as many hits (over 128M). 

How exactly have you invalidated the notion that the relative hit count between two directly comparable alternatives suggests which one is more likely to be correct?  I'd be worried if "definitely" got 100k hits but "definately" got 14M. 

        dependencies 

        Posted Jul 4, 2009 16:29 UTC (Sat)
                               by  ajf  (guest, #10844)
                              [ Link ] 

      Quite right, I should have compared it to the  definantly  count and concluded definately was "more likely to be correct" - which an utterly worthless conclusion, because both are still wrong. And that's exactly where your comparison leaves us.

        dependencies 

        Posted Jul 10, 2009 8:55 UTC (Fri)
                               by  Lennie  (subscriber, #49641)
                              [ Link ] 

I think the one about connectivity is easily explained. 

The provider says: we provide connectivity. 

The customer gets it connection and things: I guess now I have connectivity too. 

Well, maybe. :-) 

PS English is not my first language. 

        Soft updates, hard problems 

        Posted Jul 3, 2009 21:11 UTC (Fri)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] 

I recall specifically reading somewhere (but I cannot find it), that the person who coined "dependence"/"dependences"/"dependence graph" purposefully avoided the word "dependency" because he felt it had negative connotations. 

In any case, a directed graph that illustrates relationships such as "A depends on B" is a graph of dependence relationships.  Whether you call it a dependency graph or a dependence graph, and whether you call the edges in said graph dependencies or dependences doesn't bother me.  The former is more standard English, I believe, but the latter is fairly common in computer science textbooks.  I try to stick to the latter when using the computer science concept, but I admit it sounds funny. 

        Soft updates, hard problems 

        Posted Jul 3, 2009 4:03 UTC (Fri)
                               by  njs  (subscriber, #40338)
                              [ Link ] 

Yeah, ever since I first heard a real description of soft updates, I've been waiting to see an LWN article about some PhD student showing up on linux-kernel: "I haven't written soft updates code, but I wrote an OCaml program that wrote soft updates code, here is a patch for the filesystem and to add the program to MAINTAINERS..." 

        Soft updates, hard problems 

        Posted Jul 3, 2009 16:34 UTC (Fri)
                               by  quotemstr  (subscriber, #45331)
                              [ Link ] 

       It seems like it ought to be possible to describe the on-disk format in some higher level form that allows a tool to work out the dependences between various updates automatically, dramatically improving the maintainability of the filesystem. If nothing else, it seems like it ought to reduce the chance of error. Hear, hear! An even better example than your VLIW compiler would be the humble parser generator: have you  read  the incomprehensible muck that vomits forth from bison? However unintelligible, it works every time.
 The difference is that for VLIW instruction sets and parsers, respectively, we have a higher-level forms in which to express the problem: high-level languages and BNF grammars, respectively. What would the equivalent representation be for on-disk data structures? Does there exist today a general representation for data dependencies?

        Soft updates, hard problems 

        Posted Jul 3, 2009 21:16 UTC (Fri)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] (7 responses)

       An LJ user pointed me to some very interesting work in this area.  He wrote the following:   The Featherstitch filesystem uses clever formal systems techniques to derive softupdates ordering requirements and optimise away unnecessary disk operations. They've basically generalized and automated Kirk McKusick's one-off analysis of FFS's ordering requirements. This technology means softupdates is no longer difficult.  
 http://featherstitch.cs.ucla.edu/ 

 I thought I should share it over here. 

        Soft updates, hard problems 

        Posted Jul 3, 2009 21:27 UTC (Fri)
                               by  vaurora  (guest, #38407)
                              [ Link ] (3 responses)

Yes, I think Featherstitch is very interesting - I saw the paper when it was first presented and was impressed.  Would anyone be interested in reading an LWN article about it? 

        Soft updates, hard problems 

        Posted Jul 3, 2009 21:47 UTC (Fri)
                               by  jzbiciak  (guest, #5246)
                              [ Link ] 

Put my vote in the "Yes" column.  :-) 

        Soft updates, hard problems 

        Posted Jul 4, 2009 2:39 UTC (Sat)
                               by  dlang  (guest, #313)
                              [ Link ] 

definantly yes. 

it would either doucment a tool that could be used by kernel developers, or give us answers for the (now inevitable) swarm of questions about why don't the kernel devs just use featherstitch and implement soft updates ;-) 

is there a filesystem simple enough to show examples of it's analysis? (I'm thinking either ext2 of ext4 without journling as possibilities) 

        Featherstich 

        Posted Jul 4, 2009 5:16 UTC (Sat)
                               by  ewen  (subscriber, #4772)
                              [ Link ] 

Yes, I'd be keen to see an article on Featherstich.  The article on soft updates was good to see here too; I'd read the original paper on soft updates and admired the approach taken even though it seemed to have a "Level of Difficulty == Superhuman".  But there are many problems in computer science like that (write a modern operating system in assembly language, anyone?), for which the computer science answer is another layer of abstraction (and tools to translate back to the lower levels).  It feels like that's what we need here too: a way to express the dependency graph of all the operations such that both the code to do it, and the code to track the order in which things hit disk, is auto-generated. 

Ewen 

        Soft updates, hard problems 

        Posted Jul 4, 2009 0:20 UTC (Sat)
                               by  njs  (subscriber, #40338)
                              [ Link ] (2 responses)

Huh, and what's *really* cool about it is that they apparently export a userspace API for expressing IO write barriers. So with the featherstitch patch, you really can say things like "write these bytes to that file, and then rename it, but don't let the rename hit the disk until after the write has completed", except with arbitrarily complex dependency structures (!). 

I don't really care whether I'm using soft-updates or journalling, just so long as my disk is safe and things are reasonably fast, but real write barriers could totally change the performance profile of higher level apps. (Except for ACID databases, of course; I guess that's why historically no-one has cared about write barriers, because the only important high-level storage service was ACID databases.) 

        Soft updates, hard problems 

        Posted Jul 4, 2009 0:41 UTC (Sat)
                               by  njs  (subscriber, #40338)
                              [ Link ] (1 responses)

They got a bunch of the important stuff right, too... the "patchgroup" handles are basically fd's, they correctly prevent circular dependencies, they do the Right Thing for all different modes of fs operation (soft-updates: barriers use soft-update magic, full journaling: barriers optimize out, metadata journaling: barriers magically upgrade only those operations with dependencies to use full journaling), and check out this example from the paper: 

 &gt; The following command line would ensure that 'in' is not removed until all changes in the preceding sort have committed to disk: $ depend 'sort &lt; in &gt; out' 'rm in'  

(Of course, really you want shell support, so you can just say 'sort &lt;in &gt;out &&! rm in' or whatever.) 

Aw, man, now I'm all excited about a research project from 2007 that will never go anywhere in real life :-(. 

        Soft updates, hard problems 

        Posted Jul 4, 2009 12:06 UTC (Sat)
                               by  nix  (subscriber, #2304)
                              [ Link ] 

Seconded. This looks really nice... 

        Soft updates, hard problems 

        Posted Jul 2, 2009 12:07 UTC (Thu)
                               by  rsidd  (guest, #2582)
                              [ Link ] (2 responses)

As someone who used FreeBSD for a long time and have lurked on its mailing lists: softupdates and background fsck (which made their appearance around FreeBSD 5.0) proved notoriously unstable -- particularly the background fsck, which many developers warned against for a long time.  Bugs crop up to this day.  And, apparently, pretty much the only person who can debug it is Kirk McKusick.   

        Soft updates, hard problems 

        Posted Jul 3, 2009 9:41 UTC (Fri)
                               by  rsidd  (guest, #2582)
                              [ Link ] (1 responses)

       Replying to myself: FreeBSD itself has moved to journalling (via  gjournal ) since version 7.  I'm not sure what the defaults are on a new install, but (a) the default kernel  supports it , and (b) for best performance, disabling softupdates is  recommended .  
  So I have to assume that not only is this article spot-on, but FreeBSD itself has had enough of softupdates.  People who continue to bring it up on linux lists are probably not the people who are likely to be able to implement it, or appreciate the issues.  Thanks for the very readable clarification!

        Soft updates, hard problems 

        Posted Jul 12, 2009 8:47 UTC (Sun)
                               by  takeda  (guest, #59543)
                              [ Link ] 

Emmm... Long time FreeBSD user as well... 

Actually the problem with soft updates isn't really in FreeBSD itself, it's in hard drives which reorder writes for speed. That most often happens because of the caching. On top of that many drives lie about writing things to disk while in fact the data is still in cache. 

The fix for that is to disable cache on the disk (setting hw.ata.wc=0 on boot), unfortunately that reduces performance. 

As for FreeBSD switching to journaling, that's not enteirly true... gjournal is part of GEOM framework and gjournal was one of tools showing what GEOM can do (among with geli, gshsec etc). It also doesn't work exactly the same as other journaling since it works on a block level (GEOM work under the filesystem layer). 

If anything, the UFS might be replaced by ZFS. 

        Soft updates, hard problems 

        Posted Jul 2, 2009 13:56 UTC (Thu)
                               by  MisterIO  (guest, #36192)
                              [ Link ] (2 responses)

Interesting article. I had heard of soft-updates, but I never read anything specific about it. After reading this article, the first thing that came to mind is : "I'm glad that Linux doesn't have it". 

        Soft updates, hard problems 

        Posted Jul 2, 2009 16:07 UTC (Thu)
                               by  nix  (subscriber, #2304)
                              [ Link ] 

I don't see how anything that changes as rapidly as Linux does could  
possibly have it. While it is true the on-disk formats don't change so  
often, they *do* change: even ext2 has gained e.g. extended attributes. 

(IIRC, at least one of the BSDs moved away from softupdates specifically  
so they could add features to the FS without enormous pain.) 

Soft updates look like something that would be just the thing to use iff  
our programs were written by AIs so we didn't need to worry about  
implementation difficulty or degree of coupling. I've long thought that it  
looked like it had fallen through a wormhole from the future... 

        Soft updates, hard problems 

        Posted Jul 3, 2009 0:57 UTC (Fri)
                               by  bojan  (subscriber, #14302)
                              [ Link ] 

 &gt; "I'm glad that Linux doesn't have it"  

Check. Looks like very, very hard to maintain stuff. 

        Soft updates, hard problems 

        Posted Jul 2, 2009 15:17 UTC (Thu)
                               by  butlerm  (guest, #13312)
                              [ Link ] (1 responses)

Journalling doesn't have to be slow, or have synchronous write  
dependencies.  In fact the primarily purpose of journalling is to avoid  
synchronous write dependencies.   

The ones that are remaining are related to the fact that data writes are  
logically part of many meta data transactions, and performing certain meta  
data transactions (notably renames) is normally unsafe without waiting for  
the corresponding data write to complete first. 

That is not a necessary constraint, however, if special considerations are  
take to undo the problematic operations after an unclean shutdown.  Soft  
updates multi-versions individual meta data structures to solve the  
consistency problem - a more general, and easier to maintain technique is  
to use the journal to roll forward, and then individually roll back certain  
transactions to restore data - meta data consistency without unnecessarily  
discarding the good version of valuable files, etc. 

        Soft updates, hard problems 

        Posted Jul 2, 2009 15:26 UTC (Thu)
                               by  butlerm  (guest, #13312)
                              [ Link ] 

That should be "user visible synchronous write dependencies", with the  
exception of non-gratuitous fsync operations of course. 

        Is this recent or? 

        Posted Jul 8, 2009 20:31 UTC (Wed)
                               by  hingo  (guest, #14792)
                              [ Link ] (1 responses)

       "Valerie Aurora (formerly Henson)" 

Congratulations?

        Is this recent or? 

        Posted Jul 8, 2009 20:35 UTC (Wed)
                               by  corbet  (editor, #1)
                              [ Link ] 

      Details  over here .

        Soft updates, hard problems 

        Posted Jul 9, 2009 12:16 UTC (Thu)
                               by  ebichete  (guest, #42572)
                              [ Link ] (1 responses)

Yale Pratt ?! 

I think you mean Yale Patt. Brilliant and inspiring professor. I took one of his classes at University of Michigan before he moved to University of Texas, Austin. 

        Soft updates, hard problems 

        Posted Jul 9, 2009 23:03 UTC (Thu)
                               by  vaurora  (guest, #38407)
                              [ Link ] 

ARgh!!!  Yes, I meant Yale Patt, the co-author of the SOSP soft updates paper. 

Gnash.  Fume.  I'll get it fixed. 

Thanks for pointing it out! 

        Soft updates, hard problems 

        Posted Aug 13, 2013 21:25 UTC (Tue)
                               by  jonabbey  (guest, #2736)
                              [ Link ] 

Still one of the best articles on LWN.  Kudos, VA. 

            Copyright &copy; 2009, Eklektix, Inc. 

            Comments and public postings are copyrighted by their creators. 
            Linux  is a registered trademark of Linus Torvalds 


