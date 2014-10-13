'''
delete middle element from a linked list

the trick here is to use a leading pointer that jumps twice for every
node that the cur_node jumps.  When lead_node reaches the end, cur_node
should be right before the middle element
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
        
    def delete_middle(self):
        if self.first_node == None:  # if the list is empty
            return None
        if self.first_node.next == None:    # this is the case of a single node
            self.first_node = None # empty the list
            self.last_node = None
        cur_node = self.first_node  # start at the beginning
        lead_node = self.first_node # seconds pointer to find the end twice as fast
        while lead_node != None and lead_node.next != None: # until lead node or next is end 
            lead_node = lead_node.next  # step forward
            if lead_node.next == None:  # if the next one is None then the length is even
                raise Exception("linked list must have odd length to find middle!")
            lead_node = lead_node.next  # next step
            if lead_node.next == None:  # if the next is None then lead is at the end
                cur_node.next = cur_node.next.next   # set current node to skip the middle
            else: 
                cur_node = cur_node.next    # otherwise step forward
        return None                

# test cases

ll1 = Linked_list()
ll1.add_node(1)
ll1.add_node(2)
ll1.add_node(3)
ll1.add_node(4)
ll1.add_node(5)
ll1.add_node(6)
ll1.add_node(7)

ll2 = Linked_list()
ll2.add_node(1)

ll3 = Linked_list()
ll3.add_node(1)
ll3.add_node(2)

ll1.list_print()
ll1.delete_middle() # should be 123567
ll1.list_print()

ll2.list_print()
ll2.delete_middle() # should empty the list
ll2.list_print()

ll3.list_print()
#ll3.delete_middle()    # should throw an exception
