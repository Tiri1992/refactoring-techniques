""" 
Split temporary variable

You have a temporary variable assigned to more than once, but it is not a loop variable nor a collecting temporary variable.
"""

# Bad
class Shape:

    def __init__(self, height: int, width: int) -> None:
        self._height = height 
        self._width = width 

    def display(self) -> None:
        # Confusing as tmp variable has more than one responsibility. I.e. it first calculates perimeter then area.
        tmp = 2 * (self._height + self._width)
        print(tmp)
        tmp = self._height * self._width
        print(tmp)


# Good
class Shape:

    def __init__(self, height: int, width: int) -> None:
        self._height = height 
        self._width = width 

    def display(self) -> None:
        # Responsibility is clearer.
        perimeter = 2 * (self._height + self._width)
        print(f"{perimeter=}")
        area = self._height * self._width
        print(f"{area=}")
