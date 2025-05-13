from ordered import OrderedLine
import pytest

def test_empty_order():
    ol = OrderedLine()
    assert ol.getOrder() == []

def test_single_insert():
    ol = OrderedLine()
    ol.insert(5)
    assert ol.getOrder() == [5]

def test_inserts_in_order():
    ol = OrderedLine()
    ol.insert(2)
    ol.insert(5)
    ol.insert(8)
    assert ol.getOrder() == [2, 5, 8]

def test_inserts_reverse():
    ol = OrderedLine()
    ol.insert(8)
    ol.insert(5)
    ol.insert(2)
    assert ol.getOrder() == [8, 2, 5]

def test_inserts_middle():
    ol = OrderedLine()
    ol.insert(2)
    ol.insert(8)
    ol.insert(5)
    assert ol.getOrder() == [2, 5, 8]

def test_duplicates():
    ol = OrderedLine()
    ol.insert(5)
    ol.insert(5)
    assert ol.getOrder() == [5]

def test_negatives():
    ol = OrderedLine()
    ol.insert(0)
    ol.insert(-10)
    ol.insert(-1)
    assert ol.getOrder() == [0, -1, -10]