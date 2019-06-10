def search(l,h):
    if h - l == 0:
        return l

    mid = l + (h - l)/2
    print('Is it less than %d?'%mid)
    if bool(mid):
        return search(l,mid)
    else:
        return search(mid,h)

k = 8
n = 2**k
s = search(0,n)
print(s)