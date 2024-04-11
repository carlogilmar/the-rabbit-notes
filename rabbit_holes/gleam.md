# Gleam Learning

> https://tour.gleam.run/

### 1. Hello World

```gleam
import gleam/io

pub fn main(){
  io.println("Hi Joe!")
}
```

**Code Organization**
- Gleam is organized in modules.
- Import modules: `import gleam/io`
- Unqualified fashion: `import gleam/io.{println}`

**Type system**
- Gleam has a robust static type system.
- Errors will appear during compile time.
- Gleam performs full type checking.

**Types**
- Int `gleam/int`
- Float `glema/float` (There are math operations per type)
- Equality `==` and `!=` check if two values have the same structure.
- Strings `import gleam/string`
- Booleans `import gleam/bool`

**Assignments**
- A value can be assigned using `let`.
- Variable not be used coan be prefixed as `let _score = 100`
- Type annotations: `let _is_cool: Bool = True`. (For documentation purposes only)
- Type imports: `let _bytes: bytes_builder.BytesBuilder = bytes_builder.new()`.
- Type aliases:

```gleam
pub type UserId =
  Int // <--- type alias

pub fn main() {
  let one: UserId = 1 // <---- using your type alias
  let two: Int = 2

```

- `pub` keyword is to type public aliases
