# Seth Mitchell (10600367)
# CS 1400
# exercise 4.3

# program for determining if circles intersect or not
import math

# inputs; defining 2 circles center (x,y) values
print("this program determins whether or not two circles intersect")
circle1_x1 , circle1_y1 = float(input("define x value for center of circle_1: x = ")), float(input("define y value for center of circle_1: y = "))
radius_1 = float(input("define the radius of circle_1: r = "))
print()

print("now for circle 2")
circle2_x2 , circle2_y2 = float(input("define x value for center of circle_2: x = ")), float(input("define y value for center of circle_2: y = "))
radius_2 = float(input("define the radius of circle_2: r = "))

# bool and logic to determine if intersecting or not; uses distance formula
# if radius1 + radius2 >= distance, then they intersect.
distance = math.sqrt(((circle1_x1 - circle2_x2) ** 2) + ((circle1_y1 - circle2_y2) ** 2))
if radius_1 + radius_2 <= 0:
    print("the two circles do not exist")
elif radius_1 + radius_2 >= distance:
    print("the two circles intersect")
else:
    print("the two circles do not intersect")
