import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()

for i in range(0,300,3):
    alex.forward(i)
    alex.right(90)

wn.exitonclick()