''' 
compress string by replacing repeated characters by the character followed by 
the number of times it repeates, only replacing it if it makes the string shorter
'''

# compress("aaabccd") should return "a3bccd"

def compress(s):
    result = []
    idx = 0
    while idx < len(s):
        c = s[idx]
        count = 1
        while idx < len(s) -1 and s[idx + 1] == c:  # must check to make sure next character exists first
            count += 1
            idx += 1
        result.append(c)
        if count > 2:
            result.append(str(count) )
        elif count == 2:
            result.append(c)
        idx += 1
    return "".join(result)
    
print compress("aaabccd")   # "a3bccd"
print compress("")  # ""
print compress("a") # "a"
print compress("aaabbcddddd")  # "a3bbcd5"
print compress("a     b")   # "a 5b"
