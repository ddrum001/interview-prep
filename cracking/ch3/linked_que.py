class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class LinkedQue:
    def __init__(self):
        self.first_in = None   # use first_in for deque
        self.last_in = None  # use last_in for enque

    def enque(self, data):
        new_node = Node() # create a new node
        new_node.data = data
        if self.first_in is None: # check if the list was empty
            self.first_in = new_node # if so point first_in to it
            # no need to set new_node.next to None, it does initially
        else:
            self.last_in.next = new_node  # otherwise point the last_node to the new_node
        self.last_in = new_node  # set first_node to the new node

    def deque(self):
        if self.first_in is None: # check if the list was empty
            raise Exception("The queue is empty! Nothing to deque.")
        data = self.first_in.data   # get the data before unlinking
        self.first_in = self.first_in.next   # move first in to the next node in the queue
        return data

    def que_print(self):   # prints queue from first in to last in
        node = self.first_in # starting with the first element in
        while node is not None:
            print node.data,
            node = node.next
        print

# test cases
'''
q1 = LinkedQue()
q1.enque(1)
q1.enque(2)
q1.enque(3)
q1.enque(4)

q1.que_print()  # should print 1234

print q1.deque()  # should print 1
q1.que_print()  # should print 234

q1.enque(5)
print q1.que_print()    # should print 2345
'''