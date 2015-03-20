#!/usr/bin/env python
import sys
for line in sys.stdin.readlines():
	if str(sys.argv[1]) in line:
		line = str(sys.argv[1]) + ': ' +str(sys.argv[2])
	print line

