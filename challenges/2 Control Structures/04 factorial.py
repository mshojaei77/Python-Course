# Write a program that prompts the user to enter a positive integer and then uses a while loop to calculate its factorial.

num = int(input("Enter a positive integer: "))  # take user input as integer

# check if num is positive
if num < 0:
    print("Error: Please enter a positive integer.")
else:
    fact = 1
    while num > 0:
        fact *= num  # multiply fact by num in each iteration
        num -= 1  # decrement num by 1 in each iteration
print("Factorial of is", fact)
