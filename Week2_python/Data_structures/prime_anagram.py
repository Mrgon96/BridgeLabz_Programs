# initialzing empty primes array and limit of numbers
n = 1000
primes = []


# function to check for prime number

def prime(n, primes):
    for n in range(n + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                # print(n)
                primes.append(n)


#checking for anagram

def isAnagram(primes):
    for i in primes:
        for j in primes:
            i = str(i)
            j = str(j)
            if (sorted(i) == sorted(j)):
               return True

#calling function
prime(n, primes)

#ranges array

ranges = []
k = 0
for i in range(0, 10):
    ranges.append([])
    min = k
    k = k + 100
    for j in primes:
        if j <= k and j >= min:
            ranges[i].append(j)

# print prime array in ranges

for i in ranges:
    print(i)


#anagrams 2d array

anagrams = []
k=0
notAnagrams = []

#checking for anagram in ranges

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




