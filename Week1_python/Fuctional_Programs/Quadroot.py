
import math

print('Enter the Values for Equation a*x*x+b*x+c')

#taking user input for a,b,c values
a = int(input('Enter a  : '))
b = int(input('Enter b  : '))
c = int(input('Enter c  : '))

#calculating delta
delta = b*b - 4*a*c
print(delta)

#calculating and printing roots
print('Root 1 of Equation is ')
r1 = (-b + math.sqrt(delta))/(2*a)
print(r1)
print('Root 2 of Equation is ')
r2 = (-b - math.sqrt(delta))/(2*a)
print(r2)