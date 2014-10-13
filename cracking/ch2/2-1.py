'''
write code to delete duplicates from an unsorted linked list
ideally without a temporary buffer

this can be done by iterating thru the nodes with current_node pointer and storing the data in a
variable called current_num.  Then a second pointer dup_finder iterates from the current pointer
until it reaches the None.  If it encounters a node where dup_finder.next.data == current_num
then it creates another pointer unique_finder that iterates from dup_finder.next until 
unique_finder.next.data != current_num.  Once it does dup_finder.next is set to unique_finder.next

Since duplicates are removed as current_node iterates forward, there is no need to make multiple passes
'''
import copy # use to create deep copies for easier debugging

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
    
    def delete_dups(self):
        current_node = self.first_node # starting at the beginning
        while current_node != None:
            current_num = current_node.data
            dup_finder = current_node
            while dup_finder != None and dup_finder.next != None: # need to find a better 
                if dup_finder.next.data == current_num:  # if the next is a duplicate
                    unique_finder = dup_finder.next  # set a pointer to the next node
                    while unique_finder.next != None and unique_finder.next.data == current_num:
                        unique_finder = unique_finder.next  # step forward until the next is unique
                    dup_finder.next = unique_finder.next    # set the node dup is pointing to the node after unique 
                dup_finder = dup_finder.next    # step forward                    
            current_node = current_node.next    # step forward


# 1231124 --> 1234

ll1 = Linked_list()
ll1.add_node(1)
ll1.add_node(2)
ll1.add_node(3)
ll1.add_node(1)
ll1.add_node(1)
ll1.add_node(2)
ll1.add_node(4)

ll2 = copy.deepcopy(ll1)    # need deep copy since linked list is a list of pointers
ll3 = Linked_list()

ll1.list_print()
ll1.delete_dups()
ll1.list_print()

ll2.add_node(4)
ll2.list_print()
ll2.delete_dups()
ll2.list_print()

ll3.list_print()    # make sure empty lists don't throw errors
ll3.delete_dups()

