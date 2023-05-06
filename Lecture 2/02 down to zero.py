# Write a program that prompts the user to enter a number and then uses a while loop to print all the numbers from that number down to 0.

num = int(input("Enter a number: "))  # take user input as integer

while num >= 0:  # keep looping until num is negative
    print(num)
    num -= 1  # decrement num by 1 in each iteration
