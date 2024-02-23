from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests"]), 
    license="MIT", 
    description="EDA example python package", 
    long_description=open("README.md").read(),
    include_requires=["numpy"], 
    url="https://github.com/Codecyp/mypackage.git", 
    author="Samuel Attivi", 
    author_email="Samuelattivi4@gmail.com"
    
)