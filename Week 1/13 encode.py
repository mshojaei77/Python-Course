# Write a program to encode a user-generated string into binary using UTF-16 encoding, then decode it back into Unicode.
user_input = input("Enter a string: ")
encoded_string = user_input.encode('utf-16')
print("Encoded string:", encoded_string)

decoded_string = encoded_string.decode('utf-16')
print("Decoded string:", decoded_string)
