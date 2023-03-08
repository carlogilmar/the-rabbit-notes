# Common Lisp


### Setup Considerations

1. Install Common Lisp
2. Install Emacs and Slime
3. Open Emacs and Slime

### Lisp Basics

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
