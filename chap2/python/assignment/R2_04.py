"""
R-2.4(p.103)

Write a Python class, Flower, that has 3 instance variable of type str,
int, and float, that respectively represent the name of the flower, its
number of petals, and its price. Your class must include a constructor
method that initializes each variable an appropriate value, and your
class should include methods for setting the value of each type, and
retrieving the value of each type.
"""

class Flower:
	def __init__(self, name: str, num_petals: int, price: float):
		self._name = name
		self._petals = num_petals
		self._price = price
	
	# Accessors
	def get_name(self):
		return self._name

	def get_petals(self):
		return self._petals

	def get_price(self):
		return self._price
	
	# Mutators
	def set_name(self, new_name: str):
		self._name = new_name

	def set_petals(self, new_num_petals: int):
		self._petals = new_num_petals
	
	def set_price(self, new_price: float):
		self._price = new_price
