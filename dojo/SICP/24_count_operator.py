def count_operator(exp, op):
    if not isinstance(exp, list):
        return 1 if exp == op else 0
    else:
        return sum(count_operator(e, op) for e in exp)

exp = ['+', 1, 2]
print(f"Expression: {exp} counter: {count_operator(exp, '+')}")
exp = ['+', 'x', ['+', 1, 2]]
print(f"Expression: {exp} counter: {count_operator(exp, '+')}")
exp = ['*', ['+', 1, 2], ['+', 'x', 'x']]
print(f"Expression: {exp} counter: {count_operator(exp, '+')}")

#def count_operator(expr, op):
#    if not isinstance(expr, list):
#        # Base case: it's not a compound expression, so no operators here
#        return 0
#    else:
#        # Check if the operator matches the head of the list
#        head_count = 1 if expr[0] == op else 0
#
#        # Recursively count in the operands (which are usually at index 1 and 2)
#        left = count_operator(expr[1], op)
#        right = count_operator(expr[2], op)
#
#        return head_count + left + right

