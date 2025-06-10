# Evaluation
def square(x):
    return x * x

print(square(2))  # 4
print(square(5))  # 25

# Composition
def sum_of_squares(x, y):
    return square(x) + square(y)

print(sum_of_squares(2,5))

def sum_of_two_largest(a, b, c):
    if a <= b and b <= c:
        print(f"Two largest are {b} & {c}")
        return sum_of_squares(b, c)
    elif b <= a and b <= c:
        print(f"Two largest are {a} & {c}")
        return sum_of_squares(a, c)
    else:
        print(f"Two largest are {a} & {b}")
        return sum_of_squares(a, b)

print(sum_of_two_largest(10, 8, 9))
