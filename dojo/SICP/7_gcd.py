# gcd(48, 18) --> 6
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(48, 18))

