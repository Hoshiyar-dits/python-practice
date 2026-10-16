# python-practice

Learn Python from basic to advanced, and prepare for technical interviews.

---

## Basic

### 1. What is Python? What are its key features?
Python is a high-level, interpreted, dynamically typed, general-purpose language. Key features: readable syntax, automatic memory management (garbage collection), a large standard library, support for multiple paradigms (procedural, OOP, functional), and cross-platform support.

### 2. Is Python compiled or interpreted?
Both. Source code (`.py`) is compiled to **bytecode** (`.pyc`), which is then executed by the Python Virtual Machine (PVM). In everyday terms it is called "interpreted" because there is no separate compile step for the user.

### 3. What are Python's built-in data types?
- Numeric: `int`, `float`, `complex`
- Text: `str`
- Sequence: `list`, `tuple`, `range`
- Mapping: `dict`
- Set: `set`, `frozenset`
- Boolean: `bool`
- Binary: `bytes`, `bytearray`, `memoryview`
- `NoneType` (`None`)

### 4. What is the difference between mutable and immutable types?
Mutable objects can be changed after creation: `list`, `dict`, `set`. Immutable objects cannot: `int`, `float`, `str`, `tuple`, `frozenset`. Only immutable (hashable) objects can be dict keys or set members.

```python
s = "abc"
# s[0] = "x"   -> TypeError
lst = [1, 2]
lst[0] = 9     # fine
```

### 5. List vs tuple?
| List | Tuple |
|------|-------|
| Mutable | Immutable |
| `[1, 2]` | `(1, 2)` |
| Slightly slower, more memory | Faster, less memory |
| Not hashable | Hashable (if contents are), can be a dict key |

Use a tuple for fixed data (coordinates, DB rows); a list for collections that change.

### 6. What is the difference between `==` and `is`?
`==` compares **values**; `is` compares **identity** (same object in memory).

```python
a = [1, 2]; b = [1, 2]
a == b   # True
a is b   # False
x is None  # correct way to check for None
```

### 7. What are `*args` and `**kwargs`?
`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict.

```python
def f(*args, **kwargs):
    print(args, kwargs)
f(1, 2, a=3)   # (1, 2) {'a': 3}
```

### 8. What is a lambda function?
A small anonymous function with a single expression: `square = lambda x: x * x`. Commonly used with `sorted`, `map`, `filter`.

### 9. Explain `break`, `continue`, and `pass`.
- `break` exits the loop.
- `continue` skips to the next iteration.
- `pass` does nothing (placeholder for an empty block).

### 10. What is slicing?
Extracting part of a sequence with `seq[start:stop:step]`. `stop` is exclusive.

```python
s = "Python"
s[0:3]   # 'Pyt'
s[-2:]   # 'on'
s[::-1]  # 'nohtyP' (reverse)
```

### 11. How do you handle string formatting?
f-strings (preferred, Python 3.6+): `f"{name} is {age}"`, with format specs like `f"{pi:.2f}"`. Older options: `"{}".format(x)` and `"%s" % x`.

### 12. What is the difference between `append()` and `extend()`?
`append(x)` adds `x` as a single element; `extend(iterable)` adds each element.

```python
a = [1]; a.append([2, 3])  # [1, [2, 3]]
b = [1]; b.extend([2, 3])  # [1, 2, 3]
```

### 13. What does `if __name__ == "__main__":` do?
It runs the code only when the file is executed directly, not when it is imported as a module. Each module's `__name__` is `"__main__"` only when it is the entry point.

### 14. What is PEP 8?
The official style guide for Python code: 4-space indentation, `snake_case` for functions/variables, `PascalCase` for classes, max ~79 chars per line, two blank lines between top-level definitions, etc.

---

## Intermediate

### 15. What are list/dict/set comprehensions?
A concise way to build collections.

```python
squares = [x * x for x in range(5)]
evens   = [x for x in range(10) if x % 2 == 0]
lengths = {w: len(w) for w in ["hi", "hello"]}
uniq    = {x % 3 for x in range(10)}
```

### 16. How does exception handling work?

```python
try:
    risky()
except ValueError as e:
    handle(e)          # runs if that exception happens
else:
    success()          # runs if no exception
finally:
    cleanup()          # always runs
