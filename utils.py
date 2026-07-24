"""Utility functions for the calculator project."""

def format_result(operation: str, a: int, b: int, result) -> str:
    """Format a calculation result as a human-readable string."""
    return f"{operation}({a}, {b}) = {result}"

def validate_integer(value: str) -> int:
    """Parse and validate an integer from string input."""
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"'{value}' is not a valid integer")
