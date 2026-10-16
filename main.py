"""Python practice: basic to advanced.

Run:
    python3 main.py          # show menu and pick a topic
    python3 main.py 3        # run topic 3 directly
    python3 main.py all      # run every topic
"""

import sys


# ---------------------------------------------------------------- BASIC

def variables_and_types():
    name = "Alice"          # str
    age = 25                # int
    height = 5.6            # float
    is_dev = True           # bool
    nothing = None          # NoneType
    for value in (name, age, height, is_dev, nothing):
        print(f"{value!r:>8} -> {type(value).__name__}")

    # Type conversion
    print(int("42") + 1, float("3.5"), str(10) + "!", bool(""), bool("x"))


def strings():
    s = "Hello, Python"
    print(s.upper(), s.lower(), len(s))
    print(s[0], s[-1], s[0:5], s[::-1])       # indexing, slicing, reverse
    print(s.split(", "), "-".join(["a", "b", "c"]))
    print(s.replace("Python", "World"), s.find("Py"), s.startswith("He"))
    print(f"{3.14159:.2f} | {42:05d} | {'left':<6}|")


def control_flow():
    for n in range(1, 16):
        if n % 15 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")
    print()

    count = 3
    while count > 0:
        print("countdown", count)
        count -= 1

    # for/else: else runs only if loop wasn't broken
    for x in [1, 3, 5]:
        if x % 2 == 0:
            break
    else:
        print("no even number found")


def collections_demo():
    nums = [3, 1, 4, 1, 5]
    nums.append(9)
    nums.sort()
    print("list:", nums)

    point = (10, 20)
    x, y = point                                # tuple unpacking
    print("tuple:", point, x, y)

    unique = set(nums)
    print("set:", unique, unique & {1, 9, 100})  # intersection

    person = {"name": "Bob", "age": 30}
    person["city"] = "Pune"
    print("dict:", person, person.get("email", "N/A"))
    for key, value in person.items():
        print(f"  {key} = {value}")


def functions():
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    def total(*args, **kwargs):
        return sum(args), kwargs

    square = lambda n: n * n

    print(greet("Sam"), greet("Sam", greeting="Hi"))
    print(total(1, 2, 3, unit="kg"))
    print(list(map(square, [1, 2, 3])))
    print(list(filter(lambda n: n % 2 == 0, range(10))))
    print(sorted(["banana", "kiwi", "apple"], key=len))


# --------------------------------------------------------- INTERMEDIATE

def comprehensions():
    squares = [n * n for n in range(6)]
    evens = [n for n in range(10) if n % 2 == 0]
    lengths = {w: len(w) for w in ["hi", "hello"]}
    unique_mod = {n % 3 for n in range(10)}
    gen = (n * n for n in range(1_000_000))   # lazy, no big list in memory
    print(squares, evens, lengths, unique_mod, next(gen), next(gen))


def exceptions():
    class InsufficientFunds(Exception):
        pass

    def withdraw(balance, amount):
        if amount > balance:
            raise InsufficientFunds(f"need {amount}, have {balance}")
        return balance - amount

    for amount in (50, 500):
        try:
            print("new balance:", withdraw(100, amount))
        except InsufficientFunds as e:
            print("error:", e)
        else:
            print("  (no error)")
        finally:
            print("  (finally always runs)")

    try:
        int("abc")
    except (ValueError, TypeError) as e:
        print("caught:", type(e).__name__, e)


