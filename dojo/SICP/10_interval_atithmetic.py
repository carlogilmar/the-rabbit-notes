def make_interval(low, high):
    return (low, high)

def lower_bound(x):
    return x[0]

def upper_bound(x):
    return x[1]

def add_interval(x, y):
    return make_interval(
        lower_bound(x) + lower_bound(y),
        upper_bound(x) + upper_bound(y)
    )

def sub_interval(x, y):
    return make_interval(
        lower_bound(x) - upper_bound(y),
        upper_bound(x) - lower_bound(y)
    )

def mul_interval(x, y):
    a, b = lower_bound(x), upper_bound(x)
    c, d = lower_bound(y), upper_bound(y)
    products = [a*c, a*d, b*c, b*d]
    return make_interval(min(products), max(products))

def div_interval(x, y):
    c, d = lower_bound(y), upper_bound(y)
    if c <= 0 <= d:
        raise ValueError("Cannot divide by interval spanning zero.")
    return mul_interval(x, make_interval(1/d, 1/c))

#x = (3, 5)
#y = (2, 4)
#
#add → (5, 9)
#mul → (6, 20)
