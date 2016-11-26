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
    filtered = []

    for p in procs:
        if not p.startswith(wl):
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
		d = os.path.expanduser(p)

		if os.path.exists(d):
			print p

			for f in filesInDir(d):
				if f != ".DS_Store":
					print "\t" + f

def filesInDir(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]



wl = (
    '/Applications/App Store.app/',
    '/Applications/Automator.app/',
    '/Applications/Calculator.app/',
    '/Applications/Calendar.app/',
    '/Applications/Chess.app/',
    '/Applications/Contacts.app/',
    '/Applications/Dashboard.app/',
    '/Applications/Dictionary.app/',
    '/Applications/DVD Player.app/',
    '/Applications/FaceTime.app/',
    '/Applications/Font Book.app/',
    '/Applications/iBooks.app/',
    '/Applications/Image Capture.app/',
    '/Applications/iTunes.app/',
    '/Applications/Launchpad.app/',
    '/Applications/Mail.app/',
    '/Applications/Maps.app/',
    '/Applications/Messages.app/',
    '/Applications/Mission Control.app/',
    '/Applications/Notes.app/',
    '/Applications/Photo Booth.app/',
    '/Applications/Photos.app/',
    '/Applications/Preview.app/',
    '/Applications/QuickTime Player.app/',
    '/Applications/Reminders.app/',
    '/Applications/Safari.app/',
    '/Applications/Siri.app/',
    '/Applications/Stickies.app/',
    '/Applications/System Preferences.app/',
    '/Applications/TextEdit.app/',
    '/Applications/Time Machine.app/',
    '/Applications/Utilities/',
    '/bin/',
#    '/Library/Application Support/',
    '/Library/Audio/',
    '/Library/CoreMediaIO/',
    '/Library/Extensions/',
#    '/Library/Frameworks/',
    '/Library/Image Capture/',
#    '/Library/Internet Plug-Ins/',
    '/Library/Messages/',
    '/Library/Modem Scripts/',
    '/Library/PDF Services/',
    '/Library/Printers/',
    '/Library/Python/',
    '/Library/QuickLook/',
    '/Library/QuickTime/',
    '/Library/Ruby/',
    '/Library/Scripts/',
    '/Library/Spotlight/',
    '/Library/Widgets/',
    '/private/etc/',
    '/private/var/',
    '/sbin/',
    '/System/Library/',
    '/usr/libexec/',
    '/usr/sbin/',
)

if __name__ == "__main__":
        main()



