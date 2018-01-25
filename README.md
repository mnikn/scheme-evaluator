# scheme-evaluator

一个基于 python3 实现的一个玩具 scheme 解释器，其中的思路主要参考于 **sicp** 的第四章，目前支持的功能有：

- 变量和函数的定义
- 四则运算
- lambda 表达式
- 闭包
- JIT

## 如何运行

执行 `evaluator.py` 即可。运行示例：

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