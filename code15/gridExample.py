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