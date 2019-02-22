# scheme-evaluator

A toy scheme evaluator implemented by python3, features:

- varible and function
- expression
- lambda expression
- closure

## How to run

Run `evaluator.py`：

```scheme
--------------------

Input Expression:

(define x 34)
ok

End Evaluation
--------------------

--------------------

Input Expression:

(+ x 5 7 8)
54

End Evaluation
--------------------

--------------------

Input Expression:

(define (add-six x) (+ x 6))
ok

End Evaluation
--------------------

--------------------

Input Expression:

(add-six x)
40

End Evaluation
--------------------
```
