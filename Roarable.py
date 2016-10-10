class Roarable(object):
	"""This represents the behavior of some cats that roar using the default method roar."""

	def __init__(self):
		super(Roarable, self).__init__()

	def roar(self):
		"""Makes the cat roar."""
		print("Roar!!")
		