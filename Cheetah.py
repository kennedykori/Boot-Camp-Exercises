from Cat import Cat
from Purrable import Purrable


class Cheetah(Cat, Purrable):
	"""Concrete class representing a Cheetah which is both a cat and purrable."""

	def __init__(self):
		super(Cheetah, self).__init__()

	def getCatKind(self):
		"""Implements this abstract method from Cat."""
		return self.getCatName()

	def getFurDescription(self):
		"""Implements this abstract method from Cat."""
		return "spotted"
