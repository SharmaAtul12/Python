# Calculator
# Perform arithmetic operations and store a calculation history

history = []


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def format_number(value):
    if value == int(value):
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def perform_calculation():
    operations = {
        "1": ("+", "Addition"),
        "2": ("-", "Subtraction"),
        "3": ("*", "Multiplication"),
        "4": ("/", "Division"),
        "5": ("%", "Modulus"),
        "6": ("**", "Power"),
    }

    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")

    choice = input("\nChoose an operation: ").strip()
    if choice not in operations:
        print("Invalid option!")
        return

    first = get_number("Enter first number: ")
    second = get_number("Enter second number: ")
    symbol, label = operations[choice]

    if symbol in ("/", "%") and second == 0:
        print("Cannot divide by zero!")
        return

    if symbol == "+":
        result = first + second
    elif symbol == "-":
        result = first - second
    elif symbol == "*":
        result = first * second
    elif symbol == "/":
        result = first / second
    elif symbol == "%":
        result = first % second
    else:
        result = first ** second

    entry = f"{format_number(first)} {symbol} {format_number(second)} = {format_number(result)}"
    history.append(entry)

    print(f"\n{label} result: {format_number(result)}")


def view_history():
    if not history:
        print("\nNo calculations yet!")
        return

    print("\nCalculation History")
    print("-" * 40)
    for index, entry in enumerate(history, 1):
        print(f"{index}. {entry}")


def clear_history():
    if not history:
        print("\nHistory is already empty!")
        return

    history.clear()
    print("\nCalculation history cleared.")


def main():
    print("=" * 40)
    print("           CALCULATOR")
    print("=" * 40)

    while True:
        print("\n1. New Calculation")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            perform_calculation()
        elif choice == "2":
            view_history()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()