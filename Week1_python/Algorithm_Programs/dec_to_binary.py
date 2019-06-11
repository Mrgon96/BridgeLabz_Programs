#taking user input
num = int(input('Enter Number to be Converted to Binary: '))

#define function 
def binary(num):
    #check for number greater than 1
    if num > 1:
        #calling function recursively 
        binary(num//2)
    #print number modulus 2    
    print(num % 2), 

#passing user input to function
binary(num)
