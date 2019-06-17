import sys

# return day value as integer
def day(d,m,y):
    y0= y - (( 14 - m)/12)
    x = y0 + y0/4 - y0/100 + y0/400
    m0 = m + 12 *((14 - m)/12) - 2
    d0 = (d + x + ((31 * m0)/12))%7
    return d0


# check for leap year
def leapYear(year):
    if year%4==0 and year%100!=0 or year%400 == 0:
        return True

    return False


# create Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

# create Queue class
class Queue:

    #intialize front and rear and none
    def __init__(self):
        self.front = self.rear = None

    #check for empty queue
    def isEmpty(self):
        return self.front == None

    # adding element to queue
    def enque(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # deleting element from queue
    def deque(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        return str(temp.data)




if __name__=="__main__":

    # making queue objects for week1 and days
    w= Queue()
    d = Queue()

    # input as command line arguments
    month = int(sys.argv[1])
    year = int(sys.argv[2])

    # lists for months and days of months
    months = [0, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print('%s  ' % months[month]),
    print('%d ' % year)

    # list for days of week
    week = ['S', 'M', 'T', 'W', 'Th', 'F', 'S']


    for i in week:
        w.enque(i)

    # print week days
    for i in range(7):
        print(w.deque()),
        print('\t'),
        i=i+1

    # checking for leap year
    if month == 2 and leapYear(year):
        days[month] = 29


    print

    d = day(1, month, year)
    for i in range(d):
        print('\t'),

    # print days
    for j in range(1, days[month] + 1):
        print(j),
        print('\t'),
        if (j + d) % 7 == 0 or j == days[month]:
            print






