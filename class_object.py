class Student:
    team_name = "INDIA"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # dunder method
    def __str__(self):
        return f"Hey my name is {self.name} and my age is {self.age}"

    def display(self):
        return f"Name is {self.name}, age is {self.age}, marks are {self.marks} and team is {self.team_name}"


s1 = Student(name='Virat', age=38, marks=90)
s2 = Student(name='Rohit', age=40, marks=91)
print(s1.display())
print(s2.display())

print(s1)
