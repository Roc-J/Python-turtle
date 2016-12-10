## 数据类型、输入、函数 ##
### 类型转换 ###
flaot()函数从一个字符串或者整数转换成一个float  
int()函数从一个字符串或者float类型转换成int  
str()函数从一个数字或者其他类型转换成一个字符串的形式  

	>>> a=100
	>>> b=float(a)
	>>> b
	100.0
	>>> c='300'
	>>> d=str(c)
	>>> d
	'300'
	>>> d=int(c)
	>>> d
	300
	>>> e=float(c)
	>>> e
	300.0
	>>>

python实际上不会将对象类型转换成另外一个类型，它实际上是创建了一个新的对象  

### type()函数 ###

	>>> a='44.2'
	>>> b=100.2
	>>> type(a)
	<type 'str'>
	>>> type(b)
	<type 'float'>
	>>>

类型转换也会发生异常，当字符串中不是数字而是字母时转换成 float或者int会发生报错。

### raw_input()函数 ###
该函数从用户输入得到一个字符串，通常是从键盘得到输入  
	
	print "Enter your name:"
	somebody = raw_input()
	print "Hi,",somebody,"how are you today?"

如果你希望用户输入的和提示的信息在一行上显示，则可以在print的后面添加一个逗号，比如:

	print "Enter your name:",
	somebody = raw_input()
	print "Hi,",somebody,"how are you today?"

简单的写法：  

	somebody = raw_input("Enter your name:")

### function/函数 ###
python中的函数是语句的序列，函数的主要目的是帮助我们将解决问题的解决方法组织成一个块来处理。

函数定义的语法:  

	def name(parameters):
		statements

正式参数: 列表中描述的名字是函数需要从用户接收的  
实际参数：用户通过函数传递的值

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

![](http://i.imgur.com/WQlQBYA.png)


上面代码通过函数实现了画一个正方形。


### range()函数 ###
range(stop) -- 产生一组整数列表  
range(start,stop[,step]) -- 产生一组列表  
	
	import turtle
	wn = turtle.Screen()
	alex = turtle.Turtle()
	
	for i in [0,1,2,3]:
	    alex.forward(50)
	    alex.left(90)
	
	wn.exitonclick()


如果我们想得到前10个奇数:  
	
	range(0,19,2)

![](http://i.imgur.com/EGtFxTH.png)

得到如图所示的图形：

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