```

Raise your own with `raise MyError("msg")`; create custom exceptions by subclassing `Exception`.

### 17. What are the four pillars of OOP in Python?
- **Encapsulation**: bundle data and methods in a class; hide internals (`_protected`, `__private` name-mangling).
- **Abstraction**: expose only what's needed (e.g. `abc.ABC` with `@abstractmethod`).
- **Inheritance**: `class Dog(Animal)` reuses parent behaviour.
- **Polymorphism**: different classes implement the same method (`speak()`) differently.

### 18. What is `self`?
The first parameter of an instance method, referring to the current object. Python passes it automatically: `obj.method()` is `Class.method(obj)`.

### 19. What is `__init__`? Is it a constructor?
`__init__` **initializes** an already-created object. The actual constructor is `__new__`, which creates the instance. You almost always only need `__init__`.

### 20. Instance method vs `@classmethod` vs `@staticmethod`?
| Type | First arg | Use |
|------|-----------|-----|
| Instance method | `self` | Works with object data |
| `@classmethod` | `cls` | Alternative constructors, class-level state |
| `@staticmethod` | none | Utility function grouped in the class |

### 21. What is `super()`?
Calls a method from the parent class (following the MRO), commonly `super().__init__(...)` in a subclass constructor.

### 22. What is MRO (Method Resolution Order)?
The order in which Python searches classes for a method in multiple inheritance, computed by the C3 linearization algorithm. See it with `ClassName.__mro__` or `ClassName.mro()`.

### 23. What is `@property`?
Turns a method into a read-only attribute (optionally with a setter), allowing validation without changing the public interface.

```python
class Temp:
    def __init__(self, c): self._c = c
    @property
    def c(self): return self._c
    @c.setter
    def c(self, value):
        if value < -273.15: raise ValueError("too cold")
        self._c = value
```

### 24. Shallow copy vs deep copy?
A shallow copy (`copy.copy`, `list[:]`) copies the outer container but shares nested objects. A deep copy (`copy.deepcopy`) recursively copies everything.

```python
import copy
a = [[1, 2]]
s = copy.copy(a); d = copy.deepcopy(a)
a[0].append(3)
s  # [[1, 2, 3]]  shared inner list
d  # [[1, 2]]
```

### 25. What is the mutable default argument problem?
Default values are evaluated **once** at function definition, so a mutable default is shared between calls.

```python
def bad(x, items=[]):   # same list every call
    items.append(x); return items
def good(x, items=None):
    items = [] if items is None else items
    items.append(x); return items
```

### 26. What are modules and packages?
A **module** is a `.py` file. A **package** is a directory of modules (traditionally with `__init__.py`). Import with `import pkg.module` or `from pkg import module`.

### 27. Why use `with open(...)` for files?
`with` is a context manager: the file is closed automatically, even if an exception occurs.

### 28. Useful `collections` classes?
- `Counter`: count items — `Counter("hello")`.
- `defaultdict`: dict with a default factory — `defaultdict(list)`.
- `namedtuple`: tuple with named fields.
- `deque`: fast appends/pops at both ends.
- `OrderedDict`: ordered dict with extra methods (plain `dict` keeps insertion order since 3.7).

### 29. What is the LEGB rule?
Name lookup order: **L**ocal → **E**nclosing function → **G**lobal (module) → **B**uilt-in. Use `global` or `nonlocal` to assign to outer-scope names.

---

## Advanced

### 30. What is a decorator?
A function that takes a function and returns a new function that extends its behaviour, applied with `@`.

```python
import functools
def log(func):
    @functools.wraps(func)          # keep original name/docstring
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b): return a + b
```

A decorator with arguments needs one more level of nesting (`def repeat(n): def decorator(func): ...`).

### 31. What is a generator? How is it different from a list?
A generator is a function using `yield`; it produces values lazily, one at a time, keeping its state between calls. It uses constant memory, while a list stores all values at once. Generators can only be iterated once.

```python
def count_up(n):
    for i in range(n):
        yield i
gen = (x * x for x in range(10**9))  # generator expression, no memory blow-up
```

### 32. Iterable vs iterator?
An **iterable** has `__iter__()` returning an iterator (list, str, dict). An **iterator** has `__next__()` and raises `StopIteration` when done. `iter(obj)` gets an iterator; `next(it)` gets the next value. Every iterator is iterable, but not vice versa.

### 33. What is a closure?
An inner function that remembers variables from its enclosing scope even after the outer function has returned.

```python
def multiplier(n):
    def mul(x): return x * n
    return mul
double = multiplier(2)
double(5)  # 10
```

### 34. What is the late-binding closure gotcha?

```python
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]           # [2, 2, 2]  -- i is looked up when called
funcs = [lambda i=i: i for i in range(3)]
[f() for f in funcs]           # [0, 1, 2]
```

### 35. How do you write a custom context manager?
Either implement `__enter__` / `__exit__` in a class, or use `contextlib.contextmanager`:

```python
from contextlib import contextmanager
@contextmanager
def timer():
    import time; start = time.time()
    yield
    print("took", time.time() - start)
