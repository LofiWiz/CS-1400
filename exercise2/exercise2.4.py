# Seth Mitchell (10600367)
# CS 1400
# Exercise 2.4

# 4: Converting Fahrenheit to Celsius:

fahrenheit = float(input("What is the temperature in degrees fahrenheit?: "))
celsius = float((fahrenheit - 32) * 5/9)
print(f"The temperature {fahrenheit} F is = {celsius} C")

# original Celsius to Fahrenheit example:

# celsius = float(input("What is the Celsius temperature? "))
# fahrenheit = 9/5 * celsius + 32
# print(f"The temperature {celsius} Celsius is {fahrenheit:.2f} Fahrenheit.")