# 1. Write a program that asks the user for their name and age and prints out a message telling them how many years they have left until they turn 100.
name = input("What's your name? ")
age = int(input("How old are you? "))
years_left = 100 - age
print(f"Hi {name}, you have {years_left} years left until you turn 100!")
