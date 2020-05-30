"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- student.py

Description:
- This module defines the Student class which inherits from the 
Customer class. The class stores instance variables of the first 
name, last name, full name, and email.
"""
from customer import Customer

class Student(Customer):
    """This class represents the information of a student at the 
    bank"""
    def __init__(self, first, last):
        """Creates a student object and stores names"""
        Customer.__init__(self, first, last, True)


