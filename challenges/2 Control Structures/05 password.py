# Write a program that prompts the user to enter a password. If the password is "password123", print a message indicating that the password has been accepted. Otherwise, 
# print a message indicating that the password is incorrect.

password = input("Enter your password: ")

if password == "password123":
    print("Password accepted!")
else:
    print("Incorrect password.")
