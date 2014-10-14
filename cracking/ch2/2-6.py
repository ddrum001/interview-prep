'''
given a linked list with a cycle in it, find the first node of the cycle

ABCDEC should return C

this is really tricky.  The trick is that the number of steps needed to 
visit every node, L, in the list is the number of steps in the cycle, C, plus the
number of steps before the cycle, B.  In algebra L = B + C, or B = L - C

hard to explain without pictures

find when the fast pointer catches the slow, in a cycle they will always meet and
there will always be C steps between their meetings since the slow one traverse C steps in
the time that the fact one traverses 2C steps.  

They actually will meet at the first multiple of C that is greater than B.

When they do meet at step C, there are L - C steps until the slow one visits every node,
which is when it will enter into a cycle again.  Since L - C  = B, we can start another
pointer from the very beginning once the fast == slow, and once slow == third
they will be at the first node of the cycle.
'''

from linked_list import Node, LinkedList

def find_cycle_start(ll):
    slow = ll.first_node
    fast = ll.first_node
    node_finder = ll.first_node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    while slow != node_finder:
        slow = slow.next
        node_finder = node_finder.next
    return node_finder.data

ll1 = LinkedList()
ll1.add_node('A')
ll1.add_node('B')
ll1.add_node('A')
ll1.add_node('B')
ll1.add_node('C')
cycle_node = ll1.last_node
ll1.add_node('D')
ll1.add_node('E')
ll1.add_node('D')
ll1.add_node('E')
ll1.add_node('D')
ll1.add_node('E')
ll1.add_node('D')
ll1.add_node('E')
ll1.add_node('D')
ll1.add_node('E')
ll1.add_node('D')
ll1.add_node('E')
ll1.add_node('D')
ll1.add_node('E')
ll1.last_node.next = cycle_node

ll1.list_print()

print find_cycle_start(ll1)
