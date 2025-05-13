import pytest
from binary import decToBase

def test_Base2():
    assert decToBase(25, 2) == "11001"
    assert decToBase(100, 2) == "1100100"

def test_Base10():
    assert decToBase(42, 10) == "42"
    assert decToBase(123, 10) == "123"

def test_Base16():
    assert decToBase(243, 16) == "F3"
    assert decToBase(255, 16) == "FF"

def test_Base8():
    assert decToBase(64, 8) == "100"
    assert decToBase(100, 8) == "144"