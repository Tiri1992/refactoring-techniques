"""
Extract method

Group together useful functionality so it can be reused in other parts of your code.

Reason:

- Allows the increase of other methods to use the method print_details.
- Allows the higher-level methods to read more like a series of comments
"""
import time

def calculating_debt(amount: float) -> tuple[float, str]:
    time.sleep(3)
    return amount ** 2, "John Doe"


# Bad
def print_debt(amount: float) -> None:
    debt, name = calculating_debt(amount) 
    print(f"{name=}")
    print(f"{debt=}")

# Good
def print_details(name: str, debt: float) -> None:
    print(f"{name=}")
    print(f"{debt=}")

def print_debt(amount: float) -> None:
    debt, name = calculating_debt(amount)
    print_details(name, debt)
