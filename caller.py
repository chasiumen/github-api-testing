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


##USER INPUT
print 'Access to Github'
uin = raw_input("Enter Github User ID>")
user = uin + '/'
url = base_url+user+'repos'

#print url
a = wrapper.git_api('test')
a.RepoNames(url)
a.totalNumberOfRepos(url)
