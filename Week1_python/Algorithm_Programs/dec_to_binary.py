num = int(input('Enter Number to be Converted to Binary: '))

def binary(num):
    if num > 1:
        binary(num//2)
    print(num % 2), 

binary(num)
