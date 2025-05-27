# Mail-ID-signIn-logIn
Mail ID signIn/logIn

from sqlalchemy import create_engine
import re
import ast
import pandas

user = {}

def signin():
    username1 = input(f'Dear user kindly enter the correct way of email to create account :')
    A = r'^[a-zA-Z0-9-.$%_]+@[a-zA-Z0-9-.$%_]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(A,username1):
        password1 = input(f'Dear user kindly enter the correct way of password to create account :')
        B = r'^[a-zA-Z0-9-.$%_]{6,}$'

        if re.fullmatch(B,password1):
            user[username1] = password1
            print('you now successfuly create the account in the website')
        else:
            print(f'kindly enter the password in correct formate')
    else:
        print(f'kindly enter the mail ID in correct formate')

def login():
    username2 = input(f'Dear user kindly enter the email Id for this website :')
    C = r'^[a-zA-Z0-9-.+$_]+@[a-zA-Z0-9-.+$_]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(C,username2):
        password2= input(f'kindly enter the password for this account :')
        D = r'^[a-zA-Z0-9-.+$_]{6,}$'

        if username2 in user and user[username2] == password2:
            print(f'you have successfuly logged in to your account')
        else:
            print('enter mail ID and password do not match')
    else:
        print(f'kindly enter the correct mail ID for this website')

def choice():
    while True:
        print(f'1 : signin')
        print(f'2 : login')
        print(f'3 : exit')
        choices = int(input(f'Kindly enter the option 1,2 and 3 :'))

        if choices == 1:
            signin()
        elif choices == 2:
            login()
        elif choices == 3:
            break

if __name__ == "__main__":
    choice()
