import json
import math

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        operation = {'operation': 'addition', 'operands': (a, b), 'result': result}
        self.history.append(operation)
        return result, operation

    def subtract(self, a, b):
        result = a - b
        operation = {'operation': 'subtraction', 'operands': (a, b), 'result': result}
        self.history.append(operation)
        return result, operation

    def multiply(self, a, b):
        result = a * b
        operation = {'operation': 'multiplication', 'operands': (a, b), 'result': result}
        self.history.append(operation)
        return result, operation

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        operation = {'operation': 'division', 'operands': (a, b), 'result': result}
        self.history.append(operation)
        return result, operation

    def square_root(self, a):
        result = math.sqrt(a)
        operation = {'operation': 'square root', 'operands': (a,), 'result': result}
        self.history.append(operation)
        return result, operation




    def show_history(self):
        print("History of Operations:")
        for idx, operation in enumerate(self.history, 1):
            print(f"{idx}. {operation}")

# Example usage:
calc = Calculator()
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Show history")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    
    if choice == '6':
        calc.show_history()
        continue

    try:
        num1 = float(input("Enter first number: "))
        if choice != '5':
            num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == '1':
        result, operation = calc.add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result, operation = calc.subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result, operation = calc.multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        try:
            result, operation = calc.divide(num1, num2)
            print("Result:", result)
        except ValueError as e:
            print(e)
    elif choice == '5':
        result, operation = calc.square_root(num1)
        print("Result:", result)
