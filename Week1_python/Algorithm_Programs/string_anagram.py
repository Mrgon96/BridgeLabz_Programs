str1 = 'test'
str2 = 'etst'

def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return 0

    str1=sorted(str1)
    str2=sorted(str2)

    for i in range(0,len(str1)):
            if str1[i] != str2[i]:
                return 0

    return 1

if(isAnagram(str1,str2)):
    print('Strings are Anagram')
else:
    print('Strings are not Anagram')    




