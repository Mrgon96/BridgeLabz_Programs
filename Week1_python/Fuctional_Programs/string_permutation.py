def toString(L):#fuction to conver list to string 
    return ' '.join(L) #join string without any space

def Permute(a,l,r): # define fuction taking three Inputs
    if l == r: #checking for equality of start and end
        print toString(a) #calling to string function and passing list
    else:
        for i in range(l,r+1): # for i in 0 and last index
            a[l],a[i]=a[i],a[l] 
            Permute(a,l+1,r) # recursively call function
            a[l],a[i]=a[i],a[l]  
   


str = 'ABC' # defining string
n = len(str) #length of string
a = list(str) # converting string to list
Permute(a,0,n-1) #passing values to function