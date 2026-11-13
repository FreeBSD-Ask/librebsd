<!-- 网页存档／手册页源｜来源：https://gitweb.dragonflybsd.org/dragonfly.git/blob_plain/HEAD:/share/man/man7/committer.7｜抓取：2026-11-13｜roff 源去宏保留参数 -->

# committer(7) 手册页

## NAME

committer instructions and rules for DragonFly committers

## SETTING UP GIT

See development 7 on how to pull a fresh copy of the DragonFly git 1 repository.

Committers have to push to crater.dragonflybsd.org via ssh 1. If the system is set up to pull from a DragonFly mirror, a remote entry will have to be set up: git remote add crater \\ ssh://crater.dragonflybsd.org/repository/git/dragonfly.git

Your ~/.gitconfig should contain at least: [user] name = Your Name email = <login>@dragonflybsd.org

Alternatively, see the user.name and user.email variables in git-config 1.

## SSH DSA KEYS

The git repository machine is crater.dragonflybsd.org, and the DragonFly developer machine is leaf.dragonflybsd.org. We create an account for you on both machines and install your public SSH key to give you access.

Your crater account is set up for repository access only. It can only operate as a git slave and cannot be logged into. That is, crater.dragonflybsd.org is only used as part of git Cm push operations.

Your leaf account is a general developer account. Any DragonFly developer can have a leaf account, whether a committer or not. It can be useful as a developer rendezvous, however. For example, people upload kernel cores to leaf so other developers can look at them. You log into your leaf account with: ssh you@leaf.dragonflybsd.org

The rules for account use are in leaf Ap s MOTD. It is very important that you never install a password or create a SSH key pair on leaf to use to access other machines. Because non-committers can have leaf accounts, leaf is not considered a secure machine.

## TESTING COMMIT ACCESS

There is a directory called /usr/src/test/test. To test your commit access, try making a modification and committing a file in this directory. Try to push the commit to crater afterwards. cd /usr/src/test/test (edit something) git commit file_you_edited git push crater

## COMMITTING REAL WORK

Make modifications as needed. For example, edit files. Files and directories can just be added locally. They are stored in your local copy of the repository and then synchronized with crater Ap s repository when you git Cm push. When adding new files make git aware of them like this: git add filename git commit filename

To actually push your changes to the repository on crater, use: git push crater

To merge bug fixes to other branches (MFC), use git Cm cherry-pick: git checkout -b rel2_2 crater/DragonFly_RELEASE_2_2 git cherry-pick <commit> git push crater rel2_2:DragonFly_RELEASE_2_2

Do not set the default remote tag to origin. It is set to crater by default. This reduces instances where accidental commits or repository operations are made on the master repository.

It is recommended to enable the MFC-detection commit hook, so that you are reminded of MFCing in case certain keywords are detected in the commit message. To do so, copy the hook into place: cp /usr/src/tools/commit-msg /usr/src/.git/hooks/commit-msg

## STRUCTURE OF COMMIT MESSAGES

As many git 1 tools display the first line of a commit message as a summary, structure your commit messages like this, if possible: One line summary of your change (less than 50 characters).

Maybe more text here describing your changes in detail (including issue tracker IDs etc).

To customize the commit template for DragonFly use: git config --add commit.template /usr/src/tools/gittemplate

## DISCUSSING COMMITTABLE WORK BEFOREHAND

Discussion prior to committing usually occurs on the kernel@, submit@, or bugs@ mailing lists and depends on the work involved. Simple and obvious work such as documentation edits or additions doesn't really need a heads up.

Simple and obvious bug fixes don't need a heads up either, other than to say that you will (or just have) committed the fix, so you don't race other committers trying to do the same thing. Usually the developer most active in a discussion about a bug commits the fix, but it isn't considered a big deal.

More complex issues are usually discussed on the lists first. Non-trivial but straight forward bug fixes usually go through a testing period, where you say something like:

Here is a patch to driver BLAH that fixes A, B, and C, please test it. If there are no objections I will commit it next Tuesday.

(usually a week, or more depending on the complexity of the patch).

New drivers or utilities are usually discussed. Committers will often commit new work without hooking it into the buildworld or buildkernel infrastructure in order to be able to continue development on it in piecemeal without having to worry about it breaking buildworld or buildkernel, and then they hook it in as a last step after they've stabilized it. Examples of this include new versions of GCC, updates to vendor packages such as bind, sendmail, etc.

## SOURCE OWNERSHIP

Areas within the repository do not belong to any committer. Often situations will arise where one developer commits work and another developer finds an issue with it that needs to be corrected.

All committed work becomes community property. No developer has a lock on any part of the source tree. However, if a developer is actively working on a portion of the source tree and you find a bug or other issue, courtesy dictates that you post to kernel@ and/or email the developer.

This means that, generally, if you do not see a commit to an area of the source tree in the last few weeks, it isn't considered active and you don't really need to confer with the developer that made the commit, though you should still post to the kernel@ mailing list and, of course, confer with developers when their expertise is needed.

One exception to this rule is documentation. If any developer commits new work, the documentation guys have free rein to go in and correct mdoc 7 errors. This is really a convenience as most developers are not mdoc 7 gurus and it's a waste of time for the doc guys to post to kernel@ for all the little corrections they make.

## CONFLICTS

On the occasion that a major code conflict occurs, for example if two people are doing major work in the same area of the source tree and forgot to collaborate with each other, the project leader will be responsible for resolving the conflict. Again, the repository is considered community property and it must be acceptable for any developer to be able to work on any area of the tree that he or she has an interest in.

## MAJOR ARCHITECTURAL CHANGES

This is generally Matt Dillon Ap s area of expertise. All major architectural changes must be discussed on the kernel@ mailing list and he retains veto power.

This isn't usually an issue with any work. At best if something doesn't look right architecturally he'll chip in with adjustments to make it fit in. Nothing ever really gets vetoed.

## SEE ALSO

git 1 Pq Pa devel/git, development 7
