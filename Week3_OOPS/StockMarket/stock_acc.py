import json


class stock():

    def __init__(self):
        self.cus_file = 'customer.json'
        self.com_file = 'company.json'
        self.tra_file = 'transaction.json'
        self.data = {}

    def create(self):
        temp = {"Customer":[]}
        with open(self.cus_file, 'w') as c:
            json.dump(temp, c, indent=2)

        c.close()

    def open(self):

        with open(self.cus_file, 'r') as c:
            self.data=json.load(c)
            # print(self.data)

        c.close()

    def write(self):

        with open(self.cus_file, 'w') as c:
            json.dump(self.data, c, indent=2)

        c.close()



s = stock()

s.open()
