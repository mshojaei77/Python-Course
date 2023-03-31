# Write a program that takes a user input number and checks if it's even or odd using an if-else statement.

num = int(input("Enter a number: "))  # take user input as integer

if num % 2 == 0:  # check if remainder is 0 when divided by 2
    print(num, "is even")
else:
    print(num, "is odd")
