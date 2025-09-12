# Program to calculate how many grains of wheat will be
# on a chessboard if you start with one grain on the first
# square and double every subsequent square.
# Print the number of the square you are on, the current square, total
square = 1
total = 1
print("n Square  Total")
for n in range(1, 7):
    print(n, square, total)
    square *= 2
    total += square
