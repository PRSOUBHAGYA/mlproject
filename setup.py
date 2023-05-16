from setuptools import find_packages,setup
from typing import List

def getrequirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path,'r') as fo:
        requirements = fo.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements
    


setup(name='Machine Learning Project',
      version= '0.0.1',
      author= 'Soubhagya Pradhan',
      author_email= 'prsoubhagyaranjan1997@gmail.com',
      packages=find_packages(),
      install_requires = getrequirements('requirements.txt')
    )