"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Collaborator:
- Lambert

Date:
- 2020 May 18

Filename:
- bank.py

Description:
- This module defines the Bank class. The class stores instance 
variable of its accounts.
"""
from account import Account

class Bank:    
    """This class represents a bank as a collection of savnings accounts."""
    # The state of the bank is a dictionary of accounts  
    def __init__(self):        
        """Creates a new dictionary to hold the accounts."""    
        self.accounts = {}        
                
    def __str__(self):        
        """Returns the string representation of the bank."""        
        return "\n".join(map(str, self.accounts.values()))    
    
    def makeKey(self, name, pin):        
        """Returns a key for the account."""        
        return name + "/" + pin    
        
    def add(self, account):       
        """Adds the account to the bank."""        
        self.accounts[self.makeKey(account.getName(), account.getPin())] = account    
        
    def remove(self, name, pin):        
        """Removes the account from the bank and        
        and returns it, or None if the account does        
        not exist."""        
        return self.accounts.pop(self.makeKey(name, pin), None)   
        
    def get(self, name, pin):        
        """Returns the account from the bank,        
        or returns None if the account does        
        not exist."""        
        return self.accounts.get(self.makeKey(name, pin), None)    

    def matureAccounts(self):
        """Computes and returns the fees minus interest accrued on        
        all accounts.""" 
        return sum([account.mature() for account in self.accounts.values])
        
    def getKeys(self):        
        """Returns a sorted list of keys."""              
        return sorted(self.accounts.keys())
        
        
