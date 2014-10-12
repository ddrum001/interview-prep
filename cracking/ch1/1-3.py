import unittest

# determine if two string are anagrams of each other

# unit tests
class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_count_char(self):
        self.assertEqual(count_char("abcdaab"), {'a':3, 'b':2, 'c':1, 'd':1})
        self.assertEqual(count_char(""), {})
    
    def test_compare_count(self):
        self.assertEqual(compare_count("abc", "cab"), True)
        self.assertEqual(compare_count("abc", "cb"), False)
        self.assertEqual(compare_count("abc", "aabc"), False)
        self.assertEqual(compare_count("abc", "caba"), False)
        self.assertEqual(compare_count("aabcc", "acabc"), True)
    
    def test_swap(self):
        self.assertEqual(swap("abc", 0, 1), "bac")
        self.assertEqual(swap("abc", 0, 2), "cba")
        self.assertEqual(swap("abcd", 1, 0), "bacd")
        self.assertEqual(swap("abcd", 1, 3), "adcb")

    def test_is_perm(self):
        self.assertEqual(is_perm("", ""), True)
        self.assertEqual(is_perm("", "a"), False)
        self.assertEqual(is_perm("b", ""), False)
        self.assertEqual(is_perm("a", "a"), True)
        self.assertEqual(is_perm("a", "b"), False)
        self.assertEqual(is_perm("ab", "ba"), True)
        self.assertEqual(is_perm("abccde", "ccdbae"), True)
        self.assertEqual(is_perm("abcde", "baace"), False)

def is_perm(s1, s2):
    if len(s1) != len(s2):  # this can be done in O(1) time
        return False
    if not compare_count(s1, s2):   # check if the character counts are the same, meaning it is a scramble
        return False
    else:
        return True
    
# helper function to swap characters in a string at locations i and j
# returns string with swap implemented
def swap(s, i, j):
    if j < i:   # check if j is before i, switch if so
        temp = j
        j = i
        i = temp
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:] 

# helper function to count number of characters in string s
# returns dictionary with characters and corresponding count
def count_char(s):
    counted_chars = {}
    for c in s:
        if c in counted_chars:
            counted_chars[c] += 1
        else:
            counted_chars[c] = 1
    return counted_chars

# helper function to see if character count is the same for two strings s1 and s2
# returns true if the strings have the same letter count, false otherwise
def compare_count(s1, s2):
    s1_count = count_char(s1)
    for c in s2:    
        if c not in s1_count:   # if the characters aren't in the array
            return False    # return False right away
        else:
            s1_count[c] -= 1    # otherwise decrement by one
            if s1_count[c] < 0: # return False immediately if the count goes negative
                return False
    # if the counts are the same, the counts will all be 0 after iterating thru
    # now just check if each value is 0
    for c in s1_count:
        if s1_count[c] != 0:
            return False
    return True

