# Basic Usage
print("Hello, world!")

# Printing Variables
name = "John"
age = 30
print("My name is", name, "and I am", age, "years old.")
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# Specifying Separator and End
print("One", "Two", "Three", sep="-", end="!")

# Flushing Buffer
import time
for i in range(5):
    print(i, end="-", flush=True)
    time.sleep(1)

# Printing to a File
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
