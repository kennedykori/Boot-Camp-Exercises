class Purrable(object):
	"""This represents the behavior of some cats that purr using the default method purr."""

	def __init__(self):
		super(Purrable, self).__init__()

	def purr(self):
		"""Makes the cat purr."""
		print("Purrrrrrr...")
