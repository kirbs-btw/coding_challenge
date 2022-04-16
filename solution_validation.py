import re

def validate(txt):
    if not "def" in txt:
        return "missing def"
    if not ":" in txt:
        return "missing :"
    if re.search("[(][)]", txt):
        return "missing param"
    if not "(" in txt and not ")" in txt:
        return "missing paren"
    if not "    " in txt:
        return "missing indent"
    if not "validate" in txt:
        return "wrong name"
    if not "return" in txt:
        return "missing return"
    return True