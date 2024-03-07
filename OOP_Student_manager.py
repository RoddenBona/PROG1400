students_list = []
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = len(students_list)
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
    def __init__(self):
        pass

    def main_menu():
        while True:
            option = input("""Main menu
                        Please Select an option below
                        
                        1) Add student
                        2) All student information
                        3) Search for a student
                        4)Grade student
                        Enter Here: """)
            if option.isdigit():
                option = int(option)
                if option == 1:
                    StudentManagementSystem.add_student()
                else:
                    if option == 2:
                        StudentManagementSystem.display_all_students(Student)
                    else:
                        if option == 3:
                            StudentManagementSystem.student_search()
                        else:
                            print("Option not in list")
            else:
                print("error invalid input")

    def add_student():
        id = len(students_list) + 1
        name = input("Enter new student name: ")
        age = input("Enter new students age: ")
        if age.isdigit():
            age = str(age)
        grade = input("Enter new student grade: ")
        if grade.isdigit():
            grade = int(grade)
        new_student = Student(id, name, age, grade)
        students_list.append(new_student)
        print(f"{new_student.student_id} {new_student.name} {new_student.age} {new_student.grade}")

    def display_all_students(Student):
        for i in students_list:
            print(f"{i.age()}")

example = Student(len(students_list), "Roland", 21, 85)

students_list.append(example)

if __name__ == "__main__":
    main = StudentManagementSystem
    main.main_menu()