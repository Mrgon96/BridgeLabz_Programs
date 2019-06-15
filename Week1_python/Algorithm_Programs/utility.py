from math import *
class utility():

#************ANAGRAM CHECK***********************   
    @staticmethod
    def isAnagram(str1,str2):
        if(len(str1)!=len(str2)): #checking if strings are of equal length and retuen false
            return False 
        str1=str1.lower() #converting strings to lowercase
        str2=str2.lower()    
        if(sorted(str1) == sorted(str2)):# using predefined soretd method to sort and comaparing strings
            return True # return true or false
        else:
            return False

#*************PRIME NUMBERS UPTO 1000********************
    @staticmethod
    def Primenum(N,Primes):#taking number and primes array
        
        for num in range(0,N+1):#checking till the last number
            if num > 1:#checking for number greater than 1
                for i in range(2,num):# taking range from 2 to num
                    if num % i == 0: #checking if num modulus 2 is zero or not
                        break
                else:
                    print(num), #print number
                    Primes.append(num)   #add number to prime array
        print('Total there are ',len(Primes),' prime Numbers in Between 1 to ', N)
        #print length of array and total count of numbers

#************************PRIME NUMBERS ANAGRAM*******************************      
    @staticmethod
    def Primegram(primes): #passing primes array to function
        for i in primes: #traversing i through primes array
            primes.remove(i) #removing 'i'th element from array
            for j in primes: #looping j through array
                # if i == j:
                #     pass
                # else:
                i=str(i) #converting i to string
                j=str(j) #converting j to string
                if(sorted(i)==sorted(j)): #checking sorted string fro equality
                    print(i,' and ', j ),#printing i and j
            # primes.append(i)
#************************PRIME NUMBERS PALINDROME*******************************  
    @staticmethod
    def Palinum(Primes): #passing primes array to function       
        for i in Primes: #traversing i through primes array
            temp = i #assigning i to temparory variable
            reverse = 0 # taking reverse variable to store remnainders
            num2 = 0 # taking variable for storing reverse of integer 
            while temp != 0: #while temporary not equal to zero
                reverse = temp % 10 # reverse as modulus of temp
                num2 = reverse + num2 * 10 # num as remainder added to multiplying to 10 with itself
                temp = temp/10 # diving temp 
            if i == num2:#checking if num2 equals i or not 
                print(i), #print num 

#************************ BINARY SEARCH INT *******************************  
    #@staticmethod
    def Bint(Nums,start,end,tofind):# passing array,start and end of array and number to find
        while start <= end: # while start is less end
            mid = int(1+(end-start)/2) #calulating middle of array

            if Nums[mid] == tofind: #cheking if middle is the number to find
                return mid

            elif Nums[mid] < tofind: # if number to find is greater tahn middle 
                start = mid + 1 # changing start of array to mid+1 

            else:
                end = mid - 1 #else change start to mid-1
        else:
            return -1        

#************************ INSERTION SORT *******************************  
    @staticmethod
    def insertsort(Numbers):#passing number array 
        for i in range(0,len(Numbers)): #looping in range of array
            key = Numbers[i] #assinging number as key

            j = i-1 # define j as i-1
            while j>=0 and key < Numbers[j]:#while j is greater than 0 and less than array index j
                Numbers[j+1]=Numbers[j]# swap numbers
                j=j-1#decrement j
            Numbers[j+1]=key #number index j+1 becomes key   

#************************ BUBBLE SORT ******************************* 
    @staticmethod
    def bubble(Numbers):#passing numbers array 
        n = len(Numbers) #define n as length of numbers array
        for i in range(0,len(Numbers)): #loop through range of array
            for j in range(0,n-i-1): #loop through 0 to last element
                if Numbers[j] > Numbers[j+1]: # checking for greater number
                    Numbers[j],Numbers[j+1] = Numbers[j+1],Numbers[j] # swapping numbers

# #*********************** DAY OF THE WEEK ******************************

    @staticmethod
    def Day(d,m,y):#passing date month and year
        Days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']# list for days
        #gregorian calender calculation formulae
        y0= y - (( 14 - m)/12)
        x = y0 + y0/4 - y0/100 + y0/400
        m0 = m + 12 *((14 - m)/12) - 2
        d0 = (d + x + ((31 * m0)/12))%7
        print('Day on Date is ',Days[d0])#getting output and printing from list


#*************************NEWTON'S SQUARE ROOT****************************

    @staticmethod
    def sqrt(c):# passing number to calculate square root of
        epsilon = 2.72 -15 # taking e as 2.72 and substracting 15 to get epsilon
        t = c # define t as c which is number takrn
        while abs(t - c/t > epsilon * t):#checking for greater than epsilon multiplied by itself 
            t = ((c/t) + t)/2.0 #calculating t if its not
             
        print(t)#print the result which will bw square root
              
#******************** TEMPARATURE CONVERSION *****************************
    @staticmethod
    def tempconv(choice): #passing choice
        if choice == 1:#if choice = 1
            C = input('Enter Celcius: ') #get celcius from user
            F = C * 9/5 + 32 #formula to calculate Fahrenheit
            print('Temparature in Fahrenheit is: ',F)# print result
        elif choice == 2:
            F = input('Enter Fahrenheit: ') #get fahrenheit as input
            C = (F - 32)*(5/9) # formula to calculate celcius
            print('Temparature in Celcius is: ',C) # print result
        else:
            print('Enter Correct Choice.......')   # if choice entered is not 1 or 2

#*************************** MONTHLY PAYMENT ***********************************
                   
    @staticmethod
    def monthpay(Y,R,P):# pass three values year,principal amount and rate of interest
        n = 12 * Y #calculate n
        r = R / (12 * 100) #calculate r
        r0 = 1 - ((1 + r) ** (~n))
        payment = (P * r) / r0 #calulate payment 
        print('Monthlyt Payment is : ',payment) # print payment


