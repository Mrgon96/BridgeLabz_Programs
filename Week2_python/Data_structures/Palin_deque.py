class Palin_deque:
    def __init__(self):
        self.deque = []

    def empty_deque(self):
        return self .deque == []

    def append_rear(self, element):
        self.deque.insert(0, element)

    def append_front(self, element):
        self.deque.insert(-1, element)

    def pop_rear(self):
        return self.deque.pop(0)

    def pop_front(self):
        return self.deque.pop(-1)

    def rear_element(self):
        return self.deque(0)

    def front_element(self):
        return self.deque(-1)

    def print_deque(self):
        for i in self.deque:
            print(i),


d = Palin_deque()
str = 'somesh'
for i in str:
    d.append_rear(i)

while len(d.deque) > 1:
    a = d.pop_front()
    b = d.pop_rear()
    if(a == b):
        print(a, ' popped from front and rear')
    else:
        break

print('Queue at last')
d.print_deque()
if d.empty_deque()== True or len(d.deque) == 1:
    print('String is Palindrome')
else:
    print('String is not palindrome')
