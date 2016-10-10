from abc import ABCMeta, abstractmethod


class Cat(object):
	"""This represents an abstract Cat containing default methods common to all cats."""

	__metaclass__ = ABCMeta

	def __init__(self):
		super(Cat, self).__init__()
		self.__name = self.__class__.__name__

	@abstractmethod
	def getCatKind(self):
		"""This method should return a string that details the kind of cat."""
		pass

	@abstractmethod
	def getFurDescription(self):
		"""Should return a string that details the fur of the given cat."""
		pass

	def getCatName(self):
		"""Returns the name of the cat."""
		return self.__name

	def growl(self):
		"""Used to make the cat growl."""
		print("Grrrowl!!")

	def walk(self):
		"""Used to make the cat walk."""
		print(self.__name + " is walking.")

	def eat(self):
		"""Makes the cat eat."""
		print(self.__name + " is eating.")

	def sleep(self):
		"""Makes the cat sleep."""
		print(self.__name + " is sleeping.")
