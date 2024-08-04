x = 42
y = 18
z = 5
# Perform the calculations described in the comments.
# Format your code so that there are spaces around operators
# except when you want to show order of operations. e.g. w = 2*x - 3

# Example: Set w to be the result when you divide x by y
w = x / y
print (f"{x} divided by {y} is {w}")  # this is a fancier way to print things that we'll discuss later.

# 1. Set w to be y to the z power
w = y ** z
print (f"{y} to the power of {z} is {w}")

# 2. Set w to be x divided by y rounded to two decimal places.
w = round(x / y, 2)
print (f"{x} divided by {y} rounded to two decimal places is {w}")

# 3. Set w to be the remainder when you divide x by y
w = x % y
print (f"{x} divided by {y} has a remainder of {w}")

# 4. Set w to be the largest integer number of times that y goes into x.
w = x // y
print (f"{y} goes into {x} {w} times (with perhaps a remainder)")

# 5. Increment the variable x (increase the value of x by 1)
x = x + 1
print(f"After being incremented, x = {x} ")

# 6. Increment the variable x using the "+=" operator.
x += 1
print(f"After being incremented, x = {x} ")

# 7. Import the math module and then set w to be the square root of y using w = math.sqrt(y)
import math
w = math.sqrt(y)
print(f"The square root of {y} is {w}")

# 8. Import the square root function from the math module and use it to set w to be
#    the square root of z using  w = sqrt(z)
from math import sqrt
w = sqrt(z)
print(f"The square root of {z} is {w}")

# 9. Use the distance formula to calculate the distance, d, between the points (x1, y1) and (x2, y2)
#    Format your code using Python style guide conventions.
#    Note: since you already imported sqrt above, you do not need to import it again.
x1, y1 = (2, -5)
x2, y2 = (-4, 12)
d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {d}")

