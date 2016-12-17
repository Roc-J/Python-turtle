## 测验 ##
一个允许用户更改标签的颜色，字体和文本的程序  

### 变量类 ###
一些小部件（如文本输入小部件，单选按钮等）可以通过使用特殊选项直接连接到应用程序变量：variable,textvariable,onvalue,offvalue和value  

此链接以两种方式工作   
如果变量因任何原因而改变，则它所连接的窗口部件将被更新以反映新值。  

x= StringVar() 保存字符串，默认为""  
x= IntVar() 保存整数，默认是0  
x= DoubleVar() 保存浮点型，默认是0.0  
x=BooleanVar() 保存布尔型，返回0是False，返回1是True 

要读取上述变量的当前值，可以调用get()。这种变量的值可以通过set()方法更改  

### 我们可以使用Canvas窗口小部件显示形状 ###

可以通过创建方法create_oval，create_arc，create_polygon或create_line在画布上绘制矩形，椭圆形，弧形，多边形或线。

	from Tkinter import *
	
	class CanvasDemo:
	    def __init__(self):
	        wn = Tk()
	        wn.title("Canvas Demo")
	        self.canvas = Canvas(wn,width=200,height=100,bg="white")
	        self.canvas.pack()
	
	        frame = Frame(wn)
	        frame.pack()
	
	        btRectangle = Button(frame,text="Rectangle",command=self.displayRect)
	        btOval = Button(frame,text="Oval",command=self.displayOval)
	        btArc = Button(frame,text="Arc",command=self.displayArc)
	        btPolygon = Button(frame, text="Polygon", command=self.displayPolygon)
	        btLine = Button(frame, text="Line", command=self.displayLine)
	        btString = Button(frame, text="String", command=self.displayString)
	        btClear = Button(frame,text="Clear",command=self.clearCanvas)
	
	        btRectangle.grid(row=1,column=1)
	        btOval.grid(row=1, column=2)
	        btArc.grid(row=1, column=3)
	        btPolygon.grid(row=1, column=4)
	        btLine.grid(row=1, column=5)
	        btString.grid(row=1, column=6)
	        btClear.grid(row=1, column=7)
	
	        mainloop()
	
	    def displayRect(self):
	        self.canvas.create_rectangle(10,10,190,90,tags="rect")
	
	    def displayOval(self):
	        self.canvas.create_oval(10,10,190,90,fill="red",tags="oval")
	
	    def displayArc(self):
	        self.canvas.create_arc(10,10,190,90,start=0,extent=90,width=8,fill="red",tags="arc")
	
	    def displayPolygon(self):
	        self.canvas.create_polygon(10,10,190,90,30,50,tags="polygon")
	
	    def displayLine(self):
	        self.canvas.create_line(10,10,190,90,fill="red",tags="line")
	        self.canvas.create_line(10,90,190,10,width=9,arrow="last",activefill="blue",tags="line")
	
	    def displayString(self):
	        self.canvas.create_text(60,40,text="Hi,I am a string",font="Times 10 bold underline",tags="string")
	
	    def clearCanvas(self):
	        self.canvas.delete("rect","oval","arc","polygon","line","string")
	
	CanvasDemo()


程序说明:   
1. 在类的初始化中，声明了一个canvas和一个frame，分别将这两个放置在窗口上   
2. 在初始化中，定义了七个按钮，用来创建不同的形状，将这七个按钮放置在frame中  
3. 定义了七个函数，分别对应七个按钮的command，而将绘图的结果显示在canvas  

![](http://i.imgur.com/pfMktpy.png)

### Tkinter 坐标系 ###

![](http://i.imgur.com/AhIaGFT.png)


### 绘图坐标   ###

![](http://i.imgur.com/CTOWhjQ.png)