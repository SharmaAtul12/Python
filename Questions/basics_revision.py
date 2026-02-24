# basics_revision.py

def variables_demo():
    print("\n--- Variables & Data Types ---")
    a = 10
    b = 3.14
    c = "Python"
    d = True
    print(type(a), type(b), type(c), type(d))


def operators_demo():
    print("\n--- Operators ---")
    x = 8
    y = 3
    print("Addition:", x + y)
    print("Subtraction:", x - y)
    print("Multiplication:", x * y)
    print("Division:", x / y)
    print("Modulus:", x % y)


def condition_demo():
    print("\n--- Conditional Statements ---")
    num = int(input("Enter number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


def loop_demo():
    print("\n--- Loops ---")
    print("For Loop:")
    for i in range(1, 6):
        print(i, end=" ")
    
    print("\nWhile Loop:")
    count = 1
    while count <= 3:
        print(count, end=" ")
        count += 1
    print()


def function_demo():
    print("\n--- Functions ---")
    def square(n):
        return n * n
    print("Square of 5:", square(5))


def list_demo():
    print("\n--- List ---")
    numbers = [1, 2, 3]
    numbers.append(4)
    print(numbers)


def tuple_demo():
    print("\n--- Tuple ---")
    t = (10, 20, 30)
    print(t)


def set_demo():
    print("\n--- Set ---")
    s = {1, 2, 2, 3}
    print(s)


def dict_demo():
    print("\n--- Dictionary ---")
    student = {"name": "Atul", "age": 20}
    print(student)


def main():
    variables_demo()
    operators_demo()
    condition_demo()
    loop_demo()
    function_demo()
    list_demo()
    tuple_demo()
    set_demo()
    dict_demo()


if __name__ == "__main__":
    main()