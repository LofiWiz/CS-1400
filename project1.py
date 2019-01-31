# CS 1400, Seth Mitchell (10600367)
# Project 1: Simple Tip Calculator for good (20%), okay (15%) and poor (10%) tips,
#            also shows the cost of the meal, along with the total cost of the meal.

# inputs
cost_meal = float(input('please enter the cost of your meal: $'))

# conversions and expressions
tip_good = float(cost_meal * .20)                             # calculating tip percentages from meal cost
tip_okay = float(cost_meal * .15)
tip_poor = float(cost_meal * .10)

tip_good_total = float(tip_good + cost_meal)                  # calculating tip percentages added to meal cost
tip_okay_total = float(tip_okay + cost_meal)
tip_poor_total = float(tip_poor + cost_meal)

# outputs                                                     # displaying the output derived from above
print()
print('here are the tip amounts for you meal!')
print(f'Good service tip (20%) = ${tip_good:.2f} (${tip_good_total:.2f} = total)')
print(f'Okay service tip (15%) = ${tip_okay:.2f} (${tip_okay_total:.2f} = total)')
print(f'Poor service tip (10%) = ${tip_poor:.2f} (${tip_poor_total:.2f} = total)')

# review of project : somethings that I learned from this project were how to better use the
#                     print(f' ') function; I hadn't before tried to display two different variables
#                     on the same line. A challenge that I ran into was trying to display all of the tips
#                     in one variable, which I learned would make a tuple, but I'm not very familiar with them.
#                     something like : tip_meal = (.20 * cost_meal), (.15 * cost_meal), (.10 * cost_meal)