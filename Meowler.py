class Meowler(object):
	"""This represents the behavior of some cats that meow using the default method meow."""
	
	def __init__(self):
		super(Meowler, self).__init__()

	def meow(self):
		"""Makes the cat meow."""
		print("MeeeeOww!")