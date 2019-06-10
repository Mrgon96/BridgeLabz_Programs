def toString(L):
    return ' '.join(L)

def Permute(a,l,r):
    if l == r:
        print toString(a)
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            Permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]  
   


str = 'ABC'
n = len(str) 
a = list(str)
Permute(a,0,n-1)