import string
from random import *
from user import User
from user import Credentials


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


def create_account(accountusername, accountname, accountpassword):
    newaccount = Credentials(accountusername, accountname, accountpassword)
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
        print("Welcome to Password Vault write sign up or Log in to start")
        print("Sign Up -or- Log In")
        option = input()
        if option == "Sign Up":
            print("Create Account")
            print("-" * 8)
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
                print("you can create multiple accounts (Create Account) and also view them (View Account)")
                print("-" * 30)
                print("Create Account -or- View Account")
                choose = input()
                print("\n")
                if choose == "Create Account":
                    print("Add Your Account Credentials")
                    print("-" * 15)
                    accountusername = loginUsername
                    print("Account Name")
                    accountname = input()
                    print("\n")
                    print("Generate automatic password(Gen) or Create new password(Crt)?")
                    decision = input()
                    if decision == "Gen":
                        characters = string.ascii_letters + string.digits
                        accountpassword = "".join(choice(characters) for x in range(randint(8, 15)))
                        print(f"Password: {accountpassword}")
                    elif decision == "Crt":
                        print("Enter your Password")
                        accountpassword = input()
                    else:
                        print("Please put in a valid choice")
                    save_account(create_account(accountusername, accountname, accountpassword))
                    print("\n")
                    print(f"Username:{accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}")

                elif choose == "View Account":
                    if find_account(accountusername):
                        print("Here is a list of your created accounts: ")
                        print("-" * 15)
                        for user in display_accounts():
                            print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")

                    else:
                        print("Invalid credentials!")
                else:
                    print("Kindly Use Correct Details!")
                    print("\n")
            else:
                print("Incorrect Details Kindly try again!")
                print("\n")
        else:
            print("Kindly choose a correct details")
            print("\n")


if __name__ == '__main__':
    main()