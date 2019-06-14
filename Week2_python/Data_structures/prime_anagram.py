n = 1000
global primes
primes = []

def prime(n, primes):
    for n in range(n + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                # print(n)
                primes.append(n)


def isAnagram(primes):
    for i in primes:
        for j in primes:
            i = str(i)
            j = str(j)
            if (sorted(i) == sorted(j)):
               return True


prime(n, primes)

ranges = []
k = 0
for i in range(0, 10):
    ranges.append([])
    min = k
    k = k + 100
    for j in primes:
        if j <= k and j >= min:
            ranges[i].append(j)

for i in ranges:
    print(i)


#**************ANAGRAMS 2D ARRAY*******************
anagrams = []
k=0
notAnagrams = []
for i in range(0,len(ranges)):
    anagrams.append([])
    for j in ranges[i]:
        ranges[i].remove(j)
        for k in ranges[i]:
            j=str(j)
            k=str(k)
            if sorted(j)==sorted(k):
                anagrams[i].append(j)
                anagrams[i].append(k)
            #anagrams[i].sort()


print('Angrams in Ranges are: ')
for a in anagrams:
    print(a)

print('Non Anagrams Are :')
for a in notAnagrams:
    print(a)


