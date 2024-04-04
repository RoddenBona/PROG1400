"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Repository: https://github.com/RoddenBona/PROG1400
Project: Student Management System
Version 1
Last edited: March 28 2024
"""

#This will be the master Student class that will include their name, age, ID, and grade
class Student:
    #
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

class GradeStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic
    def display_info(self):
        return f"ID: {self.student_id} Name: {self.name} Age: {self.age} Grade: {self.grade} Thesis: {self.thesis_topic}"

class StudentManagementSystem:
    def add_student():
        new_id = len(mylist) + 1
        new_name = input()
        new_age = input()
        new_grade = input()
        mylist.append(GradeStudent(new_id,new_name,new_age,new_grade))

    def search_student():
        ID = input()
        if ID.isdigit():
            ID = int(ID) -1
            try:
                print(GradeStudent.display_info(mylist[ID]))
            except:
                print("Error: Not Found")
        else:
            print("Error Invalid")

    def see_all():
        for i in mylist:
            print(GradeStudent.display_info(i))

    def delete_student():
            ID = input()
            if ID.isdigit():
                ID = int(ID) -1
                deletion = input("""Are you sure you wish to delete this student record?
                                 1)Yes
                                 2)No""")
                if deletion == 1:
                    mylist.remove(mylist[ID])
                else:
                    if deletion == 2:
                        print("Deletion process aborted")
                    else:
                        print("Error: Invalid")
            else:
                print("Error: Invalid")

    def main_menu():
        while True:
            option = input("""Welcome to the NSCC Student Managent System
                           Please select one of the options provided below
                           1)Add new student entry
                           2)Update Student information
                           3)Search for student record
                           4)See all Student records
                           5)Delete Student entry
                           6)Exit program""")
            if option.isdigit():
                option = int(option)
                if option == 1:
                    StudentManagementSystem.add_student()
                else:
                    if option == 2:
                        search = input("Enter ID of the student record you wish to update")
                        if search.isdigit():
                            search = int(search) -1
                            try:
                                GradeStudent.update_info(mylist[search])
                            except:
                                print("Error: Not found")
                    else:
                        if option == 3:
                            StudentManagementSystem.search_student()
                        else:
                            if option == 4:
                                StudentManagementSystem.see_all()
                            else:
                                if option == 5:
                                    StudentManagementSystem.delete_student()
                                else:
                                    if option == 6:
                                        print("Thank you for using the NSCC Student Management System. Goodbye")
                                        break
                                    else:
                                        print("Error: Invalid")
            else:
                print("Error: Invalid")


mylist = []

mylist.append(GradeStudent(1,"Mark",20,80,"Biology"))
mylist.append(GradeStudent(2,"John",25,90,"Astrology"))

StudentManagementSystem.main_menu()