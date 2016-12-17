## 模块module ##
### 为什么使用模块 ###
1. 它使得python文件更小，在代码中更容易找到东西  
2. 共享性，一旦创建了一个模块，可以在许多程序中使用它。下次在我们需要相同的功能时，可以直接使用。  
3. 不需要使用所有的模块，模块化意味着您可以使用不同的部件组合来完成不同的作业，灵活的实现需求。  

### 桶块 ###
function就像是积木  
可以把一个模块当做是一个构建块，可以在一个桶块中拥有尽可能少或者尽可能多的块，并且可以有多个不同的存储桶。  

![](http://i.imgur.com/vDUCazg.png)

### 创建module ###
创建一个module，module实际上就是一个python文件  

举一个例子说明:  
先创建一个文件add_module.py文件，里面只写了一个 函数

	def add_op(add1,add2):
	    return add1 + add2

另外在创建一个文件test.py,在该文件中引入刚刚创建的那个add_module文件。

	import add_module
	
	print add_module.add_op(12,45)

可以看到可以使用另一个文件中定义的函数，这叫做引入模块

### 命名空间 ###
当import模块时，同时导入了命名空间，有两种方式导入一个模块的命名空间  

* import Tkinter

Tkinter仍然是一个分离的命名空间,需要用Tkinter.来引用该命名空间下的  
Window = Tkinter.Tk()

* from Tkinter import *

Tkinter的命名空间被包含在该文件的命名空间  
Window = Tk()

### Radio Buttons ###

单选按钮的使用

	from Tkinter import *
	root = Tk()
	v = IntVar()
	
	Label(root,text="Choose a programming language",justify=LEFT,padx=20).pack()
	Radiobutton(root,text="Python",padx=20,variable=v,value=1).pack(anchor=W)
	Radiobutton(root,text="Javc",padx=20,variable=v,value=2).pack(anchor=W)
	
	mainloop()

程序说明:  
1. from语句导入了Tkinter下命名空间的所有内容  
2. 生成一个窗口root  
3. v=IntVar() intVar是对“整数”类型的包装  
4. 生成两个单选按钮，加入v中  

程序执行结果:

![](http://i.imgur.com/VhCKWru.png)


还可以使用for将列表中的信息显示成一排单选按钮来进行选择：

	from Tkinter import *
	
	root = Tk()
	v = IntVar()
	v.set(1)
	
	language = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
	
	def ShowChoice():
	    print v.get()
	
	Label(root,text="Choose your favourite programming language:",justify=LEFT,padx=20).pack()
	
	for txt,val in language:
	    Radiobutton(root,text=txt,padx=20,variable=v,command=ShowChoice,val=val).pack(anchor=W)
	
	mainloop()

程序执行结果：

![](http://i.imgur.com/k7dSriI.png)

### 复选框 ###
前面是单选框的例子，我们还可以用复选框来显示

	from Tkinter import *
	wn = Tk()
	
	def var_status():
	    print("male:%d,\n female:%d" % (var1.get(),var2.get()))
	
	Label(wn,text="your sex:").grid(row=0,sticky=W)
	var1 = IntVar()
	Checkbutton(wn,text="male",variable=var1).grid(row=1,sticky=W)
	var2 = IntVar()
	Checkbutton(wn,text="female",variable=var2).grid(row=2,sticky=W)
	Button(wn,text="Quit",command=wn.quit).grid(row=3,sticky=W,pady=4)
	Button(wn,text="Show",command=var_status).grid(row=4,sticky=W,pady=4)
	
	mainloop()


程序说明:  
1. GUI上生成了5个控件，一个是标签label，俩个复选框，两个按钮  
2. 定义了一个函数var_status()来显示IntVar()中的变量  
3. wn.quit是窗口退出函数  

### 变量类 ###
x= StringVar() 保存字符串，默认为""  
x= IntVar() 保存整数，默认是0  
x= DoubleVar() 保存浮点型，默认是0.0  
x=BooleanVar() 保存布尔型，返回0是False，返回1是True  