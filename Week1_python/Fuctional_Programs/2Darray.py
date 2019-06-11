#user input for rows and columns
rows = int(input('Enter Number of Rows: '))
cols = int(input('Enter Number of Cols: '))

#defining array
array = [[0]*cols]*rows

#taking array elements as input
print('Enter Array Elements:')
for i in range(0,len(array),1):
    for j in range(len(array)):
        array[i][j]=int(input('Enter element: '))  

#printing array
for r in array:
    for c in r:        
        print c,
    print         
