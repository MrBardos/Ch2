# Program to practice writing for loops
#1. Print "Baby Shark" and then use a for loop to print "doo" six times.
print("Baby Shark")
for i in range(6):
    print("doo")

#2. Print the 4th powers from 1 to 10,000, e.g. 1, 16, 81, ..., 10000.
print("Fourth powers.")
for i in range(1, 11):
    print(i ** 4)


#3. Count down from 100 by sevens. e.g. 100, 93, 86, ... 2
print("Counting down from 100 by sevens.")
for i in range(100, 0, -7):
    print(i)


#4. Start with the number n = 1.
#   In a for loop, update the variable n to be 1 + 1 / n
#   Loop 15 times, updating and printing n each time.
#   What number do you end up with?
print("Continued fraction of a famous number.")
n = 1
for i in range(15):
    n = 1 + 1/n
    print(n)