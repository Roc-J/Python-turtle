## 几何管理器 ##

Tkinter使用几何管理器在容器中管理组件  

下面介绍三种布局方式  
* grid manager  
* pack manager  
* place manager  

### Grid Manager网格管理器 ###

网格管理器将容器当做不可见的网格，可以将组件放置在单元格中。我们通过指定的行和列来放置窗口小组件，当然，还可以通过参数rowspan和columnspan将窗口组件放置在多个行和列中  

下面通过一个实例来简单的实现网格布局的用法


	# -*- coding=utf8 -*-
	from Tkinter import *
	
	# 创建一个类
	class GridManagerDemo:
	    def __init__(self):
	        # 创建窗口
	        window = Tk()
	        window.title("网格布局管理")
	
	        # 创建一个消息Message
	        message = Message(window,text="这个消息占据了三行三列")
	        message.grid(row=1,column=1,rowspan=3,columnspan=3)
	        # 创建标签和文本框
	        Label(window,text="用户名:").grid(row=1,column=4)
	        Entry(window).grid(row=1,column=5,padx=5,pady=5)
	        Label(window, text="密码:").grid(row=2, column=4)
	        Entry(window).grid(row=2, column=5, padx=5, pady=5)
	        Button(window,text="登录:").grid(row=3,column=5)
	
	        window.mainloop()
	
	GridManagerDemo()


程序运行结果： 

![](http://i.imgur.com/IzODXhb.png)

grid()用法最简单的就是在参数里指定是几行几列  



