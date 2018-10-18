from chicken import Chicken
from cat import Cat

class Unknown(Chicken,Cat):
	"""docstring for ClassName"""
	def __init__(self, name, age, height):
		Cat.__init__(self,name, age, height)
		Chicken.__init__(self,name)

