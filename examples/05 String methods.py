# Define a sample string to work with
sample_string = "Hello, World!"

# String methods for case
print(sample_string.upper())
print(sample_string.lower())
print(sample_string.capitalize())
print(sample_string.title())
print(sample_string.swapcase())

# String methods for searching
print(sample_string.count('l'))
print(sample_string.find('l'))
print(sample_string.rfind('l'))
print(sample_string.index('l'))
print(sample_string.rindex('l'))
print(sample_string.startswith('Hello'))
print(sample_string.endswith('ld'))
print(' '.join(sample_string))
print(sample_string.partition(','))
print(sample_string.rpartition(','))

# String methods for slicing and indexing
print(sample_string[4])
print(sample_string[-1])
print(sample_string[2:7])
print(sample_string[:5])
print(sample_string[7:])
print(sample_string[:-3])
print(sample_string[-6:-1])

# String methods for manipulation
print(sample_string.replace('Hello', 'Hi'))
print(sample_string.strip())
print(sample_string.rstrip())
print(sample_string.lstrip())
print(sample_string.center(20))
print(sample_string.ljust(20))
print(sample_string.rjust(20))
print(sample_string.zfill(20))
print(sample_string.expandtabs(8))

# String methods for formatting
print("My name is {} and I am {} years old".format("John", 30))
print("My name is {1} and I am {0} years old".format(30, "John"))
print("My name is {name} and I am {age} years old".format(name="John", age=30))
print(f"My name is {'John'} and I am {30} years old")

# String methods for splitting
print(sample_string.split())
print(sample_string.split(','))
print(sample_string.splitlines())

# String methods for encoding and decoding
encoded_string = sample_string.encode()
print(encoded_string)
decoded_string = encoded_string.decode()
print(decoded_string)
