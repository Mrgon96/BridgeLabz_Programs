import math 

 # taking integer input
N = int(input('Enter Number to calculate prime Factors: ')) 

def factors(N): 

    #checking if number is divided by 2, print 2 as factor
    while N % 2 == 0: 
        print 2, 
        # divide the number by 2
        N = N / 2
          
#next for loop checks for n divided by i=3 and also increase i by 2 
    for i in range(3,int(math.sqrt(N))+1,2): 
        while N % i== 0: 
            # print i,divide number by i
            print i, 
            N = N / i 
              
# if Number after diving becomes prime check here and print
    if N > 2: 
        print N 
          
factors(N) 
  
