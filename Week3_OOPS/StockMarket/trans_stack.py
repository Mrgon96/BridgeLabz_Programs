from Week3_OOPS.StockMarket.stack_link import Stack
import json


class trans_Stack():

    def __init__(self):
        self.data = ''
        # define filename
        self.file = 'transaction_stack.json'

    def create(self):
        # create transactions json file
        temp = {"transactions": []}
        with open(self.file, 'w') as c:
            json.dump(temp, c, indent=2)

        c.close()

    # function to open transactions file
    def open(self):

        with open(self.file, 'r') as c:
            self.data = json.load(c)
            # print(self.data)

        c.close()

    # function to write in transaction file
    def write(self):

        with open(self.file, 'w') as c:
            json.dump(self.data, c, indent=2)

        c.close()

    # function to add transaction
    def addtrans(self, transaction, customer, company, shares):
        self.open()

        # creating stack object
        s = Stack()

        # define trans empty dictionary
        trans = {}
        trans["Transaction_type"] = transaction
        trans["customer"] = customer
        trans["company"] = company
        trans["shares_bought"] = shares

        # write data in transaction json
        self.data["transactions"].append(trans)
        s.push(trans)
        self.write()






