import random


def deck():
    # arrays for suits and rank
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # insert data in big array as deck of cards
    cards = []
    for i in suits:
        for j in rank:
            cards.append(i+'-'+j)

    # 2D array for distribution
    dis = []


    for i in range(4):
        player = []
        for j in range(9):
            # generate random number
            m = random.randrange(len(cards))
            card = cards[m]
            player.append(card)
            # remove given card from deck
            cards.remove(card)
        dis.append(player)

    # print arrays for players
    for i in range(len(dis)):
        print('Player', i+1, 'cards: ')
        print(dis[i])


deck()
