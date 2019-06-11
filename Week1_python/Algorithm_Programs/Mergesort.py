#defining numbers list
Listnum = [3,6,4,7,1,8,2,5]

#define function mergesort
def Mergesort(l1):
    #chek for length 
    if len(l1) > 1:
        #calculate mid as middle of list
        mid = len(l1) // 2

        #dividing main list
        N1 = l1[:mid]
        N2 = l1[mid:]

        #passing divided lists again to mergesort function
        Mergesort(N1)
        Mergesort(N2)

        #define some variables
        i = j = k = 0

        #check for less than legth
        while i < len(N1) and j < len(N2):

            #swapping 
            if N1[i] < N2[j]:
                l1[k]=N1[i]
                i+=1
            else:
                l1[k]=N2[j]
                j+=1
            k+=1

        while i < len(N1):
            l1[k] = N1[i]    
            i+=1
            k+=1

        while j < len(N2):
            l1[k] = N2[j]    
            j+=1
            k+=1           


#print given array and sortrd array
print('Given Array:')
print(Listnum),
print('')
Mergesort(Listnum) #calling mergesort fuction passing list to it
print('Sorted Array: ')
print(Listnum),
