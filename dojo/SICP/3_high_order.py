def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

print(apply_twice(square, 2))  # square(square(2)) → 16

# Anonymous function: add = lambda x: x + 1
def compose(f, g):
    return lambda x: f(g(x))

def inc(x):
    return x + 1

def double(x):
    return x * 2

h = compose(double, inc)  # h(x) = double(inc(x))
print(h(3))  # → 8 (inc 3 = 4, double 4 = 8)

def make_adder(n):
    return lambda x: x + n

add5 = make_adder(5)
print(add5(10))  # → 15

add1 = make_adder(1)
print(add1(7))   # → 8
