notes = [2000,500,100,50,20,10,5,1]
print(notes)
counter = [0]*10
Amount = int(input('Enter the Amount: '))
for i,j in zip(notes,counter):
    if Amount>=i:
        j=Amount//i
        Amount=Amount-j*i
        print (i,':',j)