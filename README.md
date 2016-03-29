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

# Setup virtual environment via python3
pyvenv venv

# Active the virtual
source venv/bin/activate

# Install jupyter python package from requirements file
pip install -r requirements.txt

# Also update pip to the latest version
pip install -U pip

# Start jupyter notebook
# It should open a web page on your browser: http://localhost:8888/tree
jupyter notebook

# Request the team to create a repository on Github
# Once that is created you can add a remote to your git
git remote add origin the-remote-url

# Once your permissions are setup you should be able to push it on github
git push origin master

# Happy SFOing
```