```

### 36. What are dunder (magic) methods?
Special methods with double underscores that let your classes work with Python syntax: `__init__`, `__repr__`, `__str__`, `__len__`, `__eq__`, `__lt__`, `__add__`, `__getitem__`, `__iter__`, `__call__`, `__enter__`/`__exit__`, `__hash__`.

### 37. `__str__` vs `__repr__`?
`__repr__` is an unambiguous representation for developers (ideally valid code to recreate the object); `__str__` is a readable form for users. `print()` uses `__str__`, falling back to `__repr__`.

### 38. What are dataclasses?
`@dataclass` auto-generates `__init__`, `__repr__`, `__eq__` (and ordering with `order=True`) from type-annotated fields. Use `field(default_factory=list)` for mutable defaults; `frozen=True` makes it immutable.

### 39. What is the GIL?
The **Global Interpreter Lock** in CPython allows only one thread to execute Python bytecode at a time. So threads do not speed up CPU-bound work, but they are fine for I/O-bound work (the GIL is released while waiting on I/O). Python 3.13+ offers an experimental free-threaded build without the GIL.

### 40. Threading vs multiprocessing vs asyncio?
| Approach | Best for | Notes |
|----------|----------|-------|
| `threading` / `ThreadPoolExecutor` | I/O-bound (network, files) | Shared memory, limited by GIL for CPU work |
| `multiprocessing` / `ProcessPoolExecutor` | CPU-bound | Separate processes, true parallelism, more overhead |
| `asyncio` | Many concurrent I/O tasks | Single thread, cooperative `async`/`await`, very lightweight |

### 41. How does memory management / garbage collection work?
CPython uses **reference counting**: an object is freed when its reference count reaches 0. A cyclic **garbage collector** (`gc` module) cleans up reference cycles that reference counting can't. Memory is managed by Python's private heap.

### 42. What are metaclasses?
A metaclass is the "class of a class"; it controls how classes are created. `type` is the default metaclass. Define one by subclassing `type` and overriding `__new__`/`__init__`. Used in frameworks (e.g. Django models, ORMs), rarely in application code.

### 43. What does `__slots__` do?
Declares a fixed set of attributes, removing the per-instance `__dict__`. This saves memory and slightly speeds up attribute access, but you can't add new attributes dynamically.

### 44. What are type hints? Are they enforced?
Annotations like `def f(x: int) -> str:` that document types. They are **not enforced at runtime**; tools like `mypy` or `pyright` check them statically.

### 45. What is `functools.lru_cache`?
A decorator that memoizes a function's results, so repeated calls with the same arguments return instantly. Great for recursive functions like Fibonacci. `functools.cache` is the unbounded version (3.9+).

### 46. What are `map`, `filter`, `reduce`, `zip`, `enumerate`?
```python
list(map(str.upper, ["a", "b"]))           # ['A', 'B']
list(filter(lambda x: x > 1, [1, 2, 3]))   # [2, 3]
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3])      # 6
list(zip([1, 2], ["a", "b"]))              # [(1, 'a'), (2, 'b')]
list(enumerate(["x", "y"], start=1))       # [(1, 'x'), (2, 'y')]
```

### 47. What is monkey patching?
Changing a class or module at runtime, e.g. `SomeClass.method = new_func`. Common in tests (`unittest.mock.patch`), risky in production code.

### 48. How do you make a class iterable?
Implement `__iter__` (returning an iterator) — easiest as a generator:

```python
class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self):
        for i in range(self.n, 0, -1):
            yield i
```

### 49. What are virtual environments and why use them?
An isolated Python environment per project with its own packages, avoiding version conflicts.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

### 50. How do you test Python code?
Use `unittest` (built in) or `pytest` (popular). Write functions named `test_*` with `assert` statements; mock external dependencies with `unittest.mock`.

```python
def add(a, b): return a + b
def test_add():
    assert add(2, 3) == 5
```

---

## Common coding questions to practice

1. Reverse a string / check palindrome — `s == s[::-1]`
2. FizzBuzz (see topic 3 in `main.py`)
3. Count character frequency — `collections.Counter`
4. Find duplicates in a list — use a `set` of seen items
5. Fibonacci with recursion + `lru_cache`, and iteratively
6. Two Sum — dict of `value -> index`, O(n)
7. Flatten a nested list — recursion or a generator
8. Check anagrams — `sorted(a) == sorted(b)` or `Counter(a) == Counter(b)`
9. Find the second largest number in a list
10. Merge two sorted lists
11. Write a decorator that times a function (see topic 11)
12. Write a generator that reads a large file line by line
