from Cat import Cat
from Meowler import Meowler
from Purrable import Purrable


class HouseCat(Cat, Meowler, Purrable):
	"""Concrete class representing a HouseCat which is a cat, meowler and is purrable."""

	def __init__(self):
		super(HouseCat, self).__init__()

	def getCatKind(self):
		"""Implements this abstract method from Cat."""
		return "Domestic Cat"

	def getFurDescription(self):
		"""Implements this abstract method from Cat."""
		return "mixed brown and white"
