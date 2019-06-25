import json
from Week3_OOPS.StockMarket.stock_acc import stock_acc
from Week3_OOPS.StockMarket.main import main
from Week3_OOPS.StockMarket.trans_stack import trans_Stack
# from Week3_OOPS.StockMarket.transqueue import trans_Queue


class main_menu():

    def __init__(self):
        self.choice = ''
        self.stock = stock_acc()    # object for customer class
        self.cust = main()      # object for company class

        # defining some self variables
        self.customer = ''
        self.shares = 0
        self.company = ''
        self.price = 0

        # object for transaction class
        self.trans = trans_Stack()
        # self.queue = trans_Queue()

    # main menu
    def menu(self):
        print('*********StockCommerce************')
        print('1. Add Account')
        print('2. Login Your Account')
        print('3. Remove Account')
        print('4. Exit')
        try:
            self.choice = input('Enter Your Choice')

            # checking for valid input
            if not self.choice.isdigit():
                raise ValueError
            else:
                if self.choice == '1':
                    self.stock.add_customer()    # add customer from customer class
                elif self.choice == '2':
                    self.login()                 # login for customer
                elif self.choice == '3':
                   self.stock.del_customer()     # delete customer account
                elif self.choice == '4':
                    exit()
                else:
                    print('Choice not in Menu')
                    self.menu()

        # exception handling
        except ValueError:
            print('Enter Correct Choice: ')
            self.menu()

    # login function
    def login(self):
        self.stock.open()

        # input as account holders name
        name = input('Enter Name of account: ')

        # checking for account in json
        for i in range(len(self.stock.data["Customer"])):
            if str(self.stock.data["Customer"][i]['Name']).casefold() == name.casefold():

                customer = str(self.stock.data["Customer"][i]['Name'])
                self.mainmenu(customer)
                return

        # if account not found
        else:
            print('No Account found with that Name/ ......')
            self.login()

    # customer Menu
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

            # get values from company class
            self.shares = self.cust.buy()
            self.company = self.cust.company_return()

            # total buy value for shares
            self.price = self.cust.share_price()

            # passing values to customer class
            self.stock.customer_buy(self.shares, self.company, customer, self.price)

            # add transaction as buy
            self.trans.addtrans(buy, customer, self.company, self.shares)
            # self.queue.addtrans(customer, self.company, self.shares)
            print('***********Shares bought*************')
            self.mainmenu(customer)
        elif ch == '2':
            sell = 'SELL'

            # checking for shares bought
            company2, shares2 = self.stock.customer_sell(customer)
            if company2 is None and shares2 is None:
                print('Please buy Some Shares')
            else:
                # self.queue.addtrans(customer, company2, shares2)

                # add transaction as sell
                self.trans.addtrans(sell, customer, company2, shares2)

                # price of each share
                price2 = self.cust.sell(company2, shares2)

                # getting price of shares sold
                self.stock.sell_value(price2, shares2, customer)
            self.mainmenu(customer)
        elif ch == '3':
            # calling check balance function
            self.stock.check_bal(self.customer)
            self.mainmenu(customer)
        elif ch == '4':
            self.menu()
        else:
            print('Enter Correct Choice...')
            self.mainmenu(customer)

m = main_menu()
m.menu()