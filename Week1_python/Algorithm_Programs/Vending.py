notes = [2000,500,100,50,20,10,5,1] # list for storing notes
counter = [0]*10 #creating counter list with ten elements
Amount = int(input('Enter the Amount: ')) # taking amount as input from user
for i,j in zip(notes,counter): # loop notes and counter simulataneously
    if Amount>=i: #cheking for amount greater than note
        j=Amount//i # dividing amount by note
        Amount=Amount-j*i  #updating amount value
        print (i,':',j) # printing notes and respective counter