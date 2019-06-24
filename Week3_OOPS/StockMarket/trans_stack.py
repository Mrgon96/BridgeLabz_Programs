from Week3_OOPS.StockMarket.stack_link import Stack
import json

class trans_Stack():

    def __init__(self):
        self.data = ''
        self.file = 'transaction_stack.json'

    def create(self):
        temp = {"transactions": []}
        with open(self.file, 'w') as c:
            json.dump(temp, c, indent=2)

        c.close()

    def open(self):

        with open(self.file, 'r') as c:
            self.data = json.load(c)
            # print(self.data)

        c.close()

    def write(self):

        with open(self.file, 'w') as c:
            json.dump(self.data, c, indent=2)

        c.close()

    def addtrans(self, transaction, customer, company, shares):
        self.open()
        s = Stack()
        trans = {}
        trans["Transaction_type"] = transaction
        trans["customer"] = customer
        trans["company"] = company
        trans["shares_bought"] = shares
        self.data["transactions"].append(trans)
        s.push(trans)
        self.write()






