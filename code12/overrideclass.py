class Parent:
    def __init__(self):
        print "create a parent object"

    def myMethod(self):
        print "this is parent method"

class Child(Parent):
    def __init__(self):
        print "create a child object"

    def myMethod(self):
        print "this is child method"

c = Child()
c.myMethod()