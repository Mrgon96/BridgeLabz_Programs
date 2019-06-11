from __future__ import division
import random #import random 

#defining function for coin flip
def CoinFlip():
    #taking input for number of flips
    flips = int(input('Enter the number of Flips ==> '))

    #initializing head counter to 0
    H=0
    #initializing tails counter to 0
    T=0

    #checking for flips greater than 0
    if flips>0:
        #for value in range of flips
        for i in range(flips):
            n=random.random()#generating random values
            print (n)
            #checking for random value to be greater than 0.5
            if n>0.5:
                H+=1 #increasing head counter
                print('heads=',H)
            else:
                T+=1 #increasing tail counter
                print('tails=',T)

         #calculating head vs tail percentage        
        result = H/T
        print('Percentage of Heads vs Tails is ',100 * result,'%')

    #condition to enter value greater than 0    
    else:
        print('Enter a Positive Integer')

#calling function
CoinFlip()
