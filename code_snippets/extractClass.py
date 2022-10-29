"""
Extract class

You have one class doing work that should be done by two (or more). Create a new class and move the relevant fields and methods from the old class
into the new class.

Rule of thumb: Consider to split a class when you notice that a subset of the data and methods go together (or perhaps depend/change together).
"""

# Bad: Needs to be split up, one class is not separating the concerns.
class Person:

    def __init__(self, name, office_area_code, office_number) -> None:
        self._name = name 
        self._office_area_code = office_area_code
        self._office_number = office_number

    def get_telephone_number(self):
        pass 


# Good: Using property for more pythonic getter methods. Also, using composition design patterns to expose TelephoneNumber attributes

class TelephoneNumber:

    def __init__(self, area_code, number) -> None:
        self._area_code = area_code
        self._number = number 

    @property
    def number(self):
        return self._number

class Person:

    def __init__(self, name, telephone_number: TelephoneNumber) -> None:
        self._name = name
        self._telphone_number = telephone_number

    def get_telephone_number(self):
        return self._telphone_number.number