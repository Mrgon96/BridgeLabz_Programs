import json
from Week3_OOPS.StockMarket.stock_acc import stock_acc
from Week3_OOPS.StockMarket.main import main
from Week3_OOPS.StockMarket.trans_stack import trans_Stack
from Week3_OOPS.StockMarket.transqueue import trans_Queue


class main_menu():

    def __init__(self):
        self.choice = ''
        self.stock = stock_acc()
        self.cust = main()
        self.customer = ''
        self.shares = 0
        self.company = ''
        self.price = 0
        self.trans = trans_Stack()
        self.queue = trans_Queue()

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

        ch = input('Enter Choice ==>')
        if ch == '1':
            buy = 'BUY'
            self.shares = self.cust.buy()
            self.company = self.cust.company_return()
            self.price = self.cust.share_price()
            self.stock.customer_buy(self.shares, self.company, customer, self.price)
            self.trans.addtrans(buy, customer, self.company, self.shares)
            self.queue.addtrans(customer, self.company, self.shares)
            print('***********Shares bought*************')
            self.mainmenu(customer)
        elif ch == '2':
            sell = 'SELL'
            company2, shares2 = self.stock.customer_sell(customer)
            if company2 is None and shares2 is None:
                print('Please buy Some Shares')
            else:
                self.queue.addtrans(customer, company2, shares2)
                self.trans.addtrans(sell, customer, company2, shares2)
                price2 = self.cust.sell(company2, shares2)
                self.stock.sell_value(price2, shares2, customer)
            self.mainmenu(customer)
        elif ch == '3':
            self.stock.check_bal(self.customer)
            self.mainmenu(customer)
        elif ch == '4':
            self.menu()
        else:
            print('Enter Correct Choice...')
            self.mainmenu(customer)

m = main_menu()
m.menu()