def account_creation():
    if create_account == "yes":
        new_username = str(input("new username: "))
        new_password = str(input("new password: "))
        username = new_username
        password = new_password

        passwords[username] = password

        print("account created.")
    elif create_account == "no":
        print("YOU HAVE NOT CREATED AN ACCOUNT")
    else:
        print("wrong input")


def ask_login():
    askedusername = str(input("what is your username? "))
    askedpassword = str(input("what is your password? "))
    # user = passwords.get(password, None) +


passwords = dict()
# create_account = input("do you want to create an account? (yes/no) ")
# account_creation()
# @ask_login()
dir(passwords)

print passwords 