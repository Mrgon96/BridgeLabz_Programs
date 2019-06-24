import json
from Week3_OOPS.StockMarket.main import main
import pandas as pd

class stock_acc():

    def __init__(self):
        self.main = main()
        self.cus_file = 'customer.json'
        self.com_file = 'company.json'
        self.tra_file = 'transaction.json'
        self.data = {}
        self.choice = ''

    def create(self):
        temp = {"Customer": []}
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
                if price < int(self.data["Customer"][i]['Balance']):
                    self.open()
                    s = {}
                    s['company'] = company
                    s['shares'] = shares
                    self.data["Customer"][i]["Stock"].append(s)
                    self.data["Customer"][i]["Balance"] = int(self.data["Customer"][i]["Balance"]) - price
                    self.write()
                else:
                    print('Dont have Enough Balance..')


    def cus_sell(self, customer):
        for i in range(len(self.data["Customer"])):
            if customer == str(self.data["Customer"][i]['Name']):
                company = input('Enter Company Name to Sell Shares of:')
                shares = int(input('Enter shares of that Company: '))
                for k in range(len(self.data["Customer"][i]["Stock"])):
                    if company.casefold() == str(self.data["Customer"][i]["Stock"][k]["company"]).casefold() and \
                     shares == int(self.data["Customer"][i]["Stock"][k]["shares"]):
                        print("Selling Your Shares")
                        del self.data["Customer"][i]["Stock"][k]
                        self.write()

            else:
                print('no record..')
                self.customer_sell(customer)
        return company, shares

    def customer_sell(self, customer):
        self.open()
        try:
            for i in range(len(self.data["Customer"])):
                if customer == str(self.data["Customer"][i]['Name']):
                    if len(self.data["Customer"][i]["Stock"]) > 0:
                        for j in self.data["Customer"][i]["Stock"]:
                            print(j)

                        company,shares = self.cus_sell(customer)
                    else:
                        print('You havent Bought any shares')
                        company = None
                        shares = None

        except ValueError:
            print('Enter Proper Values..........')
            self.customer_sell(customer)

        return company, shares



    def sell_value(self, price, shares, customer):
        total = shares * price

        self.open()
        for i in range(len(self.data["Customer"])):
            if customer.casefold() == str(self.data["Customer"][i]['Name']).casefold():
                self.data["Customer"][i]["Balance"] = int(self.data["Customer"][i]["Balance"]) + total
                self.write()

    def check_bal(self, customer):
        for i in range(len(self.data["Customer"])):
            if customer.casefold() == str(self.data["Customer"][i]['Name']).casefold():
                print('Your Balance is')
                print(self.data["Customer"][i]["Balance"])


    # def del_comp(self, company, shares, customer):
    #     self.open()
    #     for i in range(len(self.data["Customer"])):
    #         if customer == str(self.data["Customer"][i]['Name']):
    #             for k in range(len(self.data["Customer"][i]["Stock"])):
    #                 if company.casefold() == str(self.data["Customer"][i]["Stock"][k]["company"]) and \
    #                         shares == self.data["Customer"][i]["Stock"][k]["shares"]:
    #                     del self.data["Customer"][i]["Stock"][k]
    #                     self.write()




























s = stock_acc()


