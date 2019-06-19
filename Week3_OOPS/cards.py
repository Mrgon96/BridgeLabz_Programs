import random


def deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    cards = []
    for i in suits:
        for j in rank:
            cards.append(i+'-'+j)

    # random.shuffle(cards)
    # print(cards)
    dis = []

    for i in range(4):
        player = []
        for j in range(9):
            m = random.randrange(len(cards))
            card = cards[m]
            player.append(card)
            cards.remove(card)
        dis.append(player)

    for i in range(len(dis)):
        print('Player', i+1, 'cards: ')
        print(dis[i])


deck()
