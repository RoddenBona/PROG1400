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
    student_list = []

    def __init__(self):
        pass

    def add_student(self, new_student):
        pass

    def display_all(self):
        for i in self.student_list:
            print(self.student_list[i])

    def search_student_display(self):
        search = input("Search for student here: ")

    def search_student_other():
        search_other = input("Search for student here: s")



ingo = Student(1,"Ingo",20,80)


