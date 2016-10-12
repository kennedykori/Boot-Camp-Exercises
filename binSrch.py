class BinarySearch(list):
    """This represents a list that can search  for an element using binary search.

    Attributes:
        a: The length of the list to create.
        b: The intervals between elements on the list.
    """

    def __init__(self, a, b):
        super(BinarySearch, self).__init__([])
        current = 1                                                              
        for cnt in range(1, a + 1):                         #   
            current = cnt * b                               # Fill the list as specified by a and b
            self.append(current)                            #
        
        self.count, self.index, self.length, self.ouput = 0, -1, len(self), {"count" : self.count, "index" : self.index}
    
    def search(self, arg):
        first, last, self.ouput["count"], self.ouput["index"] = 0, len(self) - 1, 0, -1

        while first <= last:
            middle = (first + last) // 2
            if self[middle] == arg:
                self.ouput["index"] = BinarySearch.index(self, arg)
                return self.ouput
            elif arg < self[middle]:
                last = middle - 1
            else:
                first = middle + 1

            self.ouput["count"] = self.ouput["count"] + 1

        return self.ouput
