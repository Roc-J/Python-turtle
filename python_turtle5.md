## 选择语句 ##
布尔值和布尔表达式  
只有两个布尔值：True False  
字母大写很重要，因为python对大小写敏感  

比较操作符  
x!=y 不等于  
x>y  大于  
x<y  小于  
x>=y 大于等于  
x<=y 小于等于  

逻辑运算符  
and or not  

### 运算符优先级 ###
![](http://i.imgur.com/eZrV14X.png)


### 条件表达式 ###

	if BOOLEAN EXPRESSION:
	    STATEMENTS_1        # executed if condition evaluates to True
	else:
	    STATEMENTS_2        # executed if condition evaluates to False


	x = 15
	if  x % 2 == 0 :    
	      print(x, "is even")
	else :   
	      print(x, "is odd")


下面的代码有错误:

![](http://i.imgur.com/mUAse24.png)

每一个else块必须匹配一个if块，如果想链接，可以使用elif  

### 嵌套if else ###
	
	if x < y:
	     print  "x is less than y”
	else:
	     if x > y:
	          print  "x is greater than y”
	     else:
	          print  "x and y must be equal”


### 多条件 ###
	if x < y:
	     print   "x is less than y”
	elif x > y:
	     print  "x is greater than y”
	else:
	      print  "x and y must be equal”
