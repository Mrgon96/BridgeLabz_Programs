#create Node class for linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

# queue created using linked list

class Queue:

    #define front and rear as none
    def __init__(self):
        self.front = self.rear = None

    #check for empty
    def isEmpty(self):
        return self.front == None

    # insert element in a queue
    def enque(self, item):
        #creating node at element
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # print queue
    def printQueue(self):
        temp = self.front
        print('This is your Queue: ')
        while temp:
            print(temp.data),
            temp=temp.next
        print

    #delete element from queue
    def deque(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        return str(temp.data)


# initialize limit and empty prime array
n = 1000
global primes
primes = []

# check for prime
def prime(n, primes):


    for n in range(n + 1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                # print(n)
                primes.append(n)


anagrams = []


#check for anagrams
def isAnagram(primes):
    for i in primes:
        primes.remove(i)
        for j in primes:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j):
                anagrams.append(i)
                anagrams.append(j)

# calling functions
prime(n, primes)
isAnagram(primes)

# create object of queue class
q = Queue()

for i in anagrams:
    q.enque(i)

q.printQueue()
