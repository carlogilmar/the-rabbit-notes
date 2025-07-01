def find_max(list):
    if len(list) == 1:
        return list[0]
    elif list[0] <= list[1]:
        return find_max(list[1:])
    else:
        sublist = list[1:]
        return find_max([list[0]]+sublist[1:])

def count_occurrences(numbers, element):
    if not isinstance(numbers, list):
        return 1 if numbers == element else 0
    else:
        return sum(count_occurrences(n, element) for n in numbers)

def is_member(collection, element):
    if not collection: # empty list
        return False
    else:
        for e in collection:
            if e == element:
                return True
        return False

def remove_duplicates(collection):
    new_collection = []
    for element in collection:
        if not is_member(new_collection, element):
            new_collection.append(element)
    return new_collection

def erase_duplicates(collection):
    if not collection: # Empty list base case
        return []
    elif is_member(collection[1:], collection[0]):
        return erase_duplicates(collection[1:])
    else:
        return [collection[0]] + erase_duplicates(collection[1:])

def is_prefix(collection1, collection2):
    if not collection1:
        return True
    if not collection2:
        return False
    elif collection1[0] == collection2[0]:
        return is_prefix(collection1[1:], collection2[1:])
    else:
        return False

def deep_reverse(lst):
    # Base Case 1: If it's not a list, return it
    if not isinstance(lst, list):
        return lst

    # Base Case 2: Empty list
    if lst == []:
        return []

    # Recursive Case
    head = lst[0]
    tail = lst[1:]

    reversed_tail = deep_reverse(tail)  # Reverse the tail
    reversed_head = deep_reverse(head)  # Reverse the head in case it's a sublist

    return reversed_tail + [reversed_head]

# ✅ Test cases
print(deep_reverse([1, 2, 3]))            # Output: [3, 2, 1]
print(deep_reverse([1, [2, 3], 4]))       # Output: [4, [3, 2], 1]
print(deep_reverse([[1, 2], [3, [4, 5]]])) # Output: [[[5, 4], 3], [2, 1]]


print(find_max([1,2,3,6,7,8,9]))
print(find_max([1,2,3,6,10,7,8,9]))
print(find_max([10,2,3,6,7,8,9]))

print(count_occurrences([1,2,3,1,4,5,1], 1))
print(count_occurrences([1,1,1,1,1,1,1], 1))

print(is_member([1,2,3,4], 4))
print(is_member([1,2,3,4], 5))

print("Remove Duplicates")
print(remove_duplicates([1,1,1,2,2,2,3,4,5,5]))
print(remove_duplicates([1,2,3,4,5]))
print(remove_duplicates(['a', 'b', 'c', 'd', 'a', 'b', 'c', 'c']))
print(erase_duplicates(['a', 'b', 'c', 'd', 'a', 'b', 'c', 'c']))

print("------------ Is prefix --------- ")
print(f"True: {is_prefix([1,2], [1,2,3,4])}")
print(f"False: {is_prefix([1,3], [1,2,3,4])}")
print(f"True: {is_prefix([], [1,2,3,4])}")
print(f"False: {is_prefix([1,2], [])}")
