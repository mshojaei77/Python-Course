''' Write a program that prompts the user to enter a greeting. The program should then check 
if the greeting contains the word 'hello' (case insensitive and ignoring any leading/trailing white space).
If the greeting includes 'hello', the program should output "$0". If the greeting starts with the letter 'h', the program should output "$20". 
Otherwise, the program should output "$100".
'''
# Get user input
answer = input("Greeting: ")

fix_answer = answer.lower().strip()

# Check if the answer has 'hello', print $0
if 'hello' in fix_answer:
    print("$0")

# Check if answer starts with 'h', print $20
elif fix_answer[0] == 'h':
    print("$20")

# Otherwise, print $100
else:
    print("$100")
