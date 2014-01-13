#!/usr/bin/python
import wrapper
import subprocess

##VARIABLES
#Github API base url
base_url = 'https://api.github.com/users/'
#url = 'https://api.github.com/users/chasiumen/repos'
#Github repo to push
repo = 'https://github.com/chasiumen/github-api-testing.git'
#working directory
wdir = '/Users/leox/github/github-api-testing/'
#commit command
date ='date +%Y%m%d'
proc= subprocess.Popen([date], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
(save, err) = proc.communicate()
save = save.strip()
ccmd = 'git commit -a --allow-empty-message -m \'' + save + '\''
#push to git
cmd = 'git push -u origin master'


##FUNCTION: Runs shell commads
def push2Github(cmd):
#    print cmd
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (r, err) = proc.communicate()
    return r


##USER INPUT
print 'Access to Github'
uin  = raw_input("Enter Github User ID>")
user = uin + '/'
url = base_url+user+'repos'

#print url

a = wrapper.git_api('test')
a.RepoNames(url)
a.totalNumberOfRepos(url)

##Github upload
add = push2Github('git add'+ wdir)
print add
commit = push2Github(ccmd)
r  = push2Github(cmd)
