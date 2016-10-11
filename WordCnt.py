def words(data):
	if type(data) is not str:
		raise ValueError("Input provided must be a string.")
	
	l_data = data.split() 					#Split the string and store the resulting list in l_data.
	
	output = {}           					#The dict where the out put is stored.
	for word in l_data:
		if word.isdigit():  				#Check if word is a number and the convert it to a number.
			word = int(word)
		try:
			output[word] = output[word] + 1 #increament the current number of words.
		except KeyError:
			output[word] = 1      			#append new word at the end of the dictionary

	return output
