
import unittest
from unittest.mock import patch
from app.account_dispatcher import  AccountDispatcher

class Account:
    def __init__(self, account_id):
        self.id = account_id



# Assuming AccountDispatcher and Account classes are defined here or imported
class TestAccountDispatcher(unittest.TestCase):

    def setUp(self):
        """Set up the test environment with a fresh AccountDispatcher."""
        self.dispatcher = AccountDispatcher()
        self.account1 = Account(1)
        

    def test_add_account(self):
        """Test if an account can be added to the dispatcher."""
        self.dispatcher.add_account(self.account1)
        self.assertIn(self.account1.id, self.dispatcher.accounts)
        self.assertEqual(self.dispatcher.get_account(1), self.account1)

    def test_get_account(self):
        """Test fetching an account from the dispatcher."""
        self.dispatcher.add_account(self.account1)
        account = self.dispatcher.get_account(1)
        self.assertEqual(account, self.account1)

    def test_get_account_not_found(self):
        """Test if ValueError is raised when getting a non-existent account."""
        with self.assertRaises(ValueError):
            self.dispatcher.get_account(999)  # Account ID that does not exist

    def test_remove_account(self):
        """Test if an account can be removed from the dispatcher."""
        self.dispatcher.add_account(self.account1)
        removed_account = self.dispatcher.remove_account(1)
        self.assertEqual(removed_account, self.account1)
        self.assertNotIn(self.account1.id, self.dispatcher.accounts)

    def test_remove_account_not_found(self):
        """Test if ValueError is raised when removing a non-existent account."""
        with self.assertRaises(ValueError):
            self.dispatcher.get_account(1)  # Account ID that does not exist

    # @patch('AccountDispatcher.remove_account')
    # def test_mock_remove_account(self, mock_remove):
    #     """Test mocking the remove_account method."""
    #     # Set up the mock to return a predefined response
    #     mock_remove.return_value = None
    #     result = self.dispatcher.remove_account(1)
    #     self.assertIsNone(result)
    #     mock_remove.assert_called_with(1)  # Assert if the method was called with account ID 1

if __name__ == '__main__':
    unittest.main()
