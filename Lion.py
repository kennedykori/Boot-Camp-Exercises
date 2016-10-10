from Cat import Cat
from Roarable import Roarable


class Lion(Cat,Roarable):
	"""Concrete class representing a Lion which is both a cat and can roar."""

	def __init__(self):
		super(Lion, self).__init__()

	def getCatKind(self):
		"""Implements this abstract method from Cat."""
		return self.getCatName()

	def getFurDescription(self):
		"""Implements this abstract method from Cat."""
		return "gold-brown"
