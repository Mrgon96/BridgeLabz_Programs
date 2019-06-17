#define class queue
class Queue:

    # define object as list
    def __init__(self):
        self.queue = []

    # adding element
    def enqueue(self, element):
        self.queue.insert(0, element)

    # deleting element
    def dequeue(self):
        return self.queue.pop(-1)

    # print queue
    def print_queue(self):
        for i in self.queue:
            print(i,'\t')

# create class object
q = Queue()

# queue length
num = int(input('Enter number of persons in a queue: '))

#bank cash element
cash = 1000
dep = 0
wid = 0
print('Enter 1 to deposit the cash')
print('Enter 2 to withdraw the cash')
print('Enter 3 to exit')

# while true
while True:

    UserChoice = int(input('Please enter a value: '))

    # if userchoice is 1
    if UserChoice == 1:
        q.enqueue(1)
        Amount = int(input('Enter the amount you want to deposit: '))

        if Amount == 0:
            print('Enter some amount!')
        else:
            dep += Amount
            cash += Amount
            print('Thank you cash deposited sucessfully!')
        q.dequeue()

    # if userchoice is 2
    elif UserChoice == 2:
        wid += 1
        q.enqueue(1)

        Amount = int(input('Enter the amount you want to withdraw: '))

        if dep >= Amount:
            dep -= Amount
            cash-= Amount
            print('Amount withdrawal sucessfully')
        else:
            print('Sorry dont have enough cash')
            q.dequeue()
    else:
        quit()




