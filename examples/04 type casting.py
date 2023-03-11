# Define variables of different data types تعریف متغییرهایی با نوع داده متفاوت
num1 = 10
num2 = 3.14
name = "John Doe"
is_student = True

# Convert data types using type casting تبدیل انواع داده
num1_str = str(num1)  # convert integer to string
num2_int = int(num2)  # convert float to integer
is_student_str = str(is_student)  # convert boolean to string
name_list = list(name)  # convert string to list

# Print the converted values and their data types چاپ مقادیر تبدیل شده و نوع آن ها
print(num1_str, type(num1_str))  # Output: "10", <class 'str'>
print(num2_int, type(num2_int))  # Output: 3, <class 'int'>
print(is_student_str, type(is_student_str))  # Output: "True", <class 'str'>
print(name_list, type(name_list))  # Output: ['J', 'o', 'h', 'n', ' ', 'D', 'o', 'e'], <class 'list'>
