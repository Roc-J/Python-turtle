## python基本编程 ##

写一个简单的程序需要二步:  
* 设计解决问题的算法  
* 使用程序语言去实现  

![](http://i.imgur.com/fRgGCuQ.png)

python的输入:   
### y=raw_input("Name？") ###

	age = raw_input("How old are you?")
	height = raw_input("How tall are you?")
	weight = raw_input("How much do you weight?")
	print "So,you're %r old,%r tall and %r heavy." % (age,height,weight)


### 变量名，赋值语句和表达式 ###
变量名用来指代在程序中会改变的值  

在python中，用**=**来表示赋值语句，赋值语句的表达式如下:  
variable = expression

python 中变量名是区分大小写的  
合法的标识符是由字母，数字和下划线组成的，并且开头必须以字母或者下划线开始，不能以数字开始。  

标识符不能是关键字，python中关键字如下:   
![](http://i.imgur.com/lUAwxVN.png)

### 同步赋值 ###
	x1,y1 = eval(raw_input("Enter x1 and y1 for point 1:"))
	x2,y2 = eval(raw_input("Enter x2 and y2 for point 2:"))

eval(str,[,globals[,locals]])函数将字符串str当成有效Python表达式来求值，并返回计算结果。 
 
	>>> eval('3+4')
	7

### python数字类型和操作 ###
![](http://i.imgur.com/v3r6y4Y.png)

计算两个点的距离

	import turtle
	
	x1,y1 = eval(raw_input("Enter x1 and y1 for poin t1:"))
	x2,y2 = eval(raw_input("Enter x2 and y2 for point 2:"))
	
	distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
	
	turtle.penup()
	turtle.goto(x1,y1)
	turtle.pendown()
	turtle.write("Point 1")
	turtle.goto(x2,y2)
	turtle.write("Point 2")
	
	turtle.penup()
	turtle.goto((x1+x2)/2,(y1+y2)/2)
	turtle.write(distance)
	
	turtle.done()

Python Turtle:  
Write a program that prompts the user to 
enter the center and radius of a circle, 
and then displays the circle and its area.

输入圆的圆心和半径进行绘制，并显示圆的面积

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
	turtle.done()