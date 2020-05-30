"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- customer.py

Description:
- This module defines the Customer class. The class stores instance 
variables of the first name, last name, full name, and email of every 
customer 
"""
class Customer:
    """This class represents the information of a customer at the 
    bank"""
    def __init__(self, first, last, student=False):
        """Creates a customer object and stores names and student 
        status"""
        self.first = first
        self.last = last
        self.full = first + " " + last
        self.email = first + "." + last + "@bank.com"
        self.student = student

    def __str__(self):
        """Returns the name of the student"""
        return self.full 

