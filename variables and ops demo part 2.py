x = 5
y = 3

print("Add: ", x + y)
print("Subtract: ", x - y)
print("Power: ", x ** y) # Note: "**" is the sign for exponentiation, not "^".
print("Divide: ", x / y)
# Integer division returns an integer value if x and y are both integers.
# Integer division drops the decimal part of the value.
print("Integer division: ", x // y)  # truncates the decimal (floor function).
print("Modulo i.e. remainder: ", x % y)

# Some built-in functions
print(abs(-24)) # absolute value
print(int(2.778)) # truncates decimals
print(round(2.778, 1)) # rounds to 1 decimal place

# A math module has many, many more functions
import math
print(math.sqrt(x))
print(math.pi, math.cos(y / x), )

# You can import a few functions so you can call the
# functions like "cos()" without typing "math.cos()"
from math import asin, degrees
print(degrees(asin(y / x)))

# You can initialize two variables on one line
length, width = 20, 3
print(length, width)

# You can initialize two variable to be the same value
x = y = 0
print(x, y)

# Increment x (make x larger by 1)
x = x + 1
print(x)

# Shortcut to increment x
x += 1
print(x)

# Shortcut to divide, etc.
x /= 4 # x = x / 4
print(x)