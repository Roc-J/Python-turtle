## 面向对象python/Tkinter ##
通过一个程序来说明：
	
	class Employee:
	    empCount = 0
	    def __init__(self,name,salary):
	        self.name = name
	        self.salary = salary
	        Employee.empCount +=1
	    def displayCount(self):
	        print "Total Employee %d" % Employee.empCount
	    def displayEmployee(self):
	        print "Name:",self.name,"Salary:",self.salary
	
	emp1 = Employee("xiaoming",4000)
	emp2 = Employee("xiaohong",5000)
	emp1.displayEmployee()
	emp2.displayEmployee()
	
	print "Total Employee %d" % Employee.empCount


程序说明:  
1. 定义了一个员工类Employee  
2. 类中定义了一个类变量empCount，这个变量记录的是员工的数量，每生成一个类的对象，该值就会增加1  
3. 初始化函数中初始化了姓名和工资  
4. 定义了displayCount()函数显示了员工的数量  
5. 定义了displayEmployee()函数显示了对象的信息

### 类继承 ###

子类从它的父类继承属性，就像这些属性是定义在子类中一样

子类能够重载父类中的数据成员和方法  

下面定义一个Parent类和一个子类Child,Child继承Parent类。  
在Parent类中定义了\_\_init__初始化，输出调用父类构造函数。  
在类Parent中还定义了三个方法  
一个parentMethod()方法输出调用本类的信息  
还有两个方法setAttr()和getAttr()分别来设置数据字段的值和得到数据字段的值。
	
	class Parent:
	    parentAttr = 200
	    def __init__(self):
	        print "Calling parent constructor"
	
	    def parentMethod(self):
	        print "running parent method"
	
	    def setAttr(self,attr):
	        self.parentAttr = attr
	
	    def getAttr(self):
	        print "Get parent attribute:",self.parentAttr
	
	class Child(Parent):
	    def __init__(self):
	        print "Calling child constructor"
	
	    def childMethod(self):
	        print "running child method"
	
	c = Child()
	c.childMethod()
	c.parentMethod()
	c.setAttr(500)
	c.getAttr()

程序运行结果:   

	Calling child constructor
	running child method
	running parent method
	Get parent attribute: 500

上面的例子中只是证明了子类继承父类，可以使用父类中的数据字段和方法。另外，子类还可以对父类中的方法进行重载。  

	class Parent:
	    def __init__(self):
	        print "create a parent object"
	
	    def myMethod(self):
	        print "this is parent method"
	
	class Child(Parent):
	    def __init__(self):
	        print "create a child object"
	
	    def myMethod(self):
	        print "this is child method"
	
	c = Child()
	c.myMethod()

上面的程序中，定义了一个父类Parent，里面除了init()函数外，只声明了一个方法myMethod()，在继承该类生成的子类Child中，对父类的方法myMethod()进行了方法重载。程序运行结果如下，可以看到在调用子类的方法时，已经把父类的那个方法覆盖了。

	create a child object
	this is child method


另外，python类中对变量的定义在前面加上__可以表示私有变量，可以对数据进行隐藏，如下所示
	
	class JustCounter:
	    __secretCount = 0
	
	    def count(self):
	        self.__secretCount +=1
	        print self.__secretCount
	
	counter = JustCounter()
	counter.count()
	counter.count()
	print counter.__secretCount

该程序将变量声明为__secretCount，该变量将成为私有变量，只能在本类中进行操作，不能直接调用。因此会出现： 
     
	print counter.__secretCount
	AttributeError: JustCounter instance has no attribute '__secretCount'


## 图形用户接口Tkinter ##
Tkinter是Python的标准GUI库，Python结合Tkinter提供了一种快速而简单的方法来创建GUI应用程序。Tkinter为Tk GUI工具包提供了强大的面向对象的界面  

	import Tkinter
	top = Tkinter.Tk()
	# Code to add widgets will go here...
	top.mainloop()


上面的代码中简单的引入Tkinter包，调用Tkinter.Tk()生成一个实例top,top.mainloop()就可以看到这个GUI窗口

Tkinter提供各种控件，例如在GUI应用程序中使用的按钮，标签和文本框。这些控件通常称为小部件。

![](http://i.imgur.com/d8My5N9.png)

### 按钮 ###
在python应用程序中使用按钮可以显示文本或者图像。可以将方法或者一个函数绑定到按钮上，在点击按钮的同时会自动的调用按钮。

语法：w=Button(master,option=value,...)  
参数：  
master: 表示父窗口  
options：这是这个小部件最常用的选项列表。 这些选项可用作键值对，以逗号分隔。

举一个小程序显示：

	from Tkinter import *
	
	window = Tk()
	label = Label(window,text="Welcome to Python")
	button = Button(window,text="Click me")
	label.pack()
	button.pack()
	
	window.mainloop()


程序说明：  
1. 首先导入Tkinter模块  
2. 创建一个窗口window  
3. 生成一个标签label  
4. 生成一个按钮button  
5. 将label,button放在窗口上  
6. 事件循环

程序运行结果：

![](http://i.imgur.com/cYOwmKO.png)

#### mianloop ####
Tkinter GUI程序在连续循环中侦听和处理事件。

![](http://i.imgur.com/vpCGl3V.png)

可以看到，当窗口进行mainloop()之后，会不断的监听和处理事件，判断是否关闭了窗口，如果没有关闭，则会一直循环执行，当关闭窗口后，才会程序终止。  

#### 按钮button绑定方法 ####

	# -*- coding=utf-8 -*-

	from Tkinter import *
	def processOK():
	    print u"按钮OK被点击"
	
	def processCancal():
	    print u"Cancal按钮被点击"
	
	window = Tk()
	btOK = Button(window,text="OK",fg="red",command=processOK)
	btCancel = Button(window,text="Cancel",bg="lightblue",command=processCancal)
	
	btOK.pack()
	btCancel.pack()
	
	window.mainloop()

在一个GUI上添加两个按钮OK和Cancel，对两个按钮绑定一个方法，点击按钮，输出文本信息。  

### 改变标签的文本 ###

在上面的代码中，我们可以添加一个标签，通过点击不同的按钮，在标签上显示不同的文本 

修改一下上面的代码：

		# -*- coding=utf-8 -*-
		
		from Tkinter import *
		
		def processOK():
		    print u"Ok按钮被点击"
		    label['text'] = "Ok"
		
		def processCancal():
		    print u"Cancal按钮被点击"
		    label['text'] = "Cancel"
		
		window = Tk()
		label = Label(window,text="Welcome to GUI programming")
		btOK = Button(window,text="OK",fg="red",command=processOK)
		btCancel = Button(window,text="Cancel",bg="lightblue",command=processCancal)
		
		label.pack()
		btOK.pack()
		btCancel.pack()
		
		window.mainloop()

