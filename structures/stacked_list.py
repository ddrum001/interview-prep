class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class StackedList:
    def __init__(self):
        self.top_node = None

    def push(self, data):
        new_node = Node() # create a new node
        new_node.data = data
        new_node.next = self.top_node # point the new data to the current top
        self.top_node = new_node   # set the top to the new node
 
    def peek(self):
        if self.top_node is None:
            raise Exception("Stack is Empty...no peeking")
        return self.top_node.data
        
    def pop(self):
        if self.top_node is None:
            raise Exception("Stack is Empty already")
        data = self.top_node.data    # get top data
        self.top_node = self.top_node.next  # resets top to be the next node
        return data
    
    def stack_print(self):   # print the stack with the left most element as the top
        node = self.top_node # starting at the top
        while node is not None:
            print node.data,
            node = node.next
        print

# test the stack

s1 = StackedList()
s1.push(3)
s1.push(2)
s1.push(1)
s1.stack_print()    # should print 123
print s1.pop()    # should print 1
s1.stack_print()    # should print 23
print s1.peek() # should print 2
s1.push(4)
s1.stack_print()    # should print 423

