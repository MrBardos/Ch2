# Program to print the first 15 numbers in the Fibonacci Sequence.
previous_2 = 0
previous_1 = 1
print(previous_2)
print(previous_1)
for i in range(13):
    new = previous_2 + previous_1
    print(new)
    previous_2 = previous_1
    previous_1 = new
