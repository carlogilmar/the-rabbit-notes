def pascal_row(n):
    # This block only will happens when n == 0 and that's all friends.
    # No continue from this.
    # Base case to prevent recursion
    if n == 0:
        return ["UNO"] # Beginning

    ### Other number is executed here ------------------- n =4
    prev = pascal_row(n-1) # pascal_row(4-1) -> pascal_row(3-1) --> pascal_row(2-1)

    # Append the start 1
    row = [1] # All rows start with 1

    # range(1,1) -> Don't make an iteration.

    print(prev)
    # This loop is to append the middle values
    for i in range(1, len(prev)):
        row.append(prev[i-1] + prev[i])

    # Append the last 1
    row.append(1)
    return row

print(pascal_row(4))
