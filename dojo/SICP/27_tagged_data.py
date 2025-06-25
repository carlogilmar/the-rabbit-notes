
def evaluate(exp):
    if not isinstance(exp, list):
      # Base case
      return exp
    else:
        op = exp[0]
        left = evaluate(exp[1])
        right = evaluate(exp[2])

        if op == 'sum':
            return left + right
        elif op == 'product':
            return left * right

exp = ['sum', 2, ['product', 3, 4]]
print(f"Evaluate: {exp}, Result: {evaluate(exp)}")
exp = ['sum', 1, 2]
print(f"Evaluate: {exp}, Result: {evaluate(exp)}")
exp = ['product', 2, 3]
print(f"Evaluate: {exp}, Result: {evaluate(exp)}")
