from setuptools import setup, find_packages
from typing import List

#Declaring function for setup functions
DESCRIPTION = "This is my first ml project."
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file
    
    return : this function is going to return a list which contain name of libraries mentioned in
             requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name="housing-predictor",
    version='0.0.2',
    author='Rahul',
    description=DESCRIPTION,
    packages=find_packages(), #["housing"], return all folder name contain __init__.py
    install_requires=get_requirements_list()
        
)

