# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
HOME = os.environ['HOME']
dirs = os.path.join(HOME, ".config/user-dirs.dirs")
places = dict()
def defaultplaces():
	for line in open(dirs):
		if line.startswith("#") is False:
			line = line.replace("$HOME", HOME)
			places[os.path.basename(
			tag(line)).strip(
			"\n")] = tag(
			line.strip(
			"\n"))
	return places
def tag(line, split=""):
	for j in line:
		if j == '"':
			continue
		split = split + j
	return split.split(
	"="
	)[1]

