students_list = []
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = 0
        self.name = ""
        self.age = 0
        self.grade = 0
    
    def display_info(self, name, age):
        pass
    
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

class StudentManagementSystem(Student):
    def __init__(self, student_id, name, age, grade):
        super().__init__(student_id, name, age, grade)

    def main_menu():
        while True:
            option = input("""Main menu
                        Please Select an option below
                        
                        1) Add student
                        2) All student information
                        3) Search for a student
                        4)Grade student
                        """)
            if option.isdigit():
                option = int(option)
            if option == 1:
                StudentManagementSystem.add_student()
            else:
                if option == 2:
                    StudentManagementSystem.display_all_students()
                else:
                    if option == 3:
                        StudentManagementSystem.student_search()
                    else:
                        if option == 4:
                            GradeSudent.display_info()
                        else:
                            print()

    def add_student():
        id = len(students_list) + 1
        name = input("Enter new student name: ")
        age = input("Enter new students age: ")
        if age.isdigit():
            age = int(age)
        grade = input("Enter new student grade: ")
        if grade.isdigit():
            grade = int(grade)
        new_student = Student(id, name, age, grade)

    def display_all_students(self):
        for i in students_list:
            self.display_info()

            #print(f"Student ID: {self.student_id} Name: {self.name} Age: {self.age} {self.grade}")

    def student_search(self):
        search = input("Enter Student ID:")
        if self.student_id in students_list:
            self.display_info



example = Student(1, "Roland", 21, 85)

students_list.append(example)