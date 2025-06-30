def is_element(ordered_set, element):
    if not ordered_set:
        return False
    elif ordered_set[0] == element:
        return True
    elif ordered_set[0] > element:
        return False
    else:
        return is_element(ordered_set[1:], element)

#def adjoin_set(element, set):
#    if is_element(set, element):
#        return set
#    else:
#        new_set = []
#        for idx, v in enumerate(set):
#            if element < v and idx == 0:
#              new_set = new_set + [element] + [v]
#            elif element > v and element < set[idx + 1]:
#              new_set = new_set + [v] + [element]
#            else:
#              new_set = new_set + [v]
#        return new_set

def adjoin_set(element, set):
    if not set:
        return [element]
    elif set[0] > element:
        return [element] + set
    elif set[0] == element:
        return set
    else:
        return [set[0]] + adjoin_set(element, set[1:])

def intersection_set(set1, set2):
    if not set1 or not set2:
        return []
    elif set1[0] == set2[0]:
        return [set1[0]] + intersection_set(set1[1:], set2[1:])
    elif set1[0] < set2[0]:
        return intersection_set(set1[1:], set2)
    elif set1[0] > set2[0]:
        return intersection_set(set1, set2[1:])

def union_ordered_list(set1, set2):
	if not set1:
		return set2
	elif not set2:
		return set1
	elif set1[0] < set2[0]:
		return [set1[0]] + union_ordered_list(set1[1:], set2)
	elif set1[0] > set2[0]:
		return [set2[0]] + union_ordered_list(set1, set2[1:])
	elif set1[0] == set2[0]:
		return [set1[0]] + union_ordered_list(set1[1:], set2[1:])

def difference_set(set1, set2):
	if not set1 or not set2:
		return []
	elif set1[0] < set2[0]:
		return [set1[0]] + difference_set(set1[1:], set2)
	elif set1[0] > set2[0]:
		return difference_set(set1, set2[1:])
	elif set1[0] == set2[0]:
		return difference_set(set1[1:], set2[1:])

print("---Ordered Sets!-----")
ordered_set = [1,3,4,5,6,7,8]
print(f"is_element <> {is_element(ordered_set, 5)}")
ordered_set = [1,3,4,5,6,7,8]
print(f"is_element <> {is_element(ordered_set, 9)}")
test = adjoin_set(3, [1, 2, 4, 5])     # → [1, 2, 3, 4, 5]
print(f"Adjoin set: {test}")
test = adjoin_set(4, [1, 2, 3, 4, 5])  # → [1, 2, 3, 4, 5]
print(f"Adjoin set: {test}")
test = adjoin_set(0, [1, 2, 3])        # → [0, 1, 2, 3]
print(f"Adjoin set: {test}")
test = adjoin_set(1, [11,22,33])        # → [0, 1, 2, 3]
print(f"Adjoin set: {test}")
test = intersection_set([], [2, 3, 5, 6])
print(f"Intersection set: {test} == []")
test = intersection_set([1, 3, 4, 6], [2, 3, 5, 6])
print(f"Intersection set: {test} == [3, 6]")
test = union_ordered_list([1,3,5], [2,3,4,5,6])
print(f"Union ordered list: {test}")
set1 = [1, 2, 3, 4, 5]
set2 = [2, 4, 6]
test = difference_set(set1, set2)  # ➞ [1, 3, 5]
print(f"Difference set: {test}")
