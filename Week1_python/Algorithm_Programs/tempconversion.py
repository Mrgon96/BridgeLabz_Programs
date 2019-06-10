from utility import utility
#importing utility

#print choices
print('1. Celcius to Fahrenheit') 
print('2. Fahrenheit to Celcius')

#get choice as Input 
choice = input('Enter Choice: ')

#passing choice to tempconv Function in utility
utility.tempconv(choice)

