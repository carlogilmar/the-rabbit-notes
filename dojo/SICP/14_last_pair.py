def last_pair(list):
    if len(list) == 1:
        return list[0]
    else:
        return last_pair(list[1:]) # [1:] tail of the list

def second_to_last(list):
    if len(list) == 2:
        return list[0]
    else:
        return second_to_last(list[1:])

def first_even(list):
    if list[0] % 2 == 0:
        return list[0]
    else:
        return first_even(list[1:])

print(last_pair([10,20,1,3])) # 3
print(second_to_last([10,20,1,100,99,3])) # 3

print(first_even([1,1,3,3,6,8,1]))