def oop():
    class Animal:
        species_count = 0                       # class attribute

        def __init__(self, name):
            self.name = name                    # instance attribute
            Animal.species_count += 1

        def speak(self):
            raise NotImplementedError

        def __repr__(self):
            return f"{type(self).__name__}({self.name!r})"

    class Dog(Animal):
        def speak(self):
            return "Woof"

    class Cat(Animal):
        def speak(self):
            return "Meow"

    class Account:
        def __init__(self, balance):
            self._balance = balance             # "protected" by convention

        @property
        def balance(self):
            return self._balance

        @classmethod
        def empty(cls):
            return cls(0)

        @staticmethod
        def is_valid(amount):
            return amount > 0

    for pet in (Dog("Rex"), Cat("Tom")):        # polymorphism
        print(pet, "says", pet.speak())
    print("animals created:", Animal.species_count)
    print("isinstance:", isinstance(Dog("x"), Animal))
    print("empty account:", Account.empty().balance, Account.is_valid(5))


def file_handling():
    import json
    import os
    import tempfile

    path = os.path.join(tempfile.gettempdir(), "practice_demo.json")
    data = {"user": "omkar", "skills": ["python", "sql"]}

    with open(path, "w") as f:                  # context manager closes file
        json.dump(data, f)
    with open(path) as f:
        loaded = json.load(f)
    print("round-trip:", loaded == data, loaded)
    os.remove(path)


def modules_and_stdlib():
    from collections import Counter, defaultdict, namedtuple, deque
    from datetime import date, timedelta
    import itertools

    print(Counter("mississippi").most_common(2))
    groups = defaultdict(list)
    for word in ["apple", "avocado", "banana"]:
        groups[word[0]].append(word)
    print(dict(groups))
    Point = namedtuple("Point", "x y")
    print(Point(1, 2))
    q = deque([1, 2, 3]); q.appendleft(0); q.pop()
    print(q)
    print(date(2026, 1, 1) + timedelta(days=45))
    print(list(itertools.combinations("ABC", 2)))


# ------------------------------------------------------------- ADVANCED

def decorators():
    import functools
    import time

    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            print(f"{func.__name__} took {time.perf_counter() - start:.6f}s")
            return result
        return wrapper

    def repeat(times):                          # decorator with arguments
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return [func(*args, **kwargs) for _ in range(times)]
            return wrapper
        return decorator

    @timer
    def slow_sum(n):
        return sum(range(n))

    @repeat(3)
    def hello():
        return "hi"

    print(slow_sum(100_000), hello(), slow_sum.__name__)

    @functools.lru_cache(maxsize=None)          # memoization
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)
    print("fib(80) =", fib(80))


def generators_iterators():
    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    class Squares:                              # custom iterator protocol
        def __init__(self, limit):
            self.i, self.limit = 0, limit

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.limit:
                raise StopIteration
            self.i += 1
            return self.i ** 2

    print(list(countdown(5)), list(Squares(4)))

    def pipeline():
        nums = (n for n in range(20))
        evens = (n for n in nums if n % 2 == 0)
        return sum(n * n for n in evens)
    print("sum of even squares:", pipeline())


def closures_and_scope():
    counter_total = 0

    def make_counter():
        count = 0

        def increment():
            nonlocal count
            count += 1
            return count
        return increment

    c = make_counter()
    print(c(), c(), c())

    def bump():
        nonlocal counter_total
        counter_total += 10
    bump()
    print("counter_total:", counter_total)

    # Late-binding gotcha
    funcs = [lambda: i for i in range(3)]
    fixed = [lambda i=i: i for i in range(3)]
    print([f() for f in funcs], [f() for f in fixed])


def context_managers():
    from contextlib import contextmanager

    class Resource:
        def __enter__(self):
            print("acquire")
            return self

        def __exit__(self, exc_type, exc, tb):
            print("release (exc:", exc_type.__name__ if exc_type else None, ")")
            return True                         # suppress exception

    with Resource():
        raise ValueError("boom")

    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")

    with tag("div"):
        print("  content")


