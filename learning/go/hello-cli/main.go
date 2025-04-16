package main

import (
    "fmt"
    "os"
)

// Run as: go run main.go Carlo
func main() {
    if len(os.Args) < 2 {
        fmt.Println("Usage: hello-go <name>")
        return
    }

    name := os.Args[1]
    fmt.Printf("Hello, %s!\n", name)
}

