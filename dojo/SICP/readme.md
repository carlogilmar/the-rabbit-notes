# Structure and interpretation of computer problems in python

1. Building abstractions with procedures
  - Expressions & Simple Procedures
  - Naming & Substitution Model
  - Conditional Expressions
  - Recursion vs Iteration
  - Higher-Order Functions
  - Functional Abstraction & Reuse

```
1.1 The Elements of Programming
	•	✅ Concepts: expressions, naming, functions, composition
	•	🐍 Python: def, arithmetic expressions, function calls
	•	💡 Elixir parallel: def, pipelines, function composition
	•	🧪 Example: square(x), square(square(x))

1.2 Procedures and the Processes They Generate
	•	✅ Concepts: recursive vs iterative processes
	•	🐍 Python: recursion vs while/for loops
	•	💡 Elixir parallel: tail recursion vs state-passing loops
	•	🧪 Example: factorial(n) (recursive and iterative), fib(n)

1.3 Formulating Abstractions with Higher-Order Functions
	•	✅ Concepts: functions as arguments/values, anonymous functions
	•	🐍 Python: lambda, passing functions, closures
	•	💡 Elixir parallel: fn, function captures (&), pipelines
	•	🧪 Example: apply_twice(f, x), compose(f, g), make_adder(n)

1.3.1 Procedures as Arguments
	•	🧪 Example: sum_of(f, a, b) — generalizes computation over ranges
	•	💡 Shows how to abstract common patterns

1.3.2 Constructing Procedures Using Lambda
	•	🐍 Python: lambda x: x * x
	•	💡 Elixir: fn x -> x * x end or &(&1 * &1)

1.3.3 Using let to Bind Variables (Elided in Python)
	•	Python doesn’t have let, but function scope + inner functions work similarly

💡 Overall Takeaways
	•	Functions are values — pass them, return them, store them
	•	Build abstractions that generalize patterns, not just behavior
	•	Recursive thinking helps describe process structure
	•	Python supports functional style even without being purely functional
	•	Your Elixir background gives you a huge advantage in understanding and applying these ideas
```
