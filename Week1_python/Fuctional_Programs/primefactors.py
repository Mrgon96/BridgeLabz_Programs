import math 
N = int(input('Enter Number to calculate prime Factors: '))  # taking integer input

def factors(N): 
    
    while N % 2 == 0: #checking if number is divided by 2
        print 2, # print 2 as factor
        N = N / 2 # divide the number by 2
          
#next for loop checks for n divided by i=3 and also increase i by 2 
    for i in range(3,int(math.sqrt(N))+1,2): #checking till square root of number
        while N % i== 0: #checking if number is divided by 3 or more
            print i, # print i
            N = N / i # divide number by i
              
# if Number after diving becomes prime check here and print
    if N > 2: 
        print N 
          
factors(N) 
  
