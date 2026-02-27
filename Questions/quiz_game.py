# quiz_game.py

# Function to display a single question
def ask_question(question_data, question_number):
    
    print(f"\nQuestion {question_number}:")
    print(question_data["question"])
    
    # Display options
    for option in question_data["options"]:
        print(option)
    
    # Take user input
    answer = input("Enter your answer (A/B/C/D): ").upper()
    
    # Validate answer
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C, or D.")
        answer = input("Enter your answer (A/B/C/D): ").upper()
    
    # Check answer
    if answer == question_data["answer"]:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! Correct answer is {question_data['answer']}")
        return 0


# Main quiz function
def quiz_game():
    
    print("===== WELCOME TO PYTHON QUIZ GAME =====")
    
    score = 0  # Variable to store total score
    
    # List of questions (Dictionary inside List)
    questions = [
        {
            "question": "What is the correct extension of Python file?",
            "options": ["A. .py", "B. .python", "C. .pt", "D. .p"],
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
            "question": "Which loop is used when number of iterations is unknown?",
            "options": ["A. for", "B. while", "C. do-while", "D. foreach"],
            "answer": "B"
        },
        {
            "question": "What does OOP stand for?",
            "options": [
                "A. Object Oriented Programming",
                "B. Only Object Programming",
                "C. Object Order Process",
                "D. Open Object Programming"
            ],
            "answer": "A"
        }
    ]
    
    # Loop through each question
    for index, question in enumerate(questions, start=1):
        score += ask_question(question, index)
    
    # Final Result
    print("\n===== QUIZ COMPLETED =====")
    print("Your Final Score:", score, "/", len(questions))
    
    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")
    
    # Performance Message
    if percentage == 100:
        print("🔥 Excellent! Perfect Score!")
    elif percentage >= 60:
        print("👍 Good Job!")
    else:
        print("📚 Keep Practicing!")


# Run program
if __name__ == "__main__":
    quiz_game()