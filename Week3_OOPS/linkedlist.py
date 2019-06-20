# Node class having object with data and next is none
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class linked list
class Linked_list:

    # intialize head
    def __init__(self):
        self.head = None

    # function to insert new node at head
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    # printing linked list
    def print_list(self):
        temp = self.head
        print('This is your Linked List: ')
        while temp:
            print(temp.data),
            temp=temp.next
        print

    # search for particular node
    def search(self,i):
        current = self.head

        while current != None:
            if current.data == i:
                return True
            current = current.next

        return False

    # function for deleting node
    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None


