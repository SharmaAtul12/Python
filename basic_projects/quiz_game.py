# quiz_game.py

# -------------------------------
# Function to ask a question
# -------------------------------
def ask_question(question_data, question_number):
    
    # Display question number and question text
    print(f"\nQuestion {question_number}:")
    print(question_data["question"])
    
    # Display all options for the question
    for option in question_data["options"]:
        print(option)
    
    # Take answer from user
    answer = input("Enter your answer (A/B/C/D): ").upper()
    
    # Validate user input
    # If user enters something other than A, B, C, or D,
    # ask the user again until a valid option is entered
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C, or D.")
        answer = input("Enter your answer (A/B/C/D): ").upper()
    
    # Check if the answer is correct
    if answer == question_data["answer"]:
        print("Correct Answer!")
        return 1   # Return 1 point for correct answer
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", question_data["answer"])
        return 0   # Return 0 points for wrong answer


# -------------------------------
# Main quiz game function
# -------------------------------
def quiz_game():
    
    # Display welcome message
    print("===== WELCOME TO THE QUIZ GAME =====")
    
    # Variable to store total score
    score = 0
    
    # List of questions (Each question is stored as a dictionary)
    questions = [
        {
            "question": "What is the correct extension of a Python file?",
            "options": ["A. .py", "B. .pt", "C. .python", "D. .p"],
            "answer": "A"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "Which data type is immutable?",
            "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            "answer": "D"
        },
        {
            "question": "Which loop continues until the condition becomes false?",
            "options": ["A. for", "B. while", "C. do-while", "D. repeat"],
            "answer": "B"
        },
        {
            "question": "What does OOP stand for?",
            "options": [
                "A. Object Oriented Programming",
                "B. Only Object Programming",
                "C. Object Order Programming",
                "D. Open Object Programming"
            ],
            "answer": "A"
        }
    ]
    
    # Loop through each question in the list
    # enumerate() gives index + question
    for index, question in enumerate(questions, start=1):
        
        # Ask question and add returned score
        score += ask_question(question, index)
    
    # Display final result
    print("\n===== QUIZ COMPLETED =====")
    print("Your Score:", score, "/", len(questions))
    
    # Calculate percentage
    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")
    
    # Show performance message based on percentage
    if percentage == 100:
        print("Excellent! Perfect Score!")
    elif percentage >= 60:
        print("Good Job!")
    else:
        print("Keep Practicing!")


# -----------------------------------
# Program execution starts here
# -----------------------------------

# This ensures the program runs only
# when this file is executed directly
if __name__ == "__main__":
    quiz_game()