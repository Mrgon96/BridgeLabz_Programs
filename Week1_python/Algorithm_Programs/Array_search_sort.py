from utility import utility #import utility class
Nums=[1,2,3,4,5,6,7,8,9] #numbers list
Strings = ['gon','ridhi','dips','shri','rups'] #strings list

#calculating length-1 for both lists
endnum=len(Nums)-1 
endStr=len(Strings)-1

#storing result of utility function in result variable
result = utility.Bint(Nums,0,endnum,5)
if result != -1: #checking for found or not
    print('Element is present at index %d'%result)
else:
    print('Element not present in List')    

result2 = utility.Bint(Strings,0,endStr,'dips')
if result2 != -1: #checking for found or not
    print('Element is present at index %d'%result2)
else:
    print('Element not present in List')       