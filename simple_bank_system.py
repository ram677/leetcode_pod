#2043. Simple Bank System

from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.num_accounts = len(balance)

    def _is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.num_accounts

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Check if both accounts are valid.
        if not (self._is_valid_account(account1) and self._is_valid_account(account2)):
            return False
        
        # Check for sufficient funds in the source account.
        if self.balance[account1 - 1] >= money:
            # Perform the transaction.
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        # Check if the account is valid.
        if not self._is_valid_account(account):
            return False
            
        # Perform the deposit.
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Check if the account is valid.
        if not self._is_valid_account(account):
            return False
            
        # Check for sufficient funds.
        if self.balance[account - 1] >= money:
            # Perform the withdrawal.
            self.balance[account - 1] -= money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

#Time Complexity:
# Each operation (transfer, deposit, withdraw) runs in O(1) time.
#Space Complexity: O(1) since we are using a constant amount of extra space.
