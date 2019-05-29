# Seth Mitchell (10600367)
# CS 1400
# Exercise 5.2

# Archery Target using python turtle module
import turtle
wn = turtle.Screen

# Archy the turtle
archy = turtle.Turtle()

# Circle White
archy.circle(130)
archy.up()
archy.left(90)
archy.forward(26)
archy.right(90)

# Circle Black
archy.fillcolor("black")
archy.begin_fill()
archy.circle(104)
archy.end_fill()
archy.up()
archy.left(90)
archy.forward(26)
archy.right(90)

# Circle Blue
archy.color("blue")
archy.fillcolor("blue")
archy.begin_fill()
archy.circle(78)
archy.end_fill()
archy.up()
archy.left(90)
archy.forward(26)
archy.right(90)

# Circle Red
archy.color("red")
archy.fillcolor("red")
archy.begin_fill()
archy.circle(52)
archy.end_fill()
archy.up()
archy.left(90)
archy.forward(26)
archy.right(90)

# Circle Yellow
archy.color("yellow")
archy.fillcolor("yellow")
archy.begin_fill()
archy.circle(26)
archy.end_fill()
archy.up()
archy.left(90)
archy.forward(26)
archy.right(90)