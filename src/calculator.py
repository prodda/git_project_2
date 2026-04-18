"""Basic calculator operations."""
import math


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b


def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
