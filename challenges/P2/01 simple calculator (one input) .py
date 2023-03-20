# Define a variable to hold the running total
total = 0

# Continuously prompt the user for input until they enter an empty string
while True:
    # Use the built-in input() function to get user input
    input_str = input("Enter an expression to evaluate (or leave blank to quit): ")

    # If the input is blank, break out of the loop
    if input_str == "":
        break

    # Split the input into operands and operator using string methods
    operands = input_str.split(" ")
    operator = operands[1]

    # Convert the operands from strings to numbers using the appropriate methods
    left_operand = int(operands[0])
    right_operand = int(operands[2])

    # Evaluate the expression using the appropriate operator
    if operator == "+":
        total = left_operand + right_operand
    elif operator == "-":
        total = left_operand - right_operand
    elif operator == "*":
        total = left_operand * right_operand
    elif operator == "/":
        total = left_operand / right_operand
    elif operator == "%":
        total = left_operand % right_operand
    elif operator == "**":
        total = left_operand ** right_operand
    elif operator == "//":
        total = left_operand // right_operand

    # Print the result
    print("Result: {}".format(total))
