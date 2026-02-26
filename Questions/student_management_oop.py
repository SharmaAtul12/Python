# student_management_oop.py

# Student class to represent a single student
class Student:
    
    # Constructor method (automatically runs when object is created)
    def __init__(self, name, age, marks):
        self.name = name      # Instance variable for student name
        self.age = age        # Instance variable for student age
        self.marks = marks    # Instance variable for student marks

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")


# StudentManagement class to manage multiple students
class StudentManagement:
    
    # Constructor method
    def __init__(self):
        self.students = []   # List to store Student objects

    # Method to add a new student
    def add_student(self):
        print("\n--- Add Student ---")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        # Create Student object
        student = Student(name, age, marks)

        # Add object to list
        self.students.append(student)

        print("Student added successfully!")

    # Method to view all students
    def view_students(self):
        print("\n--- Student List ---")

        if not self.students:
            print("No students available.")
            return

        # Loop through student objects
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. ", end="")
            student.display()

    # Method to search student by name
    def search_student(self):
        print("\n--- Search Student ---")
        name = input("Enter name to search: ")

        for student in self.students:
            if student.name.lower() == name.lower():
                print("Student Found:")
                student.display()
                return

        print("Student not found.")

    # Method to calculate average marks
    def calculate_average(self):
        print("\n--- Calculate Average Marks ---")

        if not self.students:
            print("No data available.")
            return

        total = 0

        # Add marks of each student
        for student in self.students:
            total += student.marks

        average = total / len(self.students)

        print("Average Marks:", average)


# Main function to run the program
def main():

    # Create StudentManagement object
    system = StudentManagement()

    # Infinite loop for menu
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM (OOP) =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.calculate_average()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


# This ensures the program runs only when executed directly
if __name__ == "__main__":
    main()