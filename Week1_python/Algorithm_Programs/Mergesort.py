Listnum = [3,6,4,7,1,8,2,5]

def Mergesort(l1):
    if len(l1) > 1:
        mid = len(l1) // 2
        N1 = l1[:mid]
        N2 = l1[mid:]

        Mergesort(N1)
        Mergesort(N2)

        i = j = k = 0

        while i < len(N1) and j < len(N2):
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


print('Given Array:')
print(Listnum),
print('')
Mergesort(Listnum)
print('Sorted Array: ')
print(Listnum),
