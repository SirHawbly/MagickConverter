#!/usr/bin/env python3

# -----------------------------------------------------------------------------

# Description:
#   takes a newline delimited file, outputs a csv file

# given a file like...
# INPUT FILE
# Name
# item
# item
#
# Name
# item
# ...

# create a csv like...
# OUPUT FILE
# Name,item,item
# ...

# -----------------------------------------------------------------------------

import csv
import sys
import os.path

# -----------------------------------------------------------------------------

def getopts(argv):
	# Empty dictionary to store key-value pairs.
	opts = {}  
	# While there are arguments left to parse...
	if len(argv) < 2:  
		return

	if not (os.path.isfile(argv[1])):
		print("txt2csv -> given file does not exist.")
		sys.exit()

	if not open(argv[1], 'rb'):
		print("txt2csv -> given file cannot be opened.")
		sys.exit()

    # return filename
	return argv[1]

# -----------------------------------------------------------------------------

# if there are headers in the file
HEADERS = ["NAME", "COST", "TYPE", "TEXT", "SET"]

# file to be opened
inputfile = getopts(sys.argv)
if (not inputfile):
	print("txt2csv -> please provide script with a valid file name.")
	sys.exit()


# create a name for the ouput, the same as input,
# except we pull off the extension and put a '.csv'
name = inputfile.split('.')
outputfile = "".join(name[:-1]) + ".csv"
	
# a set for the reformatted data
outputdata = []

# -----------------------------------------------------------------------------

with open(inputfile, "r") as cardfile:
    with open(outputfile, "w") as writefile:

        outwriter = csv.writer(writefile)
        entry = []

		# write out the headers for the file
        outwriter.writerow(HEADERS)

		# go through every line in the file, and 
        for row in cardfile:
			# if its a newline, create a new entry, and
			# put the old one into output data.
            if (row == '\n'):
                outputdata += [entry, ]
                entry = []

			# else we can put it into the current entry
            else:
                # print(row)
                # pass the row, minus the trailing newline
                entry += row[:-1],

		# for every card that was added to the ouput 
		# set, put it into the output file.
        for card in outputdata:
            # print(card[0])
            outwriter.writerow(card)

print("text2csv -> complete, " + str(inputfile) + " was reformatted into " + str(outputfile) + ".")
# end the program
sys.exit()

# -----------------------------------------------------------------------------

