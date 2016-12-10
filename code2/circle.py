import turtle
import time

'''Write a program that prompts the user to
enter the center and radius of a circle,
and then displays the circle and its area.
'''
x1,y1 = eval(raw_input("Enter the center of circle:"))
radius = eval(raw_input("Enter the radius of circle:"))
turtle.penup()
turtle.goto(x1,y1-radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

area = radius*radius*3.14
turtle.goto(x1,y1)
turtle.write(area)
# handle = turtle.Turtle()
#
# for shapeitem in ["arrow","blank", "circle", "classic", "square", "triangle", "turtle"]:
#     handle.shape(shapeitem)
#     handle.left(50)
#     handle.forward(50)
#     time.sleep(2)

turtle.done()