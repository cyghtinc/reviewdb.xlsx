
GIT_REPO = r'C:\Users\Yaron Shamul\Documents\GitHub\reviewdb.xlsx\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

from git import Repo 
"""
import subprocess as cmd

cp = cmd.run("git config --global user.name 'cyghtinc'", check=True, shell=True)
cp = cmd.run("git config --global user.password 'git5git5'", check=True, shell=True)


cp = cmd.run("git add .", check=True, shell=True)
cp = cmd.run("git commit -m 'wasome'", check=True, shell=True)
cp = cmd.run("git push", check=True, shell=True)
"""

repo = Repo(GIT_REPO)
repo.git.add(update=True)
repo.index.commit(COMMIT_MESSAGE)
origin = repo.remote(name='origin')
origin.push()
