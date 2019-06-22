import json
from Week3_OOPS.StockMarket.stock_acc import stock_acc
from Week3_OOPS.StockMarket.main import main


class main_menu():

    def __init__(self):
        self.choice = ''
        self.stock = stock_acc()
        self.cust = main()
        self.customer =''
        self.shares = 0
        self.company = ''
        self.price = 0


    def menu(self):
        print('*********StockCommerce************')
        print('1. Add Account')
        print('2. Login Your Account')
        print('3. Remove Account')
        print('4. Exit')
        try:
            self.choice = input('Enter Your Choice')
            if not self.choice.isdigit():
                raise ValueError
            else:
                if self.choice == '1':
                    self.stock.add_customer()
                elif self.choice == '2':
                    self.login()
                elif self.choice == '3':
                   self.stock.del_customer()
                elif self.choice == '4':
                    exit()
                else:
                    print('Choice not in Menu')
                    self.menu()
        except ValueError:
            print('Enter Correct Choice: ')
            self.menu()

    def login(self):
        self.stock.open()
        name = input('Enter Name of account: ')
        for i in range(len(self.stock.data["Customer"])):
            if str(self.stock.data["Customer"][i]['Name']).casefold() == name.casefold():

                customer = str(self.stock.data["Customer"][i]['Name'])
                self.mainmenu(customer)
                return
        else:
            print('No Account found with that Name/ ......')
            self.login()

    def mainmenu(self, customer):
        self.customer = customer
        print('Welcome ', self.customer)
        print('1. Buy Shares')
        print('2. Sell Shares')
        print('3. Check Balance')
        print('4. logout')

        ch = input('Enter Choice')
        if ch == '1':
            self.shares = self.cust.buy()
            self.company = self.cust.company_return()
            self.price = self.cust.share_price()
            self.stock.customer_buy(self.shares, self.company, self.customer, self.price)
            print('***********Shares bought*************')
            self.mainmenu(customer)
        elif ch == '2':
            self.cust.sell()
        elif ch == '3':
            self.cust.checkbalance()
        elif ch == '4':
            self.menu()
        else:
            print('Enter Correct Choice...')
            self.mainmenu(customer)

m = main_menu()
m.menu()