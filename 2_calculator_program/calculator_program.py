# PYTHON CALCULATOR PROGRAM

# First, let's going to ask what kind of operation the users wants
operator = input("What kind of operator do you want? (+ - * /): ")

# Now, let's ask for the numbers to make the operation
num1 = float(input("Give me one number: "))
num2 = float(input("Give me a second number: "))

# Acording with the operator we will make the operation
if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} {operator} {num2} is {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} {operator} {num2} is {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} {operator} {num2} is {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"The result of {num1} {operator} {num2} is {round(result, 3)}")
else:
    print(f"{operator} is not a valid operator!")