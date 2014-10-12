# replace spaces with %20

def replace_spaces(s):
    result = []
    for c in s:
        if c == ' ':
            result.append('%20')
        else:
            result.append(c)
    return "".join(result)
    
print replace_spaces("hello world") # should print "hello%20world"

"""
this approach takes a single pass n steps with O(n) additional space to create
the new array.  This could be done in place with a low level language like
C++ if we used pointers
"""