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
some of the commonly used string methods in Python are:
1. `len()`: Returns the length of the string.
2. `lower()`: Converts the string to lowercase.
3. `upper()`: Converts the string to uppercase.
4. `strip()`: Removes leading and trailing whitespace from the string.
5. `replace(old, new)`: Replaces occurrences of a substring with another substring.


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
1. Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
2. Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
3. Logical operators: `and`, `or`, `not`
4. Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`
5. Bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`
6. Membership operators: `in`, `not in`
7. Identity operators: `is`, `is not`

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

# 17. Python If-Else Statements
If-else statements are used for conditional execution of code blocks. The syntax is as follows:
```python
if condition:
    # code block to execute if condition is true
else:
    # code block to execute if condition is false
```

# 18. Python Match Case Statements
Match-case statements are used for pattern matching in Python. They allow you to match a value against different patterns and execute code based on the match. The syntax is as follows:
```python
match value:
    case pattern1:
        # code block to execute if value matches pattern1
    case pattern2:
        # code block to execute if value matches pattern2
    case _:
        # code block to execute if value does not match any pattern
```    

# 19. Python Loops
Python supports two main types of loops: `for` loops and `while` loops.
- `for` loops are used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.
```python
for item in sequence:
    # code block to execute for each item
```
- `while` loops are used to execute a block of code as long as a specified condition is true.
```python
while condition:
    # code block to execute while condition is true 
```

# 20. Python Functions
A function is a block of code that performs a specific task and can be reused throughout the program. Functions are defined using the `def` keyword, followed by the function name and parentheses. The syntax is as follows:
```python
def function_name(parameters):
    # code block to execute
    return value  # optional
```

# 21. Python Classes and Objects
Python is an object-oriented programming language, which means it allows you to create classes and objects.
- A class is a blueprint for creating objects. It defines the properties and behaviors that the objects created from the class will have.
- An object is an instance of a class. It is created using the class constructor and can access the properties and methods defined in the class.
```python
class MyClass:
    def __init__(self, property1, property2):
        self.property1 = property1
        self.property2 = property2

    def my_method(self):
        # code block to execute
        return self.property1 + self.property2
```

# 22. Python Inheritance
Inheritance is a feature of object-oriented programming that allows a class (called the child class or subclass) to inherit properties and methods from another class (called the parent class or superclass). This allows for code reuse and the creation of a hierarchical relationship between classes.
```python
class ParentClass:
    def __init__(self, property1):
        self.property1 = property1
    
    def parent_method(self):
        return self.property1
    
class ChildClass(ParentClass):
    def __init__(self, property1, property2):
        super().__init__(property1)  # Call the constructor of the parent class
        self.property2 = property2  
    
    def child_method(self):
        return self.property1 + self.property2
```

# 23. Python Polymorphism
Polymorphism is a feature of object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It allows for methods to be defined in different classes with the same name but with different implementations. This enables the same method to behave differently based on the object that is calling it.
```python
class Animal:
    def sound(self):
        pass
    
    def make_sound(self):
        return self.sound()

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
# Example usage:
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!   
```

# 24. Python Encapsulation
Encapsulation is a feature of object-oriented programming that restricts access to the internal state and behavior of an object. It allows you to hide the implementation details of a class and expose only the necessary methods and properties to the outside world. This helps to protect the integrity of the object's data and prevents unintended modifications.
```python
class MyClass:
    def __init__(self, property1):
        self.__property1 = property1  # Private property

    def get_property1(self):
        return self.__property1  # Public method to access the private property
    
    def set_property1(self, value):
        self.__property1 = value  # Public method to modify the private property
``` 