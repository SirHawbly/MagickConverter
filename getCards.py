#!/usr/bin/env python3

# -----------------------------------------------------------------------------

import csv
import operator
import sys
import os.path

# -----------------------------------------------------------------------------

# CSV Fromat
# Count,Name,Type,Cost,Rarity,Price,Section
COUNT = 0
NAME = 1
TYPE = 2
MANA = 3
RARITY = 4
COST = 5
SECTION = 6

OUTHEADERS = ['COUNT','NAME','TYPE','MANA']
CARDTYPES = ["Artifact", "Conspiracy", "Creature", 
              "Enchantment", "Instant", "Land", 
              "Phenomenon", "Plane", "Planeswalker", 
              "Scheme", "Sorcery", "Tribal", 
              "Vanguard"]

# -----------------------------------------------------------------------------

def getopts(argv):
	# Empty dictionary to store key-value pairs.
	opts = {}  
	# While there are arguments left to parse...
	if not argv or len(argv) < 3:  
		print("txt2csv -> usage './text2csv allCards decklist'.")
		sys.exit()

	if not (os.path.isfile(argv[1])):
		print("txt2csv -> first given file does not exist.")
		sys.exit()

	if not open(argv[1], 'r'): 
		print("txt2csv -> first given file cannot be opened.")
		sys.exit()


	if not (os.path.isfile(argv[2])):
		print("txt2csv -> second given file does not exist.")
		sys.exit()

	if not open(argv[2], 'r'):
		print("txt2csv -> second given file cannot be opened.")
		sys.exit()

    # return filename
	return [argv[1], argv[2]]

# -----------------------------------------------------------------------------

files = getopts(sys.argv)

cardList = files[0]
deckFile = files[1]

name = files[1].split('.')
outputFile = "".join(name[:-1]) + "-decklist.csv"

output = {}

# -----------------------------------------------------------------------------

for t in CARDTYPES:
    output.update( { t : [] } )

output.update( {'NOTYPE' : []} )

# -----------------------------------------------------------------------------

with open(cardList, "r") as allcards:
    with open(deckFile, "r") as decklist:

        cards = list(csv.reader(allcards))
        deck  = list(csv.reader(decklist))
        entry = []
        linenum = 1

        for line in deck:
            # print(line)
            for card in cards:
                # print(card)
                if line[NAME] in card:
                    found = 0
                    # print(str(line) + " : " + str(card))
                    for t in CARDTYPES:
                        if t in line[TYPE]:
                            output[t] += [[line,card], ]
                            found = 1
                            break
                    if (found != 1):
                        output['NOTYPE'] += [[line,card], ]


        # print(len(output))

        with open(outputFile, "w") as outfile:

            out = csv.writer(outfile)

            for cardtype in output:

                output[cardtype].sort()
                for row in [[], [cardtype], ['------------']]:
                    out.writerow(row)

                output[cardtype].sort()
                for tup in (output[cardtype]):

                    line = tup[0]
                    card = tup[1]

                    inline = line[0:4] + card[3:] + line[4:]
                    # print('\ntup: ' + str(tup) + '\ninline: ' + str(inline) + '\n\n')

                    out.writerow(inline)

print("getCards -> complete, " + str(cardList) + " was outputted and modified into " + str(outputFile) + ".")

sys.exit()

# -----------------------------------------------------------------------------

