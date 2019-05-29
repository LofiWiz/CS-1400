# Seth Mitchell (10600367)
# CS 1400
# Exercise 6.5

# functions to find sphere area and volume
import math

# surface area of sphere function
def sphereArea(radius):
    """ find sphere suface area given radius"""
    area = (4 * math.pi * (radius ** 2))
    return area
# volume of sphere funciton
def sphereVolume(radius):
    """ find sphere volume given radius"""
    volume = ((4 * math.pi) * ((radius ** 3) / 3))
    return volume

# Main and invoking functions
def main():
    radius = float(input("please input the radius value: "))
    print("the surface area =",sphereArea(radius), "and the volume =",sphereVolume(radius),".")
main()
