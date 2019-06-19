import re
from datetime import date


def replace():
    message = '''Hello <<name>>, 
We have your full name as <<full name>> in our system.
your contact number is 91-xxxxxxxxxx.
Please,let us know in case of any clarification 
Thank you BridgeLabz 01/01/2016.'''

    print(message)
    print()
    print('****Modified Message****')

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    try:
        firstname = input('Enter Your Firstname: ')
        lastname = input('Enter Your Lastname: ')

        mobile = input('Enter 10 digit mobile no. : ')
        if mobile.isdigit() and firstname.isalpha() and lastname.isalpha():
            mobile = '91-'+mobile
            fullname = firstname + ' ' + lastname
            list1 = [firstname, fullname, mobile, d1]
            patterns = ['<<name>>', '<<full name>>', '91-xxxxxxxxxx', '01/01/2016']

            for i in range(4):
                message = re.sub(patterns[i], list1[i], message)
            print()
            print(message)

        else:
            raise ValueError
    except ValueError:
        print('Enter Name in Alphabets and Mobile in Numbers only(without Whitespaces)')


replace()
