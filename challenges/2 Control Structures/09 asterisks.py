'''
Write a program that prompts the user to enter a number and then uses nested loops to generate a pattern of asterisks 
such that each row has one more asterisk than the previous row until it reaches the user input number:
*
**
***
****
*****
'''
n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
