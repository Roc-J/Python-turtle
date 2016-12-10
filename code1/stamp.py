import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(range(5,60,2))
tess.up()

for size in range(5,60,2):
    tess.stamp()
    tess.forward(size)
    tess.right(24)

wn.exitonclick()