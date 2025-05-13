import pytest
from binary import hexToChar

def test_HexValues():
    assert hexToChar(10) == 'A'
    assert hexToChar(11) == 'B'
    assert hexToChar(12) == 'C'
    assert hexToChar(13) == 'D'
    assert hexToChar(14) == 'E'
    assert hexToChar(15) == 'F'

