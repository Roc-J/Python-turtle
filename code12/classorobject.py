class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    def displayEmployee(self):
        print "Name:",self.name,"Salary:",self.salary

emp1 = Employee("xiaoming",4000)
emp2 = Employee("xiaohong",5000)
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount