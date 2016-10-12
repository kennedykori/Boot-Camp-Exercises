def find_missing(aList, bList):
	"""Finds the the element that is not present on both lists.
	
	"""
	if len(aList) == 0 and len(bList) == 0:
		return 0

	aList.sort()
	bList.sort()

	if aList == bList:
		return 0

	for x, y in zip(xrange(len(aList)), xrange(len(bList))):
		if aList[x] > bList[y]:
			return bList[y]
		elif bList[y] > aList[x]:
			return aList[x]

	if len(aList) > len(bList):
		return aList[len(aList) - 1]
	else:
		return bList[len(bList) - 1]
    