class Car(object):

	def __init__(self, name = None, model = None, typ = None):
		if name == None:
			self.name = "General"
		else:
			self.name = name

		if model == None:
			self.model = "GM"
		else:	
			self.model = model

		if typ == None or typ == "saloon":
			self.type = "saloon"
			self.num_of_wheels = 4
		elif typ == "trailer":
			self.type = "trailer"
			self.num_of_wheels = 8
		else:
			self.typ = typ
			self.num_of_wheels = 4
			
		self.speed = 0

		if self.name == "Koenigsegg" or self.name == "Porshe":
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

	def is_saloon(self):
		if self.type == "saloon":
			return True
		else:
			return False

	def drive(self, shift):
		if shift == 3:
			self.speed = 1000
		elif shift == 7:
			self.speed = 77

		return self
