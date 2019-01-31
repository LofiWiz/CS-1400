# Exercise 2; CS 1400 UVU, Seth Mitchell (10600367)

#program that evaluates for the squares of 1,2,3,4,5
x = 1,2,3,4,5
print([x ** 2 for x in range(1,6)])

#program for coverting degrees fahrenheit to celsius
fahrenheit = float(input("enter the temperature in degrees fahrenheit: "))
celsius = ((fahrenheit - 32)*(5/9))
print(f"The temperature {fahrenheit} fahrenheit is {celsius} degrees celsius!")