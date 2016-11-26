#!/usr/bin/env python

import os, sys
import subprocess

daemonPaths = [
    "/Library/LaunchAgents",
    "/Library/LaunchDaemons",
    "/Library/StartupItems",
    "~/Library/LaunchAgents",
]

# any(item.startswith('qwerty') for item in myList)


def main():
    procs = getProcesses()
    procs = notWhitelisted(procs)

    for l in procs:
        print l

    print "" 

    showDaemons()


def notWhitelisted(procs):
    wl = [line.rstrip('\n') for line in open('./wl.txt')]

    filtered = []
    for p in procs:
        if p not in wl:
            filtered.append(p)

    return filtered


def getProcesses():
    ps = subprocess.Popen("ps -ax -eo comm", shell=True, stdout=subprocess.PIPE)
    procs = ps.stdout.read()
    ps.stdout.close()
    ps.wait()

    procs = procs.splitlines()
    procs = filter(lambda x: x.startswith('/'), procs)
    procs = list(set(procs))
    procs.sort()

    return procs


def showDaemons():
    for p in daemonPaths:
        print p

        for f in filesInDir(os.path.expanduser(p)):
            print "\t" + f


def filesInDir(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]



if __name__ == "__main__":
    main()
