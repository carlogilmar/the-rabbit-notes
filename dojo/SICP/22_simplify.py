def simplify(exp):
    print("[Start] Simplify function execution here.")
    if not isinstance(exp, list):
        print(f"[Not a list] Returning single element {exp}")
        # Base case
        return exp
    else:
        print(f"[List of elements] Start iteration for: {exp}")

        op = exp[0]
        left = simplify(exp[1])
        right = simplify(exp[2])

        if op == '+' and left == 0:
            return right
        elif op == '+' and right == 0:
            return left
        elif op == '*' and (left == 1 or right == 1):
            return 'x'
        elif op == '*' and (left == 0 or right == 0):
            return 0
        else:
            return [op, left, right]


#print(f" Result is: {simplify(['*', 1, 'x'])}")
#print(f" Result is: {simplify(['/', 2, 'x'])}")
print(simplify(['+', ['*', 1, 'x'], 2]))

