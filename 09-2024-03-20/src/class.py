#!/usr/bin/env python3
# -*- coding: utf-8 -*-
        
class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Student(Person):
    def __init__(self, name, reason):
        super().__init__(name = name, description = reason)

class Instructor(Person):
    def __init__(self, name, bio, skills):
        super().__init__(name = name, description = bio)
        # self.name = name
        # self.description = bio
        self.skills = skills

    # def __str__(self):
    #     return f"{self.name}: {self.description}\n{self.skills}"
        
class Class:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.participants = []
        
    def add_participant(self, participant):
        self.participants.append(participant)
        
    def print_details(self):
        print(f"Class: {self.date} --- {self.subject}")
        print("")
        print("Instructors:")
        for part in self.participants:
            if type(part).__name__ == "Instructor":
                print(part)
                print(part.skills)
        print("")
        print("Students:")
        for part in self.participants:
            if type(part).__name__ == "Student":
                print(part)        

print("automatically running :-)")

a = Student("Dirk", "Moechte Python lernen")
python_class = Class("30.06.2022", "Python OOP class")

aleks = Instructor("Aleks", "Informatikstudent an der TU", ["Python", "Machine Learning"])

ich = Student("Dirk", "Ich moechte Python lernen")
anan = Student("Anan", "Ich moechte Python lernen")

python_class.add_participant(aleks)
python_class.add_participant(ich)
python_class.add_participant(anan)

python_class.print_details()
