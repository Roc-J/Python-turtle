## 动画 ##
动画可以通过显示一系列图纸来创建  
Canvas类可以用来开发动画，可以在canvas上显示图形和文本，并使用move(tags,dx,dy)方法将带有指定标签的图形向右移动dx像素（如果dx为正），dy像素向下（如果dy为正）  
如果dx或者dy为负，图形向左或者向上移动~  

下面通过一个程序来说明，创建一个canvas，在上面创建2个矩形，将第一个矩形进行移动

	# -*- coding=utf8 -*-
	from Tkinter import *
	root = Tk()
	# 创建一个Canvas，设置其背景色为白色
	cv = Canvas(root,bg = 'white')
	# 创建两个同样的rectangle，比较移动前后的不同
	rt1 = cv.create_rectangle(
	    10,10,110,110,
	    tags = "rect")
	cv.create_rectangle(
	    10,10,110,110,
	    tags = "rect")
	# 移动rt1
	cv.move(rt1,20,40)
	cv.pack()
	root.mainloop()
	# move可以指定x,y在相对偏移量，可以为负值

程序运行结果如下: 

![](http://i.imgur.com/JsxPOcD.png)

当然也可以添加工具来控制动画的速度，停止动画，并回复动画




