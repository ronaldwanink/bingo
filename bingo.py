import random, numpy

# possible values for columns and card
B = range(1,16)
I = range(16,31)
N = range(31,46)
G = range(46,61)
O = range(61,76)
BINGO = numpy.arange(1,75)

assert len(B) == 15
assert len(I) == 15
assert len(N) == 15
assert len(G) == 15
assert len(O) == 15

#number of bingo cards and rounds that we are playing
numberOfCards = 10
numberOfRounds = 200000
NumberOfColumnBingos = 0
NumberOfRowBingos = 0

print('Playing '+str(numberOfRounds)+' rounds of bingo simulation with '+str(numberOfCards)+' cards')

# predefine the cards in memory
cards = []
for i in range(numberOfCards):
    cards.append(i)

for card in cards:
    cards[card] = [0]*25

# begin the round: fill cards with numbers
for round in range(numberOfRounds):

    print('-----------------------')
    print('Round '+str(round))
    for card in cards:
        j = random.sample(B,5)
        card[0] = j[0]
        card[1] = j[1]
        card[2] = j[2]
        card[3] = j[3]
        card[4] = j[4]

        j = random.sample(I,5)
        card[5] = j[0]
        card[6] = j[1]
        card[7] = j[2]
        card[8] = j[3]
        card[9] = j[4]

        j = random.sample(N,5)
        card[10] = j[0]
        card[11] = j[1]
        # card[12] = j[2]
        card[12] = 0
        card[13] = j[3]
        card[14] = j[4]

        j = random.sample(G,5)
        card[15] = j[0]
        card[16] = j[1]
        card[17] = j[2]
        card[18] = j[3]
        card[19] = j[4]

        j = random.sample(O,5)
        card[20] = j[0]
        card[21] = j[1]
        card[22] = j[2]
        card[23] = j[3]
        card[24] = j[4]

        # print('card = ')
        # print(f"{card[0]:3d} {card[5]:3d} {card[10]:3d} {card[15]:3d} {card[20]:3d}")
        # print(f"{card[1]:3d} {card[6]:3d} {card[11]:3d} {card[16]:3d} {card[21]:3d}")
        # print(f"{card[2]:3d} {card[7]:3d} {card[12]:3d} {card[17]:3d} {card[22]:3d}")
        # print(f"{card[3]:3d} {card[8]:3d} {card[13]:3d} {card[18]:3d} {card[23]:3d}")
        # print(f"{card[4]:3d} {card[9]:3d} {card[14]:3d} {card[19]:3d} {card[24]:3d}")
        # print()

    # check bingo cards for problems
    for card in cards:
        if len(card) != 25: raise 'Length of card not correct'
        for i in range(25):
            if card[i] <= 0 and i != 12: raise 'Number on card not correct'
            if card[i] > 75: raise 'Number on card too high'

    # predraw the balls
    draw = random.shuffle(BINGO)
    # print('draw = '+ str(BINGO))

    # pick ball by ball, update all bingo cards and check for Bingo!
    for ball in BINGO:

        # print('Ball '+str(ball))
        # update the cards, add 100 if the number is crossed on the card
        for card in cards:
            # print('card2 '+str(card))

            for i in range(25):
                if card[i] == ball: 
                    card[i] += 100
                    break
        
            # print('card3 '+str(card))

        # check if there is a column bingo
        RoundHadBingo = 0

        for card in cards:
            SomeoneYellsColumnBingo = 0
            SomeoneYellsRowBingo = 0
            # print('card4 '+str(card))
            # check if there is a column bingo
            if card[0] > 100 and card[1] > 100 and card[2] > 100 and card[3] > 100 and card[4] > 100: SomeoneYellsColumnBingo = 1
            if card[5] > 100 and card[6] > 100 and card[7] > 100 and card[8] > 100 and card[9] > 100: SomeoneYellsColumnBingo = 2
            if card[10] > 100 and card[11] > 100 and card[12] > 100 and card[13] > 100 and card[14] > 100: SomeoneYellsColumnBingo = 3
            if card[15] > 100 and card[16] > 100 and card[17] > 100 and card[18] > 100 and card[19] > 100: SomeoneYellsColumnBingo = 4
            if card[20] > 100 and card[21] > 100 and card[22] > 100 and card[23] > 100 and card[24] > 100: SomeoneYellsColumnBingo = 5

            # check if there is a row bingo
            if card[0] > 100 and card[5] > 100 and card[10] > 100 and card[15] > 100 and card[20] > 100: SomeoneYellsRowBingo = 1
            if card[1] > 100 and card[6] > 100 and card[11] > 100 and card[16] > 100 and card[21] > 100: SomeoneYellsRowBingo = 2
            if card[2] > 100 and card[7] > 100 and card[12] > 100 and card[17] > 100 and card[22] > 100: SomeoneYellsRowBingo = 3
            if card[3] > 100 and card[8] > 100 and card[13] > 100 and card[18] > 100 and card[23] > 100: SomeoneYellsRowBingo = 4
            if card[4] > 100 and card[9] > 100 and card[14] > 100 and card[19] > 100 and card[24] > 100: SomeoneYellsRowBingo = 5

            if SomeoneYellsColumnBingo > 0 or SomeoneYellsRowBingo > 0:
                if SomeoneYellsColumnBingo > 0: 
                    NumberOfColumnBingos += 1
                    # print()
                    # print('Ball '+str(ball)+' gave bingo on column '+str(SomeoneYellsColumnBingo)+' on card:')
                    # print(f"{card[0]:3d} {card[5]:3d} {card[10]:3d} {card[15]:3d} {card[20]:3d}")
                    # print(f"{card[1]:3d} {card[6]:3d} {card[11]:3d} {card[16]:3d} {card[21]:3d}")
                    # print(f"{card[2]:3d} {card[7]:3d} {card[12]:3d} {card[17]:3d} {card[22]:3d}")
                    # print(f"{card[3]:3d} {card[8]:3d} {card[13]:3d} {card[18]:3d} {card[23]:3d}")
                    # print(f"{card[4]:3d} {card[9]:3d} {card[14]:3d} {card[19]:3d} {card[24]:3d}")
                    # print()
                    RoundHadBingo = 1
                if SomeoneYellsRowBingo > 0: 
                    NumberOfRowBingos += 1
                    # print()
                    # print('Ball '+str(ball)+' gave bingo on row '+str(SomeoneYellsRowBingo)+' on card:')
                    # print(f"{card[0]:3d} {card[5]:3d} {card[10]:3d} {card[15]:3d} {card[20]:3d}")
                    # print(f"{card[1]:3d} {card[6]:3d} {card[11]:3d} {card[16]:3d} {card[21]:3d}")
                    # print(f"{card[2]:3d} {card[7]:3d} {card[12]:3d} {card[17]:3d} {card[22]:3d}")
                    # print(f"{card[3]:3d} {card[8]:3d} {card[13]:3d} {card[18]:3d} {card[23]:3d}")
                    # print(f"{card[4]:3d} {card[9]:3d} {card[14]:3d} {card[19]:3d} {card[24]:3d}")
                    # print()
                    RoundHadBingo = 1

        # if bingo was yelled, stop the round
        if RoundHadBingo == 1:
            # for card in cards:
            #             print('cardX = ')
            #             print(f"{card[0]:3d} {card[5]:3d} {card[10]:3d} {card[15]:3d} {card[20]:3d}")
            #             print(f"{card[1]:3d} {card[6]:3d} {card[11]:3d} {card[16]:3d} {card[21]:3d}")
            #             print(f"{card[2]:3d} {card[7]:3d} {card[12]:3d} {card[17]:3d} {card[22]:3d}")
            #             print(f"{card[3]:3d} {card[8]:3d} {card[13]:3d} {card[18]:3d} {card[23]:3d}")
            #             print(f"{card[4]:3d} {card[9]:3d} {card[14]:3d} {card[19]:3d} {card[24]:3d}")
            #             print()
            p1 = NumberOfColumnBingos / (NumberOfColumnBingos + NumberOfRowBingos) * 100
            p2 = NumberOfRowBingos / (NumberOfColumnBingos + NumberOfRowBingos) *100
            print('Column bingos: '+str(NumberOfColumnBingos)+f" ({p1:2.2f}%)"+' / Row bingos: '+str(NumberOfRowBingos)+f" ({p2:2.2f}%)")
            break

print('Done')

