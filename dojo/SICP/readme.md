# Structure and interpretation of computer problems in python

- **1 Building abstractions with procedures**
  - Expressions & Simple Procedures
  - Naming & Substitution Model
  - Conditional Expressions
  - Recursion vs Iteration
  - Higher-Order Functions
  - Functional Abstraction & Reuse
- **2 Building abstractions with data**
  - Introduction to data abstraction
  - Hierarchical data and the closure property
  - Symbolic data
  - Multiple representations for abstract data
  - Systems with generic operations

(Website)[https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-4.html#%_toc_start]

### List of concepts

```
⭐️ Concept Summary Chapter 1
I. Expressions
II. Procedures

⭐️ Concept Summary Chapter 2
I. Constructors
II. Selectors
III. Data abstraction barrier
IV. Closure Property

```

## 📘 Chapter 1 Summary — *Building Abstractions with Procedures* (SICP in Python)

> This chapter explores how to build expressive, composable programs by treating procedures (functions) as abstractions. These ideas are deeply familiar to Elixir developers and map cleanly into Python with a functional mindset.

---

### 1.1 **The Elements of Programming**
- ✅ Concepts: expressions, naming, functions, composition
- 🐍 Python: `def`, arithmetic expressions, function calls
- 💡 Elixir parallel: `def`, pipelines, function composition
- 🧪 Example: `square(x)`, `square(square(x))`

---

### 1.2 **Procedures and the Processes They Generate**
- ✅ Concepts: recursive vs iterative processes
- 🐍 Python: recursion vs `while`/`for` loops
- 💡 Elixir parallel: tail recursion vs state-passing loops
- 🧪 Example: `factorial(n)` (recursive and iterative), `fib(n)`

---

### 1.3 **Formulating Abstractions with Higher-Order Functions**
- ✅ Concepts: functions as arguments/values, anonymous functions
- 🐍 Python: `lambda`, passing functions, closures
- 💡 Elixir parallel: `fn`, function captures (`&`), pipelines
- 🧪 Example: `apply_twice(f, x)`, `compose(f, g)`, `make_adder(n)`

---

### 1.3.1 **Procedures as Arguments**
- 🧪 Example: `sum_of(f, a, b)` — generalizes computation over ranges
- 💡 Shows how to abstract common patterns

---

### 1.3.2 **Constructing Procedures Using Lambda**
- 🐍 Python: `lambda x: x * x`
- 💡 Elixir: `fn x -> x * x end` or `&(&1 * &1)`

---

### 1.3.3 **Using `let` to Bind Variables**
- 📝 Python doesn’t have `let`, but function scope + local variables provide similar control

---

## 💡 Overall Takeaways
- **Functions are values** — pass them, return them, store them
- **Build abstractions** that generalize patterns, not just behavior
- **Recursive thinking** helps describe process structure
- Python supports **functional style** even without being purely functional
- Your Elixir background gives you a huge advantage in understanding and applying these ideas


## 🌿 SICP 2.1 — Introduction to Data Abstraction (Summary)

**Main idea:**
Separate *what* data means from *how* it is implemented.

### ✅ Key Concepts

- **Constructor**: builds a data object from inputs
  _e.g._ `make_rational(n, d) → (n, d)`
- **Selectors**: extract data from an object
  _e.g._ `numerator(r), denominator(r)`
- **Data Abstraction Barrier**:
  Users of a data object **only interact with it via interface**, never the internal structure.
  This makes refactoring or changing implementations easy.
- **Closure Property**:
  An operation has the **closure property** if it takes values of a certain type and **returns a result of the same type**.
  - You always know what type of result you’ll get.
  - You can reuse the operation recursively or iteratively.
  - You can build complex, hierarchical, or scalable structures.
  - You can write generic, reusable logic that works at any level.

## 2.3 Symbolic Data

In this chapter, SICP explores how symbols and symbolic structures can be manipulated just like numbers and data structures. Instead of thinking only in terms of math and vectors, we move into symbols, lists, sets, and trees — foundational for building interpreters, algebra systems, and knowledge representations.

The key idea: symbols are data too. You can store, inspect, combine, and process symbolic expressions with recursive procedures.

Concepts:

- `Quotation (')`: Marks a list or symbol as data, not something to evaluate. 'x is a symbol. '(+ x 1) is a list representing an expression.
- `Symbols`: Identifiers treated as literal data, not variables. Used for reasoning about expressions.
- `Tagged Lists`: Lists where the first item is a tag indicating the kind of data (e.g., ['sum', a, b]) — a pattern used for building interpreters.
- `Symbolic Differentiation`: Using recursion to manipulate algebraic expressions represented as nested lists.
- `Sets as Lists`: Representing mathematical sets using lists, and building operations like union, intersection, and membership tests.
- `Ordered Sets`: An optimization: keeping sets sorted so membership and union can be done more efficiently.
- `Trees`: Lists that contain other lists — enabling hierarchical data like parse trees or file systems.
Set of Trees
Representing and querying deeply nested symbolic structures.
Symbolic Pattern Matching
Looking at structure rather than just values to decide what to do — a core idea in building compilers and interpreters.

`Agenda of Topics for 2.3`
1. Quotation and Symbols: Expressions as data.
2. Symbolic Algebra: Differentiation
3. Tagged Data & Pattern Recognition
4. Sets Represented as Lists
5. Sets as Ordered Lists
6. Sets Represented as Trees
7. Symbolic Trees and Nested Structures
8. Extended Symbolic Manipulation

## 2.4 Sets represented as lists

- ´Set as List´: A set is represented as a list (e.g. [1, 2, 3] for {1, 2, 3})
- ´Membership´: A function like element_of_set(x, s) returns True if x ∈ s
- ´Adjoin (Add)´: Add an item if not present´: adjoin_set(x, s)
- ´Union´: Combine elements from both sets (no duplicates)
- ´Intersection´: Return only elements found in both sets
- ´Abstraction Barrier´: User doesn’t care if it’s an unordered list or sorted list — same interface

