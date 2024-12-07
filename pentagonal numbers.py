# Program to print the first 15 pentagonal numbers.
pent = 0
for additional in range(1, 1 + 14 * 3 + 1, 3):
    pent += additional
    print(pent)
