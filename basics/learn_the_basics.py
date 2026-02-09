"""
Learn the Basics of Python Programming
=======================================

This module teaches fundamental Python concepts through simple, runnable examples.
Each function demonstrates a core concept with doctests you can verify.

Run all examples:
    python -m doctest basics/learn_the_basics.py -v
Or:
    pytest basics/learn_the_basics.py --doctest-modules
"""

# =============================================================================
# 1. VARIABLES AND DATA TYPES
# =============================================================================
# Python has several built-in data types. You don't need to declare types —
# Python figures them out automatically (dynamic typing).


def demonstrate_data_types() -> dict[str, str]:
    """
    Show Python's core data types.

    >>> result = demonstrate_data_types()
    >>> result["integer"]
    'int'
    >>> result["float"]
    'float'
    >>> result["string"]
    'str'
    >>> result["boolean"]
    'bool'
    >>> result["list"]
    'list'
    >>> result["dictionary"]
    'dict'
    """
    integer = 42  # Whole numbers
    floating = 3.14  # Decimal numbers
    string = "Hello, World!"  # Text
    boolean = True  # True or False
    items = [1, 2, 3]  # Ordered, mutable collection
    mapping = {"key": "value"}  # Key-value pairs

    return {
        "integer": type(integer).__name__,
        "float": type(floating).__name__,
        "string": type(string).__name__,
        "boolean": type(boolean).__name__,
        "list": type(items).__name__,
        "dictionary": type(mapping).__name__,
    }


# =============================================================================
# 2. ARITHMETIC OPERATIONS
# =============================================================================
# Python supports standard math operations plus a few extras.


def basic_arithmetic(a: float, b: float) -> dict[str, float]:
    """
    Perform basic arithmetic operations on two numbers.

    >>> result = basic_arithmetic(10, 3)
    >>> result["addition"]
    13
    >>> result["subtraction"]
    7
    >>> result["multiplication"]
    30
    >>> result["division"]
    3.3333333333333335
    >>> result["floor_division"]
    3
    >>> result["modulus"]
    1
    >>> result["exponentiation"]
    1000
    """
    return {
        "addition": a + b,  # 10 + 3 = 13
        "subtraction": a - b,  # 10 - 3 = 7
        "multiplication": a * b,  # 10 * 3 = 30
        "division": a / b,  # 10 / 3 = 3.333...
        "floor_division": a // b,  # 10 // 3 = 3 (rounds down)
        "modulus": a % b,  # 10 % 3 = 1 (remainder)
        "exponentiation": a**b,  # 10 ** 3 = 1000
    }


# =============================================================================
# 3. STRINGS
# =============================================================================
# Strings are sequences of characters. Python provides many built-in methods.


def string_basics(text: str) -> dict[str, str | int | list[str]]:
    """
    Demonstrate common string operations.

    >>> result = string_basics("Hello, World!")
    >>> result["uppercase"]
    'HELLO, WORLD!'
    >>> result["lowercase"]
    'hello, world!'
    >>> result["length"]
    13
    >>> result["reversed"]
    '!dlroW ,olleH'
    >>> result["words"]
    ['Hello,', 'World!']
    >>> result["first_five"]
    'Hello'
    >>> result["replaced"]
    'Hello, Python!'
    """
    return {
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "length": len(text),
        "reversed": text[::-1],  # Slice with step -1 reverses
        "words": text.split(),  # Split on whitespace
        "first_five": text[:5],  # Slicing: index 0 to 4
        "replaced": text.replace("World", "Python"),
    }


def format_greeting(name: str, age: int) -> str:
    """
    Demonstrate f-string formatting — the modern way to build strings.

    >>> format_greeting("Alice", 25)
    'Hello, Alice! You are 25 years old.'
    >>> format_greeting("Bob", 30)
    'Hello, Bob! You are 30 years old.'
    """
    return f"Hello, {name}! You are {age} years old."


# =============================================================================
# 4. LISTS
# =============================================================================
# Lists are ordered, mutable collections that can hold any type.


def list_basics() -> dict[str, list[int] | int]:
    """
    Demonstrate common list operations.

    >>> result = list_basics()
    >>> result["original"]
    [1, 2, 3, 4, 5]
    >>> result["appended"]
    [1, 2, 3, 4, 5, 6]
    >>> result["first"]
    1
    >>> result["last"]
    6
    >>> result["sliced"]
    [2, 3, 4]
    >>> result["sorted_desc"]
    [6, 5, 4, 3, 2, 1]
    >>> result["length"]
    6
    """
    numbers = [1, 2, 3, 4, 5]
    original = numbers.copy()  # Save a copy before modifying

    numbers.append(6)  # Add to end

    return {
        "original": original,
        "appended": numbers,
        "first": numbers[0],  # Indexing starts at 0
        "last": numbers[-1],  # Negative index = from end
        "sliced": numbers[1:4],  # Slice: index 1, 2, 3
        "sorted_desc": sorted(numbers, reverse=True),
        "length": len(numbers),
    }


def list_comprehension(numbers: list[int]) -> dict[str, list[int]]:
    """
    List comprehensions are a concise way to create new lists.

    >>> result = list_comprehension([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    >>> result["squared"]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    >>> result["evens"]
    [2, 4, 6, 8, 10]
    >>> result["even_squared"]
    [4, 16, 36, 64, 100]
    """
    return {
        "squared": [n**2 for n in numbers],
        "evens": [n for n in numbers if n % 2 == 0],
        "even_squared": [n**2 for n in numbers if n % 2 == 0],
    }


