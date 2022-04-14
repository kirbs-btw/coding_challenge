def count(txt):
    a = 1
    for i in txt:
        if i == "-":
            a += 1
    return a

"""
def count(txt):
    return txt.count("-") + 1

learned:
there is a count method for patterns inside strings 
"""