#!/usr/bin/env python

import magic
import os, pprint

wl = [line.rstrip('\n') for line in open('./wl.txt')]

pprint.pprint(wl)
exit()

for l in wl:
	if os.path.exists(l):
		print magic.from_file(l, mime=True) + "\t" + l
