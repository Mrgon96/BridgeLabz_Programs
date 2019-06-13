class Queue:
    def __init__(self):
        self.queue = []

    def enque(self, element):
        self.queue.insert(0, element)

    def deque(self):
        return self.queue.pop(-1)

    def print_queue(self):
        for i in self.queue:
            print(i,'\t')


q = Queue()

num = int(input('Enter number of persons in a queue: '))

for i in range(1,num+1):
    q.enque(i)


q.print_queue()

cash = 1000
d = cash

def deposit(cash,d):
    dep = int(input('Enter Amount to be Deposited: '))
    d =dep
    cash += d


def withdraw(d):
    w = int(input('Enter amount to be withdrawn: '))
    if w <= d:
        print('Amount Withdrawn')
        d = d-w
    else:
        print('You cant Withdraw That much')
        withdraw(d)



for i in range(0,num+1):
    choice = int(input('1 for withdraw, 2 for Deposit'))
    if choice == 1:
        withdraw(d)
    elif choice == 2:
        deposit(cash,d)
    else:
        print('Enter Correct Choice: ')





