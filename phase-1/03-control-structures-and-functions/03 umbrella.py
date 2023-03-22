status = input("is it raining? yes/no :")
status = status.lower()
if status == "yes":
    print("you should take an umbrella")
elif status == "no":
    print("you you don't need an umbrella")
else:
    print("please just enter 'yes or 'no'  ")
