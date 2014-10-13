'''
given a NxN matrix of bytes (image), rotate by 90 degrees
try to do so in-place

010             000
010     ->      111
011             100

'''
# nice pretty print for debugging
def pretty_print(lst):
    for col in range(len(lst) ):
        for row in range(len(lst) ):
            print lst[col][row],
        print
    print
    return True

# start with a version that doesn't perform in-place
def rotate(sqr_lst):
    result = []
    n = len(sqr_lst)
    for col in range(n):
        tmp = []
        for row in range(n):
            tmp.append( sqr_lst[n - 1 - row][col] ) 
            # starting from left to right
            # the new array is made by iterating up thru a column
            # this effectively shifts 90 degrees
        result.append(tmp)
    return result

def rotate_in_place(sqr_lst):
    pass
    '''
    this can be done by shifting each ring around, storing the one entry that
    is being moved temporarily (in constant space storage).  This is repeated
    with each inner layer.  Each element of the outer ring is shifted by
    n-1 spaces. Need to build a function that adds in a clever way: if the row
    is at the max value allowed, then the column starts counting up.  When they're
    both at max_value then row starts decrementing until at some min_value, then
    the col decrements.  After the outer ring is complete, max_value is decremented,
    min_value is incremented, and the amount the value "shifts" decrements by 2
    and this repeats while max_value > min_value.
    '''

sqr_lst1 = [ [0, 1, 0], [0, 1, 0], [0, 1, 1] ]
sqr_lst2 = [ [1, 1, 0], [0, 1, 0], [0, 0, 1] ]

pretty_print(sqr_lst2)
pretty_print(rotate(sqr_lst2) )
