from Lion import Lion
from Cheetah import Cheetah
from HouseCat import HouseCat
from Cat import Cat

if __name__ == "__main__":
	lion = Lion() 			# Create a lion instance.
	cheetah = Cheetah() 	# Create a cheetah instance.
	houseCat = HouseCat()	# Create a houseCat instance.

	#Polymorphism
	print("************************************** Polymorphism **************************************")
	for cat in (lion, cheetah, houseCat):
		print(cat.getCatName() + " is " + cat.getFurDescription())

	#Inheritance
	print("")
	print("************************************** Inheritance **************************************")
	print("HouseCat is a subclass of Cat : ", issubclass(HouseCat, Cat))
	print("houseCat is an instance of Cat : ", isinstance(houseCat, Cat))

	#Encapsulation
	print("")
	print("************************************** Encapsulation **************************************")
	print("Kind of lion is : " + lion.getCatKind())			# self.__name is hidden and has to be called using getCatName()
	print("Name of lion is : " + lion.getCatName())
	print("Kind of cheetah is : " + cheetah.getCatKind())
	print("Name of cheetah is : " + cheetah.getCatName())
