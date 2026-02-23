def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Taking input
num = int(input("Enter a number: "))
result = factorial(num)

print("Factorial of", num, "is", result)