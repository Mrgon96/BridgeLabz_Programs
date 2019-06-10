def power2():
    number = int(input('Enter a Number: ')) # taking integer input

    if number > 31: #checking for number not greater than 31
        print('Enter a value Less than or Equal to 31')
    else:
        for i in range(1,number+1): #looping value of i 
            print(2**i) #printig 2 raised to the power of i  

power2()