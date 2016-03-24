# Template for a repository in SFO Project

To get started with a brand new repository:

```shell
# Clone this repository
git clone https://github.com/sfo-project/dimension-flow-type-geometry-regiem.git

# Rename the repo the new name for the repository
mv dimension-flow-type-geometry-regiem the-new-name

# Change directory to the new repository
cd the-new-name

# Remove the git repository information and create a new one
rm -rf .git
git init

# Request the team to create a repository on Github
# Once that is created you can add a remote to your git
git remote add origin the-remote-url

# Once your permissions are setup you should be able to push it on github
git push origin master

# Happy SFOing
```
