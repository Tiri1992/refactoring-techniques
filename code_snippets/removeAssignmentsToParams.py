"""
Remove assignments to parameters

Its better to assign an input parameter to another parameter if the functions logic modifies its state in anyway. In the example below,
the input_value is used to supply an input to the function and to hold the result for the caller. Makes much more sense to split this variable.
"""

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


