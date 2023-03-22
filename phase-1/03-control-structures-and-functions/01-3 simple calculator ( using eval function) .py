while True:
    expression = input("Enter an arithmetic expression, or press enter to quit: ")
    if expression == "":
        break
    else:
        result = eval(expression)
        print("Result: ", result)
