def consecutive_zeros(txt):
    n = 0
    f = 0
    for i in txt:
        if i == "1":
            n = 0
        else:
            n += 1
            if n > f:
                f = n
    return f