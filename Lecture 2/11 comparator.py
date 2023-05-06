# Write a program that takes two numbers as input from the user, compares them 
# and prints out whether the first number is greater than, less than, or equal to the second number.

a = float(input("A: ")) 
b = float(input("B: "))
if a>b:
    print("A>B : A is grater than B")
elif a<b:
    print("A<B : A is less than B")
elif a==b:
    print("A=B : A is equal to B")
else: 
    print("Error")
    
