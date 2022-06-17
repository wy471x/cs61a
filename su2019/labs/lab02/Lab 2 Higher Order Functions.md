# Lab 2: Higher Order Functions 

## Environment Diagram Practice

###  Q4: Make Adder

Draw the environment diagram for the following code:

```
n = 9
def make_adder(n):
    return lambda k: k + n
add_ten = make_adder(n+1)
result = add_ten(n)
```

There are 3 frames total (including the Global frame). In addition, consider the following questions:

1. In the Global frame, the name `add_ten` points to a function object. What is the intrinsic name of that function object, and what frame is its parent?
2. In frame `f2`, what name is the frame labeled with (`add_ten` or λ)? Which frame is the parent of `f2`?
3. What value is the variable `result` bound to in the Global frame?

#### Answer

![Q4](/home/dunk/github-repo/cs61a/su2019/labs/lab02/Q4.png)

1. func λ(k) ，its parent frame is  f1.
2. global frame , f1. parent of f2 is f1.
3. result is 19.

###  Q5: Lambda the Environment Diagram

Try drawing an environment diagram for the following code and predict what Python will output.

**You do not need to submit or unlock this question through Ok.** Instead, you can check your work with the [Online Python Tutor](http://tutor.cs61a.org/), but try drawing it yourself first!

```
>>> a = lambda x: x * 2 + 1
>>> def b(b, x):
...     return b(x + a(x))
>>> x = 3
>>> b(a, x)
______
```

#### Answer

```python
>>> a = lambda x: x * 2 + 1
>>> def b(b, x):
...     return b(x + a(x))
... 
>>> x = 3
>>> b(a, x)
21
```

