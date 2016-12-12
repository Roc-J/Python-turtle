## 迭代Iteration ##
迭代就是执行语句的序列  

### 重新访问for循环 ###
for循环执行列表中的每一个元素  

每一项依次(重新)分配给循环变量，并且执行循环体  

	for f in ['Joe','Amy','Brad','Angelina','Zuki','Thandi','Paris']:
	    print "Hi",f,"please come to my party on Saturday"

执行结果如图:  

	Hi Joe please come to my party on Saturday
	Hi Amy please come to my party on Saturday
	Hi Brad please come to my party on Saturday
	Hi Angelina please come to my party on Saturday
	Hi Zuki please come to my party on Saturday
	Hi Thandi please come to my party on Saturday
	Hi Paris please come to my party on Saturday

绘制条形图：

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
	
	turtle.done()

运行结果如图:

![](http://i.imgur.com/xZNLtgR.png)

### range() ###

	>>> range(5)
	[0, 1, 2, 3, 4]
	>>> range(2,9)
	[2, 3, 4, 5, 6, 7, 8]
	>>> range(1,6,2)
	[1, 3, 5]
	>>> range(6,1,-1)
	[6, 5, 4, 3, 2]
	>>> range(1.5,8.5,2)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: range() integer end argument expected, got float.
	>>>

* range(n) 参数为n，生成一个从0开始增到小于n的列表  
* range(n,m) 参数为n,m，生成一个从n开始，小于m的一组列表  
* range(start,stop,step) 参数为start，stop,step

举一个例子来说明range()函数的用法：  
下面的例子先定义了一个函数，这个函数是一个加法器，输入一个参数，从1叠加到该函数，求和  

	# -*- coding=utf-8 -*-
	"""定义一个函数加法器"""
	def SumTo(aBound):
	    theSum = 0
	    for i in range(1,aBound+1):
	        theSum = theSum + i
	
	    return theSum
	
	print SumTo(4)
	
	print SumTo(100)

### while循环 ###

	count = 0
	while count < 100:
		print("the program is running ..")
		count = count + 1

while循环  
一般来说，while循环语句执行流程:  
1. 评估条件是否成立，判断是否等于False或者True  
2. 如果条件是False，退出while循环继续执行while下面的语句  
3. 如果条件是True，执行while循环体返回步骤1  

### for循环和while循环的不同 ###
1. for循环创建了一个已经定义的迭代，因为我们明确的知道了我们需要迭代多少次  
2. while循环执行次数是取决于条件语句的，需要去判断是否是False来终止执行。因为我们不需要知道什么时候发生，所以我们可以把这当做是未知的迭代。  

下面的代码包含了未知的循环，但是为什么不能终止

	n = 10
	answer = 1
	while n>0:
		answer = answer + n
		n = n + 1
	print answer

因为上面的代码中条件状态永远不能为False，所以是一个死循环。  