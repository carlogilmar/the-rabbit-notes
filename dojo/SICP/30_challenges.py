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
