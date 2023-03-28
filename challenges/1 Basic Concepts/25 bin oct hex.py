# Create a Python program that prompts the user to enter a decimal number, and then converts that number into binary, octal, and hexadecimal forms.

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)[2:] # remove the leading '0b'
octal = oct(decimal)[2:] # remove the leading '0o'
hexadecimal = hex(decimal)[2:] # remove the leading '0x'

print("Binary: ", binary)
print("Octal:  ", octal)
print("Hexadecimal: ", hexadecimal)
