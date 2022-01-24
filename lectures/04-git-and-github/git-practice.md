## This is how we will practice using git and GitHub

### Start

We'll find it handy to have our github username in an
[environmental variable](https://linuxhint.com/bash-environment-variables/):

```
export GHUSER=.... your github username ...
```
For example, for me this line would be:
```
export GHUSER=mjuric
```

Let's also set the default editor to
[`nano`](https://en.wikipedia.org/wiki/GNU_nano)
```
export EDITOR=nano
```
(if you're familiar with Emacs or Vi, feel free to use those instead).

### Basics

Let's create a directory, and a few (two) files in a directory:

```
mkdir "astr302-$GHUSER"
cd "astr302-$GHUSER"
echo "# My first ASTR 302 git repository" > README.md
echo "A file I do not whish to track" > AnotherFile.txt
```

I'll now create a git _repository_ where git will store snapshot of these
files, using the `git init` command:

```
git init
```

Now git will be able to "track" (store snapshots of) files in your current
directory.  You have to run `git init` only once for that directory.

Running `git init` created a directory named `.git`, where the snapshots will be stored:

```
ls -l .git
```

If you want to send someone all of your snapshots, it's as easy as copying
this directory (but there's a better way!  more later!)

Some more bookkeeping before we begin. We need to tell git what our name and preferred e-mail are:

```
git config --global user.email "mjuric@astro.washington.edu"
git config --global user.name "Mario Juric"
```

Now we can begin!  Git doesn't automatically snapshot the contents of
everything in the directory -- you have to tell it what is the set of files
echo "We’re practicing git here." >> README.mdI want it to snapshot.  We do this using the `git add` command.  For
example:

```
git add README.md
```

Note that at this point, we didn’t take a snapshot yet.  To do that, we use
the `git commit` command:

```
git commit
```

We've just created a snapshot, which is referred to as a _commit_ in git. 
Running `git commit` opens an editor in which you can write your _commit
message_.  This is meant to be a short description of the set of files (or
changes to files; we’ll show that in a minute).  It should remind you what
this snapshot is about (or tell others with whom you share this code) .

A convention for commit messages is to start with a short (\<50 characters)
one-line description of the reason for the commit, followed by a blank line,
followed by a longer paragraph (if needed).  See
[here](https://github.com/erlang/otp/wiki/writing-good-commit-messages) for
an example of how to write useful commit messages.

At this point, git has stored a single commit:

```
git log
```

We can also check the status of the files in my directory
```
git status
```

Let’s now edit the README.md and check the status again:
```
echo "">> README.md
echo "We’re practicing git here." >> README.md

git status
```

Committing all these changes:
```
git commit -a

git log
```

The `-a` argument to `git commit` tells git to commit all files it's
tracking and that have changed.  Alternatively, you could've ran `git add`
for every file individually, before running `git commit`.  Note that `git
add` serves two somewhat different purposes: it tells git which files to
track, but it also tells git which files to include into the next commit (as
an aside: these can be viewed as being one and the same...).

How to see the differences to a previous version:
```
git diff HEAD^
```

Git keeps a history of all commits.  The top of this history is called the
“HEAD”.  Adding a ^ means “one before head”.

Let’s make more changes:
```
git add AnotherFile.txt
git commit
```

And a prettier log may be shown with:

```
git log --oneline
```

### Branches

Imagine you have your program/analysis working reasonably well.  Now you
want to make some changes, but are worried you’ll mess up your code if they
don’t work out.  One way to do it is to just copy the whole directory into a
backup folder.

But git provides a facility — branches — to do it much more effectively. 
Creating a branch is like creating a parallel universe: what happens there
won’t affect what’s in the “main” universe (called the _master branch_). 
You're free to experiment with your changes on a different branch, and then
merge it back into _master_ once you're happy with the results.

Let's create and check out a branch named `new-feature`.

```
git branch

git branch new-feature
git branch

git checkout new-feature
git branch
\# A shorthand for create-and-checkout-a-branch is `git checkout -b new-feature`

```

Let’s make some edits:
```
echo "New edits" >> README.md
git status
git commit -a
```

See the history:
```
git log --oneline
```

Note how individual commits are identified by their _commit id_, a 40-character unique checksum such as 9e130f7b1ff3bfdcf23702ee18da5b7cdc8b6ef4 (a so-called SHA1 hash).

We can switch back to the `master` branch
```
git checkout master
cat README.md
```

Note how changes made on the `new-feature` branch are not visible here (as expected).

We can go ahead and also make some changes on master:
```
echo "Another tracked file" > AnotherFile.txt
git commit -a
```

Let's look at what all this looks like:
```
git log --oneline
git log --oneline --graph --all
```

Now we can bring the two sets of changes together: “merge” the two branches.

```
git merge new-feature
git log --oneline --graph --all
```

This is “branch & merge” technique is a powerful way to incrementally develop analyses or codes.

### Merge conflicts

Sometimes there are conflicting changes in two branches; this is what is known as a _merge conflict_.
When you attempt a merge with conflicting changes, git will stop and ask for your help.

To practice this, I've created a repository on GitHub that has a merge
conflict between two branches.  Let's `clone` it with:
```
cd ..
git clone https://github.com/uw-astr-302-w22/merge-conflict-demo.git
```
(n.b. we'll get to talking about GitHub, cloning, etc. in just a bit).

Now enter the cloned directory and run `git log`:
```
$ cd merge-conflict-demo
$ git log --graph --all --oneline
* d609eb5 (origin/feature/add) added an implementation of 'add'
| * 3dcfa3f (HEAD -> master, origin/master, origin/HEAD
) Change how we initialize the dict
|/  
* b4b4804 Initial implementation of 'mul'
```
You'll find there's a branch named `origin/feature/add`; let's try to merge it:
```
$ git merge origin/feature/add
Auto-merging calc
CONFLICT (content): Merge conflict in calc
Automatic merge failed; fix conflicts and then commit the result.
```
Run `git status` to see what's going on:
```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   calc

no changes added to commit (use "git add" and/or "git commit -a")
```
This tells us that the file `calc` has been modified on both branches and git cannot tell how to merge the changes. Let's see what's happened:
```
$ cat calc
#!/usr/bin/env python

import sys

def add(args):
	res = 0.0
	for arg in args:
		res += arg
	return res

def mul(args):
	prod = 1.0
	for arg in args:
		prod *= arg
	return prod

<<<<<<< HEAD
operators = dict(mul=mul)
=======
operators = {
	'mul': mul,
	'add': add
}
>>>>>>> origin/feature/add

if __name__ == "__main__":
	op = sys.argv[1]
	args = [ float(arg) for arg in sys.argv[2:] ]
	print(operators[op](args))
```

Notice the block enclosed in `<<<<` and `>>>>` -- this is the part where git
needs our help. Our destination branch advocates for one set of lines (those between
`<<<<` and `====`). The branch we're merging advocates for another (those between `====`
and `>>>>`).

We need to edit the file and choose one (let's choose the second option). 
After the edits, we have:
```
$ cat calc
#!/usr/bin/env python

import sys

def add(args):
	res = 0.0
	for arg in args:
		res += arg
	return res

def mul(args):
	prod = 1.0
	for arg in args:
		prod *= arg
	return prod

operators = {
	'mul': mul,
	'add': add
}

if __name__ == "__main__":
	op = sys.argv[1]
	args = [ float(arg) for arg in sys.argv[2:] ]
	print(operators[op](args))
```

and now let's finish the merge by committing:

```
git commit -a
```

The log now shows the merge:
```
$ git log --graph --all --oneline
*   1b9adf3 (HEAD -> master) Merge remote-tracking branch 'origin/feature/add'
|\  
| * d609eb5 (origin/feature/add) added an implementation of 'add'
* | 3dcfa3f (origin/master, origin/HEAD) Change how we initialize the 
dict
|/  
* b4b4804 Initial implementation of 'mul'
```

The best way to resolve merge conflicts is to avoid them in the first place
-- try not to introduce conflicting changes on different branches. However,
when they do happen, git will helpfully flag the problematic areas in the
files, while merging the others.

Note: this type of merge conflict resolution works only with text files.  If
there are conflicts between binary files (for example, two images), you will
have to choose one or the other.

### GitHub

How do we effectivelly share our repositories? This is where GitHub comes in.

First, let’s move back to our practice directory:
```
cd ~/astr302-$GHUSER
```

Then, let us create a new repository on github, (named astr302-$GHUSER, where
$GHUSER is your github username) and then:

```
git remote add origin https://github.com/$GHUSER/astr302-$GHUSER.git
git push --all -u
```

Sidenote: GitHub will recommend you a "remote address" starting with
`https://` by default -- unless you've set up [SSH
keys](https://help.github.com/articles/connecting-to-github-with-ssh/). 

The `push` command _copies_ all the commits stored on your local hard
drive repository (the `.git` directory) to GitHub.  Now refresh the page on
GitHub and explore what GitHub has to offer!

You can consider the copy on GitHub as your 'backup copy'.  Even if you lose
your entire computer, the commits of your files are safe and sound on
GitHub.

As you make new changes and new commits, you should occasionally push them _upstream_:
```
git push
```
This will push the commits from the current branch to the GitHub copy.  Make
it a habit to do this at least once a day.

### Collaboration with GitHub

`git` has a very different collaboration philosophy compared to (e.g.) Google
Docs.  In Google Docs, you edit in real time, seeing your and everyone
else's changes as they happen.  With `git`, you make a copy of the files
(a `clone` of the repository), make the edits on the copy, and use `git` 
(and/or GitHub) to merge them with the original. To signal that a set
of changes is ready to be merged into the original, you open a [Pull Request](https://help.github.com/articles/about-pull-requests/).

I'll begin by demonstrating a typical collaboration workflow on a toy
scientific calculator project that you can find at
https://github.com/uw-astr-302-w22/astr-302-scicalc.  Take note, as 
your Homework #2 will be very similar to what I'm about to do!

#### Practice

* Let's go back to our toy project `astr302-$GHUSER` and practice some more:
  - Please pair up.
  - Open an issue in your partner's repository, reporting that README.md is poorly formatted
  - Partner: Reply to the issue by politely agreeing it could use some
    fixing, and asking the reporter to send a pull request ("send a PR").
  - Contributor: Fork the repository by clicking the fork button on GitHub. 
    This will create a _clone_ of your partner's repository in your own
    GitHub account.  This clone contains a copy of everything in the
    original (usually referred to as 'upstream') repository.  GitHub also
    remembers where you forked the repository from.
  - Next, clone the fork to your computer. For example:
  ```
      git clone https://github.com/mjuric/astr302-mjuric
  ```
  This will now copy the repository from GitHub to your own computer, where you can freely edit it.
  - Make the edits -- edit README.md to add the newlines between each sentence.
  - Next, commit those changes:
  ```
      git commit -a
  ```
  - These changes have now been committed locally; push them back to GitHub as well:
  ```
      git push
  ```
  - On GitHub, create a pull request.
  - Partner: Review and accept the pull request.

* Let us come up with some other enhancement proposals for the scientific
  calculator (at least one per person!).  Don't make them too difficult
  (they will be your homework).  Open some issues at
  https://github.com/uw-astr-302-w22/astr-302-scicalc/issues.

## More things to try out

### Syncing with Upstream

  * When you pushed the ‘fork’ button on GitHub, the result was a full-fledged, but independent, clone of the original repository. If the original repository changes, you don’t get those changes by default. That way you can independently work on your own copy w/o worrying that someone will change things underneath you.
  * The issue is what to do when you *do* want changes from the upstream repository. That’s easy — use git’s capability to merge new changes from the upstream repository.

  * First, tell git about the upstream repository:

    git remote add upstream git@github.com:mjuric/astr302-mjuric

    You have to do this only once!

  * Now, say:

      git pull upstream master

    And this will fetch upstream changes.

    Now we can push it back:

      git push

    and view the changes on GitHub.

  * For more information:
    - https://help.github.com/articles/configuring-a-remote-for-a-fork/
    - https://help.github.com/articles/syncing-a-fork/

### Tagging, working with branches

Remembering a particular version — tagging:
```
git tag v1.0 bc54184ae2e8963eaad7c254f5b11c1153459ab0
git log --oneline --decorate --graph --all
```

Checking out a previous version:
```
git checkout v1.0
git checkout -b bugfix-1
```

Resetting master to a previous version:
```
git reset --hard v1.0
```

