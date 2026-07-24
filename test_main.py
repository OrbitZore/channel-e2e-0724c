"""Tests for the calculator module."""
import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 7) == 21
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(15, 3) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
