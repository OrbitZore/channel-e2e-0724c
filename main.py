"""A simple calculator module for E2E testing."""

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"3 * 7 = {multiply(3, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
