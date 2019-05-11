# Seth Mitchell (10600367)
# CS 1400

# Project 1: Simple Tip Calculator
# creating a simple tip calculator, I decided to break it into segments during pseudo,
# the catagories were inputs, tip equations, and print statements.

# inputs
cost_meal = float(input('please enter the cost of your meal: $'))

# tip equations
good_service = float(cost_meal * .20)
okay_service = float(cost_meal * .15)
poor_service = float(cost_meal * .10)

good_total = float(good_service + cost_meal)
okay_total = float(okay_service + cost_meal)
poor_total = float(poor_service + cost_meal)

# print statements
print()
print(f'the cost of your meal was: ${cost_meal:.2f}!')
print(f'good service tip (20%) = ${good_service:.2f}', f'(${good_total:.2f} total)')
print(f'okay service tip (15%) = ${okay_service:.2f}', f'(${okay_total:.2f} total)')
print(f'poor service tip (10%) = ${poor_service:.2f}', f'(${poor_total:.2f} total)')

# ending comment: difficulties that I encountered were making sure that the totals
# added up for the tips. Trying create the print statements, I realized that I needed
# to show a total, which I could only think of making a variable in order to do so. I learned
# a lot about the print(f' and how to use it, I struggled a little to do it right the first time.