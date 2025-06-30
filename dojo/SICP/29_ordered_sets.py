def is_element(ordered_set, element):
    if not ordered_set:
        return False
    elif ordered_set[0] == element:
        return True
    elif ordered_set[0] > element:
        return False
    else:
        return is_element(ordered_set[1:], element)

def adjoin_set(set, element):
    return set

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
