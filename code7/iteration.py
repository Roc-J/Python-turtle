import turtle

for f in ['Joe','Amy','Brad','Angelina','Zuki','Thandi','Paris']:
    print "Hi",f,"please come to my party on Saturday"

for i in [48,117,200,240,160,260,220]:
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(i)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(i)
    turtle.end_fill()
    turtle.left(90)

width,height = turtle.screensize()
print width,height
turtle.done()
