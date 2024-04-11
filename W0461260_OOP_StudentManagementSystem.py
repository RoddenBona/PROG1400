"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1400
Repository: https://github.com/RoddenBona/PROG1400
Project: Student Management System
Version 1.0
Last edited: April 4 2024
"""

#This will be the master Student class that will include their name, age, ID, and grade
class Student:
    #Initializing  the attributes of the Student class
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    #display info will be overided by another display_info function later down
    def display_info(self):
        pass
    
    #This is a function made for updating the student grades upon being their ID being searched
    def update_info(self):
        self.name = input("Enter new name: ")
        self.age = input("Enter new age: ")
        self.grade = input("Enter new grade: ")
        print("Information has been updated: ")

#This subclass will contain the thesis of the said students
class GradeStudent(Student):
    #So GradeStudent will inhierit the main attributes of main Student class. but we'll add on the thesis topic attribute
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic
    def display_info(self):
        return f"ID: {self.student_id} Name: {self.name} Age: {self.age} Grade: {self.grade} Thesis: {self.thesis_topic}"

#This class is the main section containing most of the functions of the program. including a main menu for navigation
class StudentManagementSystem:
    #The add_student function does exactly that. Asking for user input to define the new students attributes
    def add_student():
        #The id is the only atrribute that doesn't take input. instead becomeing the number of items in the list + 1
        #This is somewhat flawed if we delete a student and the ID's no longer match the index
        new_id = len(mylist) + 1
        new_name = input("Enter new student's name: ")
        new_age = input("Enter new student's age: ")
        new_grade = input("Enter new student's grade: ")
        new_thesis = input("Enter new student's thesis topic: ")
        #After all variables are given by the user. Append the list with a new student using the given variables
        mylist.append(GradeStudent(new_id,new_name,new_age,new_grade,new_thesis))
        print("New record has been added")

#This the student search program. It searches for the student records via their ID
    def search_student():
        #User inputs the ID of the student they wish to see the record of
        ID = input("Enter student ID to search: ")
        #now because the list index starts at 0. We minus 1 from the inputed number so the ID and input match up
        #This is why deleting a record is problematic, as the code currently does not reassign the IDs to match input again
        if ID.isdigit():
            ID = int(ID) -1
            try:
                #If input is a valid index number. Try to display the student information using the GradeStudent display function
                print(GradeStudent.display_info(mylist[ID]))
            except:
                #If not. Print an error message
                print("Error: Not Found")
        else:
            #This error is for if the input was not a digit number
            print("Error Invalid")

#The simplest function of the program. Simply just iterate throught the list of students and print the info
    def see_all():
        for i in mylist:
            print(GradeStudent.display_info(i))

#This was not required of the progam for this assignment. But I did make a delete record function.
#As I said before the program does not reassign IDs after removal. So looking up ID's after one was removed will be a pain
    def delete_student():
            ID = input("Eter student ID to search: ")
            if ID.isdigit():
                ID = int(ID) -1
                #The program will ask for conformation to delete the record from the system.
                deletion = input("""Are you sure you wish to delete this student record?
                                 1)Yes
                                 2)No
                                 Enter option here: """)
                if deletion == 1:
                    #If answered yes. remove the index of the given ID from the list
                    mylist.remove(mylist[ID])
                    print("record has been removed")
                else:
                    #Otherwsie leave back t menu
                    if deletion == 2:
                        print("Deletion process aborted")
                    else:
                        print("Error: Invalid")
            else:
                print("Error: Invalid")

#This is the main menu function. Giving easy access to all the above functions
    def main_menu():
        while True:
            option = input("""Welcome to the NSCC Student Managent System V1
                           Please select one of the options provided below
                           1)Add new student entry
                           2)Update Student information
                           3)Search for student record
                           4)See all Student records
                           5)Delete Student entry
                           6)Exit program
                           Enter option here: """)
            if option.isdigit():
                option = int(option)
                if option == 1:
                    StudentManagementSystem.add_student()
                else:
                    #The update info function is the only function that needs to have this extra input
                    #Due to the fcat that the update_info function is part of the Student class and not part of the
                    #management system. Nor was I made with a search input in the student class.
                    if option == 2:
                        search = input("Enter ID of the student record you wish to update: ")
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
                                        print("Thank you for using the NSCC Student Management System V1. Goodbye")
                                        break
                                    else:
                                        print("Error: Invalid")
            else:
                print("Error: Invalid")

#This the list variable we'll be using to store all the GradeStudent class objects
mylist = []

#These are 2 example entries put in to test the program
mylist.append(GradeStudent(1,"Mark",20,80,"Biology"))
mylist.append(GradeStudent(2,"John",25,90,"Astrology"))

#This will start the main menu upon booting up the program
StudentManagementSystem.main_menu()