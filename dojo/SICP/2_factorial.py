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

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"Calculando fib({n-1}) y fib({n-2})")
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

def i_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
      a, b = b, a + b
    return a

print(i_fibonacci(35))
