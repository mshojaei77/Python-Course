# write a Python script that will take input from the user in the form of the size of land (in meters) and the size of each mosaic (also in meters). 
# The script should then calculate how many mosaics will be required to completely cover the land and output the result to the user.
lsize = float(input("How many meters is the land? "))
msize = float(input("How many meters is every mosaic? "))
mosaic = lsize / msize
print("you need ",int(mosaic) , "mosaic")
