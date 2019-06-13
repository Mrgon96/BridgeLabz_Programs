n = 1000
global primes
primes = []
def prime(n,primes):
    for n in range(n+1):
        if n >1:
            for i in range(2,n):
                if n % i == 0:
                    break
            else:
                #print(n)
                primes.append(n)

prime(n,primes)

ranges = []
k = 0
for i in range(0,10):
    ranges.append([])
    min = k
    k = k + 100
    for j in primes:
        if j <=k and j >= min:
            ranges[i].append(j)

for i in ranges:
    print(i)
