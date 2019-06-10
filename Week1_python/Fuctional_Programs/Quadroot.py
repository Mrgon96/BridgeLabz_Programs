import math

print('Enter the Values for Equation a*x*x+b*x+c')
a = int(input('Enter a  : '))
b = int(input('Enter b  : '))
c = int(input('Enter c  : '))

delta = b*b - 4*a*c
print(delta)


print('Root 1 of Equation is ')
r1 = (-b + math.sqrt(delta))/(2*a)
print(r1)
print('Root 2 of Equation is ')
r2 = (-b - math.sqrt(delta))/(2*a)
print(r2)