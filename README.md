# Template for a repository in SFO Project

Please make sure to install the requirements first:
- [Github Desktop](https://desktop.github.com/) - Windows/OSX only
- [Python](https://www.python.org/downloads/) - Make sure to check `Add python to PATH` option during the installation process.

To get started with a **brand new** repository. Otherwise jump into `Virtual Environment` section.

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

### For Windows
Once you install Github Desktop it should add `Github Shell` shortcuts to your desktop. Please use that to do the following commands:
```powershell
# In case you have not cloned/downloaded the repository then use the following command:
git clone the-repository-url
# For example for 2D-flow-over-cylinder-laminar repository will be:
git clone https://github.com/sfo-project/2D-flow-over-cylinder-laminar

# Move to the repository you just cloned
cd the-repository-name
# For example for 2D-flow-over-cylinder-laminar repository
cd 2D-flow-over-cylinder-laminar

# Ask python to create the virtual environment
python -m venv venv

# Activate the virtual environment
venv/Scripts/activate.bat

# You should see (venv) at the beginning of the command line:
# Example: (venv) C:\Temp\
```

### For Linux/OSX
```shell
# In case you have not cloned/downloaded the repository then use the following command:
git clone the-repository-url
# For example for 2D-flow-over-cylinder-laminar repository will be:
git clone https://github.com/sfo-project/2D-flow-over-cylinder-laminar

# Move to the repository you just cloned
cd the-repository-name
# For example for 2D-flow-over-cylinder-laminar repository
cd 2D-flow-over-cylinder-laminar

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

## Add Remote
Request the team to create a repository on Github. Once that is created you can add a remote to your git:
```shell
git remote add origin the-remote-url
```

Once your permissions are setup you should be able to push it on github
```shell
git push origin master
```

Happy SFOing!
