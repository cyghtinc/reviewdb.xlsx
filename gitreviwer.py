
PATH_OF_GIT_REPO = r'https://github.com/cyghtinc/reviewdb.xlsx.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'


import subprocess as cmd

cp = cmd.run("git add .", check=True, shell=True)
cp = cmd.run("git commit -m 'wasome'", check=True, shell=True)
cp = cmd.run("git push", check=True, shell=True)
