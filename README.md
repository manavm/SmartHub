### Repository for Mobile Development for SmartHub

Guidelines to ensure proper Git workflow

To check the status of your repository:

```
git status
```

If your local branch is not in sync with the remote branch:

```
git pull origin <branch>
```

To create a new branch:

```
git checkout -b <branch_name>
```

## Pushing local branch to remote

If you'd like to commit all files:

```
git add -A
git commit -m "Insert commit message here"
git push origin <branch>
```

If you'd only like to commit particular files:

```
git add <files>
git commit -m "Insert commit message here"
git push origin <branch>
```
