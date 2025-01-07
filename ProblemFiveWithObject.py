#!Python 3

#Mery's game

#imports
import random

#global varubals
if __name__ == '__main__':
    deckNumaricly = [[3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [6, 0], [6, 1], [6, 2], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3], [8, 0], [8, 1], [8, 2], [8, 3], [9, 0], [9, 1], [9, 2], [9, 3], [10, 0], [10, 1], [10, 2], [10, 3], [11, 0], [11, 1], [11, 2], [11, 3], [12, 0], [12, 1], [12, 2], [12, 3], [13, 0], [13, 1], [13, 2], [13, 3], [14, 0], [14, 1], [14, 2], [14, 3]]
    discarded = []
    players = []

    class basePlayer:
        def __init__(self, name, isDealer, hand, playedCards, startCardNum, score):
            self.name = name
            self.isDealer = isDealer
            self.hand = hand
            self.playedCards = playedCards
            self.startCardNum = startCardNum
            self.score = score
        
        def __str__(self):
            return f"{self.name}, {self.isDealer}, {self.hand}, {self.playedCards}, {self.startCardNum}, {self.score}"

#functions
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
            card = f"Jack of {suit[cardNum[1]]}"
        elif cardNum[0] == 12:
            card = f"Queen of {suit[cardNum[1]]}"
        elif cardNum[0] == 13:
            card = f"King of {suit[cardNum[1]]}"
        elif cardNum[0] == 14:
            card = f"Ace of {suit[cardNum[1]]}"
        else:
            card = f"{cardNum[0]} of {suit[cardNum[1]]}"
    if printCard:
        print(card, end='  ')
    return card

def dealNumaricly():
    #print(len(deck))
    for i in range(int(numberOfPlayers/3)+1):
        
        deck = deckNumaricly
    random.shuffle(deck)
    for player in players:
        card = deck.pop(random.randrange(len(deck)))
        player.hand.append(card)
        player.startCardNum = player.hand[0][0]
        if player.isDealer:
            wild = player.hand[0][0]
    for player in players:
        print(player, 'hi')
        for i in range(player.startCardNum - 1):
            card = deck.pop(random.randrange(len(deck)))
            player.hand.append(card)
        print(player)
        player.hand.sort()
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
                print(f"{pleyedCards[i]} is not a excepted card.")
        for i in pleyedNumarical:
            if i not in player.hand:
                print(f'{showNumaricalCard(i, printCard = False)} is not in your hand.')
                break
        else:
            pleyedNumarical.insert(0, True)
    pleyedNumarical.pop(0)
    #print(pleyedNumarical)
    return pleyedNumarical

def pickUpCard(player, deck, wildCard):
    print(f'{showNumaricalCard(wildCard, printCard=False, noSuit=True)}s are wild.\n')
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
                player.hand.append(card)
                player.hand.sort()
                print(f"\nYou picked up a {showNumaricalCard(card, printCard=False)}.\n")
                return 
            try:
                pickUpCard = becomeNumaricalCard(pickUpCard)
            except:
                print(f"{pickUpCard} is not in the discard pile.\n")
            if pickUpCard[0] in posibilitys['full set'] or pickUpCard[0] in posibilitys['wild set']:
                pickUpAbove = discarded.index(pickUpCard)
                for i in range(len(discarded)):
                    #print(i, pickUpAbove, discarded)
                    if i >= pickUpAbove:
                        print(f"You picked up a {showNumaricalCard(discarded[i], printCard=False)}.\n")
                        player.hand.append(discarded.pop(i))
                        discarded.insert(i,'place holder')
            else:
                #print(pickUpCard, discarded)
                card = deck.pop(random.randrange(len(deck)))
                player.hand.append(card)
                player.hand.sort()
                print(f"You picked up a {showNumaricalCard(card, printCard=False)}.\n")
                break
        while 'place holder' in discarded:
            discarded.remove('place holder')
    else:
        #print('i am deid')
        card = deck.pop(random.randrange(len(deck)))
        player.hand.append(card)
        player.hand.sort()
        print(f"You picked up a {showNumaricalCard(card, printCard=False)}.\n")

