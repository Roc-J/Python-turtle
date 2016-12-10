import turtle

"""Make turtle t draw a square of with side sz"""
def drawSquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

# set up the window and its attributes
wn = turtle.Screen()
wn.bgcolor('lightgreen')
# create alex
alex = turtle.Turtle()
drawSquare(alex,50)

wn.exitonclick()