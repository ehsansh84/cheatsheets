# Git cheatsheet by Ehsan Shirzadi

### Store credential:
`git config --global credential.helper store`

### Clone from a specific branch:
`git clone -b branch repo`

### Add files to git:
`git add file`

### Commit files:
`git commit -am "Message"`

### Push commits to repo:
`git push`

### Pull commits from repo:
`git pull`

### Change to another branch:
`git checkout branch`

### Merge dev into master:
```
git checkout master
git merge dev
```

### How to clear commit history for main branch:
```
git checkout --orphan latest_branch
git add -A
git commit -am "commit message"
git branch -D main
git branch -m main
git push -f origin main
```

### Shows wether remote and origin synced :
```
git remote show origin
```
### To sync data between remote and local:
```
git fetch
```

### Shows the log in form of graph one line percommit:
```
git log --graph --oneline --all
```
### To delete a remote branch:
```
git push --delete origin branch_name
```
### To delete a local branch:
```
git branch -d branch_name
```
### To close an issue in a commit use `Closes #1` in commit message. 1 is issue number

###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com
