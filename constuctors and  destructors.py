"""
Introduction to Python, OOP, Constructors, and Destructors

1. Python Overview
- High-level, interpreted
- Simple syntax
- Versatile (web, AI, data science, automation)
- Dynamically typed, object-oriented, cross-platform

2. Development Environment
- Interpreter: executes Python code
- Editor/IDE: VS Code, PyCharm, etc.
- Terminal/cmd: run programs
- Workflow: write -> save .py -> run -> view output

3. OOP Basics
- Object-oriented programming uses objects (data + behavior)
- Models real world entities
- Principles: Encapsulation, Inheritance, Polymorphism, Abstraction

4. Classes and Objects
- Class: blueprint/template
- Object: instance

5. Constructors and Destructors
- Constructor: __init__(), called on creation
- Destructor: __del__(), called on cleanup
"

print("=== Python OOP: Constructors & Destructors Demo ===")

class Student:
    """Student class demo with constructor and destructor."""

    def __init__(self, name, age):
        # Constructor: initialize object data
        self.name = name
        self.age = age
        print(f"[__init__] Student created: {self.name}, age {self.age}")

    def study(self):
        print(f"{self.name} is studying.")

    def __del__(self):
        # Destructor: clean up resources
        print(f"[__del__] Student object destroyed: {self.name}")


def main():
    print("\nCreating student object...")
    s1 = Student("John", 20)
    s1.study()

    print("\nCreating another student object...")
    s2 = Student("Jane", 22)
    s2.study()

    print("\nExplicitly deleting objects to demonstrate destructor behavior")
    del s1
    del s2

    print("\nEnd of main(), objects go out of scope after function returns")


if __name__ == "__main__":
    main()

    print("\nForcing garbage collection to show __del__ behavior")
    gc.collect()

    print("\nSummary Table")
    print("Topic        | Key Idea")
    print("Python       | Simple, high-level programming language")
    print("Env          | Tools used to write and run code")
    print("OOP          | Uses objects to structure programs")
    print("Class        | Blueprint")
    print("Object       | Instance of class")
    print("Constructor  | Initializes object")
    print("Destructor   | Cleans up object")
