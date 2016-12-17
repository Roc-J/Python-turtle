class Parent:
    parentAttr = 200
    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print "running parent method"

    def setAttr(self,attr):
        self.parentAttr = attr

    def getAttr(self):
        print "Get parent attribute:",self.parentAttr

class Child(Parent):
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print "running child method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(500)
c.getAttr()