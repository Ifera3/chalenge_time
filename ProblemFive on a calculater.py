#!Python 3

#Mery's game

#imports
import random

#global varubals
if __name__ == '__main__':
    deckStanderd = ['3 of Clubs', '3 of Dimands', '3 of Harts', '3 of Spades', '4 of Clubs', '4 of Dimands', '4 of Harts', '4 of Spades', '5 of Clubs', '5 of Dimands', '5 of Harts', '5 of Spades', '6 of Clubs', '6 of Dimands', '6 of Harts', '6 of Spades', '7 of Clubs', '7 of Dimands', '7 of Harts', '7 of Spades', '8 of Clubs', '8 of Dimands', '8 of Harts', '8 of Spades', '9 of Clubs', '9 of Dimands', '9 of Harts', '9 of Spades', '10 of Clubs', '10 of Dimands', '10 of Harts', '10 of Spades', 'Jack of Clubs', 'Jack of Dimands', 'Jack of Harts', 'Jack of Spades', 'Queen of Clubs', 'Queen of Dimands', 'Queen of Harts', 'Queen of Spades', 'King of Clubs', 'King of Dimands', 'King of Harts', 'King of Spades', 'Ace of Clubs', 'Ace of Dimands', 'Ace of Harts', 'Ace of Spades']
    deckNumaricly = [[3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [6, 0], [6, 1], [6, 2], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3], [8, 0], [8, 1], [8, 2], [8, 3], [9, 0], [9, 1], [9, 2], [9, 3], [10, 0], [10, 1], [10, 2], [10, 3], [11, 0], [11, 1], [11, 2], [11, 3], [12, 0], [12, 1], [12, 2], [12, 3], [13, 0], [13, 1], [13, 2], [13, 3], [14, 0], [14, 1], [14, 2], [14, 3]]
    discarded = []
    cardDeal = {'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12,'King':13, 'Ace':14}
    #numberOfPlayers = 2
    players = {}
    """
    inside players dictionary
    'Player1' : {
        'hand' : [],
        'isDealer' : True,
        'startCardNum' : 3,
        'playedCards' : [],
        'score' : 0
    },
    'Player2' : {
        'hand' : [],
        'isDealer' : False,
        'startCardNum' : 3,
        'playedCards' : [],
        'score' : 0
    }"""

#functions
def deal(deck):
    print(len(deck))
    for player in players:
        card = deck.pop(random.randrange(len(deck)))
        players[player]['hand'].append(card)
        for num in cardDeal:
            if num in players[player]['hand'][0]:
                players[player]['startCardNum'] = cardDeal[num]
        if players[player]['isDealer']:
            wild = players[player]['hand'][0]
    for player in players:
        for i in range(players[player]['startCardNum'] - 1):
            card = deck.pop(random.randrange(len(deck)))
            players[player]['hand'].append(card)
        print(len(players[player]['hand']),players[player]['startCardNum'])
    print(players)
    print(wild)
    print(len(deck))
    return wild

def becomeNumaricalCard(cardName):
    cardName = cardName.lower()
    cardName = cardName.split('of')
    cardName[0] = cardName[0].strip()
    cardName[1] = cardName[1].strip()
    #print(cardName)
    if cardName[0] == 'ace':
        cardnum = 14
    elif cardName[0] == 'king':
        cardnum = 13
    elif cardName[0] == 'queen':
        cardnum = 12
    elif cardName[0] == 'jack':
        cardnum = 11
    else:
        cardnum = int(cardName[0])
    if cardName[1] == 'clubs':
        cardSiut = 0
    elif cardName[1] == 'dimands':
        cardSiut = 1
    elif cardName[1] == 'harts':
        cardSiut = 2
    elif cardName[1] == 'spades':
        cardSiut = 3
    #print([cardnum, cardSiut])
    return [cardnum, cardSiut]

def showNumaricalCard(cardNum, noSuit = False, printCard = True):
    suit = ['Clubs', 'Dimands', 'Harts', 'Spades']
    if noSuit:
        if cardNum == 11:
            card = "Jack"
        elif cardNum == 12:
            card = "Queen"
        elif cardNum == 13:
            card = "King"
        elif cardNum == 14:
            card = "Ace"
        else:
            card = str(cardNum)
    else:
        if cardNum[0] == 11:
            card = "Jack of {location}".format(location=suit[cardNum[1]])
        elif cardNum[0] == 12:
            card = "Queen of {location}".format(location=suit[cardNum[1]])
        elif cardNum[0] == 13:
            card = "King of {location}".format(location=suit[cardNum[1]])
        elif cardNum[0] == 14:
            card = "Ace of {location}".format(location=suit[cardNum[1]])
        else:
            card = "{numbercard} of {location}".format(location=suit[cardNum[1]], numbercard=cardNum[0])
    if printCard:
        print(card, end='  ')
    return card

def dealNumaricly(deck):
    #print(len(deck))
    random.shuffle(deck)
    for player in players:
        card = deck.pop(random.randrange(len(deck)))
        players[player]['hand'].append(card)
        players[player]['startCardNum'] = players[player]['hand'][0][0]
        if players[player]['isDealer']:
            wild = players[player]['hand'][0][0]
        players[player]['playedCards'] = []
    for player in players:
        for i in range(players[player]['startCardNum'] - 1):
            card = deck.pop(random.randrange(len(deck)))
            players[player]['hand'].append(card)
        players[player]['hand'].sort()
        #print(len(players[player]['hand']),players[player]['startCardNum'])
    #print(players)
    #print(wild)
    #print(len(deck))
    discarded.append(deck.pop(random.randrange(len(deck))))
    return deck, wild

def cardsPlayable(player, discard = False):
    pleyedNumarical = []
    pleyedCards = ['','']
    while len(pleyedNumarical) < len(pleyedCards):
        pleyedNumarical = []
        if discard:
            pleyedCards = input("Enter the card you are discarding (eg: 8 of Dimands): ")
        else:
            pleyedCards = input("enter the cards you are playing in a list with comas to seprate them (eg: 3 of Harts, 3 of Clubs, 3 of Spades)\n If you can't play any sets of three cards enter No Sets: ")
        pleyedCards = pleyedCards.strip()
        pleyedCards = pleyedCards.lower()
        if pleyedCards == 'no sets':
            return 'no sets'
        #print(pleyedCards)
        pleyedCards = pleyedCards.split(',')
        pleyedCards.insert(0, False)
        #print(pleyedCards)
        for i in range(1, len(pleyedCards)):
            #print(pleyedNumarical, i)
            try:
                pleyedNumarical.append(becomeNumaricalCard(pleyedCards[i]))
                #print(pleyedNumarical)
            except:
                print("{unexpectedcard} is not a excepted card.".format(unexpectedcard=pleyedCards[i]))
        for i in pleyedNumarical:
            if i not in players[player]['hand']:
                print('{die} is not in your hand.'.format(die=showNumaricalCard(i, printCard = False)))
                break
        else:
            pleyedNumarical.insert(0, True)
    pleyedNumarical.pop(0)
    #print(pleyedNumarical)
    return pleyedNumarical

def pickUpCard(player, deck, wildCard):
    print('{die}s are wild.\n'.format(die=showNumaricalCard(wildCard, printCard=False, noSuit=True)))
    posibilitys = opptions(player, wildCard, discard=True)
    #print(posibilitys)
    if len(discarded) > 0:
        print("Discard Pile:")
        for card in discarded:
            showNumaricalCard(card)
        pickUpCard = ''
        while type(pickUpCard) == str:
            pickUpCard = input("\n\nEnter the card you would like to pick up: ")
            pickUpCard = pickUpCard.strip()
            pickUpCard = pickUpCard.lower()
            #print(pickUpCard)
            if pickUpCard == "can't pick up" or pickUpCard == "can't pick up":
                #print('you did this')
                card = deck.pop(random.randrange(len(deck)))
                players[player]['hand'].append(card)
                players[player]['hand'].sort()
                print("\nYou picked up a {cardup}.\n",format(cardup=showNumaricalCard(card, printCard=False)))
                return 
            try:
                pickUpCard = becomeNumaricalCard(pickUpCard)
            except:
                print("{cardup} is not in the discard pile.\n".format(cardup=pickUpCard))
            if pickUpCard[0] in posibilitys['full set'] or pickUpCard[0] in posibilitys['wild set']:
                pickUpAbove = discarded.index(pickUpCard)
                for i in range(len(discarded)):
                    #print(i, pickUpAbove, discarded)
                    if i >= pickUpAbove:
                        print("You picked up a {cardup}.\n".format(cartdyp=showNumaricalCard(discarded[i], printCard=False)))
                        players[player]['hand'].append(discarded.pop(i))
                        discarded.insert(i,'place holder')
            else:
                #print(pickUpCard, discarded)
                card = deck.pop(random.randrange(len(deck)))
                players[player]['hand'].append(card)
                players[player]['hand'].sort()
                print("You picked up a {cardup}.\n".format(cartdyp=showNumaricalCard(discarded[i], printCard=False)))
                break
        while 'place holder' in discarded:
            discarded.remove('place holder')
    else:
        #print('i am deid')
        card = deck.pop(random.randrange(len(deck)))
        players[player]['hand'].append(card)
        players[player]['hand'].sort()
        print("You picked up a {cardup}.\n".format(cartdyp=showNumaricalCard(discarded[i], printCard=False)))

def opptions(player, wildCard, discard = False):
    cardCount = {}
    options = {'full set':[], 'wild set':[]}
    for i in players[player]['hand']:
        if i[0] in cardCount:
            cardCount[i[0]] = cardCount[i[0]] + 1
        elif i[0] not in cardCount:
            cardCount[i[0]] = 1
    #print(cardCount, wildCard)
    if discard:
        for i in cardCount:
            if i != wildCard:
                if cardCount[i] >= 2:
                    #print(i, '3')
                    options['full set'].append(i)
                if wildCard in cardCount:
                    if cardCount[i] == 1:
                        #print(i, 'wild 2')
                        options['wild set'].append(i)
        if wildCard in cardCount:
            if len(options['wild set']) >= 3 and cardCount[wildCard] >= 2:
                options['full set'].append(wildCard)
    else:
        for i in cardCount:
            if i != wildCard:
                if cardCount[i] > 2:
                    #print(i, '3')
                    options['full set'].append(i)
                if wildCard in cardCount:
                    if 3 > cardCount[i] > 1:
                        #print(i, 'wild 2')
                        options['wild set'].append(i)
    return options

def cardPlay(player, deck, wildCard):
    playedCards = cardsPlayable(player)
    safty = players[player]['hand']
    #print(players[player]['hand'], safty)
    if playedCards != 'No Sets':
        playedNum = {}
        for i in playedCards:
            #print(i)
            if i[0] in playedNum:
                playedNum[i[0]] = playedNum[i[0]] + 1
            elif i[0] not in playedNum:
                playedNum[i[0]] = 1
        for difplayer in players:
            for down in players[difplayer]['playedCards']:
                if down[0] in playedNum:
                    for cardplay in playedCards:
                        if down[0] == cardplay[0]:
                            killdex = players[player]['hand'].index(cardplay)
                            players[player]['playedCards'].append(players[player]['hand'].pop(killdex))
                            killdex = playedCards.index(cardplay)
                            playedCards.pop(killdex)
                            playedCards.insert(killdex, 'placeHolder')
        while 'placeHolder' in playedCards:
            playedCards.remove('place')
        for i in playedNum:
            #print(playedNum[i], i)
            if playedNum[i] >= 3 and i != wildCard:
                #print(players[player]['hand'], i)
                for cardplay in playedCards:
                    #print(playedCards, cardplay)
                    if i == cardplay[0]:
                        #print(playedCards, cardplay)
                        killdex = players[player]['hand'].index(cardplay)
                        players[player]['playedCards'].append(players[player]['hand'].pop(killdex))
                        #print(playedCards, cardplay)
                if wildCard in playedNum and i != wildCard:
                    playSet = input("Would you like to play your set of {sets}s with a wild {cardwilld} (y or n): ".format(cardwilld=showNumaricalCard(wildCard,noSuit = True, printCard = False), sets=showNumaricalCard(i, noSuit = True, printCard = False)))
                    if playSet == 'y' or playSet == 'Y':
                        for cardplay in playedCards:
                            if wildCard == cardplay[0]:
                                #print(playedCards, cardplay)
                                #print(players[player]['playedCards'])
                                killdex = players[player]['hand'].index(cardplay)
                                players[player]['playedCards'].append(players[player]['hand'].pop(killdex))
                                killdex = playedCards.index(cardplay)
                                playedCards.pop(killdex)
                                #print(playedCards, cardplay)
                                break
            elif playedNum[i] >= 2 and wildCard in playedNum and wildCard != i:
                playSet = input("Would you like to play your set of {sets}s with a wild {cardwilld} (y or n): ".format(cardwilld=showNumaricalCard(wildCard,noSuit = True, printCard = False), sets=showNumaricalCard(i, noSuit = True, printCard = False)))
                if playSet == 'y' or playSet == 'Y':
                    for cardplay in playedCards:
                        #print(playedCards, cardplay, i)
                        if i == cardplay[0]:
                            #print(playedCards, cardplay)
                            killdex = players[player]['hand'].index(cardplay)
                            players[player]['playedCards'].append(players[player]['hand'].pop(killdex))
                            #print(playedCards, cardplay)
                    #print(players[player]['hand'],i)
                    for cardplay in playedCards:
                        if wildCard == cardplay[0]:
                            #print(playedCards, cardplay)
                            killdex = players[player]['hand'].index(cardplay)
                            players[player]['playedCards'].append(players[player]['hand'].pop(killdex))
                            killdex = playedCards.index(cardplay)
                            playedCards.pop(killdex)
                            #print(playedCards, cardplay)
                            break
            #print(safty, len(players[player]['hand']))
            if len(players[player]['hand']) == 0:
                players[player]['hand'] = safty
    return deck

def discard(player):
    disCard = ''
    while type(disCard) == str or len(disCard) > 1:
        disCard = cardsPlayable(player, discard = True)
    killdex = players[player]['hand'].index(disCard[0])
    discarded.append(players[player]['hand'].pop(killdex))
    #print(discarded)

def smallestHand():
    small = 14
    for player in players:
        if len(players[player]['hand']) < small:
            small = len(players[player]['hand'])
    return small

def play(deck, wildCard):
    while smallestHand() > 0:
        for player in players:
            print("Your hand:\n")
            for card in players[player]['hand']:
                showNumaricalCard(card)
            print('\n')
            pickUpCard(player, deck, wildCard)
            print("Your hand:\n")
            for card in players[player]['hand']:
                showNumaricalCard(card)
            print('\n')
            #print(opptions(player, wildCard), '\n')
            deck = cardPlay(player, deck, wildCard)
            #print(players[player]['hand'])
            discard(player)
            #print(players[player]['hand'])

def scoring(wildCard):
    score = 0
    nextdealer = False
    for player in players:
        if nextdealer:
            players[player]['isDealer'] = True
            nextdealer = False
        for downCard in players[player]['playedCards']:
            if downCard[0] == wildCard or downCard[0] == 14:
                score = score + 100
            elif downCard[0] < 9:
                score = score + 5
            elif 8 < downCard[0] < 14:
                score = score + 10
        for heldCard in players[player]['hand']:
            if heldCard[0] == wildCard or heldCard[0] == 14:
                score = score - 100
            elif heldCard[0] < 9:
                score = score - 5
            elif 8 < heldCard[0] < 14:
                score = score - 10
        players[player]['score'] = players[player]['score'] + score
        print(f"{player} scored {score} this round and {players[player]['score']} in total")
        if players[player]['isDealer']:
            if player == f'Player{numberOfPlayers}':
                players['player1']['isDealer'] = True
            else:
                players[player]['isDealer'] = False
                nextdealer = True

def main():
    activeDeck, wildCard = dealNumaricly(deckNumaricly)
    print(players)
    play(activeDeck, wildCard)
    scoring(wildCard)

if __name__ == '__main__':
    numberOfPlayers = ''
    while type(numberOfPlayers) == str:
        numberOfPlayers = input('how many players are playing?: ')
        try:
            numberOfPlayers = int(numberOfPlayers)
        except:
            print(f"{numberOfPlayers} in not a number.")
    for i in range(numberOfPlayers):
        players[f'Player{i+1}'] = {'hand' : [], 'isDealer' : False, 'startCardNum' : 3, 'playedCards' : [], 'score' : 0}
    players['Player1']['isDealer'] = True
    #print(players)
    #input()
    for repeat in range(2):
        main()