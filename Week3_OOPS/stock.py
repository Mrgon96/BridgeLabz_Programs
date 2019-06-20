import json

class stock():

    filename = 'stock.json'
    try:
        with open(filename, 'r') as f:
            # load json data
            data = json.load(f)

        # print json data
        print(json.dumps(data, indent=4))
        print("*************************")

    except IOError:
        print("File is not here")

    def each_stock(self):
        self.total=[]
        print("Values for Individual Stock are")
        print('Name', '\t', 'Value')
        print("**********************")
        for d in range(7):
            name = self.data["stocks"][d]["name"]
            value = self.data["stocks"][d]["shares"] * self.data["stocks"][d]["price"]
            print(name, '\t', round(value, 3))
            self.total.append(value)


    def totalvalue(self):
        sum = 0
        for i in self.total:
            sum = sum + i
        print("Total Value of Stocks is: ",round(sum, 4))




s =stock()
s.each_stock()
s.totalvalue()


