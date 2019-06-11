def power2():
     # taking integer input
    number = int(input('Enter a Number: '))

     #checking for number not greater than 31
    if number > 31:
        print('Enter a value Less than or Equal to 31')
    else:
        for i in range(1,number+1): 
            #printig 2 raised to the power of i  
            print(2**i) 

power2()