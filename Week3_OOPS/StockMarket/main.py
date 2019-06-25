import json


class main():
    def __init__(self):
        # define file names
        self.cus_file = 'customer.json'
        self.com_file = 'company.json'
        self.tra_file = 'transaction.json'

        # define some self variables
        self.data = {}
        self.company_name = ''
        self.shares = 0
        self.i = 0

    # function to open company json
    def open_company(self):

        with open(self.com_file, 'r') as c:
            self.data=json.load(c)
            #print(self.data)
            #print(json.dumps(self.data,indent=4))

        c.close()

    # function to write company json
    def write_company(self):

        with open(self.com_file, 'w') as c:
            json.dump(self.data, c, indent=2)

        c.close()

    # buy function
    def buy(self):
        self.open_company()
        # check for companies in  company json
        for i in range(len(self.data["Companies"])):
            print(i+1, self.data["Companies"][i])

        # user input to get name of company
        self.company_name = input('Enter Company Name to Buy Shares of: ')
        if self.company_name.isalpha():
            for i in range(len(self.data["Companies"])):
                if str(self.data["Companies"][i]['Name']).casefold() == self.company_name.casefold():
                    try:
                        self.i = i

                        # user input for number of shares to buy
                        self.shares = int(input('Enter Number of Shares to Buy'))
                        if self.shares > self.data["Companies"][i]['Shares']:
                            print('Exceeding Shares limit')
                            self.buy()
                        else:

                            # subtract shares of company
                            self.data["Companies"][i]['Shares'] = self.data["Companies"][i]['Shares'] - self.shares
                            self.write_company()

                    except ValueError:
                        print('Enter Shares in Numbers')
                        self.buy()
        else:
            print('Enter Proper Company name')
            self.buy()

        # return number for shares bought
        return self.shares

    # sell function
    def sell(self, company, shares):
        self.open_company()

        # find company in company json
        for i in range(len(self.data["Companies"])):
            if str(self.data["Companies"][i]['Name']).casefold() == company.casefold():

                # add shares to company shares
                self.data["Companies"][i]['Shares'] = int(self.data["Companies"][i]['Shares']) + shares
                self.write_company()

            # return price of 1 share
            return int(self.data["Companies"][i]['price'])

    def company_return(self):
        # return company name
        return self.company_name

    def share_price(self):
        # return total price for shares bought
        return self.shares * int(self.data["Companies"][self.i]['price'])


    # function to add company in company json
    def add_company(self):
        try:
            # take input for name shares and per share price
            name = input('Enter Name of Company: ')
            shares = input('Enter Shares of Company: ')
            price = input('Enter price of 1 share: ')


            if name.isalpha() == False and shares.isdigit() == False and price.isdigit() == False:
                raise ValueError
            else:
                self.open_company()
                comp = {}
                comp['Name'] = name
                comp['Shares'] = int(shares)
                comp['price'] = int(price)

                # add data
                self.data["Companies"].append(comp)
                # write data to json file
                self.write_company()
        except ValueError:
            print('Enter proper Values....')
            self.add_company()

    # function to remove company from company json
    def remove_company(self):
        self.open_company()
        try:
            company=input('Enter Name of Company to be Removed: ')
            if company.isalpha() is False:
                raise  ValueError
            else:
                for i in range(len(self.data["Companies"])):
                    if company.casefold() == str(self.data["Companies"][i]['Name']).casefold():
                        del self.data["Companies"][i]
                        self.write_company()

        except ValueError:
            print('Enter Proper Company name: ')
            self.remove_company()

    # company Menu
    def compmenu(self):

        print('******COMPANY MENU********')
        print('1. Add Company')
        print('2. Remove Company')
        print('3. Exit')
        ch = int(input('Enter Choice: '))
        if ch == 1:
            self.add_company()
            print('......Company Added.........')
            self.compmenu()
        elif ch == 2:
            self.remove_company()
            print('........Company Removed.........')
            self.compmenu()
        elif ch == 3:
            exit()
        else:
            print('Enter Proper Choice')
            self.compmenu()


m = main()
m.compmenu()


