import random
import turtle
"""create the window and turtle"""
wn = turtle.Screen()
alex = turtle.Turtle()
# get the width and height of the window
x1 = alex.window_width()/2
y1 = alex.window_height()/2
# get the current position(x,y)
x = alex.xcor()
y = alex.ycor()
# while loop ,create a randint(0,1) to determine turn which direction
while (x<=x1 and x>= -x1) and (y<=y1 and y>=-y1):
    flag = random.randint(0, 1)
    flag = int(flag)
    if flag==0:
        alex.left(90)
    else:
        alex.right(90)
    alex.forward(50)
    x = alex.xcor()
    y = alex.ycor()

wn.exitonclick()
