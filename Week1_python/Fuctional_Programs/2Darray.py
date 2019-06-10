rows = int(input('Enter Number of Rows: '))
cols = int(input('Enter Number of Cols: '))

array = [[0]*cols]*rows
print('Enter Array Elements:')
for i in range(0,len(array),1):
    for j in range(len(array)):
        array[i][j]=int(input('Enter element: '))  

for r in array:
    for c in r:        
        print c,
    print         
