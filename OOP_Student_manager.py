

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = 1
        self.name = ""
        self.age = 0
        self.grade = 0
    
    def display_info(self, name, age,):
        self.__name = name


        return f"Name: {self.name} Age: {self.age}, Grade: {self.grade}"
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

class GradeSudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic
    def display_info(self):
        return f"{self.thesis_topic}"
    

def add_student():
    new_name = input("What is the student's name?: ")
    new_age = input("What is the student's age? ")
    if new_age.isdigit():
        new_age = int(new_age)
    new_grade = input("What is the student's current grade? ")
    if new_grade.isdigit():
        new_grade = int(new_grade)
    new_id = Student.id + 1


student1 = Student()
Name = input("Enter new student name: ")
age = input("Enter new student age: ")
grade = input("Enter new student grade: ")

