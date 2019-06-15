class Node:
    def __init__(self,data):
        self.data = data
        self.next=None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enque(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def printQueue(self):
        temp = self.front
        print('This is your Queue: ')
        while temp:
            print(temp.data),
            temp=temp.next
        print

    def deque(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        return str(temp.data)

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

anagrams=[]

def isAnagram(primes):
    for i in primes:
        primes.remove(i)
        for j in primes:
            i = str(i)
            j = str(j)
            if (sorted(i) == sorted(j)):
               anagrams.append(i)
               anagrams.append(j)


prime(n, primes)
isAnagram(primes)


q =Queue()

for i in anagrams:
    q.enque(i)

q.printQueue()