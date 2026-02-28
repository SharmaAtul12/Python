# student_management_file.py

import json   # Used to store data permanently in JSON format

FILE_NAME = "students_data.json"


# Function to load student data from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)   # Convert JSON back to Python list
    except FileNotFoundError:
        return []   # If file does not exist, return empty list


# Function to save student data to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)   # Save with formatting


# Add new student
def add_student():
    students = load_students()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student saved permanently!")


# View all students
def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")


# Main menu
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT (FILE SYSTEM) =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()