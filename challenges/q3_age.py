# محاسه سن دقیق یک شخص
# exact age calculator
dob = int(input("Day of Birth: "))
mob = int(input("Month of Birth: "))
yob = int(input("Year of Birth: "))
              
dot = int(input("Day of Today: "))
mot = int(input("Month of Today: ") )
yot = int(input("Year of Today: " )  )              
                
day = dot - dob
month = mot - mob
year = yot - yob
print ( f"you have {year} year,  {month} month and {day} days  old now!!" )
