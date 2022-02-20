#Import modules
import unittest
from user import user


# Define class that will help test the different components of the application details
class Testuser(unittest.TestCase):
    '''
    Test class that test users feature or charaterictics of their details.

    '''

    def setUp(self):
        '''
        Set up  to be run before each test is made or executed.
        '''
        self.new_user = user("Martin", "Omollo", "2022M")  # create detail object

    def test_init(self):
        '''
        test_init test case to test if the object/details is initialized correctly
        '''

        self.assertEqual(self.new_user.user_name, "Martin")

        self.assertEqual(self.new_user.password, "2022M")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()  # save the new details
        self.assertEqual(len(user.user_list), 1)

    def test_delete_user(self):
        '''
        test_delete_details to test if we can remove a details from our details list
        '''
        self.new_contact.save_contact()
        test_user = user("Test", "user", "0700000000", "tommorow@martin.com")  # new details
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a details object
        self.assertEqual(len(user.user_list), 1)


if __name__ == '__main__':
    unittest.main()