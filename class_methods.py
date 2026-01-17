class Student:
    # class attribute
    college_name = 'IITM'

    def __init__(self, name, age):
        # object attributes
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hey my name is {self.name} and age is {self.age} in college {self.college_name}.'

    def display(self):
        print(f'My name is {self.name} and age is {self.age}.')

    @classmethod
    def change_college_name(cls, new_college_name):
        cls.college_name = new_college_name


s1 = Student(name='Virat', age=38)
s1.college_name = 'PICT'
print(s1)
print(Student.college_name)
s1.change_college_name(new_college_name='PICT')
print(s1)
print(Student.college_name)

s2 = Student(name='rohit', age=40)
print(s2)
