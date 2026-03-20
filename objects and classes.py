class Student:
    name = ""
    age = 0

s1 = Student()
s1.name = "John"
s1.age = 20
print(f"s1: name={s1.name}, age={s1.age}")

class StudentWithInit:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

s2 = StudentWithInit("Alice", 21)
print(f"s2: name={s2.name}, age={s2.age}")

class StudentWithDel:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"StudentWithDel object '{self.name}' destroyed")

s3 = StudentWithDel("Bob")
del s3

