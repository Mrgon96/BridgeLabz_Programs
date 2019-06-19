import json


def readfile():

    filename = 'inventory.json'
    try:
        with open(filename, 'r') as f:
            # load json data
            data = json.load(f)

        # print json data
        print(json.dumps(data, indent=4))
        print("*************************")

        print('Name', '\t', 'Value')
        print('---------------')

        for d in range(4):
            # call json objects from loaded data
            a = data["inventory"][d]["name"]
            b = data["inventory"][d]["price"] * data["inventory"][d]["weight"]

            print(a, '\t', b)

    except IOError:
        print("File is not here")


readfile()
