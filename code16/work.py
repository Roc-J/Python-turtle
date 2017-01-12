from Tkinter import *

class CanvasEventDemo():
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=200, height=200, bg="white")
        self.radius = 50
        self.canvas.bind_all("<Button-1>",self.increseCircle)
        self.canvas.bind_all("<Button-3>", self.decreseCircle)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        mainloop()

    def increseCircle(self,event):
        self.radius = self.radius + 1
        self.clearCanvas()
        self.canvas.create_oval(0, 0, self.radius*2, self.radius*2, fill="red", tags="oval")

    def decreseCircle(self,event):
        self.radius = self.radius - 1
        self.clearCanvas()
        self.canvas.create_oval(0, 0, self.radius*2, self.radius*2, fill="red", tags="oval")

    def clearCanvas(self):
        self.canvas.delete("oval")

CanvasEventDemo()