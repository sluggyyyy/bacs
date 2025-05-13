import pytest
from binary import charToHex

def test_Alpha():
    assert charToHex('A') == 10
    assert charToHex('B') == 11
    assert charToHex('C') == 12
    assert charToHex('D') == 13
    assert charToHex('E') == 14
    assert charToHex('F') == 15
