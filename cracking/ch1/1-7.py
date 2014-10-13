'''
for every 0 in a M x N matrix, replace the corresponding rows and cols with 0
this can be done in place with two loops or with one loop and an extra matrix

1234            0204
0567    -->     0000
8902            0000

'''

def zero(lst):
    M = len(lst)    # height
    N = len(lst[0]) # width, assuming the matrix isn't empty
    zero_rows = set( [] )
    zero_cols = set( [] )
    # first iterate thru to find the rows and cols that have 0's
    for i, row in enumerate(lst):
        for j, n in enumerate(row):
            if n == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    # next set all the corresponding values to 0
    for i in zero_rows:
        for j in range(N):
            lst[i][j] = 0
    for j in zero_cols:
        for i in range(M):
            lst[i][j] = 0
    return True

# nice pretty print for debugging
def pretty_print(lst):
    for i in range(len(lst) ):
        for j in range(len(lst[0]) ):
            print lst[i][j],
        print
    print
    return True

lst1 = [ [1, 2, 3, 4], [0, 5, 6, 7], [8, 9, 0, 2] ]

pretty_print(lst1)
zero(lst1)
pretty_print(lst1)