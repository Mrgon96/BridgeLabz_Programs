import json

# define address class
class Address:
    def __init__(self):
        # define variables
        self.data = {}
        self.filename='address.json'
        self.choice = ''
        self.uchoice = ''

    # function to create file
    def create(self):
        temp = {'AddressBook': []}
        with open(self.filename, 'w') as file:
            json.dump(temp, file, indent=2)
        file.close()

    # function open and read file
    def open(self):
        with open(self.filename, 'r') as file2:
            self.data = json.load(file2)
        file2.close()

    # function to write in file
    def write(self):
        with open(self.filename, 'w') as file3:
            json.dump(self.data, file3, indent=2)
        file3.close()

    def add(self):
        # define dictionary in python and object for json

        a = {}
        a['first_name'] = input('Enter Your First Name: ')
        a['last_name'] = input('Enter Your Last Name: ')
        a['address'] = input('Enter Your Address: ')
        a['city'] = input('Enter Your City: ')
        a['state'] = input('Enter Your State: ')
        a['zip'] = input('Enter Your Zip: ')
        a['phone_number'] = input('Enter Your Phone Number: ')
        try:
            # validation
            if a['first_name'].isalpha()  and a['last_name'].isalpha() and a['address'].isalpha() and \
        a['city'].isalpha() and a['state'].isalpha() and a['zip'].isdigit() and a['phone_number'].isdigit():
                self.data["AddressBook"].append(a)
                self.write()
            else:
                raise ValueError

        # Exception handling
        except ValueError:
            print('Enter DATA Again ')
            print('Enter Names and Numbers Properly')
            self.add()

    # function to remove record
    def remove(self):
        first = input('Enter First name: ')
        last = input('Enter Last name: ')
        for i in range(len(self.data["AddressBook"])):
            # checking for first and last name
            if str(self.data["AddressBook"][i]['first_name']).casefold() == first.casefold() and \
                 str(self.data["AddressBook"][i]['last_name']).casefold() == last.casefold():
                print("Record Deleted Successfully")
                del self.data["AddressBook"][i]

                return
        else:
            print("\nNo Record Found ")

    # function to update particular fields of record
    def update(self):
        first = input('Enter First name: ')
        last = input('Enter Last name: ')
        # search address book for first and last name
        for i in range(len(self.data["AddressBook"])):
            if str(self.data["AddressBook"][i]['first_name']).casefold() == first.casefold() and \
                    str(self.data["AddressBook"][i]['last_name']).casefold() == last.casefold():
                print('Your Record is present')
                print('What do you want to update? ')
                print('1.Address 2.City 3.State 4.Zip 5.Phone number:')
                self.uchoice = input('Enter Choice')
                if self.uchoice == '1':
                    ad = input('Enter New Address')
                    self.data["AddressBook"][i]['address'] = ad
                elif self.uchoice == '2':
                    ad = input('Enter New City')
                    self.data["AddressBook"][i]['city'] = ad
                elif self.uchoice == '3':
                    ad = input('Enter New State')
                    self.data["AddressBook"][i]['state'] = ad
                elif self.uchoice == '4':
                    ad = input('Enter New Zip Code')
                    self.data["AddressBook"][i]['zip'] = ad
                elif self.uchoice == '5':
                    ad = input('Enter New Phone Number')
                    self.data["AddressBook"][i]['phone_number'] = ad
                else:
                    print('Enter Correct Choice')
                    self.update()

                return
        else:
            print("\nNo Record Found ")

    # function to validate choice
    def menu(self):
        try:
            print('*********Address Book Menu**********')
            print('1. Add record')
            print('2. Remove record')
            print('3. Update record')
            print('4. Print Address Book')
            print('5. Exit')
            self.choice = input('Enter your choice ==> ')
            if self.choice.isdigit()!=True:
                raise ValueError
            else:
                self.options()

        except ValueError:
            print('Incorrect Choice')
            print('Enter Again')
            self.menu()

    # function to print address Book
    def print(self):
        self.open()
        for i in range(len(self.data["AddressBook"])):
            f = str(self.data["AddressBook"][i]['first_name'])
            l = str(self.data["AddressBook"][i]['last_name'])
            a = str(self.data["AddressBook"][i]['address'])
            c = str(self.data["AddressBook"][i]['city'])
            s = str(self.data["AddressBook"][i]['state'])
            z = str(self.data["AddressBook"][i]['zip'])
            p = str(self.data["AddressBook"][i]['phone_number'])
            print('Number ', i+1)
            print('First Name:', f)
            print('Last Name: ', l)
            print('Address: ', a)
            print('City: ', c)
            print('State: ', s)
            print('Zip: ', z)
            print('Phone Number: ', p)

    # main menu for Address Book
    def options(self):
        if self.choice == '1':
            self.open()
            self.add()
            self.menu()
        elif self.choice == '2':
            self.open()
            self.remove()
            self.write()
            self.menu()
        elif self.choice == '3':
            self.open()
            self.update()
            self.write()
            self.menu()
        elif self.choice == '4':
            self.print()
        elif self.choice == '5':
            exit()
        else:
            print('Enter Correct Choice...')
            self.menu()


# make object and call class
a = Address()
a.menu()














