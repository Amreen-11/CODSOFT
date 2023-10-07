def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  operation = input("Choose an operation (+, -, *, /): ")

  if operation == '+':
    result = add(num1, num2)
  elif operation == '-':
    result = subtract(num1, num2)
  elif operation == '*':
    result = multiply(num1, num2)
  elif operation == '/':
    result = divide(num1, num2)
  else:
    result = "Invalid operation"

  print("Result: ", result)
  again = input("Would you like to perform the calculation again(y/n): ").lower()
  if again!='y':
    break
    
