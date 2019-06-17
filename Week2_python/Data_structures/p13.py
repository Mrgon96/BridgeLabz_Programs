class Node:
    def __init__(self, data):
        self.data = data
        self.next= None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popping = self.head.data
            self.head = self.head.next
            return popping


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

anagrams = []
def Primegram(primes):
    for i in primes:
        primes.remove(i)
        for j in primes:
            # if i == j:
            #     pass
            # else:
            i = str(i)
            j = str(j)
            if (sorted(i) == sorted(j)) and j not in anagrams and i not in anagrams:
                anagrams.append(j)
                anagrams.append(i)




s =Stack()
primes.sort()
Primegram(primes)
for i in anagrams:
    s.push(i)

print(anagrams)

print("anagrams in reverse order: ")

reverse = []
print('')
for j in range(len(anagrams)):
    j=s.pop()
    reverse.append(j)

print(reverse)