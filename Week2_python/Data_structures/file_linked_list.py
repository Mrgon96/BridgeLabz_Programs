fileName = '123.txt'

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head=None

    def push(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        print('This is your Linked List: ')
        while temp:
            print(temp.data),
            temp=temp.next
        print

    def search(self,i):
        current = self.head

        while current != None:
            if current.data == i:
                return True

        return False

try:
    fp = open(fileName, 'r')
    if fp:
        print('File Opened Successfully! ')
        content = fp.read()
        Words = content.split()


except IOError:
    print('File is not Present')


if __name__=='__main__':
    link_list = Linkedlist()
    for i in Words:
        link_list.push(i)

    link_list.printList()

    str1 = input('Enter the String you want to Search: ')

    if link_list.search():
        print('Element Found.....')
    else:
        print('Element not found.....')

#closing the file
fp.close()