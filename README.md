# Template for a repository in SFO Project

To get started with a brand new repository:

## Initial Setup
This setup needs to be done for the very first time only:

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
```

## Virtual Environment
This environment will help us setup `Jupyter` for the project.

NOTE: Make sure to check `Add python to PATH` option for step below.

Download/install python3 from [here](https://www.python.org/downloads/).

### For Windows
```powershell
# Move to the repository you just cloned
cd the-new-name

# Ask python to create the virtual environment
python -m venv venv

# Activate the virtual environment
venv/Scripts/activate.bat

# You should see (venv) at the beginning of the command line:
# Example: (venv) C:\Temp\
```

### For Linux/OSX
```shell
# Move to the repository you just cloned
cd the-new-name

# Setup virtual environment via python3
pyvenv venv

# Active the virtual
source venv/bin/activate

# You should see (venv) at the beginning of the command line:
# Example: (venv) $
```

## Jupyter
Once you have your virtual environment activated then you can install `Jupyter` packages:

```shell
# Install jupyter python package from requirements file
pip install -r requirements.txt

# Install nbextensions manually
pip install https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip

# Start Jupyter notebook
Jupyter notebook
# It should open a web page on your browser on http://localhost:8888/tree
```

To enable extensions such as `spell-checker` go to http://localhost:8888/nbextensions and activate the extensions.

Request the team to create a repository on Github. Once that is created you can add a remote to your git:
```shell
git remote add origin the-remote-url
```

Once your permissions are setup you should be able to push it on github
```shell
git push origin master
```

Happy SFOing!
