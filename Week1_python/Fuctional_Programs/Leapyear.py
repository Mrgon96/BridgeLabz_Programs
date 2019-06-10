def Checkyear(Year):#defining Function to check Leap Year
    return (((Year%4==0) and (Year%100!=0)) or (Year%400==0))
#function checks for year fully divided [by 4 and not by 100] or by 400    
#Funnction returns Boolean Value

Year = int(input('Enter Year: '))#taking year as integer input

count=len(str(Year))#checking len of year entered

if count < 4 or count > 4:#checking for 4 digits of year value
    print('Enter 4 Digit Year Value')       
else :
    if(Checkyear(Year)):#calling function which returns boolean
        print(Year,' is Leap Year')
    else:
        print(Year,'is not a Leap Year')    
    