#!Python 3

#Mary's game

#imports
import random

#global varubals
deckStanderd = ['3 of Clubs', '3 of Dimands', '3 of Harts', '3 of Spades', '4 of Clubs', '4 of Dimands', '4 of Harts', '4 of Spades', '5 of Clubs', '5 of Dimands', '5 of Harts', '5 of Spades', '6 of Clubs', '6 of Dimands', '6 of Harts', '6 of Spades', '7 of Clubs', '7 of Dimands', '7 of Harts', '7 of Spades', '8 of Clubs', '8 of Dimands', '8 of Harts', '8 of Spades', '9 of Clubs', '9 of Dimands', '9 of Harts', '9 of Spades', '10 of Clubs', '10 of Dimands', '10 of Harts', '10 of Spades', 'Jack of Clubs', 'Jack of Dimands', 'Jack of Harts', 'Jack of Spades', 'Queen of Clubs', 'Queen of Dimands', 'Queen of Harts', 'Queen of Spades', 'King of Clubs', 'King of Dimands', 'King of Harts', 'King of Spades', 'Ace of Clubs', 'Ace of Dimands', 'Ace of Harts', 'Ace of Spades']
deckNumaricly = [[3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [6, 0], [6, 1], [6, 2], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3], [8, 0], [8, 1], [8, 2], [8, 3], [9, 0], [9, 1], [9, 2], [9, 3], [10, 0], [10, 1], [10, 2], [10, 3], [11, 0], [11, 1], [11, 2], [11, 3], [12, 0], [12, 1], [12, 2], [12, 3], [13, 0], [13, 1], [13, 2], [13, 3], [14, 0], [14, 1], [14, 2], [14, 3]]
cardDeal = {'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12,'King':13, 'Ace':14}
cardPoint = {'3':5, '4':5, '5':5, '6':5, '7':5, '8':5, '9':10, '10':10, 'Jack':10, 'Queen':10,'King':10, 'Ace':100}
players = {
    'Player1' : {
        'hand' : [],
        'isDealer' : True,
        'startCardNum' : 3
    },
    'Player2' : {
        'hand' : [],
        'isDealer' : False,
        'startCardNum' : 3
    },
    'Player3' : {
        'hand' : [],
        'isDealer' : False,
        'startCardNum' : 3
    }
}

#functions

def showNumaricalCard(cardNum):
    suit = ['Clubs', 'Dimands', 'Harts', 'Spades']
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
    print(card)
    return card

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
        

def main():
    #3 player set
    wild = deal(deckStanderd)


if __name__ == '__main__':
    main()