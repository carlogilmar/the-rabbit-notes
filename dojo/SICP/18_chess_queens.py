def is_safe(col, queens):
    row = len(queens)
    for r, c in enumerate(queens):
        if c == col or abs(c -col) == abs(row-r):
            return False
    return True

print(is_safe(0, [2,6,1,7,2,4,6,7]))
