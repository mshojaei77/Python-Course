'''
Write a program that uses a for loop to iterate through a range of numbers from 1 to 10. If the number is odd, 
print a message saying "Odd number found: x", where x is the number. 
If the number is even, continue to the next iteration without printing anything.
'''


for num in range(1, 11):
    if num % 2 == 1:
        print("Odd number found:", num)
    else:
        continue
