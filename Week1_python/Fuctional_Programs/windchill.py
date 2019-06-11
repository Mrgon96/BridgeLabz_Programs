#taking user inputs
t = float(input('Enter temparature: '))
v = float(input('Enter Wind Speed: '))

#cheking for limits of values
if t > 50 and v >120 or v < 3:
    print('Enter Tempature less than 50 and windspeed less than 120 greater than 3') 
else:
    #formula to calculate effective speed
    w=35.74+0.6215*t+(0.4275*t-35.75)*(v**0.16)
    print('Effective temparature is: ',w)