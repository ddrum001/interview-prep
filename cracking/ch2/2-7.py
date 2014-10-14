'''
write a function that checks if a linked list is a palindrome

I use a stack (made from linked lists) to keep track of the first half of the 
linked list in reversed form
'''

from linked_list import Node, LinkedList
from stacked_list import StackedList

def is_palindrome(ll):
    fast = ll.first_node    # traverses twice as fast for finding the middle node
    slow = ll.first_node    # normal iterator
    first_half_reversed = StackedList()
    while fast is not None and fast.next is not None:   # check to see if two steps are possible
        fast = fast.next.next   # two steps forward
        first_half_reversed.push(slow.data) # push data to stack in reversed order
        slow = slow.next    # step forward
    if fast is not None:    # check if list length is odd (if so two steps will land on None)
        slow = slow.next    # step once to skip middle node
    while slow is not None: # step forward until the end
        if slow.data != first_half_reversed.pop():  # check if first half matches second half
            return False
        slow = slow.next
    return True

# test cases

ll1 = LinkedList()
ll1.add_node('a')
ll1.add_node('b')
ll1.add_node('b')
ll1.add_node('a')

ll2 = LinkedList()
ll2.add_node('a')
ll2.add_node('b')
ll2.add_node('c')
ll2.add_node('b')
ll2.add_node('a')

ll3 = LinkedList()
ll3.add_node('a')
ll3.add_node('b')
ll3.add_node('c')
ll3.add_node('d')
ll3.add_node('b')

print is_palindrome(ll1)    # should return True
print is_palindrome(ll2)    # should return True
print is_palindrome(ll3)    # should return False



ll2.add_node('b')
ll2.add_node('b')
ll2.add_node('a')
        
    