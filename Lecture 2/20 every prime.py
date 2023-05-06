# Write a program that prints all prime numbers between 1 and 100 (inclusive).
count = 0
print("The prime numbers between 1 and 100 are:\n")
for num in range(2, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, end=" ")
        count += 1
        if count % 10 == 0:
            print("\n")
