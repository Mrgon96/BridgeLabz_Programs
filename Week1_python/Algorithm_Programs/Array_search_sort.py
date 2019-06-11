from utility import utility #import utility class

#numbers list
Nums=[1,2,3,4,5,6,7,8,9] 

#strings list
Strings = ['gon','ridhi','dips','shri','rups'] 

#calculating length-1 for both lists
endnum=len(Nums)-1 
endStr=len(Strings)-1

#storing result of utility function in result variable
result = utility.Bint(Nums,0,endnum,5)

#checking for found or not
if result != -1: 
    print('Element is present at index %d'%result)
else:
    print('Element not present in List')    

result2 = utility.Bint(Strings,0,endStr,'dips')

#checking for found or not
if result2 != -1: 
    print('Element is present at index %d'%result2)
else:
    print('Element not present in List')       