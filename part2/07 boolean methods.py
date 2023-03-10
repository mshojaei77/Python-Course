x = True

# Boolean methods
print(x.bit_length())  # Returns the number of bits required to represent the integer
print(x.conjugate())  # Returns self, the complex conjugate of any non-complex argument
print(x.denominator)  # Returns the denominator of a rational number in lowest terms
print(x.imag)  # Returns the imaginary part of a complex number
print(x.numerator)  # Returns the numerator of a rational number in lowest terms
print(x.real)  # Returns the real part of a complex number
print(x.to_bytes(1, byteorder='big'))  # Returns an array of bytes representing an integer. The first argument specifies the length of the byte array, and the second argument specifies the byte order ('big' or 'little')

# Operator methods
print(x.__and__(False))  # Performs a bitwise and operation
print(x.__or__(False))  # Performs a bitwise or operation
print(x.__xor__(False))  # Performs a bitwise xor operation
print(x.__invert__())  # Performs a bitwise inversion
print(x.__bool__())  # Returns the boolean value of the object (True or False)

# Boolean operators for comparison
print(5 == 5)
print(5 != 5)
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 <= 3)

# Boolean operators for logic
print(True and False)
print(True or False)
print(not True)

# Boolean operators for identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)
print(a is not b)
print(a is c)

# Boolean operators for membership
d = [1, 2, 3, 4, 5]

print(1 in d)
print(6 in d)
print(1 not in d)


