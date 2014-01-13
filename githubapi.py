#!/usr/bin/python
import requests
import json
import sys


class git_api:
    def __init__(self, name):
        self.__name__ = name
        print 'Created git_api successfully'

    def RepoNames(self, url):
        r = requests.get(url)
        if (r.ok):
            data = json.loads(r.text or r.content)
            print '==========List of the Repos=========='
            print '(' + url + ')'
            #json_out = json.dumps(data, sort_keys=True, indent=4)
            for i in range(0, len(data)):
                print data[i]['name']
        else:
            print "Error: Unreachable to the host", 'url'
            sys.exit()

    def totalNumberOfRepos(self, url):
        r = requests.get(url)
        if (r.ok):
            data = json.loads(r.text or r.content)
            print 'Total number of Repo: ' + '[' + str(len(data)) + ']'

#url = 'https://api.github.com/users/chasiumen/repos'
#a = git_api('test')
#a.RepoNames(url)
#a.totalNumberOfRepos(url)
