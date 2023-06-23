import unittest
from bankaccount import BankAccount

b = BankAccount()

class TestMethods(unittest.TestCase):

    def testInit(self):

        self.assertEqual(b.__init__(), None)

    def testDeposit(self):

        self.assertEqual(b.deposit(20.00), 20.00)

    def testWithdraw(self):

        self.assertEqual(b.withdraw(10.00), -20.00)
        self.assertEqual(b.withdraw(25.00), -55.00)

    def testAddInterest(self):

        self.assertEqual(b.addInterest(3), 0.00)

    def testGetBalance(self):

        self.assertEqual(b.getBalance(), 20.00)

if __name__ == "__main__" :
    unittest.main()