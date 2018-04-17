import sys
import imp
import shutil
import errno
import json
from collections import defaultdict
import subprocess
"""Collect command-line options in a dictionary"""
dependencies=defaultdict(list)
def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

#copy files to a local folder and print , store gradle dependency information
def parse_gradle(path):

    p = subprocess.Popen(['gradle','dependencies'], cwd=path, stdout=subprocess.PIPE)
    out, err = p.communicate()
    out= out.splitlines()
    list=[]
    for i in out:
        if "+---" in i or "\---"in i:
            list.append(i)
    #print list

    for i in list:
        i= i.replace("\---","")
        formatted=i.split(":")
        dependencies[i]=formatted
    print  dependencies
    json.dump(dependencies, open("gradle_dep.json", 'w'))



if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)
    if '-project' in myargs:  # Example usage.
        print("Analyzing " + myargs['-project'])

    else:
        print "enter a project path after giving the option -project"
    if '-projecttype' in myargs:  # Example usage.
        if myargs['-projecttype'] == 'gradle':
            print("project type set to -> " + myargs['-projecttype'])
            parse_gradle(myargs['-project'])

    else:
        print "usage dependencygrab -project <path to project> -projecttype <type of project eg. gradle,mave,node,scala>"
    print "dependencies captured"