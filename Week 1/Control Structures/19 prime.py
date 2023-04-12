# Write a program that takes an integer input from the user and determines whether it is a prime number or not

# Get input from user
num = int(input("Enter an integer: "))

# Check if number is prime
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

# Output result
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
