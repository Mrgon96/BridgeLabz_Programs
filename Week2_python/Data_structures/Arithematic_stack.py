class Arithmetic_stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0 , item)

    def pop(self):
        return self.items.pop(0)

    def print_Stack(self):
        for i in self.items:
            print(i)


s = Arithmetic_stack()

expression = '(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)'

for i in expression:
    if( i == '('):
        s.push('(')
    elif( i == ')'):
        s.pop()

if s.isEmpty():
    print('Arithmatic expression is balanced')
else:
    print('Arithmatic expression is not balanced')