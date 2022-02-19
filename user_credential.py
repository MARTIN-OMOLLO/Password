import pyperclip
import random
import string

# Global Variables
global users_list 
class User:
	'''
	Class to create user account and save their details
	'''
    #Class Details
    #global users_list
    users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties/characteristics for each user details input.
		'''

		# Details Init
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
