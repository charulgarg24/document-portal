'''
there are some proejct and package that we can sue in the form of package,
but the project that we are creating is created by me , so nobody can use it as a package,
so here we do setup.py file so that our proejct convert into package 
and later we can host this project on pypi 
'''
from setuptools import setup, find_packages
setup(
    name="document_portal",
    author="Charul Agrawal",
    version="0.1",
    package=find_packages()
)