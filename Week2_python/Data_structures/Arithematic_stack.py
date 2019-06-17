#class Defined to create stack

class Arithmetic_stack:

    def __init__(self):
        self.items = []          # initializing the stack

    def isEmpty(self):
        return self.items == []   # checking for empty

    def push(self, item):
        self.items.insert(0 , item)    # pushing item in top of stack

    def pop(self):
        return self.items.pop(0)      # pop item from top

    def print_Stack(self):
        for i in self.items:           # print stack
            print(i)



# create stack classs object
s = Arithmetic_stack()


# expression to be checked
expression = '(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)'

def balance_eq():
        # push and pop for every bracket found
        for i in expression:

            if( i == '('):
                s.push('(')
            elif( i == ')'):
                s.pop()

# checking for balanced expression
        if s.isEmpty():
            return True
        else:
            return False

if(balance_eq()):
    print('Equation is Balanced')
else:
    print('Equation is not balanced')