# -----------------------------------------------------------------------------

import csv
import operator

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


for t in CARDTYPES:
    output.update( { t : [] } )
output = {'NOTYPE' : []}

with open("output.csv", "r") as allcards:
    with open("esper.csv", "r") as decklist:

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


        print(len(output))

        with open("cardlist.csv", "w") as outfile:

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

# -----------------------------------------------------------------------------
