'''
given two linked lists conatining digits, return the sum of the digits
for simplicity we assume they're stored in reverse order

    1617    is a linked list 7161
 +   295    is a linekd list 592
 
 should return 
    1912    as a linked list 2191 
    
'''

from linked_list import Node, Linked_list

def add_ll(ll1, ll2):
    cur_node1 = ll1.first_node
    cur_node2 = ll2.first_node
    result = Linked_list()  # used to hold answer without modifying existing ll
                            # alternatively could replace both ll as we iterate
    digit_sum = 0   # used to hold sums for the carry
    while cur_node1 != None or cur_node2 != None:  # while both aren't at the end
        if cur_node1 != None:   # check if the first ll is done
            digit_sum += cur_node1.data # add to the sum
            cur_node1 = cur_node1.next  # step forward
        if cur_node2 != None:   # check if the second ll is done
            digit_sum += cur_node2.data # add to the sum
            cur_node2 = cur_node2.next  # step forward
        result.add_node( digit_sum % 10 )   # add a node with the ones entry of digit_sum
        digit_sum = ( digit_sum - (digit_sum % 10) ) / 10   # remove the one digits, then get the 10s digit
    return result
        
# test case

ll1 = Linked_list()
ll1.add_node(7)
ll1.add_node(1)
ll1.add_node(6)
ll1.add_node(1)

ll2 = Linked_list()
ll2.add_node(5)
ll2.add_node(9)
ll2.add_node(2)

ll3 = Linked_list()

ll1.list_print()
ll2.list_print()
add_ll(ll1, ll2).list_print()   # should return 2191
add_ll(ll2, ll1).list_print()   # should also return 2191
add_ll(ll1, ll3).list_print()   # should work with empty list, return 7161