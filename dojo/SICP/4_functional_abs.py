def sum_of(f, a, b):
    result = 0
    for x in range(a, b + 1):
        result += f(x)
    return result

# Sum of squares from 1 to 3: 1² + 2² + 3² = 14
print(sum_of(lambda x: x * x, 1, 3))

# Sum of identities (just 1 + 2 + 3)
print(sum_of(lambda x: x, 1, 3))
