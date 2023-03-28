# What is the Python code to calculate the energy (E) in joules for an object of mass (m) in kilograms 
# using Einstein's famous equation E = m * c^2, where c is the speed of light in meters per second and set as a constant of 300,000,000 m/s ?

m = int(input("m: "))
c = 300000000
E = m * (c ** 2)
print(E)
