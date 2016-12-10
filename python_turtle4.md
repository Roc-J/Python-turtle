## function /函数 ##
### 返回值的函数 ###

	def square(x):
	    y = x*x
	    return y
	
	toSquare = 10
	result = square(toSquare)
	print "The result of",toSquare,"squared is",result

运行结果：
	
	The result of 10 squared is 100

### 变量名和参数是局部的 ###

![](http://i.imgur.com/tA2URYT.png)

变量y只在函数运行时存在，我们把这叫做生存时间，当函数执行完，返回return时，局部变量就会销毁。  

![](http://i.imgur.com/WMxmFLz.png)

局部域和全局域  
python先在函数定义范围内找局部变量，如果没有找到，python才会寻找全局变量。

### 累加器 ###
	
	def square(x):
	    runningtotal = 0
	    for counter in range(x):
	        runningtotal = runningtotal + x
	
	    return runningtotal
	
	toSquare = 10
	result = square(toSquare)
	print "The result of",toSquare,"squared is",result

通过使用for循环和变量来实现累加


### 函数调用 ###

	def square(x):
	    y = x*x
	    return y
	
	def sum_of_square(x,y,z):
	    a = square(x)
	    b = square(y)
	    c = square(z)
	
	    return a+b+c
	
	a = -5
	b = 10
	c = 2
	
	result = sum_of_square(a,b,c)
	print result

