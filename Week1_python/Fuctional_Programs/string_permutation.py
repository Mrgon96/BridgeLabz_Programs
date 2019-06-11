#fuction to conver list to string 
def toString(L):
    return ' '.join(L) 

# define fuction taking three Inputs
def Permute(a,l,r): 
    #checking for equality of start and end
    if l == r:
        print toString(a) 
    else:
        for i in range(l,r+1): 
            #swap values
            a[l],a[i]=a[i],a[l] 
            Permute(a,l+1,r) # recursively call function
            a[l],a[i]=a[i],a[l]  
   


str = 'ABC' # defining string
n = len(str) #length of string
a = list(str) # converting string to list
Permute(a,0,n-1) #passing values to function