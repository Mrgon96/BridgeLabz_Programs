from utility import utility

#define number upto which prime numbers needed
N = 1000

#define primes array
Primes = []

#checking and printing palindromes
utility.Primenum(N,Primes)
print('Palindrome Numbers are ')
utility.Palinum(Primes)
print('')

#checking and printing anagrams
print('Anagram Pairs are: ')
utility.Primegram(Primes)

