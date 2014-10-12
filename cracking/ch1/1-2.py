def reverse(text):
    result = [] # use string buffer to prevent immutable string issue
                # also should look into using bytearray for ascii
    length = len(text)
    for i in range(length):
        result.append(text[length - 1 - i ] )   # need to subtract 1 since indices start at 0
    return "".join(result)  # nifty way to join an array of characters with "" between each entry

print reverse("abc d f e")
print reverse("")
print reverse("a")
print reverse("ab")

