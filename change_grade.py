#!/usr/bin/env python

import re
import fileinput

def change_grade(arg_array):

	comments=""
	values=""

	for line in fileinput.input('-'):
		m = re.search(arg_array[1], line)
		values = line.rstrip().split(',')
		if m:
			values[3] = arg_array[2]
		print ",".join(values)
	return(values, comments)	

if __name__=='__main__':
	from sys import stderr,stdout,argv,exit

	if len(argv) != 3:
		stderr.write("Usage: change_grade.py STRING VALUE\n")
		exit(1)

	(values, comments) = change_grade(argv)
	stderr.write(comments)
