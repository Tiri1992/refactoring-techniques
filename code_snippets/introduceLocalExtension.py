"""
Introduce Local Extension

The server class requires additional methods but you can't modify the class. Be wary of overusing inheritance for extending functionality as this can cause an inheritance explosion. In most cases
favour composition.
"""

# Bad
class Human:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def client():
    employee = Human("John", 25)
    print(f"Employee profile -> {employee.name}-{employee.age}")

# Good
class Human:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Employee(Human):

    def get_profile(self) -> str:
        return f"{self.name}-{self.age}"

def client():
    employee = Employee("John", 25)
    print(f"Employee profile -> {employee.get_profile()}")
    


