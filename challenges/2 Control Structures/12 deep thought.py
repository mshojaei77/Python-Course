# Write a program that prompts the user to enter a number or word. 
# If the input is equal to 42, "forty-two", or "forty two" (case insensitive and ignoring any leading/trailing white space), output "Yes". Otherwise, output "No".

answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
