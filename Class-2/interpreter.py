# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!



# Prompt the user for an arithmetic expression
expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

# Split the expression into x, operator, and z using space as the delimiter
x, operator, z = expression.split(' ')

# Convert x and z to float
x = float(x)
z = float(z)

# Calculate the result
result = None

if operator == '+':
    result = x + z
elif operator == '-':
    result = x - z
elif operator == '*':
    result = x * z
elif operator == '/':
    if z != 0:
        result = x / z
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")

# Output the result
if result is not None:
    print(f"Result: {result:.1f}")