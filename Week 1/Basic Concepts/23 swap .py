# Write a Python script to swap two variables a and b using a temporary variable. 

a = input("a: ")
b = input("b: ")
temp = a
a = b
b = temp
print("a: ",a,"b: ", b)

# Write a Python script to swap two variables a and b without using a temporary variable.
a = input("a: ")
b = input("b: ")
a, b = b, a
print("a: ", a, "b: ", b)
