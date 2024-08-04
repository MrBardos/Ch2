# Variables can store various types of data.
# You do not need to explicitly specify
value = 2000 # integers
interest_rate = 0.07 # floating point numbers
name = "Peabody" # strings

print("Account: ", name, " value: ", value)

# Set the variable value to be a new number.
# Since the result of the calculation is a floating point number,
# The variable value has now been changed to be a floating point type
value = value * (1 + interest_rate)
print("Account: ", name, " value: ", value)

# You can ask the user to enter a number using the input() function
# But since input() returns a string, you must convert the string to an integer (or float)
year = int(input("How many years? "))
value = value * (1 + interest_rate) ** year
print("Account: ", name, " value: ", value)

# You can explicitly set the type of a variable using functions
dollar = int(value) # dollar is an integer type. The decimal places of value are truncated
print(dollar)