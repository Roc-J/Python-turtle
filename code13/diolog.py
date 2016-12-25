# -*- coding=utf8 -*-
from Tkinter import *
# 引入SimpleDialog模态对话框
from SimpleDialog import *

root = Tk()
# 创建一个SimpleDialog
# buttons:显示的按钮
# default:默认选中的按钮
dlg = SimpleDialog(root,
                   text = '你有未选择的题目！',
                   buttons = ['确定'],
                   default = 0,
                   )
# 执行对话框
dlg.go()
root.mainloop()