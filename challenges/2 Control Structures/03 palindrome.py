# Write a program that takes a string as input and prints whether or not it is a palindrome (a word that reads the same backward as forward) using an if-else statement.

string = input("Enter a string: ")  # take user input as string

# check if the string is equal to its reverse
if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
