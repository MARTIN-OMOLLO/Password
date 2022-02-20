#import modules
import random
import string

# Global variables
global users_list


# Users class
class User:
    '''
    Class that generates new instances of users
    '''

    # define users_list
    userslist = []

    def __init__(self, firstname, lastname, username, password):
        '''
        __init__ methos that helps us define properties for our objects or details.
        '''
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user details into user userlist
        '''
        User.userslist.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user details from the userslist
        '''
        User.userslist.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns details from the userlist
        '''
        return cls.userslist

    @classmethod
    def find_by_number(cls, number):
        '''
        method that takes in a username and returns a user that matches that number
        '''
        for user in cls.userslist:
            if user.password == number:
                return user

    @classmethod
    def user_exist(cls, number):
        for user in cls.userslist:
            if user.username == number:
                return True
                return False


# Credentials class
class Credentials:
    '''
    Class that generates new instances of Credentials
    '''

    accounts = []

    def __init__(self, accountusername, accountname, accountpassword):
        '''
        __init__ method that helps us define properties for our objects or details.
        '''

        self.accountusername = accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword

    def save_account(self):
        '''
        save_account method saves user info into accounts
        '''
        Credentials.accounts.append(self)

    def delete_account(self):
        '''
        delete_account method deletes a saved Credential from accounts
        '''
        Credentials.accounts.remove(self)

    @classmethod
    def display_accounts(cls):
        '''
        method that returns a list of the accounts
        '''
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number
        '''
        for account in cls.accounts:
            if account.accountusername == number:
                return account