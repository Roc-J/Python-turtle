## 字符串 ##

集合数据类型:  
int,float,bool,str  

在字符串上的操作   

	"hello"-1  
	"hello"/123  
	message*"Hello"  
	"12"+2

这些都是在python中不可运行的~

### 字符串的级联 ###

	fruit = "banana"  
	bakedGood = "nut bread"  
	print fruit + bakedGood

### 重复 ###

	print "GO"*6
	name = "Packers"
	print name*3
	print name + "Go"*3
	print (name + "Go")*3

序号操作:  
对字符串中的每一个字符进行操作：  

![](http://i.imgur.com/h1GCprY.png)

	school = "Luther Collage"
	m = school[2]
	print m
	lastchar = school[-1]
	print lastchar

运行结果:  

	>>> school = "Luther Collage"
	>>> m = school[2]
	>>> print m
	t
	>>> lastchar = school[-1]
	>>> print lastchar
	e
	>>>

### 字符串函数 ###

* upper() 字符串大写  
* lower() 字符串小写  
* capitalize() 首字母大写  
* strip() 字符串前后的空格都去掉  
* lstrip() 字符串前面的空格去掉  
* rstrip() 字符串后面的空格去掉  
* count(item) 返回item在字符串中的数量  
* replace(old,new) 用new字符串替换old字符串  

下面的程序是函数使用的例子

	ss = "Hello World"
	print ss.upper()
	
	tt = ss.lower()
	print tt
	
	ss = "     Hello,World    "
	els = ss.count("l")
	print els
	
	print "***" + ss.strip() + "***"
	print "***" + ss.lstrip() + "***"
	print "***" + ss.rstrip() + "***"
	
	news = ss.replace("o","***")
	print news

下面是程序运行的结果：

	HELLO WORLD
	hello world
	3
	***Hello,World***
	***Hello,World    ***
	***     Hello,World***
	     Hell***,W***rld    

* center(width) 函数是将字符串以width长度进行输出，原字符串位于中间位置  
* ljust(width) 函数是将字符串以width长度进行输出，原字符串位于左边位置  
* rjust(width) 函数是将字符串以width长度进行输出，原字符串位于右边位置  
* find(str) 函数是在原字符串中查找str第一次出现的位置  
* rfind(str) 函数是在原字符串中查找str从右边第一次出现的位置  
* index（str）函数是在原字符串中查找str第一次出现的位置  
* len(str) 函数是计算字符串的长度  

下面写程序举例说明: 

	food = "banana bread"
	print (food.capitalize())
	
	print "*" + food.center(25) + "*"
	print "*" + food.ljust(25) + "*"
	print "*" + food.rjust(25) + "*"
	
	print food.find("e")
	print food.find("na")
	print food.find("b")
	
	print food.rfind("e")
	print food.rfind("na")
	print food.rfind("b")
	
	print food.index("e")
	
	fruit = "Banana"
	sz = len(fruit)
	lastch = fruit[sz-1]
	print lastch

程序执行结果: 

	Banana bread
	*       banana bread      *
	*banana bread             *
	*             banana bread*
	9
	2
	0
	9
	4
	7
	9
	a

### Slice操作 ###
对字符串取字符串的操作是slice()  

	fruit = 'banana'
	print fruit[:3]
	print fruit[3:]
	print fruit[0:4]

程序运行结果是:  

	ban
	ana
	bana

1. slice()操作[n:m]返回从第n个字符到第m个字符。包括第n个字符，不包括第m个字符。  
2. 如果省略第一个参数，那么从字符串的开头截取字符串  
3. 如果省略第二个参数，那么截取到字符串的结尾  


### 字符串的比较 ###
字符串可以用>或者<号进行比较。  
ord("character") 可以将字符转换成数字  
chr(number) 可以把数字转换成字符


	print "apple" < "Apple"
	print ord("A")
	print ord("B")
	print chr(65)
	print chr(78)

程序运行结果: 

	False
	65
	66
	A
	N

字符串是不可变的，这意味着我们不能改变一个已经存在的字符串，最好是我们去对原有字符串进行操作创建一个新的字符串  

	greeting = "Hello,world!"
	newGreeting = 'J' + greeting[1:]
	print newGreeting
	print greeting

运行结果:  

	Jello,world!
	Hello,world!

### 遍历字符串中的每一个字符 ###

	for achar in "Go Spot Go":
	    print achar,
	
	fruit = "apple"
	for idx in range(len(fruit)):
	    print fruit[idx],

运行结果如下:  
	
	G
	o
	 
	S
	p
	o
	t
	 
	G
	o
	a
	p
	p
	l
	e

in 和 not in 是来判断元素是否在一个列表，字符串或者可迭代的序列中：  

	print 'p' in 'apple'
	print 'i' in 'apple'
	print 'ap' in 'apple'
	print 'pa' in 'apple'

运行结果:  

	True
	False
	True
	False

