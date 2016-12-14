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
* 