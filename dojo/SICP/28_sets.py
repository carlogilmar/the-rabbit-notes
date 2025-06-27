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
        return "No lo es"
    elif list[0] == element:
        return "Es miembro"
    else:
        return is_member2(list[1:], element)


print(f"Member in empty list: {is_member2([], 1)}")
print(f"Member in list: {is_member2([1,2,3,4], 3)}")
print(f"Not Member in list: {is_member2([1,2,3,4], 5)}")
