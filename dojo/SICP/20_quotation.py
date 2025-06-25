#def pretty_print(args):
#    if not isinstance(args[1], list):
#      return f"({args[1]} {args[0]} {args[2]})"
#    else:
#      return f"( {pretty_print(args[1])} {args[0]} {pretty_print(args[2])} )"
#
#print(pretty_print(['/', ['*', 'x', 2], ['+', 1, 1]])) # Output: ((x * 2) / (1 + 1))
#print(pretty_print(['/', ['*', 'x', ['+', 1, 2]], ['+', 1, 1]])) # Output: ((x * 2) / (1 + 1))

def pretty_print2(expr):
    # Base case: if it's not a list, it's a symbol or number
    if not isinstance(expr, list):
        return str(expr)

    # Recursive case: it's a compound expression
    operator = expr[0]
    left = expr[1]
    right = expr[2]

    # Recursively pretty print left and right operands
    left_str = pretty_print2(left)
    right_str = pretty_print2(right)

    return f"({left_str} {operator} {right_str})"

print(pretty_print2(['-', ['*', 'x', 2], 1]))
print(pretty_print2(['-', ['*', 'x', 2], ['+', 4, ['-', 10, 1]]]))
