fileName = 'abc.txt'

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head=None

    def push(self,newData):


        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        
        if newData < self.head.data:
            newNode.next = self.head
            self.head = newNode
        else:

            while(temp):
                temp = temp.next
            temp.next = newNode


        # temp = self.head
        # while(temp.next):
        #     if newData < self.head.data:
        #         newNode.next = self.head
        #         self.head = newNode
        #     elif newData > temp.data and newData < temp.next.data:
        #         temp.next = newNode
        #         newNode.next = temp.next.next


        #     while(temp.next):
        #         temp =temp.next
        #     temp.next = newNode



        # while temp.next != None:
        #
        #     if(newData > temp.data):
        #         newNode = Node(newData)
        #         temp.next = newNode
        #         newNode.next = None
        #     temp=temp.next


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
            current = current.next

        return False

    def deleteNode(self, key):
        temp = self.head

        if (temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp==None:
            return

        prev.next =temp.next

        temp = None




if __name__=='__main__':

    try:
        fp = open(fileName, 'r')

        if fp:
            print('File Opened Successfully! ')
            content = fp.read()
            Words = content.split()


    except IOError:
        print('File is not Present')

    link_list = Linkedlist()
    for i in Words:
        link_list.push(i)


    link_list.printList()

    str1 = input('Enter the String you want to Search: ')

    if link_list.search(str1):
        print('Element Found in Linked List.....')
        link_list.deleteNode(str1)
        Words.remove(str1)
        fw = open(fileName, "w+")
        for i in Words:
            fw.write(i)
            fw.write('\n')
        link_list.printList()
    else:
        print('Element not found Linked list.....')
        print("Adding ",str1," to List")
        link_list.push(str1)
        Words.append(str1)
        fa = open(fileName,"a")
        fa.write('\n')
        fa.write(str1)

#closing the file
fp.close()