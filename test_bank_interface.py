import unittest
from bank_interface import *

class TestBankInterface(unittest.TestCase):
    def setUp(self):
        pass

    def test_initial_balance(self):
        self.assertEqual(check_balance(), 0)

    def test_deposit_funds(self):
        deposit(100)
        self.assertEqual(check_balance(), 100)

    def test_withdraw_funds(self):
        deposit(100)
        withdraw(50)
        self.assertEqual(check_balance(), 50)

    def test_withdraw_more_than_balance(self):
        deposit(100)
        self.assertFalse(withdraw(150))

if __name__ == '__main__':
    unittest.main()
