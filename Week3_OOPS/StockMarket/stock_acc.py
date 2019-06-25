import json
import pandas as pd


class stock_acc():

    def __init__(self):
        # define file names
        self.cus_file = 'customer.json'
        self.com_file = 'company.json'
        self.tra_file = 'transaction.json'

        # define self variables
        self.data = {}
        self.choice = ''

    # function to create customer json
    def create(self):
        temp = {"Customer": []}
        with open(self.cus_file, 'w') as c:
            json.dump(temp, c, indent=2)

        c.close()

    # function to open customer json
    def open(self):

        with open(self.cus_file, 'r') as c:
            self.data=json.load(c)
            # print(self.data)

        c.close()

    # function to write customer json
    def write(self):

        with open(self.cus_file, 'w') as c:
            json.dump(self.data, c, indent=2)

        c.close()

    # Function to add customer account
    def add_customer(self):
        self.open()
        customer = {}
        try:
            # user inputs
            customer['Name'] = input('Enter Your Name: ')
            customer['Balance'] = input('Enter Your Balance: ')

            # empty stock list
            customer['Stock'] = []
            if customer['Name'].isalpha() is False and customer['Balance'].isdigit() is False:
                raise ValueError
            else:
                # write data into customer json
                self.data['Customer'].append(customer)
                self.write()
        except ValueError:
            print('Enter Proper values')
            self.add_customer()

    # function to delete customer account
    def del_customer(self):
        self.open()
        # user input name to delete account
        name = input('Enter Name of account to delete: ')
        for i in range(len(self.data["Customer"])):
            if str(self.data["Customer"][i]['Name']).casefold() == name.casefold():

                # delete customer account and write into json
                del self.data["Customer"][i]
                self.write()
                print('Record Deleted Successfully')
                return
        else:
            print('No record found/......')

    # function for shares bought by customer
    def customer_buy(self, shares, company, customer, price):
        self.open()
        for i in range(len(self.data["Customer"])):
            if customer == str(self.data["Customer"][i]['Name']):

                # check for balance of customer
                if price < int(self.data["Customer"][i]['Balance']):
                    self.open()
                    s = {}
                    s['company'] = company
                    s['shares'] = shares
                    self.data["Customer"][i]["Stock"].append(s)
                    self.data["Customer"][i]["Balance"] = int(self.data["Customer"][i]["Balance"]) - price
                    self.write()
                else:
                    print('Dont have Enough Balance....')

    # function to sell customer shares
    def cus_sell(self, customer):
        for i in range(len(self.data["Customer"])):
            if customer == str(self.data["Customer"][i]['Name']):
                # take input for company name and shares to sale
                company = input('Enter Company Name to Sell Shares of:')
                shares = int(input('Enter shares of that Company: '))

                # delete the company and shares object from stock array
                for k in range(len(self.data["Customer"][i]["Stock"])):
                    if company.casefold() == str(self.data["Customer"][i]["Stock"][k]["company"]).casefold() and \
                     shares == int(self.data["Customer"][i]["Stock"][k]["shares"]):
                        print("Selling Your Shares")
                        del self.data["Customer"][i]["Stock"][k]
                        self.write()

            else:
                print('no record..')
                self.customer_sell(customer)

        # return company name and shares
        return company, shares

    # function to sell customer shares
    def customer_sell(self, customer):
        self.open()
        try:
            for i in range(len(self.data["Customer"])):
                if customer == str(self.data["Customer"][i]['Name']):
                    if len(self.data["Customer"][i]["Stock"]) > 0:

                        # print stock array for customer
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

        # return company name and shares
        return company, shares

    # calculate sell value for shares
    def sell_value(self, price, shares, customer):
        total = shares * price

        self.open()
        for i in range(len(self.data["Customer"])):
            if customer.casefold() == str(self.data["Customer"][i]['Name']).casefold():

                # adding total sell value to customer balance
                self.data["Customer"][i]["Balance"] = int(self.data["Customer"][i]["Balance"]) + total
                self.write()

    # function to check balance
    def check_bal(self, customer):
        for i in range(len(self.data["Customer"])):
            if customer.casefold() == str(self.data["Customer"][i]['Name']).casefold():
                # print customer balance
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


