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
        return str(self._key) + " " + str(self._value) + " " + str(self._index) + " "

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

class AdaptablePriorityQueueHeap:
    def __init__(self):
        self._body = []
        self._size = 0

    def __str__(self):
        """ Return a breadth-first string of the values. """
        # method body goes here
        ans = ""
        for i in self._body:
            ans += "k"+str(i._key) + " " + "i"+str(i._index) + " " + "v"+str(i._value) + " "
        return ans

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
        # method body goes here
        elt = Element(key,value,self._size)
        self._body.append(elt)
        self._upheap(self._size)

        self._size += 1
        return elt

    def min(self):
        """ Return the min priority key,value. """
        # method body goes here
        if self._body:
            return self._body[0]
        else:
            return "None"

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        # method body goes here
        if self._body:
            output = self._body[0]
            if self._size > 1:
                self._body[0] = self._body.pop()
                self._body[0]._index = 0
                if self._size > 1:
                    self._size -= 1
                    self._downheap(0)
            else:
                self._size -= 1
                self._body.pop()
            return (output._key,output._value)
        else:
            return "None"

    def update_key(self,element, new_key):

        if element._key < new_key:
            element._key = new_key
            self._downheap(element._index)
        else:
            element._key = new_key
            self._upheap(element._index)

    def get_key(self,element):
        return self._body[element._index]._key

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def length(self):
        return self._size

    def _upheap(self, posn):
        """ Bubble the item in posn in the heap up to its correct place. """

        item = self._body[posn]
        current_position = posn
        while True:
            parent_position = (current_position - 1) // 2
            if parent_position < 0:
                break
            else:
                if item._key < self._body[parent_position]._key:
                    self._body[current_position], self._body[parent_position] = self._body[parent_position], self._body[current_position]
                    self._body[current_position]._index, self._body[parent_position]._index = self._body[parent_position]._index, self._body[current_position]._index
                    current_position = parent_position
                else:
                    break


    def _downheap(self, posn):
        """ Bubble the item in posn in the heap down to its correct place. """

        current_position = posn
        while True:
            children = [current_position*2+1,current_position*2+2]
            if children[0] >= self._size:
                children[0] = None
            if children[1] >= self._size:
                children[1] = None

            if children[0] and not children[1]:
                min_child = children[0]
            elif children[1] and not children[0]:
                min_child = children[1]
            elif not children[0] and not children[1]:
                break
            else:
                d = {children[0]: self._body[children[0]]._key,children[1]: self._body[children[1]]._key}
                min_child = min(d, key=lambda k: d[k])

            if self._body[current_position]._key > self._body[min_child]._key:
                self._body[current_position], self._body[min_child] = self._body[min_child], self._body[current_position]
                self._body[current_position]._index, self._body[min_child]._index = self._body[min_child]._index, self._body[current_position]._index
                current_position = min_child
            else:
                break
    



def testadd():
    print('Testing that we can add items to an array-based binary heap PQ')
    pq = AdaptablePriorityQueueHeap()
    print('pq has size:', pq.length(), '(should be 0)')
    a = pq.add(25,25)
    b = pq.add(4, 4)
    print('pq has size:', pq.length(), '(should be 2)')
    print(pq, '(should be 4,25, could also show index and value)')
    c = pq.add(19,19)
    d = pq.add(12,12)
    print(pq, '(should be 4,12,19,25)')
    e = pq.add(17,17)
    f = pq.add(8,8)
    print(pq, '(should be 4,12,8,25,17,19)')
    print('pq length:', pq.length(), '(should be 6)')
    print('pq min item:', pq.min(), '(should be 4)')
    print()
    print(pq)
    pq.update_key(c,1)
    pq.update_key(b,40)
    print(pq)


    return pq


if __name__ == "__main__":
    testadd()
