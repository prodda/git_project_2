"""Tests for calculator"""
import pytest
from calculator import (
    add, subtract, multiply, divide,
    modulo, power, square_root, factorial,
)
from validator import (
    validate_number, validate_operation, validate_range,
    validate_positive, validate_non_negative, validate_integer,
)


class TestAdd:
    def test_positive(self):
        assert add(2, 3) == 5

    def test_negative(self):
        assert add(-1, -4) == -5

    def test_float(self):
        assert add(1.5, 2.5) == 4.0

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 7) == -4


class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(99, 0) == 0

    def test_negative(self):
        assert multiply(-2, 5) == -10


class TestDivide:
    def test_exact(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestModulo:
    def test_basic(self):
        assert modulo(10, 3) == 1

    def test_even(self):
        assert modulo(8, 4) == 0

    def test_by_zero(self):
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            modulo(5, 0)


class TestPower:
    def test_basic(self):
        assert power(2, 10) == 1024

    def test_zero_exponent(self):
        assert power(99, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == pytest.approx(0.5)


class TestSquareRoot:
    def test_perfect_square(self):
        assert square_root(25) == 5.0

    def test_float(self):
        assert square_root(2) == pytest.approx(1.41421, rel=1e-4)

    def test_zero(self):
        assert square_root(0) == 0.0

    def test_negative(self):
        with pytest.raises(ValueError, match="negative number"):
            square_root(-1)


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_five(self):
        assert factorial(5) == 120

    def test_negative(self):
        with pytest.raises(ValueError, match="negative number"):
            factorial(-3)


class TestValidateNumber:
    def test_integer_string(self):
        assert validate_number("42") is True

    def test_float_string(self):
        assert validate_number("3.14") is True

    def test_negative_string(self):
        assert validate_number("-7") is True

    def test_letters(self):
        assert validate_number("abc") is False

    def test_none(self):
        assert validate_number(None) is False

    def test_actual_int(self):
        assert validate_number(5) is True


class TestValidateOperation:
    @pytest.mark.parametrize("op", ["+", "-", "*", "/"])
    def test_valid_ops(self, op):
        assert validate_operation(op) is True

    @pytest.mark.parametrize("op", ["**", "//", "mod", "", "^"])
    def test_invalid_ops(self, op):
        assert validate_operation(op) is False


class TestValidateRange:
    def test_in_range(self):
        assert validate_range(500) is True

    def test_lower_bound(self):
        assert validate_range(-1000) is True

    def test_upper_bound(self):
        assert validate_range(1000) is True

    def test_below_range(self):
        assert validate_range(-1001) is False

    def test_above_range(self):
        assert validate_range(1001) is False

    def test_custom_range(self):
        assert validate_range(50, min_val=0, max_val=100) is True
        assert validate_range(-1, min_val=0, max_val=100) is False


class TestValidatePositive:
    def test_positive(self):
        assert validate_positive(1) is True

    def test_zero(self):
        assert validate_positive(0) is False

    def test_negative(self):
        assert validate_positive(-5) is False

    def test_string(self):
        assert validate_positive("abc") is False


class TestValidateNonNegative:
    def test_positive(self):
        assert validate_non_negative(3) is True

    def test_zero(self):
        assert validate_non_negative(0) is True

    def test_negative(self):
        assert validate_non_negative(-1) is False


class TestValidateInteger:
    def test_whole_float(self):
        assert validate_integer(4.0) is True

    def test_true_int(self):
        assert validate_integer(7) is True

    def test_fractional(self):
        assert validate_integer(3.5) is False

    def test_string_int(self):
        assert validate_integer("6") is True

    def test_string_float(self):
        assert validate_integer("6.7") is False
        