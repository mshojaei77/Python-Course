# Write a function in Python that calculates the BMI (Body Mass Index) for a person 
# based on their weight and height input, and returns the BMI value as a float rounded off to two decimal places.

w = float(input("enter your weight in kilograms: "))
h = float(input("enter your height in meters: "))
bmi = w / h**2
print("bmi: ", round(bmi,2))
