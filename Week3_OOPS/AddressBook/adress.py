import tkinter as tk
from tkinter import *
import json
import pandas as pd
from pandas.io.json import json_normalize

class Address():
    def __init__(self):
        self.data={}
        self.filename='address.json'
        self.choice = ''
        self.uchoice = ''

    def create(self):
        temp = {'AddressBook':[]}
        with open(self.filename, 'w') as file:
            json.dump(temp, file, indent=2)
        file.close()

    def open(self):
        with open(self.filename, 'r') as file2:
            self.data = json.load(file2)
        file2.close()

    def write(self):
        with open(self.filename, 'w') as file3:
            json.dump(self.data, file3, indent=2)
        file3.close()

    # def gui(self):
    #     a = Tk()
    #     a.title('Address Book')
    #     a.geometry("400x550")
    #
    #     Label(a, text='First Name', bg='lightgreen').place(x=150, y=20)
    #     Label(a, text='Last Name', bg='lightgreen').place(x=150, y=80)
    #     e1 = Entry(a, highlightcolor='purple')
    #     e2 = Entry(a, highlightcolor='purple')
    #     e1.place(x=100, y=45)
    #     e2.place(x=100, y=105)
    #     Label(a, text='Address', bg='lightgreen').place(x=160, y=150)
    #     e3 = Entry(a, highlightcolor='purple')
    #     Label(a, text='City', bg='lightgreen').place(x=170, y=210)
    #     e4 = Entry(a, highlightcolor='purple')
    #     Label(a, text='State', bg='lightgreen').place(x=165, y=270)
    #     e5 = Entry(a, highlightcolor='purple')
    #     e3.place(x=100, y=175)
    #     e4.place(x=100, y=235)
    #     e5.place(x=100, y=295)
    #     Label(a, text='Zip', bg='lightgreen').place(x=175, y=330)
    #     e6 = Entry(a, highlightcolor='purple')
    #     e6.place(x=100, y=355)
    #     Label(a, text='Mobile Number', bg='lightgreen').place(x=135, y=390)
    #     e7 = Entry(a, highlightcolor='purple')
    #     e7.place(x=100, y=415)
    #     submitbutton = Button(a, highlightcolor='green', width=10, height=2, text='Submit', command=self.add()).place(x=130,
    #                                                                                                              y=475)
    #     a.mainloop()

    def add(self):
        a = {}
        a['first_name'] = input('Enter Your First Name: ')
        a['last_name'] = input('Enter Your Last Name: ')
        a['address'] = input('Enter Your Address: ')
        a['city'] = input('Enter Your City: ')
        a['state'] = input('Enter Your State: ')
        a['zip'] = input('Enter Your Zip: ')
        a['phone_number'] = input('Enter Your Phone Number: ')
        try:
            if a['first_name'].isalpha()  and a['last_name'].isalpha() and a['address'].isalpha() and \
        a['city'].isalpha() and a['state'].isalpha() and a['zip'].isdigit() and a['phone_number'].isdigit():
                self.data["AddressBook"].append(a)
                self.write()
            else:
                raise ValueError


        except ValueError:
            print('Enter DATA Again ')
            print('Enter Names and Numbers Properly')
            self.add()


    def remove(self):
        first = input('Enter First name: ')
        last = input('Enter Last name: ')
        for i in range(len(self.data["AddressBook"])):
            if str(self.data["AddressBook"][i]['first_name']).casefold() == first.casefold() and \
                 str(self.data["AddressBook"][i]['last_name']).casefold() == last.casefold():
                print("Record Deleted Successfully")
                del self.data["AddressBook"][i]

                return
        else:
            print("\nNo Record Found ")

    def update(self):
        first = input('Enter First name: ')
        last = input('Enter Last name: ')
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
            print(f, '\t\t', l, '\t\t', a, '\t\t\t', c)


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



a = Address()
a.menu()














