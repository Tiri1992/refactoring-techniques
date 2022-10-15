"""
Substitute Algorithm

Ideal if you would like to break down a complex algorithm into one that is cleaner and more maintainable.
"""
from typing import Optional

# Bad
def found_person(people: list[str]) -> str:
    for i in range(len(people)):
        if people[i] == "Don":
            return "Don"
        if people[i] == "John":
            return "John"
        if people[i] == "Kent":
            return "Kent"
    return ""

# Good 
def found_person(people: list[str]) -> Optional[str]:
    to_identify = {"Don", "John", "Kent"}
    for name in people:
        if name in to_identify:
            return name
    return None 