## 面向对象python/Tkinter ##
通过一个程序来说明：
	
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


程序说明:  
1. 定义了一个员工类Employee  
2. 类中定义了一个类变量empCount，这个变量记录的是员工的数量，每生成一个类的对象，该值就会增加1  
3. 初始化函数中初始化了姓名和工资  
4. 定义了displayCount()函数显示了员工的数量  
5. 定义了displayEmployee()函数显示了对象的信息