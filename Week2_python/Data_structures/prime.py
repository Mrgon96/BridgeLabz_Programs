# intialize empty array and limit of 1000
n = 1000
global primes
primes = []

# check for prime
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

# inserting elements in ranges in array
for i in range(0,10):
    ranges.append([])
    min = k
    k = k + 100
    for j in primes:
        if j <=k and j >= min:
            ranges[i].append(j)

# printing ranges array
for i in ranges:
    print(i)
