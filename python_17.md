## 菜单（Menu) ##
菜单按钮组件  
一个是菜单的一部分，并显示在应用程序的顶部，这对用户始终存在  

菜单部件  
一个显示当用户点击任何菜单按钮时的选择列表  

例如，加入一个文件菜单，可以使用下面的代码：  

	# Adding Menubar in the widget  
	menubar = Menu(root)
	filemenu = Menu(menubar,tearoff=0)  # 文件菜单
	root.config(menu=menubar) # 显示菜单

将菜单项加入到菜单中  
格式：  
mymenu.add_command(label="Mylabel",accelerator="KeyBoardShortcut",compound=LEFT,image=myimage,underline=0,command=callback)

### 菜单的其他类型 ###
* 复选框按钮：此菜单允许你通过选中/取消选中菜单进行是/否选择
* 单选按钮： 此菜单允许你从多种选项中选择一个  
* 级联按钮： 此菜单仅打开显示另一个选项列表   

下面简单示范一个菜单例子：

	from Tkinter import *
	
	class MenuDemo():
	    def __init__(self):
	        window = Tk()
	        menubar = Menu(window)
	        filemenu = Menu(menubar,tearoff=0)
	        filemenu.add_command(label="New")
	        filemenu.add_command(label="Open")
	        filemenu.add_command(label="Save")
	        filemenu.add_separator()
	        filemenu.add_command(label="Close")
	        menubar.add_cascade(label="File",menu=filemenu)
	        window.config(menu=menubar)
	
	        mainloop()
	
	MenuDemo()

程序运行结果:

![](http://i.imgur.com/gIs7d3c.png)

点击File会显示下面的菜单项

程序说明：  
1. 使用Menu()来创建一个菜单栏menubar  
2. 使用Menu(menubar,tearoff=0)来创建一个文件菜单filemenu     
3. 使用menubar.add_cascade(label="File",menu=filemenu)将刚刚创建的filemenu加到菜单栏上   
4. 使用filemenu.add_command(label="name")来增加菜单项  


### 弹出菜单 ###
弹出菜单也可以称为是上下文菜单，就像一个常规菜单，但是不是像传统的那样有菜单栏，它是一个浮在屏幕上的任何地方。  

创建一个弹出式菜单类似于创建一个常规的菜单  
1. 创建一个Menu实例  
2. 向菜单添加菜单项  
3. 将一个窗口部件绑定到一个事件上来弹出菜单  


