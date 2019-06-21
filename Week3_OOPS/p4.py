import json


def insert():

    try:
        n = (input("Enter Number of records to be Inserted maximum(10):"))
        filename = "1.json"
        temp = {'Inventory': []}
        with open(filename, 'w') as f:
            json.dump(temp, f, indent=2)
            f.close()

        with open(filename, 'r') as f2:
            lst = json.load(f2)
            f2.close()

        add={}
        if n.isdigit() != True:
            raise ValueError
        elif int(n) > 10:
            raise ValueError
        else:
            n = int(n)
            for i in range(n):
                add['Name'] = (input('Enter Name :'))
                add['Weight'] = input('Enter Weight: ')
                add['Price'] = input('Enter Price: ')
                lst["Inventory"].append(add)

                with open('1.json', 'w') as data:  # Open The File In Write Mode
                    json.dump(lst, data, indent=2)  # Write Content In JSON Using json.dump Method
                    data.close()



    except ValueError:
        print('Enter Again......')
        insert()


insert()
