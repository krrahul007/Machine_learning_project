from setuptools import setup, find_packages
from typing import List

#Declaring function for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Rahul Kumar"
DESCRIPTION = "This is my first ml project."

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file
    
    return : this function is going to return a list which contain name of libraries mentioned in
             requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), 
    install_requires=get_requirements_list()
        
)

