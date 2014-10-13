'''
write a function to return the kth to last element

use two pointers one that lags by k elements
first iterate the cur_node k times from the starting node
if it reaches the end, raise an exception
otherwise iterate both cur_node and lag_node forward until cur_node.next == None
and return the data of lag_node
'''
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def test(self):
        self.assertEqual(ll1.kth_from_last(1), 7)
        self.assertEqual(ll1.kth_from_last(2), 6)
        self.assertEqual(ll1.kth_from_last(7), 1)
#        self.assertRaises(Exception, kth_from_last(8), ll1 )

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
        
    def kth_from_last(self, k):
        cur_node = self.first_node  # starting at the beginning
        lag_node = self.first_node
        for i in range(k):
            if cur_node == None:    # check to make sure you're not at the end
                raise Exception("k can't be larger than the list!")
            cur_node = cur_node.next    # otherwise step forward
        while cur_node != None: # until cur_node is at the end
            cur_node = cur_node.next    # move each of them forward 
            lag_node = lag_node.next
        return lag_node.data

ll1 = Linked_list()
ll1.add_node(1)
ll1.add_node(2)
ll1.add_node(3)
ll1.add_node(4)
ll1.add_node(5)
ll1.add_node(6)
ll1.add_node(7)

ll2 = Linked_list()
        