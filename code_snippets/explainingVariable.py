"""
Explaining variable

This is useful when you need to extract expressions that are complicated to understand and rename them into something simpler.
"""

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

if __name__ == "__main__":
    name = "64bit_macbookpro_os"
    print(some_complicated_expression(name))