def dunder_and_dataclasses():
    from dataclasses import dataclass, field

    class Vector:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __eq__(self, other):
            return (self.x, self.y) == (other.x, other.y)

        def __len__(self):
            return 2

        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    print(Vector(1, 2) + Vector(3, 4), Vector(1, 1) == Vector(1, 1), len(Vector(0, 0)))

    @dataclass(order=True)
    class Employee:
        salary: int
        name: str = field(compare=False)
        skills: list = field(default_factory=list, compare=False)

    staff = [Employee(500, "A"), Employee(300, "B")]
    print(sorted(staff))


def concurrency():
    import asyncio
    import time
    from concurrent.futures import ThreadPoolExecutor

    def io_task(n):
        time.sleep(0.2)
        return n * 2

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(io_task, range(5)))
    print("threads:", results, f"{time.perf_counter() - start:.2f}s (not 1.0s)")

    async def fetch(n):
        await asyncio.sleep(0.2)
        return n * 10

    async def run_all():
        return await asyncio.gather(*(fetch(i) for i in range(5)))

    start = time.perf_counter()
    print("asyncio:", asyncio.run(run_all()), f"{time.perf_counter() - start:.2f}s")


def type_hints_and_mutability():
    from typing import Optional

    def find(items: list[str], target: str) -> Optional[int]:
        return items.index(target) if target in items else None

    print(find(["a", "b"], "b"), find(["a"], "z"))

    # Mutable default argument gotcha
    def bad_append(x, items=[]):
        items.append(x)
        return items

    def good_append(x, items=None):
        items = [] if items is None else items
        items.append(x)
        return items

    print(bad_append(1), bad_append(2))
    print(good_append(1), good_append(2))

    # Shallow vs deep copy
    import copy
    original = [[1, 2], [3, 4]]
    shallow, deep = copy.copy(original), copy.deepcopy(original)
    original[0].append(99)
    print("shallow:", shallow, "deep:", deep)
    print("is vs ==:", [1] == [1], [1] is [1])


TOPICS = [
    ("Basic", "Variables & types", variables_and_types),
    ("Basic", "Strings", strings),
    ("Basic", "Control flow", control_flow),
    ("Basic", "Collections (list/tuple/set/dict)", collections_demo),
    ("Basic", "Functions, *args, **kwargs, lambda", functions),
    ("Intermediate", "Comprehensions", comprehensions),
    ("Intermediate", "Exceptions", exceptions),
    ("Intermediate", "OOP", oop),
    ("Intermediate", "File handling & JSON", file_handling),
    ("Intermediate", "Standard library", modules_and_stdlib),
    ("Advanced", "Decorators & caching", decorators),
    ("Advanced", "Generators & iterators", generators_iterators),
    ("Advanced", "Closures & scope", closures_and_scope),
    ("Advanced", "Context managers", context_managers),
    ("Advanced", "Dunder methods & dataclasses", dunder_and_dataclasses),
    ("Advanced", "Concurrency (threads, asyncio)", concurrency),
    ("Advanced", "Type hints, mutability, copying", type_hints_and_mutability),
]


def run_topic(index):
    level, title, func = TOPICS[index]
    print(f"\n=== {index + 1}. [{level}] {title} ===")
    func()


def show_menu():
    print("\nPython Practice Topics")
    for i, (level, title, _) in enumerate(TOPICS, start=1):
        print(f"  {i:>2}. [{level:<12}] {title}")
    print("   a. Run all\n   q. Quit")


def main():
    if len(sys.argv) > 1:
        choices = [sys.argv[1]]
    else:
        choices = None

    while True:
        if choices is None:
            show_menu()
            try:
                choice = input("\nChoose a topic: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print()
                return
        else:
            choice = choices.pop().lower()

        if choice in ("q", "quit", "exit"):
            return
        if choice in ("a", "all"):
            for i in range(len(TOPICS)):
                run_topic(i)
        elif choice.isdigit() and 1 <= int(choice) <= len(TOPICS):
            run_topic(int(choice) - 1)
        else:
            print("Invalid choice.")

        if choices is not None:             # CLI argument mode: run once
            return


if __name__ == "__main__":
    main()
