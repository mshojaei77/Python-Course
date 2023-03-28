# Write a program to remove all leading, trailing, and both leading and trailing whitespaces from a user-generated string using each of the three methods.
user_input = input("Enter a string: ")

stripped_string = user_input.strip()
print("Stripped string:", stripped_string)

left_stripped_string = user_input.lstrip()
print("Left-stripped string:", left_stripped_string)

right_stripped_string = user_input.rstrip()
print("Right-stripped string:", right_stripped_string)
