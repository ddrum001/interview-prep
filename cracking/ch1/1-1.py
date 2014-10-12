def unique_char_dict(s):
    char_seen = {}
    for c in s:
        if c in char_seen:
            return False
        else:
            char_seen[c] = True
    return True

def unique_char(s):
    char_seen = {}
    for c in s:
        if c in char_seen:
            return False
        else:
            char_seen[c] = True
    return True

#unit tests

print unique_char_dict('')
print unique_char_dict('abc')
print unique_char_dict('abb')
