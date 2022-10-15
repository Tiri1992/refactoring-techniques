"""
Replace Temp with Query

You are using a temporary variable to hold the result of an expression. By replacing a temp with a query method you are allowing other methods
in your class to access the returned value. This is vital for the extraction method.

This is conditional as long as the expression accessed in the query isn't time consuming.
"""

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