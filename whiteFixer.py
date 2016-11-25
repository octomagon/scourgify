#!/usr/bin/env python

import magic
import os

wl = [line.rstrip('\n') for line in open('./wl.txt')]

for l in wl:
	if os.path.exists(l):
		print magic.from_file(l, mime=True) + "\t" + l
