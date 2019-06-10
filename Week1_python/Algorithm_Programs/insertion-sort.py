from utility import utility
Nums=[4,5,8,7,2,1,3,6]
Strings=['gon','dips','rups','ridhi','aanya']

utility.insertsort(Nums)
print('sorted List Afetr insertion sort is')
for i in range(len(Nums)):
    print(Nums[i]),
print('')
utility.insertsort(Strings)
print('Sorted Strings Are: ')
for j in Strings:
    print(j),