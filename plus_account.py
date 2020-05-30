"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- advantage_plus.py

Description:
- This module defines the Advantage_Plus class which stores 
all information for an Advantage Plus Account at the bank.
Advantage_Plus_Account inherits from the account class. 
The class stores instance variable of waiving the maintnance 
fee. This class also stores class variables of the interest
rate and the monthly fee.
"""
from account import Account

class Advantage_Plus_Account(Account):
    """This class represents the Advantage Plus Account at the Bank"""

    RATE = 0.011
    MONTH_FEE = 12.00

    def __init__(self, customer, pin, balance=0.0):
        """Creates an Advantage Plus Savings Account"""
        Account.__init__(self,customer, pin, 'Advantage Plus', balance)
        if customer.student:
            self.waive = True
        else:
            self.waive = False

