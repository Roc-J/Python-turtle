class Car:
    def __init__(self,name):
        self.name = name
        print "this is a car"
        print self.name

    def runing(self):
        print "the car is running"

print "create obj do :"
obj = Car("baoma")
print "self do thing"
obj.runing()


