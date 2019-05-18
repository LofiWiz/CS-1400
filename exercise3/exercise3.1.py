# Seth Mitchell (10600367)
# CS 1400
# exercise 3.1

import math
# Translations:

#1
print(float((3+4) * 5))
print()

#2
n = float(input("define the numeric value of n; n =  "))
print((n * (n-1)) / 2)
print()

#3
r = float(input("define the value of r (radius); r = "))
print((4 * math.pi * r ** 2))
print()

#4
r = float(input("define the value of r (radius); r = "))
a = float(input("define the numeric value of a; a = "))
b = float(input("define the numeric value of a; a = "))
print(math.sqrt((r * (math.cos(a) ** 2) + (math.cos(b)) ** 2)))
print()

#5
print("for the following, not that x2 - x1 can NOT  == 0")
y_1 = float(input("define the numeric value of y1; y1 = "))
y_2 = float(input("define the numeric value of y2; y2 = "))
x_1 = float(input("define the numeric value of x1; x1 = "))
x_2 = float(input("define the numeric value of x2; x2 = "))
print((y_2 - y_1) / (x_2 - x_1))