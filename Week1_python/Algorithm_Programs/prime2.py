from utility import utility

N = 1000
Primes = []
utility.Primenum(N,Primes)
print('Palindrome Numbers are ')
utility.Palinum(Primes)
print('')
print('Anagram Pairs are: ')
utility.Primegram(Primes)


    # @staticmethod
    # def Primegram(primes):
    #     for i in primes:
    #         for j in primes:
    #             if i == j:
    #                 break
    #             else:
    #                 i=str(i)
    #                 j=str(j)
    #                 if(sorted(i)==sorted(j)):
    #                     print(i,' and ', j ),