def count_symbol(expr, target):
    if not isinstance(expr[0], list):
        return 1 if expr == target else 0
    else:
        return sum(count_symbol(part, target) for part in expr)

print(count_symbol(['+', 'x', ['*', 'x', 2]], 'x'))# → 2


