# advanced_revision.py

import math


def recursion_demo():
    print("\n--- Recursion (Factorial) ---")
    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n - 1)
    print("Factorial of 5:", factorial(5))


def oop_demo():
    print("\n--- OOP (Class & Object) ---")
    class Student:
        def __init__(self, name):
            self.name = name
        
        def display(self):
            print("Student Name:", self.name)
    
    s1 = Student("Atul")
    s1.display()


def exception_demo():
    print("\n--- Exception Handling ---")
    try:
        num = int(input("Enter number: "))
        print(10 / num)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input")


def file_demo():
    print("\n--- File Handling ---")
    with open("sample.txt", "w") as f:
        f.write("Hello Python")
    
    with open("sample.txt", "r") as f:
        print(f.read())


def lambda_demo():
    print("\n--- Lambda Function ---")
    square = lambda x: x * x
    print("Square of 6:", square(6))


def comprehension_demo():
    print("\n--- List Comprehension ---")
    squares = [x*x for x in range(5)]
    print(squares)


def module_demo():
    print("\n--- Module Usage ---")
    print("Square root of 16:", math.sqrt(16))


def main():
    recursion_demo()
    oop_demo()
    exception_demo()
    file_demo()
    lambda_demo()
    comprehension_demo()
    module_demo()


if __name__ == "__main__":
    main()