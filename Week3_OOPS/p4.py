import json

def insert():

    try:
        n = (input("Enter Number of records to be Inserted maximum(10):"))

        if n.isdigit() != True:
            raise ValueError
        elif int(n) > 10:
            raise ValueError
        else:
            n = int(n)
            for i in range(n):
                n = (input('Enter Name :'))
                w = input('Enter Weight: ')
                p = input('Enter Price: ')

                my_json_string = """{
                   "inventory": [ 
                   ]
                }
                """
                with open('1.json', 'w') as file:
                    json.dump(my_json_string, file, indent=4)

                #with open('1.json', 'a') as f:
                 #   ["inventory"].append({"name":n,"weight":w,"price":p})





    except ValueError:
        print('Enter Again......')
        insert()


insert()