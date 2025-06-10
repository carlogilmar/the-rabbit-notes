# Evaluation
def square(x):
    return x * x

print(square(2))  # 4
print(square(5))  # 25

# Composition
def sum_of_squares(x, y):
    return square(x) + square(y)

print(sum_of_squares(2,5))
