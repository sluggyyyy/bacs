import pytest
from minABC import min_abc

def test_min_abc_all_positive():
    assert min_abc(5, 3, 7) == 3
    assert min_abc(1, 2, 3) == 1

def test_min_abc_mixed_signs():
    assert min_abc(-5, 3, 7) == -5
    assert min_abc(1, -2, 3) == -2

def test_min_abc_duplicates():
    assert min_abc(5, 5, 7) == 5
    assert min_abc(1, 2, 2) == 1

def test_min_abc_zero():
    assert min_abc(0, 1, 2) == 0
    assert min_abc(1, 0, 2) == 0