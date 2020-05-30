"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- tester.py

Description:
- This module defines several methods that test the functionality of 
the Bank class, Account class, Advantage_Plus class, 
Advantage_Relationship class, Advantage_Safe class, Advantage_Savings 
class, and Customer class
"""
from bank import Bank
from safe_account import Advantage_Safe_Account
from relationship_account import Advantage_Relationship_Account
from plus_account import Advantage_Plus_Account
from savings_account import Advantage_Savings_Account
from student import Student
from customer import Customer
import random

def getFirst():
    """Returns a random first name from the given list of names"""
    first = ['James',
            'John',
            'Robert',
            'Michael',
            'William',
            'David',
            'Richard',
            'Joseph',
            'Thomas',
            'Charles',
            'Christopher',
            'Daniel',
            'Matthew',
            'Anthony',
            'Donald',
            'Mark',
            'Paul',
            'Steven',
            'Andrew',
            'Kenneth',
            'Joshua',
            'George',
            'Kevin',
            'Brian',
            'Edward',
            'Ronald',
            'Timothy',
            'Jason',
            'Jeffrey',
            'Ryan',
            'Jacob',
            'Gary',
            'Nicholas',
            'Eric',
            'Stephen',
            'Jonathan',
            'Larry',
            'Justin',
            'Scott',
            'Brandon']
    return first[random.randrange(len(first))]

def getLast():
    """Returns a random last name from the given list of names"""
    last = ['Smith',
            'Johnson',
            'Williams',
            'Brown',
            'Jones',
            'Miller',
            'Davis',
            'Garcia',
            'Rodriguez',
            'Wilson',
            'Martinez',
            'Anderson',
            'Taylor',
            'Thomas',
            'Hernandez',
            'Moore',
            'Martin',
            'Jackson',
            'Thompson',
            'White',
            'Lopez',
            'Lee',
            'Gonzalez',
            'Harris',
            'Clark',
            'Lewis',
            'Robinson',
            'Walker',
            'Perez',
            'Hall']
    return last[random.randrange(len(last))]

def createBank(num=5):    
    """Returns a bank object with a given number of accounts"""  
    bank = Bank()  
    customers=[]
    for i in range(num):
        #random account type
        acc = random.randrange(4)
        #random starting balance
        bal = random.randrange(10_000)
        #random name and random choice of student or not
        cust = Customer(getFirst(),getLast(),random.choice([True, False]))
        if acc==0:
            bank.add(Advantage_Relationship_Account(cust,1000 + i,bal))
        elif acc==1:
            bank.add(Advantage_Savings_Account(cust,1000 + i,bal))
        elif acc==2:
            bank.add(Advantage_Safe_Account(cust,1000 + i,bal))
        else:
            bank.add(Advantage_Plus_Account(cust,1000 + i,bal))
    print(bank)
   
def testStudentAccount():    
    """Test functionality for Advantage_Plus account."""    
    c = Student("John", "Doe")
    account = Advantage_Plus_Account(c, "1000", 500.00)     
    account.deposit(100)   
    print("Expect 600:", account.getBalance())    
    account.withdraw(100) 
    print("Expect 500:", account.getBalance())   
    account.mature()
    print("Expect 500.46:", account.getBalance()) 

def testCustomerAccount():    
    """Test functionality for Advantage_Plus account."""    
    c = Customer("John", "Doe")
    account = Advantage_Plus_Account(c, "1000", 500.00)     
    account.deposit(100)   
    print("Expect 600:", account.getBalance())    
    account.withdraw(100) 
    print("Expect 500:", account.getBalance())   
    account.mature()
    print("Expect 488.46:", account.getBalance()) 
    
def testOverdraft():
    """Tests Overdraft Error"""    
    c = Customer("John", "Doe")
    account = Advantage_Plus_Account(c, "1000", 500.00)     
    account.withdraw(600)

def testNegativeDeposit():
    """Tests a negative deposit to an account"""   
    c = Customer("John", "Doe")
    account = Advantage_Plus_Account(c, "1000", 500.00)     
    account.deposit(-100)

def testNegativeWithdraw():
    """Tests a negative withdraw to an account"""   
    c = Customer("John", "Doe")
    account = Advantage_Plus_Account(c, "1000", 500.00)     
    account.withdraw(-100)

if __name__ == "__main__":    
    test = 6

    if test == 1:
        createBank()
    if test == 2:
        testStudentAccount()
    if test == 3:
        testCustomerAccount()
    if test == 4:
        testOverdraft()
    if test == 5:
        testNegativeDeposit()
    if test == 6:
        testNegativeWithdraw()