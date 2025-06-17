def reverse(list):
    if len(list) == 1:
        return list
    else:
        return reverse(list[1:]) + [list[0]] # append element in list [0,2,3] + [1]

print(reverse([1,2,3,4,5]))
