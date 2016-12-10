import turtle

def drawMulticolorSqure(t,sz):
    """Make turtle t draw a multi-color square of sz"""
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

alex = turtle.Turtle()
alex.pensize(3)

size = 20
for i in range(15):
    drawMulticolorSqure(alex,size)
    size = size + 10
    alex.forward(10)
    alex.right(18)

wn.exitonclick()