# =============================================================================
# 5. DICTIONARIES
# =============================================================================
# Dictionaries store key-value pairs. Keys must be immutable (strings, numbers, tuples).


def dictionary_basics() -> dict[str, str | list[str] | int]:
    """
    Demonstrate common dictionary operations.

    >>> result = dictionary_basics()
    >>> result["name"]
    'Alice'
    >>> result["keys"]
    ['name', 'age', 'language']
    >>> result["values"]
    ['Alice', 30, 'Python']
    >>> result["size"]
    3
    >>> result["default"]
    'Not found'
    """
    person = {"name": "Alice", "age": 25}

    # Update a value
    person["age"] = 30

    # Add a new key-value pair
    person["language"] = "Python"

    return {
        "name": person["name"],
        "keys": list(person.keys()),
        "values": list(person.values()),
        "size": len(person),
        "default": person.get("email", "Not found"),  # Safe access with default
    }


# =============================================================================
# 6. CONDITIONALS (if / elif / else)
# =============================================================================
# Control the flow of your program based on conditions.


def classify_number(n: int) -> str:
    """
    Classify a number as positive, negative, or zero.

    >>> classify_number(5)
    'positive'
    >>> classify_number(-3)
    'negative'
    >>> classify_number(0)
    'zero'
    """
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def check_even_odd(n: int) -> str:
    """
    Check whether a number is even or odd.

    >>> check_even_odd(4)
    'even'
    >>> check_even_odd(7)
    'odd'
    >>> check_even_odd(0)
    'even'
    """
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


# =============================================================================
# 7. LOOPS
# =============================================================================
# Loops let you repeat actions. Python has `for` and `while` loops.


def sum_with_for_loop(numbers: list[int]) -> int:
    """
    Sum a list of numbers using a for loop.

    >>> sum_with_for_loop([1, 2, 3, 4, 5])
    15
    >>> sum_with_for_loop([10, 20, 30])
    60
    >>> sum_with_for_loop([])
    0
    """
    total = 0
    for n in numbers:
        total += n  # Shorthand for total = total + n
    return total


def countdown(start: int) -> list[int]:
    """
    Count down from 'start' to 1 using a while loop.

    >>> countdown(5)
    [5, 4, 3, 2, 1]
    >>> countdown(3)
    [3, 2, 1]
    >>> countdown(0)
    []
    """
    result = []
    while start > 0:
        result.append(start)
        start -= 1
    return result


def fizzbuzz(n: int) -> list[str]:
    """
    Classic FizzBuzz: for numbers 1 to n, return:
    - "FizzBuzz" if divisible by both 3 and 5
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - the number as a string otherwise

    >>> fizzbuzz(15)[-1]
    'FizzBuzz'
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    >>> fizzbuzz(3)
    ['1', '2', 'Fizz']
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# =============================================================================
# 8. FUNCTIONS
# =============================================================================
# Functions are reusable blocks of code. They take inputs and return outputs.


def greet(name: str = "World") -> str:
    """
    A function with a default parameter.

    >>> greet()
    'Hello, World!'
    >>> greet("Python")
    'Hello, Python!'
    """
    return f"Hello, {name}!"


def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    >>> calculate_area(5, 3)
    15
    >>> calculate_area(2.5, 4)
    10.0
    """
    return length * width


def factorial(n: int) -> int:
    """
    Calculate n! using recursion — a function that calls itself.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# =============================================================================
# 9. TUPLES AND SETS
# =============================================================================
# Tuples are immutable sequences. Sets are unordered collections of unique items.


def tuple_basics() -> tuple[int, ...]:
    """
    Tuples are like lists but cannot be changed after creation.

    >>> point = tuple_basics()
    >>> point
    (10, 20, 30)
    >>> point[0]
    10
    >>> len(point)
    3
    """
    return (10, 20, 30)


def set_operations(a: set[int], b: set[int]) -> dict[str, set[int]]:
    """
    Demonstrate set operations: union, intersection, difference.

    >>> result = set_operations({1, 2, 3}, {2, 3, 4})
    >>> result["union"] == {1, 2, 3, 4}
    True
    >>> result["intersection"] == {2, 3}
    True
    >>> result["difference"] == {1}
    True
    """
    return {
        "union": a | b,  # Items in either set
        "intersection": a & b,  # Items in both sets
        "difference": a - b,  # Items in a but not b
    }


# =============================================================================
# 10. ERROR HANDLING
# =============================================================================
# Use try/except to handle errors gracefully instead of crashing.


def safe_divide(a: float, b: float) -> float | str:
    """
    Divide two numbers, handling division by zero.

    >>> safe_divide(10, 3)
    3.3333333333333335
    >>> safe_divide(10, 0)
    'Cannot divide by zero'
    >>> safe_divide(0, 5)
    0.0
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_list_access(items: list, index: int) -> str:
    """
    Safely access a list element by index.

    >>> safe_list_access(["a", "b", "c"], 1)
    'Found: b'
    >>> safe_list_access(["a", "b", "c"], 10)
    'Index 10 is out of range'
    """
    try:
        return f"Found: {items[index]}"
    except IndexError:
        return f"Index {index} is out of range"


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
