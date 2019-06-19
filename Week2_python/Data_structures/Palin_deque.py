# creating a DEqueue
class Palin_deque:

    # create empty dequeue
    def __init__(self):
        self.deque = []

    # check for empty deque
    def empty_deque(self):
        return self .deque == []

    # insert element at rear
    def append_rear(self, element):
        self.deque.insert(0, element)

    # insert element at front
    def append_front(self, element):
        self.deque.insert(-1, element)

    # delete element from rear
    def pop_rear(self):
        return self.deque.pop(0)

    # delete element from front
    def pop_front(self):
        return self.deque.pop(-1)

    # get element from rear
    def rear_element(self):
        return self.deque(0)

    # get element from front
    def front_element(self):
        return self.deque(-1)

    # print DEqueue
    def print_deque(self):
        for i in self.deque:
            print(i),


d = Palin_deque()
str2 = input('Enter String to Check for Palindrome: ')

# insert elements in adequeue
for i in str2:
    d.append_rear(i)


def check_palin():
    # while length is greate than 1
    while len(d.deque) > 1:
        # pop element from front and rear
        a = d.pop_front()
        b = d.pop_rear()

        # if popped elements are same
        if (a == b):
            print(a, ' popped from front and rear')
        else:
            break

    print('Queue at last')
    d.print_deque()

    # check for palindrome
    if d.empty_deque() == True or len(d.deque) == 1:
        return True
    else:
        return False


if(check_palin()):
    print('String is Palindrome....')
else:
    print('String is not palindrome')
