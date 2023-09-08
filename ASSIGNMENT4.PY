#hybrid inheritance
class School:
	def func1():
		print("This function is in school.")
  
class Student1(School):
	def func2():
		print("This function is in student 1. ")

class Student2(School):
	def func3():
		print("This function is in student 2.")

class Student3(Student1, School):
	def func4():
		print("This function is in student 3.")
  
object = Student3.func1()
object = Student3.func2()
object = Student2.func3()
object = Student3.func4()