# Seth Mitchell (10600367)
# CS 1400
# exercise 3.3

#program for finding cost per square inch of pizza; given the diameter and price of pizza. 

import math

# inputs
diameter_pizza = float(input("please eneter the diameter (size) of your pizza (in inches); diameter = "))
price_pizza = float(input("please enter the price of your pizza; price = $"))

# conversions and calculations
area_pizza = float(math.pi * (diameter_pizza / 2) **2)
cost_pizza_final = price_pizza / area_pizza

# outputs and results
print(f"the cost of your pizza is ${cost_pizza_final:.2f} per square inch!")

#results for 8 diameter, $5.00 pizza: .10 per square inch. 
#results for 23 diameter, $20.00 pizza: .05 per square inch. 