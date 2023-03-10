# Using if-else statement
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

# Using if-elif-else statement
y = -2
if y > 0:
    print("y is positive")
elif y == 0:
    print("y is zero")
else:
    print("y is negative")

# Using a nested if statement
z = 10
if z > 0:
    if z % 2 == 0:
        print("z is positive and even")
    else:
        print("z is positive and odd")
else:
    print("z is not positive")

# Using the ternary operator
a = -7
b = "positive" if a > 0 else "non-positive"
print(f"a is {b}")
    
    
