''' Write a function that takes a mathematical expression as input and evaluates it, then returns the result rounded to one decimal point. 
The expression will be in the form of "x operator z", where x and z are numbers 
and operator is either "+" for addition, "-" for subtraction, "*" for multiplication or "/" for division. 
If the operator is division ("/"), make sure to check if z is not zero before performing the operation. If z is zero, print "ZeroDivisionError" and return None.
'''

math = input("What do you want to know? ")
x, y, z = math.split(" ")
new_x, new_z = float(x), float(z)

if y == "+":
    result = new_x + new_z
elif y == "-":
    result = new_x - new_z
elif y == "*":
    result = new_x * new_z
elif y == "/" and z != 0:
    result = new_x / new_z
else:
    print("ZeroDivisionError")

print(round(result,1))
