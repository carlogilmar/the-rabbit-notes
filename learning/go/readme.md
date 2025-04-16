# Learning Go

## 🌱 Phase 1: Getting Started With Go

1. Install Go and Set Up Your Environment
- ✅ Install Go from the official site https://golang.org/dl/
- ✅ Use go version and go env to verify your setup
- ✅ Create your first Go workspace
- ✅ Learn how Go uses the GOPATH and go.mod (Go modules)

2. Hello, World! and First Project
- ✅ Create a simple "Hello, World!" program
- ✅ Understand the structure: package main, func main()
- ✅ Use go run, go build, go install

3. Go Tooling Basics
- ✅ Format code with gofmt (or go fmt)
- ✅ Use go vet for static analysis
- ✅ Use go doc and godoc to explore packages
- ✅ Use go mod init, go mod tidy, go get

## 🧠 Phase 2: Understanding Go’s Language Features

4. Basic Syntax and Types
- ✅ Variables (var, :=)
- ✅ Basic types: int, float64, string, bool
- ✅ Constants
- ✅ Type conversions

5. Control Structures
- ✅ if, else, switch, for (only one loop!)
- ✅ break, continue, goto
- ✅ defer, panic, recover (important for error handling)

6. Functions and Error Handling
- ✅ Function definitions
- ✅ Multiple return values
- ✅ Named return values
- ✅ Error handling with error type
- ✅ Idiomatic error handling: if err != nil { ... }

## 🏗️ Phase 3: Core Building Blocks
7. Data Structures
- ✅ Arrays
- ✅ Slices (a must-learn)
- ✅ Maps
- ✅ Structs
- ✅ Pointers (differences vs references in Elixir)

8. Methods and Interfaces
- ✅ Methods on structs
- ✅ Interfaces
- ✅ Type embedding (composition over inheritance)
- ✅ Type assertions and type switches

9. Packages and Modular Code
- ✅ Creating your own packages
- ✅ Importing packages
- ✅ Using standard library effectively (fmt, os, io, net/http, etc.)

## 🧪 Phase 4: Testing and Documentation

10. Unit Testing
- ✅ Write tests with the testing package
- ✅ Use go test
- ✅ Use table-driven tests (a Go idiom)
- ✅ Use t.Run, t.Error, t.Fatal, and t.Parallel
- ✅ Coverage reports: go test -cover

11. Documentation
- ✅ Document your code with comments
- ✅ Generate docs with godoc
- ✅ Explore well-documented Go libraries

## 🕸️ Phase 5: Concurrency and Goroutines (Optional for Basics)

- ✅ Learn how to use go func() to launch a goroutine
- ✅ Learn how to use sync.WaitGroup and sync.Mutex
- ✅ Use channels: chan T
- ✅ Understand buffered vs unbuffered channels
- ✅ Select statement for multiplexing



