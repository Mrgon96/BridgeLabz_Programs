import tkinter as tk
from tkinter import *
import json

class Address():
    def add_gui(self):
        a = Tk()
        a.title('Address Book')
        a.geometry("400x550")

        Label(a, text='First Name', bg='lightgreen').place(x=150, y=20)
        Label(a, text='Last Name', bg='lightgreen').place(x=150, y=80)
        self.e1 = Entry(a, highlightcolor='purple')
        self.e2 = Entry(a, highlightcolor='purple')
        self.e1.place(x=100, y=45)
        self.e2.place(x=100, y=105)
        Label(a, text='Address', bg='lightgreen').place(x=160, y=150)
        self.e3 = Entry(a, highlightcolor='purple')
        Label(a, text='City', bg='lightgreen').place(x=170, y=210)
        self.e4 = Entry(a, highlightcolor='purple')
        Label(a, text='State', bg='lightgreen').place(x=165, y=270)
        self.e5 = Entry(a, highlightcolor='purple')
        self.e3.place(x=100, y=175)
        self.e4.place(x=100, y=235)
        self.e5.place(x=100, y=295)
        Label(a, text='Zip', bg='lightgreen').place(x=175, y=330)
        self.e6 = Entry(a, highlightcolor='purple')
        self.e6.place(x=100, y=355)
        Label(a, text='Mobile Number', bg='lightgreen').place(x=135, y=390)
        self.e7 = Entry(a, highlightcolor='purple')
        self.e7.place(x=100, y=415)
        submitbutton = Button(a, highlightcolor='green', width=10, height=2, text='Submit', command=self.insert()).place(x=130,
                                                                                                            y=475)

        a.mainloop()

    def insert(self):
        data = {
            "first_name": self.e1.get(),
            "last_name": self.e2.get(),
            "Address": self.e3.get(),
            "City": self.e4.get(),
            "State": self.e5.get(),
            "Zip": self.e6.get(),
            "Mobile": self.e7.get()
        }

        with open('address.json', 'w') as f:
            json.dump(data, f, indent=4)

a = Address()
a.add_gui()


