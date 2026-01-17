# __ -> private

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


s1 = Student('virat', 38)
print(s1)
# private variable -> only accessible within class ✅
#                     outside the class            ❌

# print(s1._Student__name)
print(s1.name)


# __________________________________________________________________________

class BankAccount:
    def __init__(self):
        # private instance attribute
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(200)
print(account.get_balance())
