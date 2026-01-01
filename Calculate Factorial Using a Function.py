def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number1 = input("Enter a number: ")
result1 = factorial(int(number1))
print(f"The factorial of {number1} is {result1}")