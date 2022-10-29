"""
Inline class

Opposite to Extract class, where the motivation stems to reduce the redundant classes. Usually when a class isn't doing very much and can be 
consumed by another class to save on code and improve readability.
"""

# Bad: Redudant class

class Age:

    def __init__(self, age) -> None:
        self._age = age

class Person:

    def __init__(self, name) -> None:
        self._name = name 

# Good: Attributes belong together under person class

class Person:

    def __init__(self, name, age) -> None:
        self._name = name 
        self._age = age