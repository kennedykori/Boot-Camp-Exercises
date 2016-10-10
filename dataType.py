def data_type(arg):
	"""The function "data_type" takes an a single argument "arg" and
	retuns an output that based on the type of arg.

	if arg is:
		a string retuns its length
		None return string "no value"
		a boolean return the boolean
		an integer return a string showing whether its greater than, equal to or less than 100
		a list return the 3rd item or None if it doesn't exist

	"""

	typ = type(arg) # Store type of arg on typ 
	if typ is str:
		return len(arg)
	elif arg is None:
		return "no value"
	elif typ is bool:
		return arg
	elif typ is int:
		if arg < 100:
			return "less than 100"
		elif arg == 100:
			return "equal to 100"
		else:
			return "more than 100"
	elif typ is list:
		if len(arg) >= 3:
			return arg[2]
		else:
			return None
