# boiler code from stack overflow for linked list, modified slightly

class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class LinkedList:
    def __init__(self):
        self.last_node = None   # use last_node for constant time insertions
        self.first_node = None

    def add_node(self, data):
        new_node = Node() # create a new node
        new_node.data = data
        if self.first_node == None: # check if its the first node
            self.first_node = new_node 
        else:
            self.last_node.next = new_node   # set the node that cur_node points at to the new node
        self.last_node = new_node #  update the current node to the new one.

    def list_print(self):
        node = self.first_node # starting at the beginning
        count = 0
        while node and count < 30:  # count included to terminate cycles
            print node.data,
            node = node.next
            count += 1
        print

