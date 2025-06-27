def is_member(list, element):
    if not list:
        # Empty list
        return False
    else:
        #List with elements
        for e in list:
            if e == element:
                return True
        return False

def is_member2(list, element):
    if not list:
        return False
    elif list[0] == element:
        return True
    else:
        return is_member2(list[1:], element)

def adjoin_set(list, element):
    if is_member2(list, element):
        return list
    else:
        return [element] + list

# Return a list of elements in both sets
def intersection_set(set1, set2):
    intersections = []
    for e in set1:
        if is_member2(set2, e):
            intersections.append(e)
    return intersections
# [e for e in set1 if is_member2(set2, e)]

def union_set(set1, set2):
    set = list(set1)
    for e in set2:
        if not is_member2(set, e):
            set.append(e)
    return set
# return set1 + [e for e in set2 if not is_member2(set1, e)]

def difference_set(set1, set2):
    set = []
    for e in set1:
        if not is_member2(set2, e):
            set.append(e)

    return set

print(f"Member in empty list: {is_member2([], 1)}")
print(f"Member in list: {is_member2([1,2,3,4], 3)}")
print(f"Not Member in list: {is_member2([1,2,3,4], 5)}")
print("----------------------------------------")
print(f"Add element to the list {adjoin_set([1,2,3], 4)}")
print(f"Don't add element is already in the list {adjoin_set([1,2,3,4,5], 5)}")
print("----------------------------------------")
print(f"Intersection: {intersection_set([1,2,3], [2,3,4])}")
print(f"Intersection: {intersection_set([1,2], [2,3,4,1,5])}")
print("----------------------------------------")
print(f"Union Set: {union_set([1, 2, 3], [2, 3, 4])}")
print(f"Union Set: {union_set([5], [5])}")
print(f"Union Set: {union_set([], [1,2])}")
print("----------------------------------------")
print(f"Difference set: {difference_set([1, 2, 3], [2, 3])}") # → [1]
print(f"Difference set: {difference_set([1, 2, 3], [4, 5])}") #→ [1, 2, 3]
print(f"Difference set: {difference_set([], [1, 2])}")  #      → []
