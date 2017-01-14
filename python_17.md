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

