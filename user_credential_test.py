import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Martin Omollo','Martin123')

	def test__init__(self):
		'''
		Test if the initialization of user instances is correctly done
		'''
		self.assertEqual(self.new_user.name,'Martin Omollo')
		self.assertEqual(self.new_user.password,'Martin123')

	def test_save_user(self):
		'''
		Test if the new users details is saved inside the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)