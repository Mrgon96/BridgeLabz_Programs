import random

def Gamble():
    stake = int(input('Enter Stake: '))
    goal = int(input('Enter goal: '))
    N = int(input('number of trials'))


    wins=0
    bets=0

    for i in range(N):
        money = stake
        while money > 0 and money < goal:
            bets+=1
            if random.randrange(0,2)==0:
                money+=1
            else:
                money-=1
            print(money)    
        if money == goal :
            wins +=1

    print(str(100*wins//N),'% wins')
    print('average bets',bets/N)


Gamble()