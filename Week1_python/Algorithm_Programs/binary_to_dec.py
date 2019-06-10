#define function
def Decimal(num):

    #decimal value intialized to zero
    decimal = 0 

    #base defined to zero
    base = 1

    #assigning value of number to temprory variable
    temp = num

    while(temp):

        #getting digit on last place
        last = temp%10

        #dividing temporary by 10
        temp = int(temp/10)

        #decimal equal to decimal added to last multiplied by 10
        decimal += last * base

        #increasing base by multiplying to 2
        base = base * 2

    #return decimal value
    return decimal

#TAKING USER INPUT AS NUMBER
num = int(input('Enter Binary Number: '))

#PRINTING FINAL DECIMAL NUMBER
print('Decimal Number is: ',Decimal(num))    