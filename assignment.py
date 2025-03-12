# Get user input
num1 = float(input("Please enter a number: "))
num2 = float(input("Now enter  the second number: "))


print("\nChoose an operation:")
print("A) Addition (+)")
print("B) Subtraction (-)")
print("C) Multiplication (*)")
print("D) Division (/)")

operation = input("Enter A, B, C, or D: ").strip().upper()


if operation == "A":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "B":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "C":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "D":
    if num2 != 0: 
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice! Please enter A, B, C, or D.")
