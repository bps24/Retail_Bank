"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- advantage_relationship.py

Description:
- This module defines the Advantage_Relationship_Account class which 
stores all information for an Advantage Relationship Account at the 
bank. Advantage_Relationship_Account inherits from the account class. 
The class stores instance variable of waiving the maintnance fee. 
This class also stores class variables of the interest rate and the 
monthly fee.
"""
from account import Account

class Advantage_Relationship_Account(Account):
    """This class represents the Advantage Relationship Account at 
    the Bank"""

    RATE = 0.013
    MONTH_FEE = 25.00

    def __init__(self, customer, pin, balance=0.0):
        """Creates an Advantage Relationship Savings Account"""
        Account.__init__(self,customer, pin, 'Advantage Relationship', balance)
        if customer.student:
            self.waive = True
        else:
            self.waive = False

    def computeFee(self):
        """Overrides the computeFee method in Account and returns
        the monthly fee of the account"""
        if self.balance > 10_000:
            return 0
        else:
            self.balance -= MONTH_FEE
            return MONTH_FEE
    