#taking user input
UserName = input('Enter Username')

#checking length of user input
if len(UserName) <= 2:
    print('Username must have minimum 3 characters')
else:    
    print('Hello',UserName,', How are you?')
    