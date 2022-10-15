"""
Move field

It may be useful to move data around if you find you need to pass a field from one record whenever you pass another record to a function. It can also
be noticable, when pieces of data that are always passed to functions together are normally best encapsulated in a single record to clarify there relationship.

NOTE: Change is a factor, if a change in one record causes a field in another record to change too, thats a sign of a field in the wrong place.

The goal is that if you have to update the same field in multiple structures, this should be an indicator to move them to another place where
it can be updated once.
"""

from datetime import datetime
# Bad

class Customer:

    def __init__(self, name, discount_rate) -> None:
        self._name = name 
        self._discount_rate = discount_rate

    def get_discount_rate(self):
        return self._discount_rate

    def become_preferred(self):
        self._discount_rate += 0.03
        # other logic

    def apply_discount(self, amount):
        return amount.substract(amount.multiply(self._discount_rate))

class CustomerContract:

    def __init__(self, start_date) -> None:
        self._start_date = start_date

# Good: Objective is to move the discount rate field from Customer -> CustomerContract
# More pythonic to use properties and dataclasses.
from dataclasses import dataclass

class Customer:

    def __init__(self, name, discount_rate) -> None:
        self._name = name 
        self.discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self._contract._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._contract = CustomerContract(
            _start_date=datetime.now(),
            _discount_rate=value,
        )

    def become_preferred(self):
        self._contract._discount_rate(self._discount_rate + 0.03)
        # other logic

    def apply_discount(self, amount):
        return amount.substract(amount.multiply(self._contract._discount_rate))

@dataclass
class CustomerContract:

    _start_date: datetime
    _discount_rate: float

if __name__ == "__main__":
    customer =Customer("Tiri", 0.03)
    print(customer.discount_rate)