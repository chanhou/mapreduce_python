#!/usr/bin/python

import sys

def reducer():

	index = {}
	oldKey = None

	for line in sys.stdin:

		data = line.strip().split("\t")

		if len(data) != 2:
			continue

		thisKey, this_index = data

		# print data

		if oldKey and oldKey != thisKey:
			if ( not( thisKey in index )):
				# index[thisKey] = []
				# print "ggg"
				index[thisKey] = []

			# print oldKey
			print "{0}\t{1}".format(oldKey, index[oldKey] )
			# print "{0}".format(index)
			# oldKey = thisKey
			# index = 0

		if oldKey is None:
			index[thisKey] = []

		oldKey = thisKey
		index[thisKey].append(int(this_index.replace('"', '',2)))

	if oldKey != None:
		print "{0}\t{1}".format(oldKey, index[oldKey])

def main():
	reducer()

main()
