---
description: most used git command line examples
---

# git command-line

## Config git global info

```sh
# config git global info
git --version
git config --global user.name "your_username"
git config --global user.email "your_email_address@example.com"
git config --global --list

# git指令不会跳转到新的界面，直接显示在命令下
git config --global core.pager ''

# specify a global exclusion list
git config --global core.excludesfile ~/.gitignore
```

## Git clone and remote

```sh
git clone <gitlab-url>
cd <project>

# add a remote source: name = devops, url = devops-clone-url
git remote add devops <devops-clone-url>
git remote -v

# push all local git history to remote source, commit number will be kept
git push devops --all
git push devops --tags

# clone all commit history if without depth
git clone —depth=1 —branch yuhua (git)
```

## Branches

### View branch

```sh
# view branches
git branch -v # -v "view current git branch"
git branch -a # -a "all branches(local and remote)"
git branch -vr # -r "remotely"
git describe --tags
```

### Fetch & Pull

```sh
# fetch and pull
git fetch -pP # fetch all
git pull
git pull origin "source-branch" # from origin pull source-branch
```

### Checkout

```sh
# create new branch and checkout
git checkout -b "branch"
git checkout "branch"
git checkout "git-tag"
git checkout "git-commit"
```

### Merge branch

```sh
# merge branch to master
git checkout master
git merge update-script
git push origin master # merge branch

git branch -d update-script # delete local branch
git push origin --delete update-script # delete remote branch
```

### Rebase branch

```sh
# rebase a branch to a specific branch/commit
git rebase <branch | commit>

# force push all commits in this branch, all commit number will change
git push -f origin branch

# if there is any conflict, fix it
git rebase --continue

# abort rebase
git rebase --abort
```

### Interactive rebase

[Interactive rebase](http://git-scm.com/book/en/Git-Tools-Rewriting-History) is your friend!

```bash
$ git rebase -i HEAD~5
```

> where `-i` is the interactive flag, and `HEAD~5` means include the last 5 commits in the interactive rebase.

When you get editor up as a result of issuing the above, take a look at the comment in the opened file:

```bash
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

The key bit for you is <mark style="color:green;">**If you remove a line here THAT COMMIT WILL BE LOST.**</mark>

So, delete the lines that reference the commits you want to be rid of, save and close, and git will handle the rest (you may have to fix some conflicts depending on the nature of the commit and the revert you're trying to delete).

It's important to note that if you have already pushed your code and others have pulled it, the above will not work as the commits will find their way back in there the next time someone who has your branch checked out does a push. The interactive rebase deletes the commits to the extent that there is no record of them, so the other clones do not know they have been deleted. Next time they push, they'll try and re-instate them as the local clones "see" that the origin does not have the objects (commits) that you have deleted.

### Rename branch

```sh
# start by switching to the local branch which you want to rename
git checkout "old branch"

# rename the local branch
git branch -m "new branch"

# push the local branch and reset the upstream branch
git push origin -u "new branch"

# delete the "old branch" remote branch
git push origin --delete "old branch"
```

### Delete branch

```sh
# delete branch
git branch -D "branch" # delete a local branch
git push origin --delete "your branch" # delete a remote branch
```

### Restore a deleted branch

```sh
# if you just deleted the branch, you'll see something like this in your terminal:
Deleted branch <your-branch> (was <sha>)

# find the 'sha' for the commit at the tip of your deleted branch 
git reflog

# to restore the branch
git checkout -b "branch" "sha"

# fatal: A branch named 'add-overheight-detection' already exists.
Just re-push your code using: git push origin <your-branch>
```

## Commit

### Push a commit

```sh
git diff # view differences
git add "file path" # stage files
git reset "file path" # unstage files
git status # view stage status
git commit -m "commit info" # commit staged changes
git push origin "target branch" # push local commit to "origin.branch"

git diff "commit 1" "commit 2" "file" # compare two versions
```

### Force push commit

```sh
# re-commit, without changing commit-info
git commit --amend --no-edit
# re-commit with new commit message
git commit --amend

# force push to the last pushed commit
git push -f origin "target branch"
```

### Delete a pushed commit

```sh
git reset --hard "commit" # commit = the last commit you want to keep
git clean -f -d # optional
git push -f
```

### Recover local code

```sh
# revert to previous commit
git reset HEAD^ # reset to current head
git reset HEAD~1 # reset to 1 commit before the current head
git reset HEAD~2 # reset to 2 commits before the current head
git reset --hard # reset all changes
git reset --soft HEAD^ # uncommit only, keep staged changes
git reset --hard HEAD^ # uncommit and reset changes
git reset --hard "commit" # recover to a specific commit
```

### Cherry pick

```sh
# append source commit to target commit
git checkout "target commit"
git cherry-pick "source commit"
git push origin "target branch"

# cherry pick from a merge commit
# -m 1 ==> pick changes from 1 commit before to the merge commit
git cherry-pick -m 1 39b48a6
```

## Manage `.gitignore` files

edit `.gitignore` to ignore files when using `git add`

```sh
# adding .DS_Store to that list
echo .DS_Store >> ~/.gitignore

# specify a global exclusion list
git config --global core.excludesfile ~/.gitignore

# remove any existing files from the repo, skipping over ones not in repo
find . -name .DS_Store -print0 | xargs -0 git rm --ignore-unmatch
```

## Submodule

```sh
# sync submodules
git submodule sync

# update to latest version
git submodule update --init --recursive
```

##
