# Seth Mitchell (10600367)
# CS 1400
# Exercise 5.3

# Shapes and Line w/ Turtles
import turtle
wn = turtle.Screen

# Meet the Crew
peach = turtle.Turtle()                  # peach/square
peach.color("#FFCBA4")
for i in range(4):
    peach.forward(150)
    peach.left(90)

sky = turtle.Turtle()                  # sky/circle
sky.color("#87CEEB")
sky.circle(130)

forest = turtle.Turtle()                  # forest/triangle
forest.color("#014421")
for i in range(3):
    forest.forward(80)
    forest.left(120)

charlie = turtle.Turtle()                  # charlie/line
charlie.color("#967117")
charlie.right(90)
charlie.forward(80)
