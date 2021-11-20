import string
import secrets
import re

# a=string.digits+string.ascii_letters+string.punctuation
# password=''
# for i in range(8):
#     password=password+secrets.choice(a)

# print('your password:',password)



def strong_password(password1):
    if len(password1)>6 and len(password1)<16:
        if re.findall("[^a-zA-Z0-9_]", password1):
            return True
        else:
            print("this is not a strong password")
            print("password1 must contain at least one character,one digit or one special character")
            a=string.digits+string.ascii_letters+string.punctuation
            password=''
            for i in range(8):
                password=password+secrets.choice(a)

            print('you can use this suggested password :',password)

            password1=input('enter password:')
            strong_password(password1)
    else:
        print("password1 length must be greater than 6")
        password1=input('enter password:')
        strong_password(password1)

password1=input('enter password:')
strong_password(password1)
# a=input('enter password:')
# strong_password(a)