# 1. What is Python ?
Python is popular server side programming language. It is used on server to create web application. It can work on different platforms like Windows , Linux , MAC. It has simple syntax similar to english language. It is also used for build AI models, chatboats, and intelligent agents that can understand the information , make decision and perform tasks automatically.

# 2. How to run python code ?
We can run python code using command `python filename.py`

# 3. How to check python version using code ?
Simply import sys and print(sys.version)

# 4. What is indentation ?
Indentation refers to the spaces at the beginning of a code line. Python uses indentation to indicate a block of code.

# 5. What is python variables ?
A variable is created when you assign a value to it.

# 6. What is python statements ?
A computer program is a list of instructions to be executed by computer. In a programming language, these programming instructions are called statements.In a programe there is many statements so each statement execute one by one in the order.

# 7. What is python casting ?
A casting is converting a datatype to another data type like int to float or float to int.

# 8. What is string ?
The text written inside double quote or single quote is known as string.

# 9. String methods in python ?
  str = "Hello"

  String length - len()  - print(len(str))  - 5
  Upper case - upper()  -  print(str.upper())  -  HELLO
  Lower case - lower()  -  print(str.lower())  - hello
  Remove whitespace - strip() -> print(str.stripe())   - it removes the space from start point and end point of string
  Replace string - replace() -> print(str.replace("H","J"))  - Jello
  Split string - split() - print(str.split(","))  - convert string to list (array)
  String count - count()  - print(str.count())

# 10. How to concatenation works in python ?
Concatenation is the operation of joining two strings together. In Python, we can concatenate strings using the `+` operator.

# 11. Python string format 
Python provides several ways to format strings. The most common methods are:
1. Using f-strings (formatted string literals):
```python
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
```
2. Using the `format()` method:
```python
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
```

# 12. Python Operators
python supports various types of operators, including:
    1. Arithmetic Operators: +, -, *, /, %, **, //
    2. Comparison Operators: ==, !=, >, <, >=, <=
    3. Logical Operators: and, or, not
    4. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
    5. Bitwise Operators: &, |, ^, ~, <<, >>
    6. Membership Operators: in, not in
    7. Identity Operators: is, is not
    8. Ternary Operator: A shorthand for an if-else statement, written as `value_if_true if condition else value_if_false`.

# 13. Python Lists
A list is a collection which is ordered and changeable. In Python lists are written with square brackets. Lists can contain items of different data types, including other lists. eg-
```python
my_list = [1, 2, 3, "Hello", [4, 5]]
``` 

# 14. Python Tuples
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. Tuples can contain items of different data types, including other tuples. eg-
```python
my_tuple = (1, 2, 3, "Hello", (4, 5))
```

# 15. Python Sets
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets. Sets do not allow duplicate items. eg-
```python
my_set = {1, 2, 3, "Hello"}
```

# 16. Python Dictionaries
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values. eg-
```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
```