"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %(x)i, y is %(y).2f, z is "%(z)s"' % {"x": x, "y": round(y, 2), "z": z})

# Use the 'format' string method to print the same thing

print('x is {0}, y is {1}, z is "{2}"'.format(x, round(y, 2), z))

# Finally, print the same thing using an f-string

print(f'x is {x}, y is {round(y, 2)}, z is "{z}"')




# NOTES NOTES NOTES ******************

# Conversion

# Meaning

# Notes

# 'd'

# Signed integer decimal.

# 'i'

# Signed integer decimal.

# 'o'

# Signed octal value.

# (1)

# 'u'

# Obsolete type – it is identical to 'd'.

# (6)

# 'x'

# Signed hexadecimal (lowercase).

# (2)

# 'X'

# Signed hexadecimal (uppercase).

# (2)

# 'e'

# Floating point exponential format (lowercase).

# (3)

# 'E'

# Floating point exponential format (uppercase).

# (3)

# 'f'

# Floating point decimal format.

# (3)

# 'F'

# Floating point decimal format.

# (3)

# 'g'

# Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.

# (4)

# 'G'

# Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.

# (4)

# 'c'

# Single character (accepts integer or single character string).

# 'r'

# String (converts any Python object using repr()).

# (5)

# 's'

# String (converts any Python object using str()).

# (5)

# 'a'

# String (converts any Python object using ascii()).

# (5)

# '%'

# No argument is converted, results in a '%' character in the result.

