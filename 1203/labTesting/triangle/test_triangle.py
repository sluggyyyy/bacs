import pytest
from triangle import triangleType

def test_equilateral_acute():
    assert triangleType(3, 3, 3) == "Equilateral Acute"

def test_isosceles_acute():
    assert triangleType(3, 3, 4) == "Isosceles Acute"

def test_scalene_right():
    assert triangleType(3, 4, 5) == "Scalene Right"

def test_isosceles_right():
    assert triangleType(4, 4, 4*2**0.5) == "Isosceles Right"

def test_scalene_acute():
    assert triangleType(4, 5, 6) == "Scalene Acute"

def test_isosceles_obtuse():
    assert triangleType(3, 3, 5) == "Isosceles Obtuse"

def test_scalene_obtuse():
    assert triangleType(3, 4, 6) == "Scalene Obtuse"