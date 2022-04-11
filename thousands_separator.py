def format_number(num):
    length = len(str(num))
    rest = length % 3

    newNum = ""
    trippleCount = 0

    for i in str(num):
        if rest > 0:
            newNum += i
            rest -= 1
        elif rest == 0 and (length % 3) != 0:
            rest -= 1
            newNum = newNum + "," + str(i)
            trippleCount += 1
        else:
            if trippleCount == 3:
                trippleCount = 0
                newNum = newNum + "," + str(i)
            else:
                newNum += i
            trippleCount += 1
    return newNum

"""
the easy solution would be:

# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)


"""