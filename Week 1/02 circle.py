# Write a Python program that asks the user to enter the radius of a circle and prints its area and circumference 
r = float(input("Enter the radius of circle: "))
pi = 3.14159265359
A= pi * (r**2)
print("Area = " , A )
C = 2 * pi * r
print("Circumference = " , C )
