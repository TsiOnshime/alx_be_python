num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /):").strip()
match operation:
    case "+":
        result = float(num1) + float(num2)
    case "-":
        result = float(num1) - float(num2)
    case "*":
        result = float(num1) * float(num2)
    case "/":
        if float(num2) != 0:
            result = float(num1) / float(num2)
        else:
            result = "Error: Division by zero is not allowed."
    case _:
        result = "Error: Invalid operation."
print(f"The result is: {result}")