
def power(base: float, exp: float) -> float:
    """Calculate base raised to the power of exp."""
    return base ** exp
"""A simple calculator module."""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

import math

def sqrt(value: float) -> float:
    """Calculate square root of a value."""
    if value < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(value)

