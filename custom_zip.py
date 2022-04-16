def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]


"""
my long solution... 
shorted in my solution above

def zap(a, b):
    arr = []
    for i in range(len(a)):
        arr.append((a[i], b[i]))
    return arr
"""