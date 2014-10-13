'''
given a is_substring function, determine is one string is a rotation of the other'
with a single call to the function

the is_substring function is defined below for easy debugging
'''

def is_substring(s1, s2):
    return s1 in s2

# is_rotation("water", "terwa") should return true
# the clever trick here is that the word repeated will always contain
# the correct string in it since you pick up where you leave off
# "terwa" + "terwa" = "terwaterwa" which contains "water"
# "erwat" + "erwat" = "erwaterwat" which also contains "water"

def is_rotation(s1, s2):
    if len(s1) != len(s2):  # check to prevent "to" being rotation of "oto"
        return False
    return is_substring(s1, s2 + s2)
    
print is_rotation("erwat", "water")
print is_rotation("water", "terwa")
print is_rotation("to", "oto")
