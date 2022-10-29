""" 
Hide delegate

Key to good modular design is encapsulation. This means that modules need to know less about other parts
of the system. This makes swaping out or changing other parts of the system easier because fewer modules need to 
be told about the change.

Something to note, when we speak of encapsulation, most of the time we think just hiding our fields but this extends further
the more we understand OOP.
"""

# Bad:
class Person:

    def __init__(self, name) -> None:
        self.name = name 

    @property
    def department(self):
        return self._department 

    @department.setter
    def department(self, value):
        self._department = value 

class Department:

    def __init__(self, charge_code, manager) -> None:
        self.charge_code = charge_code
        self.manager = manager 

# Accessing the code now exposes to the client how department class works.

person = Person("John")
manager = person.department.manager 

# Good: Reduce coupling by hiding department class from client

class Person:

    def __init__(self, name) -> None:
        self.name = name 

    @property
    def department(self):
        return self._department 

    @department.setter
    def department(self, value):
        self._department = value 

    @property
    def manager(self):
        return self._department.manager

class Department:

    def __init__(self, charge_code, manager) -> None:
        self.charge_code = charge_code
        self.manager = manager 


# Now clients can access the manager attribute directly from person without having to interact with the Department class.
person = Person("John")
person.manager