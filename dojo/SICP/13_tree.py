def make_tree(label, left, right):
    return [label, left, right]

def label(tree):
    return tree[0] # label

def left_branch(tree):
    return tree[1]

def right_branch(tree):
    return tree[2]

def count_leaves(tree):
    if not tree: # Empty list
        return 0
    elif not left_branch(tree) and not right_branch(tree):
        return 1
    else:
        return count_leaves(left_branch(tree)) + count_leaves(right_branch(tree))


tree = ["root", ["left", ["left.left", [], []], ["left.right", [], []]], ["right", [], []]]
print(count_leaves(tree))
