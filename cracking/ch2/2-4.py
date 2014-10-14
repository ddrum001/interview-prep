'''
given a pivot x and a linked list, change the list to
have all elements < x before the elements >= x

839175 with x=6 should return something like 315879

not that the elements < x and > x still aren't ordered amongst
themseleves, but those less than x are to the left of the rest

this can be done in-place using the crucial step in quicksort:
track two nodes, cur_node that iterates forward and also
first_greater_node that tracks the first node greater than
the elements that are less than x.  When nodes are greater they
stay where they are, but when nodes are < x then they are
swapped with the first_greater_node, which mean the next node
is the new first_greater_node and the pointer should be incremented
'''

class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class Linked_list:
    def __init__(self):
        self.last_node = None
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
        while node:
            print node.data,
            node = node.next
        print
        
    def part_on_pivot(self, x):
        cur_node = self.first_node  # start at the beginning
        first_greater_node = self.first_node
        while cur_node != None: # until at the end
            if cur_node.data < x:   
                cur_node.data, first_greater_node.data = first_greater_node.data, cur_node.data
                first_greater_node = first_greater_node.next    # step forward the first greater node
            cur_node = cur_node.next    # step forward current step
        return None
        
ll1 = Linked_list()
ll1.add_node(8)
ll1.add_node(3)
ll1.add_node(9)
ll1.add_node(1)
ll1.add_node(7)
ll1.add_node(5)

ll1.list_print()
ll1.part_on_pivot(6)
ll1.list_print()
