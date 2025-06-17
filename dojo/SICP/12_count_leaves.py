

# Count nested elements
def count_leaves(x):
    if not isinstance(x, list):
        return 1
    else:
        return sum(count_leaves(sub) for sub in x) # generator exprssion
        #total = 0
        #for sub in x:
        #    total += count_leaves(sub)
        #return total

def deep_reverse(x):
    if not isinstance(x, list):
        return x
    else:
        return [deep_reverse(sub) for sub in reversed(x)]

print(count_leaves([1, [2, [3, 4, 5, 6, 7]], 8])) # -> 5

print(deep_reverse([1, [2, [3, 4, 5, 6, 7]], 8]))
