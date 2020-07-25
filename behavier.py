print("marvellous infosystem")
print("Demonstration of behavier of class")

class Demo:
	def __init__(self):
		self.i=0
		self.j=0
	
	def fun(self):
		print("Inside instance")
		

	@classmethod
	def gun(cls):
		print("Inside class method")

	@staticmethod
	def sun():
		print("Inside static")


obj1=Demo()
obj1.fun()
Demo.gun()
Demo.sun()







