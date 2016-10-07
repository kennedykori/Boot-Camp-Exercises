#Fibonacci serries:
#The sum of the two eleemnts defines the next
def fibonacci(size):
	a, b, fibSeries = 0, 1, []
	while len(fibSeries) < size:
		fibSeries.append(b)
		a, b = b, a + b

	return fibSeries
