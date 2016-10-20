class node:
    def __init__(self, data):
        self._data = data
        self._next = None
    
    def set_next(self, n):
        self._next = n

    def get_next(self):
        return self._next
    
    def data(self):
        return self._data

class linked:
    def __init__(self):
        self.head = None

    def append(self, data):
        ptr = self.head

        # if list is empty
        if ptr is None:
            # set the head to a new node
            self.head = node(data)
            return

        # traverse the list to the last item
        while ptr.get_next() is not None:
            ptr = ptr.get_next()
        # make a new last item, creating a new node
        ptr.set_next( node(data) )

    def print_contents(self):
        ptr = self.head
        
        # if list is empty, exit
        if ptr is None:
            return
        
        # otherwise, print each piece of data and traverse
        # until you're at the last node
        while ptr._next is not None:
            print ptr.data()
            ptr = ptr._next
        # but don't forget to print that last node
        print ptr.data()
