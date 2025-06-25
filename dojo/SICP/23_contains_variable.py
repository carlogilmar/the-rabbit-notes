def contains_variable(exp, var):
    if not isinstance(exp, list):
        # Base Case when the exp is not a list
        return exp == var
    else:
        left = contains_variable(exp[1], var)
        print(f"Evaluating left {exp[1]}: {left}")
        right = contains_variable(exp[2], var)
        print(f"Evaluating right {exp[2]}: {right}")
        return left or right


exp = ['+', 'x', 2]
print(f" Expression {exp} contains x?: {contains_variable(exp, 'x')}")
exp = ['*', 3, 'x']
print(f" Expression {exp} contains x?: {contains_variable(exp, 'x')}")
exp = ['*', 5, 'y']
print(f" Expression {exp} contains x?: {contains_variable(exp, 'x')}")
exp = 4
print(f" Expression {exp} contains x?: {contains_variable(exp, 'x')}")
exp = ['*', ['+', 1, 'x'], 1]
print(f" Expression {exp} contains x?: {contains_variable(exp, 'x')}")

