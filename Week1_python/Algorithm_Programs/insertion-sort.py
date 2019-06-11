#import utility
from utility import utility

#define Numbers list
Nums=[4,5,8,7,2,1,3,6]

#define Strings list
Strings=['gon','dips','rups','ridhi','aanya']

#pass lists to Insertsort function 
utility.insertsort(Nums)
print('sorted List Afetr insertion sort is')

#printing sorted list
for i in range(len(Nums)):
    print(Nums[i]),
print('')


utility.insertsort(Strings)

#printing sorted list
print('Sorted Strings Are: ')
for j in Strings:
    print(j),