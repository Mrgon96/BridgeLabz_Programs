import random
from Week3_OOPS.queue_linked import Queue

def deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    cards = []
    for i in suits:
        for j in rank:
            cards.append(i+'-'+j)
    cards = sorted(cards)
    # print(cards)

    q = Queue()

    # random.shuffle(cards)
    # print(cards)
    dis = []

    for i in range(4):
        player = []

        for j in range(9):
            m = random.randrange(len(cards))
            card = cards[m]
            j = Queue()
            j.enque(card)
            player.append(card)
            cards.remove(card)
        dis.append(player)
        q.enque(player)

    for i in range(len(dis)):
        print('Player', i+1, 'cards: ')
        print(q.deque())


deck()
