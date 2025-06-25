def calculate_derivative(expr, var):
    # Base case 1: expr is the variable itself
    if expr == var:
        return 1

    # Base case 2: expr is a number (constant)
    if isinstance(expr, (int, float)):
        return 0

    # Base case 3: expr is a different symbol
    if isinstance(expr, str):
        return 0

    # Recursive case 1: Sum rule → d/dx(a + b) = d/dx(a) + d/dx(b)
    if isinstance(expr, list) and expr[0] == '+':
        left = calculate_derivative(expr[1], var)
        right = calculate_derivative(expr[2], var)
        return ['+', left, right]

    # Recursive case 2: Product rule → d/dx(a * b) = a * d(b) + d(a) * b
    if isinstance(expr, list) and expr[0] == '*':
        f = expr[1]
        g = expr[2]
        df = calculate_derivative(f, var)
        dg = calculate_derivative(g, var)
        return ['+', ['*', f, dg], ['*', df, g]]

    # Fallback for now
    return "Unhandled expression structure"
