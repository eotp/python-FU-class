#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:27:47 2022

@author: ak
"""


        
class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Student(Person):
    pass

class Instructor(Person):
    pass
        
class Class:
    pass 

if __name__ == "__main__":
    print("automatically running :-)")
    a = Class()
    # python_class = Class("30.06.2022", "Python OOP class")
    
    # aleks = Instructor("Aleks", "Informatikstudent an der TU", ["Python", "Machine Learning"])
    
    # ich = Student("Mein Name", "Ich moechte Python lernen")
    
    # python_class.add_participant(aleks)
    # python_class.add_participant(ich)
    
    # python_class.print_details()
