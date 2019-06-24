from Week3_OOPS.StockMarket.quelink import Queue
import json
from datetime import datetime

class trans_Queue():

    def __init__(self):
        self.data = ''
        self.file = 'transaction_queue.json'

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

    def addtrans(self, customer, company, shares):
        self.open()
        q = Queue()
        trans = {}
        trans["customer"] = customer
        trans["company"] = company
        trans["shares_bought"] = shares
        trans["date-time"] = datetime.datetime.now()
        self.data["transactions"].append(trans)
        q.enque(trans)
        self.write()

