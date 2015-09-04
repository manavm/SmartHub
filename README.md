### Repository for SmartHub

## Dependencies

The following python libraries need to be installed. First, install pip. Then, install the following dependencies:

```
pip install python-nest
pip install requests[security]
```

## Git
Guidelines to ensure proper Git workflow

To check the status of your repository:

```
git status
```

If your local branch is not in sync with the remote branch:

```
git pull origin <branch>
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

## Workflow

Each member will create their own branch when working on a new feature. 

To create a new branch:

```
git checkout -b <branch_name>
```

To make sure that your branch is synced with master:

First, make sure that there are no local changes.

```
git checkout master
git pull origin master
git checkout <feature_branch>
git merge master
git push origin <feature_branch>
```

Once you are ready to merge a feature branch with master, follow the procedures to push your local branch to remote:

```
git add <files>
git commit -m "Insert commit message here"
git push origin <branch>
```

Then, using the Github GUI, create a Pull request.
