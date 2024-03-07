class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = 0
        self.name = ""
        self.age = 0
        self.grade = 0
    
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
    def __init__(self, student_list):
        self.student_list = []
    
    def add_student(self, new_student):
        self.student.append(new_student)
        print(self.student_list)

    def display_all(self):
        for i in self.student:
            print(self.student[i])

    def search_student_display(self):
        pass

    def search_student_other():
        pass