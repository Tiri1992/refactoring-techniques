# Refactoring: Improving the design of existing code

These are adapted notes from Martin Fowlers book "Refactoring". They are also adapted from a [repo](https://github.com/HugoMatilla/Refactoring-Summary) which I found very helpful but was written in Java and required something in python.

You can find the source code of these snipped in the `.code_snippets` folder. I hope this will be helpful for those pythonistas out there looking for techniques to refactor code.

**Note**: If there are any typos or suggested changes, feel free to submit an issue + pull request.


## Composing methods

### 1. Extract method

```python
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
```

Group together useful functionality so it can be reused in other parts of your code.

Reason:

- Allows the increase of other methods to use the method print_details.
- Allows the higher-level methods to read more like a series of comments

### 2. Inline method

```python
# Bad:
class Temperature:

    def __init__(self, celcius: int) -> None:
        self._celcius = celcius

    def is_cold(self):
        return self.is_less_than_zero()

    def is_less_than_zero(self):
        return self._celcius < 0

# Good
class Temperature:

    def __init__(self, celcius: int) -> None:
        self._celcius = celcius

    def is_cold(self):
        return self._celcius < 0
```

Reason:

- Indirection is needless, i.e. `is_less_than_zero` is self explanatory
- When group of methods are badly factored and grouping makes it sufficiently clearer.