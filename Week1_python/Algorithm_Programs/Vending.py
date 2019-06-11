 # list for storing notes
notes = [2000,500,100,50,20,10,5,1]

#creating counter list with ten elements
counter = [0]*10 

# taking amount as input from user
Amount = int(input('Enter the Amount: ')) 

# loop notes and counter simulataneously
for i,j in zip(notes,counter): 
    #cheking for amount greater than note
    if Amount>=i: 
        # dividing amount by note
        j=Amount//i 

        #updating amount value
        Amount=Amount-j*i 

        # printing notes and respective counter
        print (i,':',j) 