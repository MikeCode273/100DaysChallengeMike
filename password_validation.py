import re

pwd = input("Enter your Password here: ")
pwd_len = len(pwd)
is_valid = False


while True:
    if pwd_len < 7 or pwd_len >20: 
        break
    elif not re.search('[A-Z]',pwd):
        break
    elif not re.search('[a-z]', pwd):
        break
    elif not re.search('[$#@]',pwd):
        break
    elif  re.search('\s',pwd):
        break
    else:
        is_valid=True
        break


if is_valid:
    print("Password is valid")
else:
    print("Password is invalid")
    print("Password should begin with Alphabet-Numbers-Symbols..!")
    print("Password length should  not be lesthan 7 and greather than 20!!")