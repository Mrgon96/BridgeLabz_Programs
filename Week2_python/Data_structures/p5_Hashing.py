filename = 'HashNumbers.txt'


try:
    fp = open(filename, 'r')

    if fp:
        print('File opened Successfully...')
        content = fp.read()
        nums = content.split()

except IOError:
        print('File is not here///.....')

print(nums)
hashTable = []

for i in range(10):
    hashTable.append([])
    for j in nums:
        j = int(j)
        if j % 11 == i:
            hashTable[i].append(j)
    if len(hashTable[i]) == 0:
        hashTable[i].append(None)


print(hashTable)

n = int(input('Enter Number to Search : '))

