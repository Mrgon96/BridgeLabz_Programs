import json



class main():
    def __init__(self):
        self.cus_file = 'customer.json'
        self.com_file = 'company.json'
        self.tra_file = 'transaction.json'
        self.data = {}
        self.company_name = ''
        self.shares = 0
        self.i = 0



    def open_company(self):

        with open(self.com_file, 'r') as c:
            self.data=json.load(c)
            #print(self.data)
            #print(json.dumps(self.data,indent=4))

        c.close()

    def write_company(self):

        with open(self.com_file, 'w') as c:
            json.dump(self.data, c, indent=2)

        c.close()



    def buy(self):
        self.open_company()
        for i in range(len(self.data["Companies"])):
            print(i+1, self.data["Companies"][i])
        self.company_name = input('Enter Company Name to Buy Shares of: ')
        if self.company_name.isalpha():
            for i in range(len(self.data["Companies"])):
                if str(self.data["Companies"][i]['Name']).casefold() == self.company_name.casefold():
                    try:
                        self.i = i
                        self.shares = int(input('Enter Number of Shares to Buy'))
                        if self.shares > self.data["Companies"][i]['Shares']:
                            print('Exceeding Shares limit')
                            self.buy()
                        else:
                            self.data["Companies"][i]['Shares'] = self.data["Companies"][i]['Shares'] - self.shares
                            self.write_company()

                    except ValueError:
                        print('Enter Shares in Numbers')
                        self.buy()
        else:
            print('Enter Proper Company name')
            self.buy()


        return self.shares

    def sell(self, company, shares):
        self.open_company()
        for i in range(len(self.data["Companies"])):
            if str(self.data["Companies"][i]['Name']).casefold() == company.casefold():
                self.data["Companies"][i]['Shares'] = int(self.data["Companies"][i]['Shares']) + shares
                self.write_company()
            return int(self.data["Companies"][i]['price'])

    def company_return(self):
        return self.company_name

    def share_price(self):
        return self.shares * int(self.data["Companies"][self.i]['price'])


m = main()


