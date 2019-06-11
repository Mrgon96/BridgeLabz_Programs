#defining Function to check Leap Year
def Checkyear(Year):
    return (((Year%4==0) and (Year%100!=0)) or (Year%400==0))

#Funnction returns Boolean Value

#taking year as integer input
Year = int(input('Enter Year: '))

#checking length of digits in year entered
count=len(str(Year))

#checking for 4 digits of year value
if count < 4 or count > 4:
    print('Enter 4 Digit Year Value')       
else :
    #calling function which returns boolean
    if(Checkyear(Year)):
        print(Year,' is Leap Year')
    else:
        print(Year,'is not a Leap Year')    
    