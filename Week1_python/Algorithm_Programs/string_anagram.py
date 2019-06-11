#defining two strings
str1 = 'test'
str2 = 'etst'

#function definition 
def isAnagram(str1,str2):

    #comparing lengths of both string
    if len(str1) != len(str2):
        return 0

    #SORTING STRINGS
    str1=sorted(str1)
    str2=sorted(str2)

    #check for each element to be same
    for i in range(0,len(str1)):
            if str1[i] != str2[i]:
                return 0

    return 1

#printing result
if(isAnagram(str1,str2)):
    print('Strings are Anagram')
else:
    print('Strings are not Anagram')    




