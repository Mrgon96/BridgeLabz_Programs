import json
from Week3_OOPS.StockMarket.main import main

class stock_acc():

    def __init__(self):
        self.main = main()
        self.cus_file = 'customer.json'
        self.com_file = 'company.json'
        self.tra_file = 'transaction.json'
        self.data = {}
        self.choice = ''

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

    def add_customer(self):
        self.open()
        customer ={}
        try:
            customer['Name'] = input('Enter Your Name: ')
            customer['Balance'] = input('Enter Your Balance: ')
            customer['Stock'] = []
            if  customer['Name'].isalpha()!=True and customer['Balance'].isdigit()!= True:
                raise ValueError
            else:
                self.data['Customer'].append(customer)
                self.write()
        except ValueError:
            print('Enter Proper values')
            self.add_customer()

    def del_customer(self):
        self.open()
        name = input('Enter Name of account to delete: ')
        for i in range(len(self.data["Customer"])):
            if str(self.data["Customer"][i]['Name']).casefold() == name.casefold():
                del self.data["Customer"][i]
                self.write()
                print('Record Deleted Successfully')
                return
        else:
            print('No record found/......')

    def customer_buy(self, shares, company, customer, price):
        self.open()
        for i in range(len(self.data["Customer"])):
            if customer == str(self.data["Customer"][i]['Name']):
                if price > int(self.data["Customer"][i]['Balance']):
                    print('Dont have Enough Balance..')
                    self.customer_buy()
                else:
                    s={}
                    s['company']=company
                    s['shares']=shares
                    self.data["Customer"][i]["Stock"].append(s)
                    self.data["Customer"][i]["Balance"] = int(self.data["Customer"][i]["Balance"]) - price
                    self.write()

    def customer_sell(self, shares, company, customer, price):
        self.open()
        for i in range(len(self.data["Customer"])):
            if customer == str(self.data["Customer"][i]['Name']):
                    s={}
                    s['company']=company
                    s['shares']=shares
                    self.data["Customer"][i]["Stock"].append(s)
                    self.data["Customer"][i]["Balance"] = int(self.data["Customer"][i]["Balance"]) - price
                    self.write()












s = stock_acc()


