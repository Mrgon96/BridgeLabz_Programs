from utility import utility  #importing utility class

#taking user inputs in two string
s1 = input('Enter 1st String: ')
s2 = input('Enter 2nd String: ')

# calling function from utility which checks and returns boolean value
if(utility.isAnagram(s1,s2)):
    print('Strings are Anagram')
else:
    print('Strings are not Anagram')    
