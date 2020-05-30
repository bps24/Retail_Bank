"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- advantage_safe.py

Description:
- This module defines the Advantage_Safe_Account class which stores 
all information for an Advantage Safe Account at the bank.
Advantage_Safe_Account inherits from the account class. 
The class stores instance variable of waiving the maintnance 
fee. This class also stores class variables of the interest
rate and the monthly fee.
"""
from account import Account

class Advantage_Safe_Account(Account):
    """This class represents the Advantage Safe Account at the Bank"""

    RATE = 0.008
    MONTH_FEE = 4.95

    def __init__(self, customer, pin, balance=0.0):
        """Creates an Advantage Safe Savings Account"""
        Account.__init__(self,customer, pin, 'Advantage Safe', balance)
        if customer.student:
            self.waive = True
        else:
            self.waive = False

    def computeFee(self):
        """Overrides the computeFee method in Account and returns
        the monthly fee of the account"""
        if self.customer.student or self.balance > 1500:
            return 0
        else:
            self.balance -= MONTH_FEE
            return MONTH_FEE
