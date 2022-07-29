# Higher Order Functions

## Q2

Draw the environment diagram for the following code:

```python
x = 5
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
d = lambda y: y * x
x = 4
result = compose1(lambda z: z - 1, d)(3)
```

There are 5 frames total (including the Global frame). In addition, consider the following questions:

1. In frame `f1` (the frame for `compose1`), the parameter `f` points to a function object. What is the intrinsic name of that function object, and what frame is its parent?
2. In frame `f2`, what name is the frame labeled with (`h` or λ)? Which frame is the parent of `f2`?
3. In frame `f3`, what name is the frame labeled with (`f`, `g`, `d`, or λ)? Which frame is the parent of `f3`? In order to compute the return value `y * x`, in which frame does Python find `x`? What is that value of `x`?
4. In frame `f4`, what name is the frame labeled with (`f`, `g`, `d`, or λ)? Which frame is the parent of `f3`?
5. What value is the variable `result` bound to in the Global frame?

## Answer

1. finction object's name is $\lambda(z)$, its parent frame is global frame.
2. f2's parent frame is f1.
3.  f3's parent frame is f2;global frame;x is 4.
4. f3's parent frame os f3.
5. result is 11.

