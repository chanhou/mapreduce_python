#!/usr/bin/python
import sys
import csv
import re

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	prev = []
	check = False
	for line in sys.stdin:

		# # YOUR CODE HERE
		# check = False
		# for i in range (len(line[4])):
		# 	if ( i+1 != len(line[4]) ):
		# 		if(line[4][i] == "." or line[4][i] == "!" or line[4][i] == "?"):
		# 			check = True
		# if (check): 
		# 	continue
		# writer.writerow(line)
		# print line
		# print "=================="
		data = line.strip().split("\t")
		# print "=================="
		# print len(data), data
		# print "=================="
# 42455
		if len(data) != 19:
			if len(data) == 5:
				if (check):
					# print prev
					qqq = prev[4].strip().split(" ")
					check = False
					for ddd in qqq:
						abc = re.match( r'.*(fantastic).*', ddd, re.IGNORECASE) #re.I
						if (abc):
							# print "=================="
							# print prev[0], ddd
							# print "******************"
							print "{0}\t{1}".format("fantastic", prev[0])
				prev = data
				check = True
			if len(data)==1 or len(data)==15:
				prev[-1] += data[0]
				# print "******************"
				# print prev

		else: # continuous length !=19 will failed
			# print prev
			# print check
			if (check):
				# print prev
				qqq = prev[4].strip().split(" ")
				check = False
				# print "******************"
				# print qqq
				# print prev[0], prev[4]

				for ddd in qqq:
					abc = re.match( r'.*(fantastic).*', ddd, re.IGNORECASE) #re.I
					if (abc): # fantastically
						# print "=================="
						# print prev[0], ddd
						# print "******************"
						print "{0}\t{1}".format("fantastic", prev[0])
			# print "-----------------"
			qqq = data[4].strip().split(" ")
			# print data[0], data[4]
			for ddd in qqq:
				abc = re.match( r'.*(fantastic).*', ddd, re.IGNORECASE)
				if (abc):
					# print "******************"
					# print data[0], ddd
					# print "******************"
					print "{0}\t{1}".format("fantastic", data[0])


		# 	print len(data), data
		# print "=================="
		# for ddd in data:
		# 	print ddd
		# print "=================="



# test_text = """\"\" \t\"\" \t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
# \"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
# \"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
# \"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
# \"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
# \"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
# """

# This function allows you to test the mapper with the provided test string
def main():
	# import StringIO
	# sys.stdin = StringIO.StringIO(test_text)
	mapper()
	# sys.stdin = sys.__stdin__

if __name__ == "__main__":
	main()