"""
Remove middle man

This is the inverse of `Hide delegate`. One of the downsides of the `hide delegate` method is that everytime a client requires a new feature
of the delegate, we need to add a delegating method to the server class. The server class acts like a `middle man`, sometimes its just more sensible
to have the client calling the delegate directly.
"""
from dataclasses import dataclass


# Bad: Very contrived example
@dataclass
class EmployeeProfile:

    department: str 
    salary: int 
    manager: str 
    level: int 


class Person:
    
    def __init__(self, name: str, profile: EmployeeProfile) -> None:
        self.name = name 
        self.profile = profile

    # Overuse of property methods, much work with little gain
    @property
    def department(self):
        return self.profile.department

    @property
    def salary(self):
        return self.profile.salary

    @property
    def manager(self):
        return self.profile.manager
    
    @property
    def level(self):
        return self.profile.level

employee_profile = EmployeeProfile(
    department="Software Engineer",
    salary=30000,
    manager="Jane Thorpe",
    level=3,
)

person = Person(name="John Doe", profile=employee_profile)
person.department
person.manager
person.level

# Good: Better to directly invoke the delegate

@dataclass
class EmployeeProfile:

    department: str 
    salary: int 
    manager: str 
    level: int 


class Person:
    
    def __init__(self, name: str, profile: EmployeeProfile) -> None:
        self.name = name 
        self.profile = profile

employee_profile = EmployeeProfile(
    department="Software Engineer",
    salary=30000,
    manager="Jane Thorpe",
    level=3,
)

person = Person(name="John Doe", profile=employee_profile)
person.profile.department
person.profile.manager
person.profile.level