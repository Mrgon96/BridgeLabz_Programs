from __future__ import division
import random #import random 

def CoinFlip():#defining function for coin flip
    flips = int(input('Enter the number of Flips ==> '))#taking input for number of flips
    H=0#initializing head counter to 0
    T=0#initializing tails counter to 0
    if flips>0:#checking for flips greater than 0
        for i in range(flips):#for value in range of flips
            n=random.random()#generating random values
            print (n)
            if n>0.5:#checking for random value to be greater than 0.5
                H+=1 #increasing head counter
                print('heads=',H)
            else:
                T+=1 #increasing tail counter
                print('tails=',T)
        result = H/T #calculating head vs tail percentage
        print('Percentage of Heads vs Tails is ',100 * result,'%')
    else:#condition to enter value greater than 0
        print('Enter a Positive Integer')


CoinFlip()
