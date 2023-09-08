#hierarchical inheritance
class Parent:
	def func1():
		print("This function is in parent class.")



class Child1(Parent):
	def func2():
		print("This function is in child 1.")



class Child2(Parent):
	def func3():
		print("This function is in child 2.")
  
obj1 = Child1.func1()
obj1 = Child1.func2()
obj2 = Child2.func1()
obj2 = Child2.func3()
