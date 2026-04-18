"""Input validation for calculator."""


def validate_number(value):
    """Validate that value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def validate_operation(op):
    """Validate that operation is supported."""
    valid_ops = ['+', '-', '*', '/']
    return op in valid_ops


def validate_range(value, min_val=-1000, max_val=1000):
    """Validate that number is within acceptable range."""
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False


def validate_positive(n):
    """Validate that a number is positive."""
    try:
        num = float(n)
        return num > 0
    except (ValueError, TypeError):
        return False


def validate_non_negative(n):
    """Validate that a number is non-negative."""
    try:
        num = float(n)
        return num >= 0
    except (ValueError, TypeError):
        return False


def validate_integer(n):
    """Validate that a number is an integer."""
    try:
        num = float(n)
        return num == int(num)
    except (ValueError, TypeError):
        return False
