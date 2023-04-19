# Write a program that prints out all possible combinations of two-digit numbers from 00 to 99, where each digit in the combination is odd.

for i in range(1, 10, 2):
    for j in range(1, 10, 2):
        print(str(i) + str(j))
