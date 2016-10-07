def primeNumbers(n):
	i, primeN = 1, []
	for x in range (1, (n + 1), 1):
	    c = 0
	    for j in range (1, (i + 1), 1):
	        a = i % j
	        if (a == 0):
	            c = c + 1

	    if (c == 2):
	          primeN.append(i)
	    else:
	          x = x - 1

	    i = i + 1

	return primeN
