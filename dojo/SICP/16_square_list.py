def square(x):
    return x*x

def square_list(list):
    if len(list) == 1:
        return [square(list[0])]
    else:
        return [square(list[0])] + square_list(list[1:])

print(square(5))
print(square_list([1,2,3,4]))
