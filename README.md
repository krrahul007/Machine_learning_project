# Machine_learning_project

### Software and account Requirement.

[1.Github Account](https://github.com/)

[2.Heroku Account](https://dashboard.heroku.com/login)

[3.VS Code IDE](https://code.visualstudio.com/download)

[4.GIT cli](https://git-scm.com/downloads)

### Creating conda enviroment

> conda create -p venv python==3.7 -y 

> conda activate venv

pip install requirements.txt 

To add files to Git git
'''
git add .
'''
OR \
'''
git add <file_name> 
'''
NOte: to igoore file or folder from git we can write name of file/folder to .gitignore file \

To check git status \
'''
git status
'''
to check all version maintained by git \
'''
git log
'''
to create version/commit all change by git \
'''
git commit -m "message:"
'''
to sent version/change to git \
'''
git push origin main
'''
To check remote url \
'''
git remote -v
'''


BUILD DOCKER IMAGE
'''
docker bulid -t <image_name>:<tagname> .

note

