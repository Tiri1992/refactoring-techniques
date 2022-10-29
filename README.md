# Refactoring: Improving the design of existing code

These are adapted notes from Martin Fowlers book "Refactoring". They are also adapted from a [repo](https://github.com/HugoMatilla/Refactoring-Summary) which I found very helpful but was written in Java and required something in python.

You can find the source code of these snipped in the `.code_snippets` folder. I hope this will be helpful for those pythonistas out there looking for techniques to refactor code.

**Note**: If there are any typos or suggested changes, feel free to submit an issue + pull request.


## Composing methods

### 1. Extract method
---

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
---

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

### 3. Inline Temp
---

```python
class Sales:

    def get_sales(self):
        pass

sales = Sales()

# Bad 
def has_exceeded_sales_target():
    total_sales = sales.get_sales()
    return total_sales > 1000

# Good
def has_exceeded_sales_target():
    return sales.get_sales() > 1000

# Much better
from enum import IntEnum

class Target(IntEnum):
    SALES = 1000


def has_exceeded_sales_target():
    return sales.get_sales() > Target.SALES
```

Reason:

- You have a temp that is assigned to once with a simple expression and the temp variable is getting in the way of other refactorings. 
- This technique is used with the Query method.
- Enums can be very powerful for readbility and maintenance instead of using magic numbers.


### 4. Replace Temp with Query
---

```python
# Bad
class BatchItem:

    def __init__(self, quantity: int, price: float) -> None:
        self._quantity = quantity
        self._price = price

    def get_discount(self):
        batch_price = self._quantity * self._price
        if batch_price > 100:
            return batch_price * 0.95
        else:
            return batch_price * 0.98
    
# Good: Better to use a query when the computation costs are low
class BatchItem:

    def __init__(self, quantity: int, price: float) -> None:
        self._quantity = quantity
        self._price = price

    def get_batch_price(self):
        return self._quantity * self._price

    def get_discount(self):
        if self.get_batch_price() > 100:
            return self.get_batch_price() * 0.95
        else:
            return self.get_batch_price() * 0.98
```

Reason:

- You are using a temporary variable to hold the result of an expression. By replacing a temp with a query method you are allowing other methods in your class to access the returned value. 
- This is conditional as long as the expression accessed in the query isn't time consuming.

### 5. Introduce Explaining Variable
---

```python
# Bad
def some_complicated_expression(name: str) -> str:
    # Lots of WTF's is going on here
    if name.split("_")[-1].upper().endswith("OS") and name.split("_")[0].upper().startswith("64BIT"):
        return "Fast mac"
    elif name.split("_")[-1].upper().endswith("PC") and name.split("_")[0].upper().startswith("32BIT"):
        return "Slow pc"
    else:
        return "Other"

# Good
def some_complicated_expression(name: str) -> str:
    # Explaining variables
    is_mac = name.split("_")[-1].upper() == "OS"
    is_pc = name.split("_")[-1].upper() == "PC"
    is_32bit = name.split("_")[0].upper() == "32BIT"
    is_64bit = name.split("_")[0].upper() == "64BIT"
    if is_mac and is_64bit:
        return "Fast mac"
    elif is_pc and is_32bit:
        return "Slow pc"
    else:
        return "Other"
```

Reason:
- When the first words that pop into your mind is "WTF"
- Expressions can be shortened.

### 6. Split Temporary Variable
--- 

```python
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

```

Reason:

- You have a temporary variable assigned to more than once, but it is not a loop variable nor a collecting temporary variable.

### 7. Remove Assignments to Parameters
---

```python
# Bad
def discount(input_value: int, quantity: int) -> int:
    if input_value > 50:
        input_value = input_value - 2
    if quantity > 100:
        input_value = input_value - 1
    return input_value

# Better
def discount(original_input_value: int, quantity: int) -> int:
    # Split the variable
    input_value = original_input_value
    if input_value > 50:
        input_value = input_value - 2
    if quantity > 100:
        input_value = input_value - 1
    return input_value

# Good: Rename variables to get better names
def discount(input_value: int, quantity: int) -> int:
    # Split the variable
    result = input_value
    if input_value > 50:
        result = result - 2
    if quantity > 100:
        result = result - 1
    return result
```

Reason:

- Its better to assign an input parameter to another parameter if the functions logic modifies its state in any way.
- The input_value above is used to supply an input to the function and to hold the result for the caller. Makes much more sense to split this variable.

### 8. Replace Method with Method Object: Command Pattern

```python
from abc import ABC, abstractmethod

# Bad
def score(candidate, medical_exam, scoring_guide):
    result = 0
    health_level = 0
    high_medical_risk_flag = False 

    if medical_exam.is_smoker:
        health_level += 10
        high_medical_risk_flag = True 
    
    certification_grade = "regular"

    if scoring_guide.state_with_low_certification(candidate.origin_state):
        certification_grade = "low"
        result -= 5

    # Lots more code like this
    result -= max(health_level - 5, 0)
    return result

# Good
class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass 


class Scorer(ICommand):

    def __init__(self, candidate, medical_exam, scoring_guide) -> None:
        # Factored out as instance variables
        self._candidate = candidate
        self._medical_exam = medical_exam
        self._scoring_guide = scoring_guide

    def execute(self):
        self._result = 0
        self._health_level = 0
        self._high_medical_risk_flag = False 

        # Extract method
        self.score_smoking()
        
        certification_grade = "regular"

        # Extract method
        self.score_based_on_origin(certification_grade)

        # Lots more code like this
        self._result -= max(self._health_level - 5, 0)
        return self._result

    def score_smoking(self):
        if self._medical_exam.is_smoker:
            self._health_level += 10
            self._high_medical_risk_flag = True  
    
    def score_based_on_origin(self, certification_grade):
        if self._scoring_guide.state_with_low_certification(self._candidate.origin_state):
            certification_grade = "low"
            self._result -= 5
```

Reason:
- Greater flexibility for the control an expression of a function than a standard function
- Commands can have complimentary expressions (i.e. rolling back changes from the command)
- Additional methods of the object can help facilitate the breakdown of the logic

### 9. Substitution Algorithm
---

```python
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
```

Reason:
- Ideal if you would like to break down a complex algorithm into one that is cleaner and more maintainable.


### 10. Extract Class
---

```python
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
```

Reason:
- One class is doing too many things and not adhering to the SRP. Better to decouple. 
- Rule of thumb: Consider to split a class when you notice that a subset of data and methods belong together.

### 11. Inline class
---

```python
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
```

Reason:
- Opposite to extract class, where the motivation stems to reduce the redundant classes. 
- Usually it makes sense to consume this into another class to improve readability

### 12. Hide delegate
---

```python
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
        # acting delegate
        return self._department.manager

class Department:

    def __init__(self, charge_code, manager) -> None:
        self.charge_code = charge_code
        self.manager = manager 


# Now clients can access the manager attribute directly from person without having to interact with the Department object.
person = Person("John")
person.manager
```

Reason:
- Encapsulation means classes should know least as possible about other levels of the system.
- Clients do not need to know the underline apis the object they are interacting with is also interacting with
- Making some changes to the delegate object should minimise damage on client code as they do not directly interact with the delegate class.

### 13. Remove middle man
---

```python
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
```

Reason:
- Sometimes hiding the delegate can become a burden if there are too many and can more overhead for little reward.
- In these scenarios its better to directly invoke the delegate if there are many attributes being invoked from the client and the api is relatively straight forward and unlikely to change.