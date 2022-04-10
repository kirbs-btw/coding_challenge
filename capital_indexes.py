def capital_indexes(txt):
    charSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr = []
    for i, f in enumerate(txt):
        if f in charSet:
           arr.append(i)
    return arr

"""
learned:
enumerate function

for i, f in enumerate(txt)
--> i = index of the item 
--> f = item value = txt[i]
"""