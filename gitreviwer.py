

from github import Github
import pandas as pd  # openpyxl == 3.0.1

#local_contents = dframe = pd.read_excel("reviewdb.xlsx")#pd.read_excel("reviewdb.xlsx", dtype=str)

git_account = Github('cyghtinc', 'git5git5')
git_account = Github('44078df37a1af38e33ccdaa94a9b5a32210ad913')
repo = git_account.get_user().get_repo('reviewdb.xlsx')#('reviewdb.xlsx')

import git
import subprocess
subprocess.Popen("cd", cwd=r'C:\Users\Yaron Shamul\Documents\GitHub\reviewdb.xlsx') 
# pull from remote origin to the current working dir:
git.cmd.Git().pull('https://github.com/cyghtinc/reviewdb.xlsx','master')
#reviewdb = repo.get_contents("reviewdb.xlsx")
#print(reviewdb)
#repo.update_file(reviewdb.path, "commit message", str(local_contents), reviewdb.sha)
