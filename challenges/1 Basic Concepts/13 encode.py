#Write a program that takes a string as input from the user and encodes it using UTF-8 encoding.
user_input = input("Enter a string: ")
encoded_string = user_input.encode('utf-8')
print("Encoded string:", encoded_string)
