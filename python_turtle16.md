## 事件和回调 ##  
### 代码访问GitHub： ###
* 命令绑定 将简单的组件绑定到function函数上
* 如果需要处理参数的话，使用lambda函数  
* 事件绑定可以使用 widget.bind(事件，回调)方法将键盘和鼠标的事件响应绑定到窗口小组件上，并在发生某些事件时调用回调的事件绑定。  
* 如何传递额外的参数到一个callback
* 怎样将事件绑定到整个应用程序或特定类的窗口小部件（通过使用bind_all()和bind_class())

### 给程序添加生命 ###
小部件功能响应函数 包括按下按钮，鼠标点击等事件，这需要将回调关联到特定事件。  

### 命令绑定 ###
最简单方式来增加函数方法到一个按钮称作command binding从而回调函数以command=some_callback形式提到窗口小部件  

举一个简单的例子来进行简单的实例

	def my_callback():
		# do something 
	Button(root,text="Click",command=my_callback())

### 传递参数到回调 ###
如果回调需要一些参数，我们可以使用lambda函数：  

	def my_callback(somearg):
		# do something with argument
	
	Button(root,text="Click",command=lambda:my_callback('some argument'))

### 事件绑定 ###
Tkinter提供一种称为bind()的事件绑定机制的替代形式来处理不同的事件，绑定事件的标准语法如下:  

widget.bind(event,handler)
下面举一个例子来详细的说明

	from Tkinter import *
	
	root = Tk()
	Label(root,text='Click at different \n locations in the frame below').pack()
	def callback(event):
	    print dir(event)
	    print "you clicked at",event.x,event.y
	
	myframe = Frame(root,bg='khaki',width=130,height=80)
	myframe.bind("<Button-1>",callback)
	myframe.pack()
	
	root.mainloop()

程序说明：  
（1）程序生成一个窗口root，pack()一个标签Label  
（2）生成一个Frame放置在root上，并进行属性的设置，并将该frame绑定一个函数callback  
（3）callback函数将显示event下的dir目录和输出一句话。

### 事件模式 ###
* <Button-1> 鼠标左击
* <Button-2> 鼠标按钮中建点击
* <Button-3> 鼠标右击
* <KeyPress-B> 键盘按键B
* <Alt-Control-KeyPress-KP_Delete> 键盘按下Alt+Ctrl+Delete  

事件          属性说明  
char    从键盘输入的字符，用于键事件    
keycode 从键盘为键事件输入的键的键代码（即Unicode)  
keysym  从键盘输入的键的键符号（即字符)，用于键事件。  
num     按钮编号(1,2,3)表示单击了哪个鼠标按钮。  
widge   触发此事件的widget对象  
x and y 窗口小部件中当前的鼠标位置(以像素为单位)  
x\_\_root and y\_\_root 当前鼠标相对于屏幕上左上角的位置，以像素为单位  

### 事件绑定的公共操作 ###

widget.bind("<Button-1>",callback) # 将widget组件绑定到鼠标左击  
widget.bind("<Button-2>",callback) # 绑定到鼠标右击  
widget.bind("<Return>",callback) # 绑定到Return(Enter)Key  
widget.bind("<FocusIn>",callback) # 绑定Focus
widget.bind("<KeyPress-A>",callback) # 绑定键盘A键  
widget.bind("<KeyPress-Caps_Lock>",callback) #绑定CapsLockkeysym  
widget.bind("<KeyPress-F1>",callback) # 绑定widget到F1  
widget.bind("<KeyPress-KP_5>",callback) #绑定keypad 数字5  
widget.bind("Motion",callback) #bind to motion over widget  
widget.bind("<Any-KeyPress>",callback) #绑定到任意键  

### 绑定的级别 ###
#### application-level binding ####
application-level绑定的语法是  
w.bind_all(event,callback)  
典型的使用如下:  
root.bind_all('<F1>',show_help)  

#### class-level binding ####
class level绑定的语法是  
w.bind_class(className,event,callback)

典型的使用如下:  
myentry.bind_class('Entry','<Control-V>',paste)