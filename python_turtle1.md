## Python Turtle Graphics（python图形绘制） ##
### 学习目标 ###
* 使用赋值来命名对象，例如turtles,screens
* 使用turtle对象来执行一些事件响应
* 介绍procedure的概念，事件响应的过程
* 介绍一些绘图程序，例如颜色color，画笔penup,pendown，画笔的大小pensize
* 操作创建多个对象

### 第一个程序 ###

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

程序说明：
1. 首先导入绘制图形的模块turtle  
2. 用turtle生成一个窗口  
3. 得到一个turtle的实例alex=turtle.Turtle()  
4. 这个实例进行action，向前前进150个单位距离  
5. left(90)进行左转  

当创建一个Turtle实例的时候，turtle方向是超东

![](http://i.imgur.com/3t0pKKP.png)

绘制如图所示程序：要求使用一个turtle画出一个白色的T在一个绿色的背景色上  
程序应该做到  
* set-up建立初始化  
* create the turtle  
* set the pen size to 10  
	
	import turtle
	
	wn = turtle.Screen()
	wn.bgcolor("green")
	jamal = turtle.Turtle()
	jamal.color("white")
	jamal.pensize(10)
	
	jamal.left(90)
	jamal.forward(150)
	
	jamal.left(90)
	jamal.forward(50)
	
	jamal.left(180)
	jamal.forward(100)
	
	wn.exitonclick()

![](http://i.imgur.com/PhuLFFJ.png)

绘制如图所示照片：  
可以看到在一个窗口上显示了两条线
	
	import turtle
	
	wn = turtle.Screen()
	
	jamal = turtle.Turtle()
	jamal.color("blue")
	jamal.pensize(10)
	
	jamal.left(90)
	jamal.forward(150)
	
	tina = turtle.Turtle()
	tina.pensize(10)
	tina.color("orange")
	tina.forward(150)
	
	wn.exitonclick()

迭代可以简化我们的程序：  
画一个正方形：

迭代1：  

	import turtle
	
	wn = turtle.Screen()
	alex = turtle.Turtle()
	
	for i in [0,1,2,3]:
	    alex.forward(50)
	    alex.left(90)
	
	wn.exitonclick()

迭代2：

	import turtle
	
	wn = turtle.Screen()
	alex = turtle.Turtle()
	
	for aColor in ["yellow","red","purple","blue"]:
	    alex.color(aColor)
	    alex.forward(50)
	    alex.left(90)
	
	wn.exitonclick()

在迭代2中，对正方形的每一条边进行不同颜色的绘制


在turtle中有更多的绘制方法和表现形式:  
1. 每一个turtle有它自己的形状，比如arrow,blank,circle,class,square,triangle,turtle  
2. 每一个turtle可以"stamp"自己的印记在容器canvas

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


显示之后：

![](http://i.imgur.com/USvhLtB.png)

而要实现如图所示的界面：

![](http://i.imgur.com/m5EDSNC.png)
	
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

## 总结 ##
### python turtle绘图实例教程 ###

python turtle是一种简单的绘图工具  
1. 使用turtle绘图首先我们需要导入turtle,如下所示：  
  from turtle import *

2. turtle绘图属性  
  （1）位置  
  （2）方向  
  （3）画笔（画笔的属性，颜色，画线的宽度）  

3. turtle绘图有许多的命令，这些命令可以划分为两种，一种为运动命令，一种为画笔控制命令  
  
（1）运行命令  
  forward(degress) # 向前移动距离degress代表距离  
  backward(degress) #向后移动距离degress代表距离  
  right(degress) #向右移动多少度   
  left(degress) #向左移动多少度  
  goto(x,y) #将画笔移动到坐标x,y的位置  
  stamp() #复制当前图形  
  speed() #画笔绘制的速度范围[0,10]整数  

  （2）画笔控制命令  
   down() #移动时绘制图形，缺省时也为绘制  
   up() #移动时不绘制图形  
   pensize(width) #绘制图形时的宽度  
   color(colorstring) #绘制图形时的颜色  
   fillcolor(colorstring) #绘制图形的填充颜色  
   fill(Ture)  
   fill(false)

### 如图显示一些methods: ###

![](http://i.imgur.com/kDm9VB8.png)  