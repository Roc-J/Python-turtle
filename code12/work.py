from Tkinter import *

window = Tk()

text = Label(window,text="Students' Answers to the Questions:")
text.pack()

canvasmid = Canvas(window, width = 500, height = 250)
canvasmid.pack()

canvas = Canvas(canvasmid, width = 250, height = 250)
canvas2 = Canvas(canvasmid, width = 250, height = 250)

textstu = [
"          ","studnet0  ","studnet1  ","studnet2  ","studnet3  ","studnet4  ","studnet5  ","studnet6  ","studnet7  "
]
for item in textstu:
    labelstu = Label(canvas2,text=str(item))
    labelstu.pack()

canvas2.pack(side=LEFT)
canvas.pack(side=RIGHT)

label0 = Label(canvas,text="0 1 2 3 4 5 6 7 8 9")
label0.pack()
studentScore = [
    ['A','B','A','C','C','D','E','E','A','D'],
    ['D','B','A','C','C','D','E','E','A','D'],
    ['E','B','A','C','C','D','E','E','A','D'],
    ['C','B','A','C','C','D','E','E','A','D'],
    ['A','B','A','C','C','D','E','E','A','D'],
    ['B','B','A','C','C','D','E','E','A','D'],
    ['B','B','A','C','C','D','E','E','A','D'],
    ['B','B','A','C','C','D','E','E','A','D'],
]
for scoreitem in studentScore:
    strtext = ""
    for item in scoreitem:
        strtext = strtext + str(item)+" "
    labelitem = Label(canvas,text=strtext,bg='lightblue')
    labelitem.pack()

textanswer = Label(window,text="The key is stored in a one-dimensional list:")
textanswer.pack()

bottom = Canvas(window, width = 500, height = 150)
bottom.pack()
key_label = Label(bottom,text="Key")
key_label.pack(side=LEFT)

answer = Canvas(bottom, width = 500, height = 150)
answer.pack(side=RIGHT)
key1 = Label(answer,text="0 1 2 3 4 5 6 7 8 9")
key2 = Label(answer,text="D B D C C D D E A D",bg="lightblue")
key1.pack()
key2.pack()
window.mainloop()
