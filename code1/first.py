# allows us to use the turtles library
import turtle
import time

# create a graphics windows
wn = turtle.Screen()
# create a turtle named alex
alex = turtle.Turtle()

# tell alex to move forward by 150 units
alex.forward(150)
# tell alex to turn 90 degress
alex.left(90)
alex.forward(75)

time.sleep(3)

wn.exitonclick()