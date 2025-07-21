# Learning Smalltalk 

## Principles

### 1. 🧱 Everything is an Object
- Every value is an object — numbers, strings, classes, code blocks, even the IDE itself.
- Objects communicate only by sending messages.

Design Insight:
> You don’t “call a function”, you send a message to an object. This models decentralized systems, like cells in a body or people in a society.

Alan Kay: `OOP to me means only messaging, local retention and protection, and hiding of state-process, and extreme late-binding of all things.`

### 2. 🧬 Code and Environment Are the Same
- There’s no separate compiler, REPL, or file structure.
- The IDE is the system. You explore and modify everything live — from the UI down to the VM internals.

Design Insight:
> This enables a fluid, iterative process of software design, where your system is always alive, malleable, and changeable.

`Contrast this with tools where you stop everything, edit a file, compile, test, restart — in Smalltalk, you’re always in the system.`

## 3. 🪞 Reflection and Introspection
- The entire system is built with objects — and you can inspect, modify, or replace any of them.
- Tools like the Inspector, Debugger, Browser, etc., let you explore the running system at any level.

Design Insight:
`Your system is transparent and explorable — you’re never debugging from the outside, you’re walking inside the world you’ve built.

## 4. 🧩 Uniformity and Simplicity
- Very small syntax (often fewer than 10 core concepts).
- No special cases — message sending is always the same.
- The class hierarchy is deep but simple (Object at the top, everything descends from it).

Design Insight:
`Cognitive load is reduced — the fewer rules you have, the more power you gain from composition and reuse.`

## 5. 🧠 Programming as Thinking and Modeling
- The goal isn’t just building code — it’s about modeling real-world domains through live, manipulable systems.
- Programs are living models of concepts — they should evolve as your understanding deepens.

Design Insight:
`Code isn’t a fixed artifact. It’s part of a dynamic knowledge-building process.`

Alan Kay: `The computer is an instrument whose music is ideas.`

## 6. 🛠️ Tools Are Not Separate From the Language
- The debugger, inspector, file browser, unit tester — all written in Smalltalk.
- You can improve, extend, or customize any part of your tools within the same language and environment.

Design Insight:
`Tooling is not a service outside the language — it’s part of the same living system. This enables moldable tools and domain-specific views.`
