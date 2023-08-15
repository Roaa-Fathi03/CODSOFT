# Simple Calculator Task

def Add(x, y):
    return x + y


def Subtract(x, y):
    return x - y


def Multiply(x, y):
    return x * y


def Divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


def Check_operation(operation_list):
    if len(operation_list) != 3:
        return True
    return False


def calculator():
    print("========= Welcome to Simple Calculator ===========")
    operation = input("Enter two numbers and an operation as in normal calculator separated by spaces (e.g. 5 + 8): ")
    operation_list = operation.split()

    if Check_operation(operation_list):
        print("Invalid input format. Please provide two numbers and an operation.")
        return

    num1 = float(operation_list[0])
    num2 = float(operation_list[2])
    operator = operation_list[1]

    if operator == '+':
        result = Add(num1, num2)
    elif operator == '-':
        result = Subtract(num1, num2)
    elif operator == '*':
        result = Multiply(num1, num2)
    elif operator == '/':
        result = Divide(num1, num2)
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    print("Result:", result)


calculator()
