def fizz_buzz(arg):
	"""This function returns 'Fiz', 'Buz', 'FizzBuzz' or the argument it receives,
	all depending on the argument of the function. If the argument is divisible by 3,
	it returns 'Fiz', if the argument is divisible by 5, it returns 'Buzz', if the 
	argument is divisible by both 3 and 5, it returns 'FizzBuzz', else it returns the 
	argument itself.

	Attributes:
		arg: The argument to be evaluated.
	"""
	db3 = (float(arg)/3.0).is_integer() #db3: boolean which is true if the is divisible by 3.
	db5 = (float(arg)/5.0).is_integer() #db5: boolean which is true if arg is divisible by 5.

	if db5 and db3:
		return "FizzBuzz"
	elif db3:
		return "Fizz"
	elif db5:
		return "Buzz"
	else:
		return arg
