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
- account.py

Description:
- This module defines the Account class which holds the information
of bank accounts. The Account class is  the parent class to 
Advantage_Plus_Account class, Advantage_Relationship_Account class, 
Advantage_Safe_Account class, Advantage_Savings_Account class. The 
class stores instance variables of a customer, pin, balance, and 
account type.
"""
class Account:
    """This class represents an account as an object with 
    infomration"""
    def __init__(self, customer, pin, type_, balance=0.0):    
        """Stores values to instance variables"""
        self.customer = customer        
        self.pin = str(pin)        
        self.balance = balance    
        self.type_ = type_      
    
    def __str__(self):        
        """Returns the string rep."""        
        result =  'Name:    ' + str(self.customer.full) + '\n'         
        result += 'PIN:     ' + str(self.pin) + '\n'         
        result += 'Balance: ' + "%.2f" % (self.balance) + '\n'
        result += 'Type:    ' + self.type_ + '\n'    
        return result    
            
    def getBalance(self):        
        """Returns the current balance."""        
        return round(self.balance,2)    
        
    def getName(self):        
        """Returns the current name."""        
        return str(self.customer)
        
    def getPin(self):        
        """Returns the current pin."""        
        return self.pin    

    def getType(self):        
        """Returns the current type."""        
        return self.type_    
        
    def deposit(self, amount):        
        """If the amount is valid, adds it        
        to the balance and returns None;        
        otherwise, returns an error message."""   
        if amount>0:     
            self.balance += amount   
        else:
            raise Exception("Amount must be > 0")     

    def withdraw(self, amount):        
        """If the amount is valid, sunstract it        
        from the balance and returns None;        
        otherwise, returns an error message."""        
        if amount < 0:            
            raise Exception("Amount must be > 0")      
        elif self.balance < amount:            
            raise Exception("Insufficient funds")        
        else:            
            self.balance -= amount            
    
    def mature(self):
        interest = self._computeInterest()
        fee = self.computeFee()
        return fee - interest

    def _computeInterest(self):        
        """Computes, deposits, and returns the interest."""        
        interest = self.balance * (self.getRate()/12)        
        self.deposit(interest)        
        return interest

    def computeFee(self):
        if not self.waive:
            self.balance -= self.MONTH_FEE   
            return self.MONTH_FEE
        return 0

    def getRate(self):
        return self.RATE