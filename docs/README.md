# Item Stock Tracker Documentation

Item Stock Tracker currently has an API documentation that can be accessed by 
navigating to the following file. 

><center><b>docs/build/index.html</b></center>

However, if someone is interested in modifying the documentation, following steps needs
to be followed.

###Prerequisites
* sphinx-- [Download & Install setuptools for Python with sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
* sphinx-rtd-theme-- [Download & Install setuptools for Python with sphinx-rtd-theme](https://pypi.org/project/sphinx-rtd-theme/)

###Introduction
The API documentation is generated via a tool called 'sphinx'. Documentation was 
generated automatically based on the docstrings of each module. However, to have
more flexibility, original python module files were not used. Instead, a set of 
skeletons were fed into sphinx to generate the documentation. These skeletons can 
be found in the following directory.

><center><b>docs/skeletons</b></center>

They are replicas of original modules but only contain signatures and docstrings.

###How to modify API documentation
1. Navigate to `docs/skeletons` folder.
2. Edit the appropriate files with your indented changes.
3. Navigate to `docs/source` folder.
4. Delete all the `.rst` files <b>except</b> for the`index.rst`
5. Go back to `docs` folder.
6. Run `sphinx-apidoc -o ./source ./skeletons/code`
7. Run `$ Make clean` on Mac, `$ .\make.bat clean` on Windows
8. Run `$ Make html` on Mac, `$ .\make.bat html` on Windows
