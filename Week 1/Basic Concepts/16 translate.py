# Write a program that takes a string as input from the user and translates it into another language using the translate() method.
user_input = input("Enter a string: ")
translation_table = str.maketrans("aeiou", "12345")
translated_string = user_input.translate(translation_table)
print("Translated string:", translated_string)
