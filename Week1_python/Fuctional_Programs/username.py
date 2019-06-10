UserName = input('Enter Username')#taking user input

if len(UserName) <= 2:#checking length of user input
    print('Username must have minimum 3 characters')
else:    
    print('Hello',UserName,', How are you?')
    