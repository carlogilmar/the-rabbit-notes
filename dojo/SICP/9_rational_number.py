def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def make_rational(n, d):
    g = gcd(n, d)
    return (n // g, d // g)

def numerator(r):
    return r[0]

def denominator(r):
    return r[1]

def add_rational(r1, r2):
    n = numerator(r1) * denominator(r2) + numerator(r2) * denominator(r1)
    d = denominator(r1) * denominator(r2)
    return make_rational(n, d)

def mul_rational(r1, r2):
    return make_rational(numerator(r1) * numerator(r2),
                         denominator(r1) * denominator(r2))

def equal_rational(r1, r2):
    return numerator(r1) == numerator(r2) and denominator(r1) == denominator(r2)

r1 = make_rational(2, 4) # (1, 2)
print(r1)
r2 = make_rational(3, 6) # (1, 2)
print(r2)
r = equal_rational(r1, r2)  # True
print(r)

r3 = add_rational(r1, r2) # (1, 1)
print(r3)
