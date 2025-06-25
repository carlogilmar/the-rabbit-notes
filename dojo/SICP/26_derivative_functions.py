def calculate_derivative(expr, var):
    if is_base_case(expr, var):
        return eval_base_case(expr, var)

    if is_sum(expr):
        return deriv_sum(expr, var)

    if is_product(expr):
        return deriv_product(expr, var)

    return "Unhandled expression structure"

# --- Base case logic ---
def is_base_case(expr, var):
    return (
        expr == var or
        isinstance(expr, (int, float)) or
        isinstance(expr, str)
    )

def eval_base_case(expr, var):
    if expr == var:
        return 1
    return 0

# --- Pattern checks ---
def is_sum(expr):
    return isinstance(expr, list) and len(expr) == 3 and expr[0] == '+'

def is_product(expr):
    return isinstance(expr, list) and len(expr) == 3 and expr[0] == '*'

# --- Derivative rules ---
def deriv_sum(expr, var):
    left = calculate_derivative(expr[1], var)
    right = calculate_derivative(expr[2], var)
    return ['+', left, right]

def deriv_product(expr, var):
    f = expr[1]
    g = expr[2]
    df = calculate_derivative(f, var)
    dg = calculate_derivative(g, var)
    return ['+', ['*', f, dg], ['*', df, g]]

# --- Test case ---
if __name__ == "__main__":
    expr = ['*', 'x', ['+', 'x', 1]]
    print(calculate_derivative(expr, 'x'))