def opptions(player, wildCard, discard = False):
    cardCount = {}
    options = {'full set':[], 'wild set':[]}
    for i in player.hand:
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
    safty = player.hand
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
            for down in difplayer.playedCards:
                if down[0] in playedNum:
                    for cardplay in playedCards:
                        if down[0] == cardplay[0]:
                            killdex = player.hand.index(cardplay)
                            player.playedCards.append(player.hand.pop(killdex))
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
                        killdex = player.hand.index(cardplay)
                        player.playedCards.append(player.hand.pop(killdex))
                        #print(playedCards, cardplay)
                if wildCard in playedNum and i != wildCard:
                    playSet = input(f"Would you like to play your set of {showNumaricalCard(i, noSuit = True, printCard = False)}s with a wild {showNumaricalCard(wildCard,noSuit = True, printCard = False)} (y or n): ")
                    if playSet == 'y' or playSet == 'Y':
                        for cardplay in playedCards:
                            if wildCard == cardplay[0]:
                                #print(playedCards, cardplay)
                                #print(players[player]['playedCards'])
                                killdex = player.hand.index(cardplay)
                                player.playedCards.append(player.hand.pop(killdex))
                                killdex = playedCards.index(cardplay)
                                playedCards.pop(killdex)
                                #print(playedCards, cardplay)
                                break
            elif playedNum[i] >= 2 and wildCard in playedNum and wildCard != i:
                playSet = input(f"Would you like to play your set of {showNumaricalCard(i, noSuit = True, printCard = False)}s with a wild {showNumaricalCard(wildCard, noSuit = True, printCard = False)} (y or n): ")
                if playSet == 'y' or playSet == 'Y':
                    for cardplay in playedCards:
                        #print(playedCards, cardplay, i)
                        if i == cardplay[0]:
                            #print(playedCards, cardplay)
                            killdex = player.hand.index(cardplay)
                            player.playedCards.append(player.hand.pop(killdex))
                            #print(playedCards, cardplay)
                    #print(players[player]['hand'],i)
                    for cardplay in playedCards:
                        if wildCard == cardplay[0]:
                            #print(playedCards, cardplay)
                            killdex = player.hand.index(cardplay)
                            player.playedCards.append(player.hand.pop(killdex))
                            killdex = playedCards.index(cardplay)
                            playedCards.pop(killdex)
                            #print(playedCards, cardplay)
                            break
            #print(safty, len(players[player]['hand']))
            if len(player.hand) == 0:
                player.hand = safty
    return deck

def discard(player):
    disCard = ''
    while type(disCard) == str or len(disCard) > 1:
        disCard = cardsPlayable(player, discard = True)
    killdex = player.hand.index(disCard[0])
    discarded.append(player.hand.pop(killdex))
    #print(discarded)

def smallestHand():
    small = 14
    for player in players:
        if len(player.hand) < small:
            small = len(player.hand)
    return small

def play(deck, wildCard):
    while smallestHand() > 0:
        for player in players:
            print("Your hand:\n")
            for card in player.hand:
                showNumaricalCard(card)
            print('\n')
            pickUpCard(player, deck, wildCard)
            print("Your hand:\n")
            for card in player.hand:
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
            player.isDealer = True
            nextdealer = False
        for downCard in player.playedCards:
            if downCard[0] == wildCard or downCard[0] == 14:
                score = score + 100
            elif downCard[0] < 9:
                score = score + 5
            elif 8 < downCard[0] < 14:
                score = score + 10
        for heldCard in player.hand:
            if heldCard[0] == wildCard or heldCard[0] == 14:
                score = score - 100
            elif heldCard[0] < 9:
                score = score - 5
            elif 8 < heldCard[0] < 14:
                score = score - 10
        player.score = player.score + score
        print(f"{player} scored {score} this round and {player.score} in total")
        if player.isDealer:
            if players.index(player) == (len(players) - 1):
                players[0].isDealer = True
            else:
                player.isDealer = False
                nextdealer = True

def main():
    activeDeck, wildCard = dealNumaricly()
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
        if i == 0:
            deal = True
        else:
            deal = False
        players.append(basePlayer(input(f"Enter the name of player {i + 1}: "), deal, [], [], 3, 0))
    #for i in players:
    #    print(i)
    #input()
    for repeat in range(2):
        main()