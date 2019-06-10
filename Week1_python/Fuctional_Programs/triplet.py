numbers = [1,-1,0,2,6,-5,-8,7,9,-4,-5,4,6]
for i in range (0,len(numbers)-2):
    for j in range (0,len(numbers)-1):
        for k in range (0,len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 0:
                print(numbers[i],numbers[j],numbers[k])