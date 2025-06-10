def factorial(n):
    if n == 0:
        return 1
    else:
        print(f"{n} * ")
        return n * factorial(n-1)

print(factorial(5)) # factorial(1000) crashed

def i_factorial(n):
    result = 1
    while n > 0:
        print(f"{n} *")
        result *= n
        n -= 1
    return result

print(i_factorial(5)) # factorial(1000) works
