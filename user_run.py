import string
from random import *
from user_credential import User
from user_credential import Credentials


def create_user(firstname, lastname, username, userpassword):
    newuser = User(firstname, lastname, username, userpassword)
    return newuser


def save_user(user):
    user.save_user()


def delete_user(user):
    user.delete_user()


def find_user(number):
    return User.find_by_number(number)


def display_users():
    return User.display_users()


def create_account(account_username, account_name, account_password):
    newaccount = Credentials(account_username, account_name, account_password)
    return newaccount


def save_account(user):
    user.save_account()


def delete_account(user):
    user.delete_account()


def find_account(number):
    return Credentials.find_by_number(number)


def display_accounts():
    return Credentials.display_accounts()


def main():
    while True:
        print("Welcome to Password Vault write Sign Up or Log In to start")
        print("Sign Up -or- Log In")
        option = input()
        if option == "Sign Up":
            print("Create Account")
            print("-" * 10)
            print("Enter your First Name..")
            firstname = input()
            print("Enter your Last Name..")
            lastname = input()
            print("Set your username..")
            username = input()
            print("Set your password..")
            userpassword = input()
            save_user(create_user(firstname, lastname, username, userpassword))
            print("Your account was created successfully. These are your account details:")
            print("-" * 10)
            print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
            print("\nUse Login to your account with your details")
            print("\n \n")
            # for user in display_users():
            #    print(f"{user.firstname} {user.lastname}.....{user.username}")
        elif option == "Log In":
            print(" your Username.. ")
            loginUsername = input()
            print(" your Pasword ")
            loginPassword = input()
            if find_user(loginPassword):
                print("\n")
                print("you can create multiple accounts (Create Another) and also view them (View your  Account Details)")
                print("-" * 30)
                print("Create Another Account -or- View your Account Details")
                choose = input()
                print("\n")
                if choose == "Create Another Account":
                    print("Add Your credential of the Account")
                    print("-" * 15)
                    accountusername = loginUsername
                    print("Account Name")
                    accountname = input()
                    print("\n")
                    print("Generate automatic password(Gen) or Create new password(Crt)?")
                    decision = input()
                    if decision == "Gen":
                        characters = string.ascii_letters + string.digits
                        accountpassword = "".join(choice(characters) for x in range(randint(6, 16)))
                        print(f"Password: {accountpassword}")
                    elif decision == "Crt":
                        print("Enter your Password")
                        accountpassword = input()
                    else:
                        print("Please put in correct details")
                    save_account(create_account(accountusername, accountname, accountpassword))
                    print("\n")
                    print(f"Username:{accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")

                elif choose == "View your Account Details":
                    if find_account(accountusername):
                        print("Here is a list of your created accounts: ")
                        print("-" * 15)
                        for user in display_accounts():
                            print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")

                    else:
                        print("Invalid credentials!")
                else:
                    print("kindly try again!")
                    print("\n")
            else:
                print("Incorrect Details kindly try again!")
                print("\n")
        else:
            print("Kindly Choose Valid Account Details")
            print("\n")


if __name__ == '__MAIN__':
    MAIN()