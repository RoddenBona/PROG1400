"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Repository: https://github.com/RoddenBona/PROG1400
Project: Student Management System
Version 1
Last edited: March 28 2024
"""
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self,student_id, name, age, grade):
        return f"ID:{self.student_id} Name:{self.name} Age:{self.age} Grade:{self.grade}"
    
    def update_info(self):
        self.name = input("Enter new name: ")
        self.age = input("Enter new age: ")
        self.grade = input("Enter new grade")
        print("Information has been updated")

class GradeSudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic
    def display_info(self):
        return f"Name: {self.name} Thesis: {self.thesis_topic}"

class StudentManagementSystem:
    def add_student():
        new_id = len(mylist) + 1
        new_name = input()
        new_age = input()
        new_grade = input()
        mylist.append(Student(new_id,new_name,new_age,new_grade))

    def search_student():
        search = input()
        if search in mylist:
            print("success")
        else:
            print("fail")




mylist = []

mylist.append(Student(1,"Mark",20,80))
mylist.append(Student(2,"John",25,90))

print(mylist)

StudentManagementSystem.add_student()

print(mylist)