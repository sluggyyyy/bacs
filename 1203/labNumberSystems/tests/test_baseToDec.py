import pytest
from binary import baseToDec

def test_Base2():
    assert baseToDec("1100100", 2) == 100

def test_Base10():
    assert baseToDec("123", 10) == 123

def test_Base16_Upper():
    assert baseToDec("F3", 16) == 243
    assert baseToDec("FF", 16) == 255

def test_Base16_Lower():
    assert baseToDec("f3", 16) == 243
    assert baseToDec("ff", 16) == 255

def test_Base8():
    assert baseToDec("100", 8) == 64
    assert baseToDec("144", 8) == 100