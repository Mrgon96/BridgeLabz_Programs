def Decimal(num):
    decimal = 0
    base = 1

    temp = num
    while(temp):
        last = temp%10
        temp = int(temp/10)

        decimal += last * base
        base = base * 2

    return decimal

num = int(input('Enter Binary Number: '))
print('Decimal Number is: ',Decimal(num))    