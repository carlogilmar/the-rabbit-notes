def is_even(x):
    return x%2==0

def filter_even(list):
    if len(list)==0:
        return []
    elif is_even(list[0]):
        return [list[0]] + filter_even(list[1:])
    else:
        return filter_even(list[1:])


print(filter_even([1,2,3,4,5,6]))
