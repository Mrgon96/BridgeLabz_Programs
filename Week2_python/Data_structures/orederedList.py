fileName = 'abc.txt'

# class Node with objects data and next as None
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# linked list class
class Linkedlist:

    # intializing head as None
    def __init__(self):
        self.head=None

    # push function for new data
    def push(self,newData):
        new_node = Node(newData)
        new_node.next = self.head
        self.head = new_node

    # sorted insert function
    def sorted_insert(self, new_node):

        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else :
            current = self.head
            while ( current.next is not None and
                    current.next.data < new_node.data ):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    # function for printing list
    def printList(self):
        temp = self.head
        print('This is your Linked List: ')
        while temp:
            print(temp.data),
            temp=temp.next
        print

    # searching element
    def search(self,i):
        current = self.head
        i=int(i)
        while current != None:
            if current.data == i:
                return True
            current = current.next

        return False

    #function to delete node
    def deleteNode(self, key):
        temp = self.head

        #if head is None
        if (temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp = None
                return

        # if head is not None
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

    # read file and store in list
        if fp:
            print('File Opened Successfully! ')
            content = fp.read()
            Words = (content.split())

    except IOError:
        print('File is not Present')

    link_list = Linkedlist()

    # inserting from list to nodes in linked list
    for i in Words:
        i = int(i)
        new_node = Node(i)
        link_list.sorted_insert(new_node)


    link_list.printList()


    str1 = input('Enter the String you want to Search: ')

    # search element in linked list
    #if present delete element and update file
    if link_list.search(str1):
        print('Element Found in Linked List.....')
        link_list.deleteNode(str1)
        Words.remove(str1)
        fw = open(fileName, "w+")
        for i in Words:
            fw.write(i)
            fw.write('\n')

    # if absent insert element and update file
    else:
        print('Element not found Linked list.....')
        print("Adding ", str1, " to List")
        link_list.push(str1)
        Words.append(str1)
        fa = open(fileName, "a")
        fa.write('\n')
        fa.write(str1)


#closing the file
fp.close()
