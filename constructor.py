# constructor is a magic method that is called when the object of the class is created.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}.")


class ClassManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)

    def display_all(self):
        for student in self.students:
            student.display()


manager = ClassManager()
manager.add_student(name='Virat', age=39)
manager.add_student(name='rohit', age=40)
manager.display_all()
