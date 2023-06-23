
# Import
import unittest
from bankaccount import BankAccount

# Create object
bank = BankAccount()

# Test suite
class Tests(unittest.TestCase) : 

    def test_Init(self) : 
        self.assertEqual(bank.__init__(initialBalance=1200), None)
        
    def test_Deposit(self) : 
        self.assertEqual(bank.deposit(50), 50)
        
    def test_Withdraw(self) :
        self.assertEqual(bank.withdraw(10), 1190)
        self.assertEqual(bank.withdraw(1230), -50)
        
    def test_AddInterest(self) : 
        self.assertEqual(bank.addInterest(3), 0)
        
    def test_GetBalance(self) : 
        self.assertEqual(bank.getBalance(), 50)


if __name__ == "__main__" :
    unittest.main()