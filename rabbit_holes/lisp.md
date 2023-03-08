# Common Lisp


### Setup Considerations

1. Install Common Lisp
2. Install Emacs and Slime
3. Open Emacs and Slime

### Lisp Basics

1. Use the repl:

```
; SLIME 2.28
CL-USER> (* 1 2 4)
6
CL-USER> "Holis"
"Holis"
CL-USER> (format t "holis crayolis")
holis crayolis
NIL
CL-USER> (defun hello-world () (format t "holis"))
HELLO-WORLD
CL-USER> (hello-world)
holis
NIL
```

2. Using the files

- Create a file `hello.lisp` or `hello.cl`.
- Write your program.
- Type (`Ctrl` + `C`), (`Ctrl` + `C`) to load the file in the repl.
- Execute your program from the repl.

![image](https://user-images.githubusercontent.com/17634377/223600095-dfb9c3ac-a0ca-410c-850c-d670a8518547.png)

