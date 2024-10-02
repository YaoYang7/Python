class Element:
    """ A key, value and index. """
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __str__(self):
        return str(self._key) + " " + str(self._value) + " " + str(self._index)

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None


class AdaptablePriorityQueueList:
    def __init__(self):
        self._body = []  
        self._size = 0        

    def __str__(self):
        return str([str(elt) for elt in self._body])
    
    def len(self):
        return len(self._body)
    
    def add(self,key,item):
        elt = Element(key,item,len(self._body))
        self._body.append(elt)
        self._size += 1
        return elt
    
    def min(self):
        minimum = self._body[0]
        for elt in self._body:
            if elt._key < minimum._key:
                minimum = elt
        return minimum

    def remove_min(self):
        m = self.min()
        self._body[m._index], self._body[-1] = self._body[-1], self._body[m._index]
        self._body[m._index]._index, self._body[-1]._index = self._body[-1]._index, self._body[m._index]._index
        self._body.pop()
        #print(f"removing (  {self._body.pop()}  )")
        self._size -= 1
        return (m._key,m._value)
        

    def update_key(self,element, new_key):
        self._body[element._index]._key = new_key

    def get_key(self,element):
        return self._body[element._index]._key

    def remove(self,element):
        self._body[element._index], self._body[-1] = self._body[-1], self._body[element._index]
        self._body[element._index]._index, self._body[-1]._index = self._body[-1]._index, self._body[element._index]._index
        print(f"removing (  {self._body.pop()}  )")      
    
    def isEmpty(self):
        if self._size == 0:
            return True
        else: 
            return False 
        
    def length(self):
        return self._size
    


if __name__ == "__main__":
    q = AdaptablePriorityQueueList()
    item1 = q.add(2,"Dog")
    item2 = q.add(4,"Cat")
    item3 = q.add(6, "Tiger")
    print(q.len())
    print(q)
    print(item1)
    q.remove_min()
    print(q)
    q.update_key(item2,1)
    print(q)
    print(q.get_key(item2))
    q.remove(item3)
    print(q)