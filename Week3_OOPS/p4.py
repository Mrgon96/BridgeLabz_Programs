import json


class Inventory:

    def __init__(self):
        # define file name
        self.filename = '1.json'
        # define empty dictionary
        self.lst = {}

    def create(self):
        # define temporary variable to write in json file
        temp = {'Inventory': []}
        # write into json file
        with open(self.filename, 'w') as f:
            json.dump(temp, f, indent=2)
            f.close()

    def open(self):
        # read the file
        with open(self.filename, 'r') as f2:
            self.lst = json.load(f2)
            f2.close()

    def write(self):
        # Open The File In Write Mode
        with open('1.json', 'w') as data:
            # Write Content In JSON Using json.dump Method
            json.dump(self.lst, data, indent=2)
            data.close()

    def insertion(self):

        try:
            # input for numbers of records to be inserted
            n = (input("Enter Number of records to be Inserted maximum(10):"))
            add = {}
            if not n.isdigit():
                # raise error if input is not Integer
                raise ValueError
            else:
                n = int(n)
                for i in range(n):
                    self.open()
                    print('Enter ', i+1, 'Value:')
                    add['Name'] = (input('Enter Name :'))
                    add['Weight'] = int(input('Enter Weight: '))
                    add['Price'] = int(input('Enter Price: '))
                    self.lst["Inventory"].append(add)
                    self.write()

        # exception handling
        except ValueError:
            print('Enter Again......')
            self.insertion()


# call the function
p = Inventory()
p.insertion()

