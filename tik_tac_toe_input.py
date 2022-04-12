def get_row_col(userInput):
    charArr = "ABC"
    index = 0
    col = int()
    for i in charArr:
        if i == userInput[0].upper():
            col = index
        index += 1

    row = int(userInput[1]) - 1

    return row, col