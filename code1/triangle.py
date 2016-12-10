import turtle

wn = turtle.Screen()

babbage = turtle.Turtle()
# babbage.shape("triangle")

n = int(raw_input("How many legs should this sprite have?"))
angle = 360/n

for i in range(n):
    # draw the leg
    babbage.right(angle)
    babbage.forward(65)
    babbage.stamp()

    # go back to the middle and turn back around
    babbage.right(180)
    babbage.forward(65)
    babbage.right(180)

babbage.shape("circle")
wn.exitonclick()