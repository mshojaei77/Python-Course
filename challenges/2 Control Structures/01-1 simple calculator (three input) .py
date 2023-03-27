# Define variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display menu of operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Perform operation based on user's choice
if choice == '1':
    print(num1, "+", num2, "=", (num1 + num2))
elif choice == '2':
    print(num1, "-", num2, "=", (num1 - num2))
elif choice == '3':
    print(num1, "*", num2, "=", (num1 * num2))
elif choice == '4':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1, "/", num2, "=", (num1 / num2))
else:
    print("Invalid input")
