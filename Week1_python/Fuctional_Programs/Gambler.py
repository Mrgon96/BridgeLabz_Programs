import random  #import random module

#Define function gamble
def Gamble():
    #take user inputs for stake,goal and trials
    stake = int(input('Enter Stake: ')) 
    goal = int(input('Enter goal: '))
    N = int(input('number of trials')) 


    wins=0 # wins intialized
    bets=0 # bets initialized

    for i in range(N):
        money = stake # money as temporay variable

        #when money is less than goal and greater than zero
        while money > 0 and money < goal: 
            bets+=1 #increasing bets value
            if random.randrange(0,2)==0: #generating random values
                money+=1
            else:
                money-=1
            print(money)   #printing money 

        #condition to check goal is reached or not
        if money == goal : 
            wins +=1 #incrementing win counter

    print(str(100*wins//N),'% wins') #printing win percentage 
    print('average bets',bets/N) #calculating average bets

#calling function
Gamble() 