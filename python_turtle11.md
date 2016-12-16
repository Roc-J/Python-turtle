## 对象Objectives ##
* 介绍对象（object）和类(class)，通过类来描述对象
* 用数据域和方法来定义类  
* 通过构造函数来创建对象，构造函数中进行初始化和一些数据字段初始化信息  

面向对象编程能够使我们开发大规模软件和GUI  
### 定义对象的类 ###
类定义了对象的属性和行为  
面向对象编程OOP（Object-oriented programming）涉及对象的使用来创建程序，一个对象代表真实世界的一个独一无二存在的实体。  
例如，一个学生，一个桌子，一个圆，一个按钮甚至一个贷款都能被看做对象。一个对象有一个独一无二的标识，状态和行为。  

一个对象的状态：也可以看做是属性，是使用变量来表示，称作数据字段  
例如，一个矩形对象的数据字段有宽度和长度，可以表征矩形的属性  
Python使用方法来定义对象的行为，也可以看做是动作，也可以把这些方法称为functions  
例如，一个圆对象可以使用getArea()方法来返回它的面积，使用getPerimeter()方法来返回它的周长。  

一个对象是一个类的实例，你可以创建一个类的多个实例创建一个类的实例就是指 实例化  
类和对象之间的关系类似于食谱和苹果派之间的关系
你可以从一个单一的食谱（类）中制作尽可能多的苹果派（对象）。

![](http://i.imgur.com/89JIp95.png)

### 定义类 ###

\_\_init__   
一个class提供一个特殊的方法，\_\_init__ ，这个方法被称为初始化构造函数，当一个对象创建时初始化对象的状态  

	class 类名字:
		初始化信息initializer
		方法methods

### 构造对象 ###
一旦类被定义，从类的构造函数中可以创建一个对象。构造函数做了两件事情：  
1. 在内存中创建了这个类的对象  
2. 使用\_\_init__ 方法初始化了一些信息  

构造函数的语法: 

	className(arguments)

![](http://i.imgur.com/djNFS2V.png)

### 访问成员变量 ###
下面通过一个例子来表示访问成员变量

	import math
	class Circle:
	    # Construct a circle object
	    def __init__(self,radius=5):
	        self.radius = radius
	    def getPerimeter(self):
	        return 2*self.radius*math.pi
	    def getArea(self):
	        return self.radius*self.radius*math.pi
	    def setRadius(self,radius):
	        self.radius = radius
	
	c = Circle(5)
	
	print c.getArea()
	print c.radius
	print c.getPerimeter()

运行结果：

	78.5398163397
	5
	31.4159265359

### self参数 ###
self是引用对象本身的参数。 使用self，可以在类定义中访问对象的成员。 例如，您可以使用语法self.x来访问实例变量x和语法self.m1（）来调用实例方法m1。  

实例变量的范围是整个类  

![](http://i.imgur.com/OMjyjKn.png)
