# Seth Mitchell (10600367)
# CS 1400
# Exercise 6.6

# Program to find area of a triangle given side lengths
import math

# function for area of triangle
def triangleArea(sideA,sideB,sideC):
    '''uses side lengths a, b, c to find area of triange'''
    p = ((sideA + sideB + sideC) / 2)           # finding 1/2 of perimeter
    area = math.sqrt(p * (p - sideA) * (p - sideB) * (p - sideC))
    return area

# body for program
def main():
    
    sideA,sideB,sideC = float(input("side length a = ")), float(input("side length b = ")),float(input("side length c = "))
    print("the area of your triangle is",triangleArea(sideA,sideB,sideC),".")

main()
