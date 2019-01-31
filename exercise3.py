# Exercise 3, Seth Mitchell, CS1400

# part 1: Mathematical expressions translated to python; each expression separated by spacing,
#         then declares the mathematical expression, followed by the code for said expression.

import math
print("(3+4)*5 = ")
print(((3+4)*5))
print()

print("n(n-1)/2 = ")
n_variable = float(input('give a value to the variable "n"; n = ',))
print(float((n_variable *(n_variable - 1)) / 2))
print()

print("4πr^2 = ")
r_radius = float(input('enter a radius "r" value; r = '))
π = math.pi
print(float((4 * π * (r_radius **2))))
print()

print("√((r cos(a)^2 + r cos(b)^2) = ")
r_radius = float(input("define the radius for the function; r = "))
a_variable = float(input('give the variable "a" a value; a = '))
b_variable = float(input('give the variable "b" a value; b = '))
print(float( ( (r_radius * math.cos(a_variable ** 2)) + (r_radius * math.cos(b_variable ** 2)) ) ** (1/2) ))
print()

print('(y_2 - y_1)/(x_2 - x_1) = ; do not include denominating equations = 0')
y_2_variable = float(input('please define a value for the y_2 variable; y_2 = '))
y_1_variable = float(input('please define a value for the y_1 variable; y_1 = '))
x_2_variable = float(input('please define a value for the x_2 variable; x_2 = '))
x_1_variable = float(input('please define a value for the x_1 variable; x_1 = '))
print(float( (y_2_variable - y_1_variable)/(x_2_variable - x_1_variable) ))
print()


# part 2: Predicting behavior of expressions
print(-10 // 3) # should be a negative integer value. (-4)
print(-10 % 3) # due to modulus, should show a negative remainder. (2)
print(10 // -3) # should give a negative integer value. (-4)
print(10 % -3) # due to modulus should give a negative remainder. (-2)
print(-10 // -3) # num and denom should yield a positive int. (3)
print()


# part 3: Write a program to calculate the cost per square inch of a pizza, given the
#         diameter and price as inputs; for an 8" diameter $5.00 and a 23" $20.00.
#         results for: 8" $5 == $0.20; 23" $20 == $0.28

# input functions
print("use this program to find how much your pizza costs per square inch!")
diameter_pizza = float(input('please type the size (diameter) of your pizza; d = '))
cost_pizza = float(input('please tell us the price of your pizza as well; $'))

# conversions, equations & variable assignments
π = math.pi
radius_pizza = float(.5 * diameter_pizza)
area_pizza = float(2 * π * radius_pizza)
cost_per_inch2 = float(cost_pizza / area_pizza)

# output function
print(f'your pizza will cost ${cost_per_inch2:.2f} per square inch!')