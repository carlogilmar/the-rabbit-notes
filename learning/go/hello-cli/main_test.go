// main_test.go
package main

import "testing"

func TestHello(t *testing.T) {
	got := SayHello("Go")
	want := "Hello, Go!"

	if got != want {
		t.Errorf("got %q, want %q", got, want)
	}
}
