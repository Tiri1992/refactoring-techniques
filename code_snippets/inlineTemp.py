""" 
Inline Temp

You have a temp that is assigned to once with a simple expression and the temp variable is getting in the way of other refactorings. This technique is used 
with the Query method.
"""

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


