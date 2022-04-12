def double_letters(txt):
    for i, f in enumerate(txt):
        if i+1 < len(txt) and f == txt[i+1]:
            return True
    return False
