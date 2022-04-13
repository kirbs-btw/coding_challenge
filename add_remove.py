import re

def add_dots(txt):
    a = ""
    for i in txt:
        a += "." + i
    return a[1:]

def remove_dots(txt):
    return re.sub("[.]", "", txt)
