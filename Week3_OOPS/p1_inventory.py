import json


def readfile():

    # define filename with extension
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
            # calculate inventory value
            b = data["inventory"][d]["price"] * data["inventory"][d]["weight"]

            print(a, '\t', b)

    # catch error
    except IOError:
        print("File is not here")


# call function
readfile()
