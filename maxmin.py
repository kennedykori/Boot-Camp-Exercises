def find_max_min(data):
	data = sorted(data)        			# Sort the list

	output = []							# Create list to return 
	if data[0] == data[len(data) - 1]:	# Check if max and min are equal
		output.append(len(data))		# Store size of input list to output and return output if max and min are equal
		return output

	output.append(data[0]) 				# Store the min element in output.
	output.append(data[len(data) - 1])	# Store the max element in output.

	return output
