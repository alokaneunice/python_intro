# command to create a file
touch file
# command to copy
cp file1 file2
# command to copy from one file to the other
cp file1 file2
# command to create a folder
mkdir folder1
# command to move a file to a folder
mv file1 file2 folder1
# command to create another folder
mkdir folder2
# command to remove a file
rm -rf file1
# command to remove a folder
rm -rf folder
# command to go back or unstage a commit in your repository
git reset commitname
# create a new branch
git branch branchname
# to switch to the new branch
git checkout newbranchname
# command to use vim
vi file1
# to save a file in vim
press i
click escape button
press (:wq!)

press enter
# command to view a file
cat file
# command not to save a file
press i
click escape button
press (:qa!)
#_____________________________________________________________
# git command
# to get the entire hitory of a project
git log
# to get untrack files
git status
# git command to add files
git add .
# git command to commit files
git commit -m "comment on what we did today"
# git command to push your code to repository
git push
# git command to change the remote repo url for pushing changes in a git repo
git remote set-url --push origin https://github.com/alokaneunice/python-flask-sqlite2.git
# to check if remote name or origin exists
git remote -v