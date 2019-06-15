import sys

def day(d,m,y):
    y0= y - (( 14 - m)/12)
    x = y0 + y0/4 - y0/100 + y0/400
    m0 = m + 12 *((14 - m)/12) - 2
    d0 = (d + x + ((31 * m0)/12))%7
    return d0



def leapYear(year):
    if year%4==0 and year%100!=0 or year%400 == 0:
        return True

    return False




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


    def deque(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        return str(temp.data)




if __name__=="__main__":
    w= Queue()
    d = Queue()

    month = int(sys.argv[1])
    year = int(sys.argv[2])

    months = [0, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print('%s  ' % months[month]),
    print('%d ' % year)
    week = ['S', 'M', 'T', 'W', 'Th', 'F', 'S']

    for i in week:
        w.enque(i)

    for i in range(7):
        print(w.deque()),
        print('\t'),
        i=i+1


    if month == 2 and leapYear(year):
        days[month] = 29


    print
    d = day(1, month, year)
    for i in range(d):
        print('\t'),
    for j in range(1, days[month] + 1):
        print(j),
        print('\t'),
        if (j + d) % 7 == 0 or j == days[month]:
            print






