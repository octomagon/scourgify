#!/usr/bin/env python

from os import listdir, geteuid
from os.path import isfile, join, expanduser, exists
from pprint import pprint
import os
import sys
import psutil


package_directory = os.path.dirname(os.path.abspath(__file__))
wl_file = os.path.join(package_directory, 'wl.txt')
daemonPaths = ["/Library/LaunchAgents", "/Library/LaunchDaemons", "/Library/StartupItems", "~/Library/LaunchAgents"]



def run():
	procs = runningProcs()

	print ""

	# Whitelist
	for p in notWhitelisted(procs):
		print p

        print ""

        showDaemons()


	# print str(len(evilProcs)) + " out of " + str(len(procs))


def runningProcs():
	processes = [proc.exe() for proc in psutil.process_iter()]
	processes = list(set(processes))
	processes.sort()

	return processes	
	

def showDaemons():
	for p in daemonPaths:
		d = expanduser(p)

		if exists(d):
			print p

			for f in filesInDir(d):
				if f != ".DS_Store":
					print "\t" + f


def notWhitelisted(procs):
	wl = [line.rstrip('\n') for line in open(wl_file)]

	filtered = []
	for p in procs:
		if p not in wl:
			filtered.append(p)	

	return filtered


def bailIfNotRoot():
	if not geteuid() == 0:
		sys.exit("You must be root to run this script.")


def filesInDir(path):
	return [f for f in listdir(path) if isfile(join(path, f))]



if __name__ == "__main__":
	run()
