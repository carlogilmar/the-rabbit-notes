def smallest_divisor(n):
    def find_divisor(n, test_divisor):
        if test_divisor * test_divisor > n:
            return n  # n is prime
        elif n % test_divisor == 0:
            return test_divisor
        else:
            return find_divisor(n, test_divisor + 1)

    return find_divisor(n, 2)

print(smallest_divisor(15))
print(smallest_divisor(77))
print(smallest_divisor(13))
