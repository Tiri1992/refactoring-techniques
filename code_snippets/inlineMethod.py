""" 
Inline method

A methods body should be just as clear as its name.
"""

# Bad:
class Temperature:

    def __init__(self, celcius: int) -> None:
        self._celcius = celcius

    def is_cold(self):
        return self.is_less_than_zero()

    def is_less_than_zero(self):
        return self._celcius < 0

# Good: Grouping makes this clearer
class Temperature:

    def __init__(self, celcius: int) -> None:
        self._celcius = celcius

    def is_cold(self):
        return self._celcius < 0